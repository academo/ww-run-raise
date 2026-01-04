# Debugging tips

## Querying KWin window information
Inquire KWin window info by selecting a window interactively with mouse:
```
qdbus6 org.kde.KWin /KWin org.kde.KWin.queryWindowInfo
```

Or query it by ID:
```
qdbus6 org.kde.KWin /KWin org.kde.KWin.getWindowInfo <window UUID here>
```

## KWin script debugging

Debug printing output from `print("message")` and `console.log("message")` commands goes to system journal from KWin scripts (embedded JavaScript inside the Python script), which can be tailed:
```bash
journalctl --user -u plasma-kwin_wayland.service -f
```

Helper function useful for listing object properties:
```javascript
function dumpObject(obj) {
    print("---- obj dump ----");
    for (var key in obj) {
        try {
            if (obj.hasOwnProperty(key)) {
                print(key + ": " + obj[key]);
            }
        } catch (e) {
            print(key + ": <error " + e + ">");
        }
    }
}
```
# KWin API
Docs: https://develop.kde.org/docs/plasma/kwin/api/
## client KWin::XdgToplevelWindow or KWin::X11Window
### KWin::XdgToplevelWindow(0x5592f2331140)
```
---- dumping properties ----
objectName:
bufferGeometry: QRectF(1280, 748, 1279, 691)
clientGeometry: QRectF(1280, 748, 1279, 691)
pos: QPointF(1279, 720)
size: QSizeF(1281, 720)
x: 1279
y: 720
width: 1281
height: 720
opacity: 1
output: KWin::DrmOutput(0x5592f294b1f0)
rect: QRectF(0, 0, 1281, 720)
resourceName: konsole
resourceClass: org.kde.konsole
windowRole:
desktopWindow: false
dock: false
toolbar: false
menu: false
normalWindow: true
dialog: false
splash: false
utility: false
dropdownMenu: false
popupMenu: false
tooltip: false
notification: false
criticalNotification: false
appletPopup: false
onScreenDisplay: false
comboBox: false
dndIcon: false
windowType: 0
managed: true
deleted: false
skipsCloseAnimation: false
popupWindow: false
outline: false
internalId: {ab4d5d88-39a6-4cb9-9ce2-5f8b772c71e2}
pid: 4264
stackingOrder: 6
fullScreen: false
fullScreenable: true
active: false
desktops: KWin::VirtualDesktop(0x5592f0c4f5d0)
onAllDesktops: false
activities: 02f09950-876c-4bf6-94c0-361b1ff5aa9f
skipTaskbar: false
skipPager: false
skipSwitcher: false
closeable: true
icon: QVariant(QIcon, QIcon("utilities-terminal",availableSizes[normal,Off]=QList(QSize(16, 16), QSize(22, 22), QSize(32, 32), QSize(48, 48), QSize(64, 64), QSize(128, 128), QSize(256, 256)),cacheKey=0x1500000000))
keepAbove: false
keepBelow: false
shadeable: false
shade: false
minimizable: true
minimized: false
iconGeometry: QRectF(2191, 1501, 42, 50)
specialWindow: false
demandsAttention: false
caption: ww-run-raise : journalctl — Konsole
captionNormal: ww-run-raise : journalctl — Konsole
minSize: QSizeF(150, 150)
maxSize: QSizeF(2.14748e+09, 2.14748e+09)
wantsInput: true
transient: false
transientFor: null
modal: false
frameGeometry: QRectF(1279, 720, 1281, 720)
move: false
resize: false
decorationHasAlpha: true
noBorder: false
providesContextHelp: false
maximizable: true
maximizeMode: 0
moveable: true
moveableAcrossScreens: true
resizeable: true
desktopFileName: org.kde.konsole
hasApplicationMenu: false
applicationMenuActive: false
unresponsive: false
colorScheme: kdeglobals
layer: 2
hidden: false
tile: null
inputMethod: false
objectNameChanged: function() { [native code] }
stackingOrderChanged: function() { [native code] }
shadeChanged: function() { [native code] }
opacityChanged: function() { [native code] }
damaged: function() { [native code] }
inputTransformationChanged: function() { [native code] }
closed: function() { [native code] }
outputChanged: function() { [native code] }
skipCloseAnimationChanged: function() { [native code] }
windowRoleChanged: function() { [native code] }
windowClassChanged: function() { [native code] }
surfaceChanged: function() { [native code] }
shadowChanged: function() { [native code] }
bufferGeometryChanged: function() { [native code] }
frameGeometryChanged: function() { [native code] }
clientGeometryChanged: function() { [native code] }
frameGeometryAboutToChange: function() { [native code] }
visibleGeometryChanged: function() { [native code] }
tileChanged: function() { [native code] }
requestedTileChanged: function() { [native code] }
fullScreenChanged: function() { [native code] }
skipTaskbarChanged: function() { [native code] }
skipPagerChanged: function() { [native code] }
skipSwitcherChanged: function() { [native code] }
iconChanged: function() { [native code] }
activeChanged: function() { [native code] }
keepAboveChanged: function() { [native code] }
keepBelowChanged: function() { [native code] }
demandsAttentionChanged: function() { [native code] }
desktopsChanged: function() { [native code] }
activitiesChanged: function() { [native code] }
minimizedChanged: function() { [native code] }
paletteChanged: function() { [native code] }
colorSchemeChanged: function() { [native code] }
captionChanged: function() { [native code] }
captionNormalChanged: function() { [native code] }
maximizedAboutToChange: function() { [native code] }
maximizedChanged: function() { [native code] }
transientChanged: function() { [native code] }
modalChanged: function() { [native code] }
quickTileModeChanged: function() { [native code] }
moveResizedChanged: function() { [native code] }
moveResizeCursorChanged: function() { [native code] }
interactiveMoveResizeStarted: function() { [native code] }
interactiveMoveResizeStepped: function() { [native code] }
interactiveMoveResizeFinished: function() { [native code] }
closeableChanged: function() { [native code] }
minimizeableChanged: function() { [native code] }
shadeableChanged: function() { [native code] }
maximizeableChanged: function() { [native code] }
desktopFileNameChanged: function() { [native code] }
applicationMenuChanged: function() { [native code] }
hasApplicationMenuChanged: function() { [native code] }
applicationMenuActiveChanged: function() { [native code] }
unresponsiveChanged: function() { [native code] }
decorationChanged: function() { [native code] }
hiddenChanged: function() { [native code] }
hiddenByShowDesktopChanged: function() { [native code] }
lockScreenOverlayChanged: function() { [native code] }
readyForPaintingChanged: function() { [native code] }
maximizeGeometryRestoreChanged: function() { [native code] }
fullscreenGeometryRestoreChanged: function() { [native code] }
offscreenRenderingChanged: function() { [native code] }
targetScaleChanged: function() { [native code] }
nextTargetScaleChanged: function() { [native code] }
closeWindow: function() { [native code] }
setReadyForPainting: function() { [native code] }
setMaximize: function() { [native code] }
```
### KWin::X11Window(0x5592f29e0980)
```
---- dumping properties ----
objectName:
bufferGeometry: QRectF(314, 1468, 1876, 1171)
clientGeometry: QRectF(314, 1468, 1876, 1171)
pos: QPointF(313, 1440)
size: QSizeF(1878, 1200)
x: 313
y: 1440
width: 1878
height: 1200
opacity: 1
output: KWin::DrmOutput(0x5592eff8adc0)
rect: QRectF(0, 0, 1878, 1200)
resourceName: emacs
resourceClass: Emacs
windowRole:
desktopWindow: false
dock: false
toolbar: false
menu: false
normalWindow: true
dialog: false
splash: false
utility: false
dropdownMenu: false
popupMenu: false
tooltip: false
notification: false
criticalNotification: false
appletPopup: false
onScreenDisplay: false
comboBox: false
dndIcon: false
windowType: 0
managed: true
deleted: false
skipsCloseAnimation: false
popupWindow: false
outline: false
internalId: {bd072701-71cf-4ad0-acc1-5bbaf97604d5}
pid: 30240
stackingOrder: 2
fullScreen: false
fullScreenable: true
active: false
desktops: KWin::VirtualDesktop(0x5592f0c4f400)
onAllDesktops: false
activities: 02f09950-876c-4bf6-94c0-361b1ff5aa9f
skipTaskbar: false
skipPager: false
skipSwitcher: false
closeable: true
icon: QVariant(QIcon, QIcon("emacs",availableSizes[normal,Off]=QList(QSize(16, 16), QSize(22, 22), QSize(32, 32), QSize(48, 48), QSize(64, 64), QSize(128, 128), QSize(256, 256)),cacheKey=0x1600000000))
keepAbove: false
keepBelow: false
shadeable: true
shade: false
minimizable: true
minimized: false
iconGeometry: QRectF(2191, 1651, 42, 50)
specialWindow: false
demandsAttention: false
caption: magit: ww-run-raise
captionNormal: magit: ww-run-raise
minSize: QSizeF(25, 18)
maxSize: QSizeF(2.14748e+09, 2.14748e+09)
wantsInput: true
transient: false
transientFor: null
modal: false
frameGeometry: QRectF(313, 1440, 1878, 1200)
move: false
resize: false
decorationHasAlpha: true
noBorder: false
providesContextHelp: false
maximizable: true
maximizeMode: 0
moveable: true
moveableAcrossScreens: true
resizeable: true
desktopFileName: emacs
hasApplicationMenu: false
applicationMenuActive: false
unresponsive: false
colorScheme: kdeglobals
layer: 2
hidden: false
tile: null
inputMethod: false
objectNameChanged: function() { [native code] }
stackingOrderChanged: function() { [native code] }
shadeChanged: function() { [native code] }
opacityChanged: function() { [native code] }
damaged: function() { [native code] }
inputTransformationChanged: function() { [native code] }
closed: function() { [native code] }
outputChanged: function() { [native code] }
skipCloseAnimationChanged: function() { [native code] }
windowRoleChanged: function() { [native code] }
windowClassChanged: function() { [native code] }
surfaceChanged: function() { [native code] }
shadowChanged: function() { [native code] }
bufferGeometryChanged: function() { [native code] }
frameGeometryChanged: function() { [native code] }
clientGeometryChanged: function() { [native code] }
frameGeometryAboutToChange: function() { [native code] }
visibleGeometryChanged: function() { [native code] }
tileChanged: function() { [native code] }
requestedTileChanged: function() { [native code] }
fullScreenChanged: function() { [native code] }
skipTaskbarChanged: function() { [native code] }
skipPagerChanged: function() { [native code] }
skipSwitcherChanged: function() { [native code] }
iconChanged: function() { [native code] }
activeChanged: function() { [native code] }
keepAboveChanged: function() { [native code] }
keepBelowChanged: function() { [native code] }
demandsAttentionChanged: function() { [native code] }
desktopsChanged: function() { [native code] }
activitiesChanged: function() { [native code] }
minimizedChanged: function() { [native code] }
paletteChanged: function() { [native code] }
colorSchemeChanged: function() { [native code] }
captionChanged: function() { [native code] }
captionNormalChanged: function() { [native code] }
maximizedAboutToChange: function() { [native code] }
maximizedChanged: function() { [native code] }
transientChanged: function() { [native code] }
modalChanged: function() { [native code] }
quickTileModeChanged: function() { [native code] }
moveResizedChanged: function() { [native code] }
moveResizeCursorChanged: function() { [native code] }
interactiveMoveResizeStarted: function() { [native code] }
interactiveMoveResizeStepped: function() { [native code] }
interactiveMoveResizeFinished: function() { [native code] }
closeableChanged: function() { [native code] }
minimizeableChanged: function() { [native code] }
shadeableChanged: function() { [native code] }
maximizeableChanged: function() { [native code] }
desktopFileNameChanged: function() { [native code] }
applicationMenuChanged: function() { [native code] }
hasApplicationMenuChanged: function() { [native code] }
applicationMenuActiveChanged: function() { [native code] }
unresponsiveChanged: function() { [native code] }
decorationChanged: function() { [native code] }
hiddenChanged: function() { [native code] }
hiddenByShowDesktopChanged: function() { [native code] }
lockScreenOverlayChanged: function() { [native code] }
readyForPaintingChanged: function() { [native code] }
maximizeGeometryRestoreChanged: function() { [native code] }
fullscreenGeometryRestoreChanged: function() { [native code] }
offscreenRenderingChanged: function() { [native code] }
targetScaleChanged: function() { [native code] }
nextTargetScaleChanged: function() { [native code] }
closeWindow: function() { [native code] }
setReadyForPainting: function() { [native code] }
setMaximize: function() { [native code] }
shapeChanged: function() { [native code] }
updateCaption: function() { [native code] }
```
## workspace KWin::QtScriptWorkspaceWrapper(0x5592f0d1cdf0)
```
---- dumping properties ----
objectName:
desktops: KWin::VirtualDesktop(0x5592f0c25250),KWin::VirtualDesktop(0x5592f0c4f5d0),KWin::VirtualDesktop(0x5592f0c4f400)
currentDesktop: KWin::VirtualDesktop(0x5592f0c4f5d0)
activeWindow: KWin::XdgToplevelWindow(0x5592f296aed0)
desktopGridSize: QSize(3, 1)
desktopGridWidth: 3
desktopGridHeight: 1
workspaceWidth: 7680
workspaceHeight: 2640
workspaceSize: QSize(7680, 2640)
activeScreen: KWin::DrmOutput(0x5592eff8adc0)
screens: KWin::DrmOutput(0x5592eff8adc0),KWin::DrmOutput(0x5592f294b1f0)
screenOrder: KWin::DrmOutput(0x5592eff8adc0),KWin::DrmOutput(0x5592f294b1f0)
currentActivity: 02f09950-876c-4bf6-94c0-361b1ff5aa9f
activities: 02f09950-876c-4bf6-94c0-361b1ff5aa9f
virtualScreenSize: QSize(2560, 2640)
virtualScreenGeometry: QRect(0, 0, 2560, 2640)
stackingOrder: KWin::LayerShellV1Window(0x5592f15e47d0),KWin::LayerShellV1Window(0x5592f1bec0b0),KWin::X11Window(0x5592f29e0980),KWin::XdgToplevelWindow(0x5592f1918170),KWin::XdgToplevelWindow(0x5592f1aed9f0),KWin::XdgToplevelWindow(0x5592f2331140),KWin::X11Window(0x5592f2605ef0),KWin::XdgToplevelWindow(0x5592f228e940),KWin::XdgToplevelWindow(0x5592f296aed0),KWin::LayerShellV1Window(0x5592f1343f70)
cursorPos: QPoint(1245, 630)
objectNameChanged: function() { [native code] }
windowAdded: function() { [native code] }
windowRemoved: function() { [native code] }
windowActivated: function() { [native code] }
desktopsChanged: function() { [native code] }
desktopLayoutChanged: function() { [native code] }
screensChanged: function() { [native code] }
screenOrderChanged: function() { [native code] }
currentActivityChanged: function() { [native code] }
activitiesChanged: function() { [native code] }
activityAdded: function() { [native code] }
activityRemoved: function() { [native code] }
virtualScreenSizeChanged: function() { [native code] }
virtualScreenGeometryChanged: function() { [native code] }
currentDesktopChanged: function() { [native code] }
cursorPosChanged: function() { [native code] }
slotSwitchDesktopNext: function() { [native code] }
slotSwitchDesktopPrevious: function() { [native code] }
slotSwitchDesktopRight: function() { [native code] }
slotSwitchDesktopLeft: function() { [native code] }
slotSwitchDesktopUp: function() { [native code] }
slotSwitchDesktopDown: function() { [native code] }
slotSwitchToNextScreen: function() { [native code] }
slotSwitchToPrevScreen: function() { [native code] }
slotSwitchToRightScreen: function() { [native code] }
slotSwitchToLeftScreen: function() { [native code] }
slotSwitchToAboveScreen: function() { [native code] }
slotSwitchToBelowScreen: function() { [native code] }
slotWindowToNextScreen: function() { [native code] }
slotWindowToPrevScreen: function() { [native code] }
slotWindowToRightScreen: function() { [native code] }
slotWindowToLeftScreen: function() { [native code] }
slotWindowToAboveScreen: function() { [native code] }
slotWindowToBelowScreen: function() { [native code] }
slotToggleShowDesktop: function() { [native code] }
slotWindowMaximize: function() { [native code] }
slotWindowMaximizeVertical: function() { [native code] }
slotWindowMaximizeHorizontal: function() { [native code] }
slotWindowMinimize: function() { [native code] }
slotWindowShade: function() { [native code] }
slotWindowRaise: function() { [native code] }
slotWindowLower: function() { [native code] }
slotWindowRaiseOrLower: function() { [native code] }
slotActivateAttentionWindow: function() { [native code] }
slotWindowMoveLeft: function() { [native code] }
slotWindowMoveRight: function() { [native code] }
slotWindowMoveUp: function() { [native code] }
slotWindowMoveDown: function() { [native code] }
slotWindowExpandHorizontal: function() { [native code] }
slotWindowExpandVertical: function() { [native code] }
slotWindowShrinkHorizontal: function() { [native code] }
slotWindowShrinkVertical: function() { [native code] }
slotWindowQuickTileLeft: function() { [native code] }
slotWindowQuickTileRight: function() { [native code] }
slotWindowQuickTileTop: function() { [native code] }
slotWindowQuickTileBottom: function() { [native code] }
slotWindowQuickTileTopLeft: function() { [native code] }
slotWindowQuickTileTopRight: function() { [native code] }
slotWindowQuickTileBottomLeft: function() { [native code] }
slotWindowQuickTileBottomRight: function() { [native code] }
slotSwitchWindowUp: function() { [native code] }
slotSwitchWindowDown: function() { [native code] }
slotSwitchWindowRight: function() { [native code] }
slotSwitchWindowLeft: function() { [native code] }
slotIncreaseWindowOpacity: function() { [native code] }
slotLowerWindowOpacity: function() { [native code] }
slotWindowOperations: function() { [native code] }
slotWindowClose: function() { [native code] }
slotWindowMove: function() { [native code] }
slotWindowResize: function() { [native code] }
slotWindowAbove: function() { [native code] }
slotWindowBelow: function() { [native code] }
slotWindowOnAllDesktops: function() { [native code] }
slotWindowFullScreen: function() { [native code] }
slotWindowNoBorder: function() { [native code] }
slotWindowToNextDesktop: function() { [native code] }
slotWindowToPreviousDesktop: function() { [native code] }
slotWindowToDesktopRight: function() { [native code] }
slotWindowToDesktopLeft: function() { [native code] }
slotWindowToDesktopUp: function() { [native code] }
slotWindowToDesktopDown: function() { [native code] }
sendClientToScreen: function() { [native code] }
showOutline: function() { [native code] }
hideOutline: function() { [native code] }
screenAt: function() { [native code] }
tilingForScreen: function() { [native code] }
clientArea: function() { [native code] }
createDesktop: function() { [native code] }
removeDesktop: function() { [native code] }
supportInformation: function() { [native code] }
raiseWindow: function() { [native code] }
getClient: function() { [native code] }
windowAt: function() { [native code] }
isEffectActive: function() { [native code] }
windowList: function() { [native code] }
```
