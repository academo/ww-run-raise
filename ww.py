#!/usr/bin/env python3
"""
ww - Utility to raise or jump to applications in KDE.

Compatible with KDE 6.x and Wayland, might also work on X11.
Uses Python 3.13 but could benefit from Python 3.14 template strings.
"""

import argparse
import hashlib
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from string import Template

try:
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    from gi.repository import GLib
except ImportError:
    print("ERROR: Required Python packages not found.", file=sys.stderr)
    print("Please install: python3-dbus python3-gi", file=sys.stderr)
    sys.exit(1)


@dataclass
class DBusMessageReceiver:
    """Receive D-Bus messages from KWin scripts."""

    has_matches: bool | None = None
    loop: GLib.MainLoop | None = None
    bus: dbus.SessionBus = field(init=False)
    bus_name: str = field(init=False)

    def __post_init__(self):
        """Initialize D-Bus connection after dataclass initialization."""
        DBusGMainLoop(set_as_default=True)
        self.bus = dbus.SessionBus()
        self.bus_name = self.bus.get_unique_name()

    def has_matches_handler(self, has_matches_str):
        """Handle hasMatches message from KWin script."""
        self.has_matches = has_matches_str.lower() == 'true'
        if self.loop:
            self.loop.quit()

    def register_handlers(self):
        """Register D-Bus method handlers."""
        self.bus.add_message_filter(self._message_filter)

    def _message_filter(self, bus, message):
        """Filter incoming D-Bus messages."""
        match message.get_member():
            case 'hasMatches' if (args := message.get_args_list()):
                self.has_matches_handler(args[0])
        return dbus.lowlevel.HANDLER_RESULT_HANDLED

    def wait_for_response(self, timeout_ms=5000):
        """Wait for a response from the KWin script."""
        self.loop = GLib.MainLoop()
        GLib.timeout_add(timeout_ms, lambda: self.loop.quit())
        self.loop.run()


SCRIPT_TEMPLATE = Template("""
function findMatchingClients(clientClass, clientCaption, clientClassRegex, currentDesktopOnly) {
    var clients = workspace.windowList();
    var compareToCaption = new RegExp(clientCaption || '', 'i');
    var compareToClassRegex = clientClassRegex.length > 0 ? new RegExp(clientClassRegex) : null;
    var compareToClass = clientClass;
    var isCompareToClass = clientClass.length > 0;
    var isCompareToRegex = compareToClassRegex !== null;
    var matchingClients = [];

    for (var i = 0; i < clients.length; i++) {
        var client = clients[i];
        var classCompare = (isCompareToClass && client.resourceClass == compareToClass);
        var classRegexCompare = (isCompareToRegex && compareToClassRegex && compareToClassRegex.exec(client.resourceClass));
        var captionCompare = (!isCompareToClass && !isCompareToRegex && compareToCaption.exec(client.caption));
        if (classCompare || classRegexCompare || captionCompare) {
            if (currentDesktopOnly && !isOnCurrentDesktop(client)) {
                continue;
            }
            matchingClients.push(client);
        }
    }

    return matchingClients;
}

function kwinactivateclient(clientClass, clientCaption, clientClassRegex, toggle, currentDesktopOnly, detectionOnly, dbusAddr) {
    var matchingClients = findMatchingClients(clientClass, clientCaption, clientClassRegex, currentDesktopOnly);

    if (detectionOnly) {
        var hasMatches = matchingClients.length > 0;
        callDBus(dbusAddr, "/", "", "hasMatches", hasMatches.toString());
        return;
    }

    if (matchingClients.length === 0) {
        return;
    }

    var activeWindow = workspace.activeWindow;

    if (matchingClients.length === 1) {
        var client = matchingClients[0];
        if (activeWindow !== client) {
            setActiveClient(client);
        } else if (toggle) {
            client.minimized = !client.minimized;
        }
    } else if (matchingClients.length > 1) {
        // Check if the active window is one of the matching windows
        var activeIsMatching = false;
        for (var j = 0; j < matchingClients.length; j++) {
            if (activeWindow === matchingClients[j]) {
                activeIsMatching = true;
                break;
            }
        }

        // Always sort by stacking order
        matchingClients.sort(function (a, b) {
            return a.stackingOrder - b.stackingOrder;
        });

        if (activeIsMatching) {
            // We're already in this app - cycle through windows (pick first)
            const client = matchingClients[0];
            setActiveClient(client);
        } else {
            // We're switching from another app - pick most recently active (last)
            const client = matchingClients[matchingClients.length - 1];
            setActiveClient(client);
        }
    }
}

/**
 * Checks if given window is on the current virtual desktop.
 * @param {KWin::XdgToplevelWindow|KWin::X11Window} client Window to inspect
 * @return {boolean} True if window is on the current desktop or on all desktops
 */
function isOnCurrentDesktop(client) {
    if (client.onAllDesktops) {
        return true;
    }
    if (workspace.currentDesktop !== undefined && client.desktops !== undefined ){
        return client.desktops.includes(workspace.currentDesktop);
    }
    return true; // fallback if API mismatch
}

function setActiveClient(client){
    workspace.activeWindow = client;
}
kwinactivateclient('$class_name', '$caption_name', '$class_regex', $toggle, $current_desktop_only, $detection_only, '$dbus_addr');
""")


