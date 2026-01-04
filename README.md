# jumpkwapp

Run or raise utility for KDE Plasma 6 on Wayland.

Initially forked from [ww-run-or-raise](https://github.com/academo/ww-run-raise) with modifications to add more features from X11 [jumpapp](https://github.com/mkropat/jumpapp). Also got some inspiration from [kdotools](https://github.com/jinliu/kdotool) for the DBus communication part.

Might also work on X11 as is and with minor modifications on Plasma 5.

## Features

- Filter windows by exact class, class regex, or caption match.
- Can restrict matches to the current virtual desktop.
- Optional toggle mode to minimize if the active window already matches.
- Optionally runs a command when no matching window exists.

## Installation

Using Python 3.13 and D-Bus modules installable from Debian 13 package manager.

```bash
sudo apt install python3-gi python3-dbus
cp jumpkwapp /usr/local/bin  # or any directory in $PATH
```

Similar packages are probably available in other distros but might be named differently.

## Usage

```
jumpkwapp [options]

-f, --filter             Match window class (exact)
-fa, --filter-alternative  Match window caption (regex, case-insensitive)
-fr, --filter-regex      Match window class (regex)
-d, --current-desktop    Only consider windows on the current desktop
-t, --toggle             Minimize the window if it is already active
-c, --command CMD        Launch CMD if no window matches
```

### Examples

- Raise an existing LibreWolf window in current virtual desktop or start it if missing:
```
jumpkwapp -f librewolf -c librewolf --current-desktop
```

Setup the hotkey in KDE's Shortcut settings panel.

## Development

See `DEBUGGING.md` for tips on inspecting KWin state.

# License

MIT licensed but the original `ww` Bash script which remains in repo history didn't have a license defined at the time.
