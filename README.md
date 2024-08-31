ww. Utility to raise or jump an applications in KDE. It interacts with KWin using KWin scripts and it is compatible with X11 and Wayland. It also works with multiple screens. It is intended as a wmctrl alternative (only for the raising windows part) compatible with wayland.

# Installing

* Download ww from this repository
* Copy `ww` into your path. e.g.:

```bash
cp ww /usr/local/bin
```

Feel free to rename it

# Usage

ww only works in KDE. It works in X11 and Wayland.

## Example

if you want to raise or jump to an open firefox window:

```bash
ww -f firefox -c firefox
```

if you want to raise or jump to an app with an specific class:

```bash
ww -f kitty.terminal -c 'kitty --class kitty.terminal'
```

Note: In this example `kitty` allows you to pass the `class` option that sets the window class.
This is a kitty feature, not a ww feature.

If you want to raise any window that matches a title. JS regexp allowed:

```bash
ww -fa 'Zoom meeting'
```

Sometimes the command to start a program only indirectly runs the actual
program, making it not directly findable, such as when using flatpaks. Then you
can use `-p` to separate the string used when searching for the application:
```bash
ww -f steam -p steam -c 'flatpak run --branch=stable --arch=x86_64 --command=/app/bin/steam --file-forwarding com.valvesoftware.Steam'
```

(The value specified to `-p` is directly passed along to `pgrep`, see "How does
it work?" below.)

## Paramaters:
```
-h  --help                show this help
-f  --filter              filter by window class
-fa --filter-alternative  filter by window title (caption)
-c  --command             command to check if running and run if no process is found
-p  --process             overide the process name used when checking if running, defaults to --command
```

# Create shortcuts

You can use KDE custom shortcuts to add a custom shortcut that calls ww

![image](https://user-images.githubusercontent.com/227916/126187702-90105aff-32a4-48dd-95c9-a7c1a2623c9e.png)


# How does it work?

Internally ww uses 2 main things to work: `pgrep` and "on demand" KWin scripts.

When you run, for example `ww -f firefox c -firefox`, ww tries to find a process running with the exact command:

`pgrep -o -a -f firefox`

This detects if the application is running or not.

Then ww creates a file inside `~/.wwscripts` to store a temporary kwin script, it loads the script, runs it, stops it and unloads it in a single go.

The kwin script is targeted to find and focus a specific window.

# TODO
Here some ideas of improvements that I'd like to explore, but my knowledge on kwin scripts doesn't allow me:

* Do not depend on pgrep to detect if an application is open?
* Use a single kwin script with signals instead of loading and running one each time?