def get_kwin_script_object(script_file):
    """Load and return a KWin script object."""
    bus = dbus.SessionBus()
    kwin_scripting = bus.get_object('org.kde.KWin', '/Scripting')
    script_id = kwin_scripting.loadScript(script_file, dbus_interface='org.kde.kwin.Scripting')
    return bus.get_object('org.kde.KWin', f"/Scripting/Script{script_id}")


def render_script_content(class_name='', caption_name='', class_regex='',
                         toggle=False, current_desktop_only=False,
                         detection_only=False, dbus_addr=''):
    """Render the KWin script with the given parameters."""
    return SCRIPT_TEMPLATE.substitute(
        class_name=class_name,
        caption_name=caption_name,
        class_regex=class_regex,
        toggle='true' if toggle else 'false',
        current_desktop_only='true' if current_desktop_only else 'false',
        detection_only='true' if detection_only else 'false',
        dbus_addr=dbus_addr
    )


def has_matching_windows(filter_by='', filter_alt='', filter_regex='',
                         current_desktop_only=False, toggle=False):
    """Query KWin to check if there are any matching windows using D-Bus."""
    receiver = DBusMessageReceiver()
    receiver.register_handlers()

    script_file = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.js', delete=False) as f:
            script_file = f.name
            script_content = render_script_content(
                class_name=filter_by,
                caption_name=filter_alt,
                class_regex=filter_regex,
                toggle=toggle,
                current_desktop_only=current_desktop_only,
                detection_only=True,
                dbus_addr=receiver.bus_name
            )
            f.write(script_content)

        script = get_kwin_script_object(script_file)
        script.run(dbus_interface='org.kde.kwin.Script')

        # Wait for the response
        receiver.wait_for_response()

        # Stop the script
        script.stop(dbus_interface='org.kde.kwin.Script')

        if script_file and os.path.exists(script_file):
            os.unlink(script_file)

        return receiver.has_matches if receiver.has_matches is not None else False

    except Exception as e:
        print(f"ERROR: Failed to query KWin: {e}", file=sys.stderr)
        if script_file and os.path.exists(script_file):
            os.unlink(script_file)
        return False


def activate_window(filter_by='', filter_alt='', filter_regex='',
                   current_desktop_only=False, toggle=False):
    """Activate a window matching the given filters."""
    script_folder = Path(os.environ.get('XDG_CONFIG_HOME', Path.home())) / '.wwscripts'
    script_folder.mkdir(exist_ok=True)

    # Create a hash of the parameters to use as script name
    info = f"{filter_by}{filter_alt}{filter_regex}{current_desktop_only}{toggle}"
    script_hash = hashlib.md5(info.encode()).hexdigest()[:32]
    script_path = script_folder / script_hash

    # Ensure script file exists
    if not script_path.exists():
        script_content = render_script_content(
            class_name=filter_by,
            caption_name=filter_alt,
            class_regex=filter_regex,
            toggle=toggle,
            current_desktop_only=current_desktop_only,
            detection_only=False,
            dbus_addr=''
        )
        script_path.write_text(script_content)

    try:
        script = get_kwin_script_object(str(script_path))
        script.run(dbus_interface='org.kde.kwin.Script')

        # Stop the script in background
        script_path_dbus = script.object_path
        subprocess.Popen(
            ['dbus-send', '--session', '--dest=org.kde.KWin', '--print-reply=literal',
             script_path_dbus, 'org.kde.kwin.Script.stop'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception as e:
        print(f"ERROR: Failed to activate window: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='ww - Utility to raise or jump to applications in KDE',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('-f', '--filter', dest='filter_by', default='',
                       help='filter by window class (exact match)')
    parser.add_argument('-fa', '--filter-alternative', dest='filter_alt', default='',
                       help='filter by window title (caption)')
    parser.add_argument('-fr', '--filter-regex', dest='filter_regex', default='',
                       help='filter by window class using regex pattern')
    parser.add_argument('-d', '--current-desktop', action='store_true',
                       help='only match windows on the current virtual desktop')
    parser.add_argument('-t', '--toggle', action='store_true',
                       help='also minimize the window if it is already active')
    parser.add_argument('-c', '--command', default='',
                       help='command to run when no matching window is found')

    args = parser.parse_args()

    if not args.filter_by and not args.filter_alt and not args.filter_regex:
        print("ERROR: You need to specify a window filter — either by class (-f), "
              "by title (-fa), or by regex (-fr).", file=sys.stderr)
        print("Use --help for more information.", file=sys.stderr)
        sys.exit(1)

    # Check if we need to launch the command
    if args.command:
        has_matches = has_matching_windows(
            filter_by=args.filter_by,
            filter_alt=args.filter_alt,
            filter_regex=args.filter_regex,
            current_desktop_only=args.current_desktop,
            toggle=args.toggle
        )

        if not has_matches:
            subprocess.Popen(args.command, shell=True)
            return

    # Activate the window
    activate_window(
        filter_by=args.filter_by,
        filter_alt=args.filter_alt,
        filter_regex=args.filter_regex,
        current_desktop_only=args.current_desktop,
        toggle=args.toggle
    )


if __name__ == '__main__':
    main()
