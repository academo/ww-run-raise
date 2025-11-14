ww. Utility to raise or jump an applications in KDE.

It interacts with KWin using KWin scripts and it is compatible with X11 and Wayland. It also works with multiple screens.

It is intended as a wmctrl alternative (only for the raising windows part)

- Compatible with KDE 5.x and 6.x
- Compatible with Wayland and X11

# Installing

- Download ww from this repository
- Copy `ww` into your path. e.g.:

```bash
cp ww /usr/local/bin
```

Feel free to rename it

# Usage

ww only works in KDE. It works in X11 and Wayland.

## Example

if you want to raise or jump to an open firefox window:

`ww -f firefox -c firefox`

if you want to raise or jump to an app with an specific class:

`ww -f kitty.terminal -c 'kitty --class kitty.terminal'`

Note: In this example `kitty` allows you to pass the `class` option that sets the window class.
This is a kitty feature, not a ww feature.

if you want to raise any window that matches a title (supports JS regexp):

`ww -fa 'Zoom meeting'`

if you want to raise or jump to a window using a regex pattern for the class:

`ww -fr '^firefox'`

if you want to toggle (minimize if active) a window:

`ww -f firefox -c firefox -t`

if you want to see information about the currently active window:

`ww -ia`

## Parameters:

```
-h  --help                show this help
-ia --info-active         show information about the active window
-f  --filter              filter by window class (exact match)
-fa --filter-alternative  filter by window title (caption)
-fr --filter-regex        filter by window class using regex pattern
-t  --toggle              also minimize the window if it is already active
-c  --command             command to check if running and run if no process is found
-p  --process             override the process name used when checking if running, defaults to --command
-u  --current-user        will only search processes of the current user (requires loginctl)
```

# Create shortcuts

You can use KDE custom shortcuts to add a custom shortcut that calls ww

![image](https://user-images.githubusercontent.com/227916/126187702-90105aff-32a4-48dd-95c9-a7c1a2623c9e.png)

# How does it work?

Internally ww uses 2 main things to work: `pgrep` and "on demand" KWin scripts.

When you run, for example `ww -f firefox -c firefox`, ww tries to find a process running with the specified process name:

`pgrep -o -f firefox`

This detects if the application is running or not.

Then ww creates a file inside `~/.wwscripts` to store a temporary kwin script, it loads the script, runs it, stops it and unloads it in a single go.

The kwin script is targeted to find and focus a specific window.

The `-ia` option works differently: it uses KWin's scripting API to query information about the currently active window without needing to filter or launch anything.

# TODO

Here some ideas of improvements that I'd like to explore, but my knowledge on kwin scripts doesn't allow me:

- Do not depend on pgrep to detect if an application is open?
- Use a single kwin script with signals instead of loading and running one each time?
