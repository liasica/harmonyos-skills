---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-landscape-and-portrait-development
title: 视频类应用横竖屏切换
breadcrumb: 最佳实践 > 行业场景解决方案 > 影音娱乐 > 视频类应用横竖屏切换
category: best-practices
scraped_at: 2026-04-29T14:13:14+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:c6ddcf58d638c6674ebce5dfc021cb565969a36468982e1c2ef755502a323c3e
---

## 概述

视频类应用横竖屏切换是指在视频类应用中，播放界面的详情页采用竖屏方式显示，用户可通过全屏按钮将页面切换至横屏方式显示，从而提供更佳的观看体验。

当前HarmonyOS应用开发主要通过以下两种方式实现视频横竖屏切换：

* 设置窗口的旋转策略，旋转整个窗口。
* 跳转到不同显示方向的页面，仅旋转子页面。

本文提供了上述两种方式的具体实现方案，开发者可根据应用自身体验的诉求进行选择，以实现视频横竖屏切换的效果。

* [通过窗口旋转实现横竖屏切换](bpta-landscape-and-portrait-development.md#section208869314175)
* [通过页面跳转实现横竖屏切换](bpta-landscape-and-portrait-development.md#section161651074615)

## 窗口旋转说明

目前HarmonyOS系统中的窗口旋转形态有四种，对应真机实际状态如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/VP_SaH25SQKh-M-4aPYvjw/zh-cn_image_0000002553741749.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=E5398BA5C068D7FB2D206A94C4AA3BDAF850558284560A081FD24ED5804BA1E6 "点击放大")

开发者可通过以下两种方式设置窗口旋转策略：

* 通过module.json5文件中的“orientation”字段进行设置。
* 调用窗口管理的[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口进行设置。

说明

上述两种方式设置窗口旋转策略的时机不同。

* module.json5文件中的“orientation”字段在窗口启动时就会生效，通常用于应用启动时就需要设置横屏或者竖屏的场景。
* [setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口在调用时进行窗口方向的设置，通常用于在应用启动之后，还需要改变显示方向的场景。

### 配置module.json5文件中的orientation字段

orientation字段用于配置应用启动时的窗口显示状态。如果应用启动时需要以默认的横屏或竖屏方式显示，建议在此字段进行相应配置。其支持的参数可参考module.json5配置项中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下的orientation字段说明。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. // Set default window orientation
9. "orientation": "portrait",
10. // ...
11. }
12. ],
13. // ...
14. "requestPermissions": [
15. {
16. "name": "ohos.permission.ACCELEROMETER"
17. }
18. ]
19. }
20. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/module.json5#L2-L67)

开发者可根据应用的默认旋转行为配置orientation字段：

* 如果应用是竖屏应用，建议配置portrait为默认旋转策略。
* 如果应用是横屏应用，如游戏类应用，启动时默认为横屏，存在以下两种情况：
  + 仅支持横屏，建议配置landscape为默认旋转策略。
  + 支持在横屏和反向横屏中切换，建议配置为auto\_rotation\_landscape。
* 如果应用是可旋转应用，建议配置auto\_rotation\_restricted为默认旋转策略。
* 如果一个应用在直板机和折叠屏折叠态为竖屏应用，在平板和折叠屏展开态默认为可旋转应用，建议配置follow\_desktop为默认旋转策略。

注意

对于需要通过控制中心进行旋转锁定控制的场景，可选择带有“restricted”后缀的旋转策略。带有此后缀的字段表示旋转行为受控制中心的旋转锁定开关控制：当旋转锁定开关开启时，窗口不会随传感器旋转；关闭时，窗口将随传感器旋转。

以如下应用为例，关闭控制中心的旋转锁定开关后，应用页面会随手机旋转而切换；开启旋转锁定开关后，则不会发生切换。需将orientation字段配置为auto\_rotation\_restricted以实现此效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/DphMuPx6QWCHObBYiwb-qg/zh-cn_image_0000002522821800.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=24E5BA4C9CD7C289B496BEA97BC85048B21A02E841867A2F809EE31DC76B8127 "点击放大")

### 调用窗口管理的setPreferredOrientation()接口

对于需要实现横竖屏切换的应用，可调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口进行设置。典型场景包括视频类和图片类应用，视频类应用实现横竖屏切换的效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/eLTzvQ5oTMCSj7oVHJo_YA/zh-cn_image_0000002553861703.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=EB3187D72A27D4394AFEE603BC713B2A78720A9BB26AAEB4EE1A76A9DB941053 "点击放大")

此类应用启动时默认为竖屏，而在视频播放页面可横屏显示，开发者需确保应用支持用户临时更改窗口显示方向。使用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口修改窗口显示方向时，窗口将保持最后一次设置的方向。即使页面跳转，窗口显示方向也不会改变。

## 通过窗口旋转实现横竖屏切换

为了实现应用的横竖屏功能，需从以下技术方面考虑：

1. 设置窗口的旋转策略。
2. 监听屏幕的窗口变化。
3. 进行布局适配。

### 设置窗口的旋转策略

首先需要设置应用启动时的旋转策略，具体可以参考[配置module.json5文件中的orientation字段](bpta-landscape-and-portrait-development.md#section1188593118171)。以多设备开发为例，为满足直板机和平板设备的不同策略，可将orientation字段设置为follow\_desktop。

在需要实现横竖屏切换的页面上，可调用窗口管理提供的[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口，将窗口显示的方向修改为横屏或竖屏的状态。例如，视频播放页面既支持竖屏，也支持横屏，可调用此接口实现横竖屏切换。

在使用setPreferredOrientation()接口时，应根据应用自身的旋转策略选择相应的参数，可封装如下方法以设置旋转策略。具体步骤如下：

1. 通过this.getUIContext().[getHostContext()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)接口获取对应的UIAbilityContext，并通过context获取对应的windowStage实例。
2. 通过windowStage.[getMainWindowSync()](../harmonyos-references/arkts-apis-window-windowstage.md#getmainwindowsync9)同步接口获取对应的窗口实例windowClass，再调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口设置窗口方向。

```
1. @Component
2. export struct VideoPlayView {
3. // ...
4. private windowClass: window.Window | undefined;
5. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
6. // ...
7. aboutToAppear(): void {
8. // ...
9. this.windowClass = this.context.windowStage.getMainWindowSync();  // Obtains the window instance
10. // ...
11. }
12. // ...

14. // Set window orientation.
15. setOrientation(orientation: window.Orientation) {
16. // Encapsulates the setPreferredOrientation interface
17. this.windowClass?.setPreferredOrientation(orientation).then(() => {
18. Logger.info(`setWin0dowOrientation ${orientation} Succeeded`);
19. }).catch((err: BusinessError) => {
20. let error = err as BusinessError;
21. Logger.error(TAG, `setWindowOrientation ${orientation} err, code: ${error.code}, message: ${error.message}`);
22. })
23. }
24. // ...
25. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L26-L293)

以视频播放为例，不仅需要通过设备旋转方向控制横竖屏，还需在旋转锁定开关开启时，支持用户手动设置横屏状态。若开发者需实现以上效果，应满足以下条件：

1. 应用跟随传感器旋转。
2. 应用受到控制中心的旋转锁定开关控制。
3. 应用支持用户临时设置窗口方向，例如：点击全屏按钮进行切换。

如果应用满足上述条件，可使用窗口管理的[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口设置orientation的枚举类型，以实现相应的旋转。当用户手动点击全屏按钮时，需触发横竖屏切换。如果此时关闭旋转锁定开关，窗口将随传感器旋转。因此，可使用以下枚举中的能力，临时旋转窗口，并使其后续跟随传感器自动旋转。

**表1** orientation部分参数列举

| orientation枚举值 | 枚举数值 | 效果描述 |
| --- | --- | --- |
| USER\_ROTATION\_PORTRAIT | 13 | 调用时临时旋转到竖屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |
| USER\_ROTATION\_LANDSCAPE | 14 | 调用时临时旋转到横屏，之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。 |

一般情况下，视频播放应用的窗口不会旋转至反向竖屏（由UX需求决定），仅支持旋转至竖屏、横屏和反向横屏。点击全屏按钮时，窗口默认旋转至横屏状态，并支持跟随传感器旋转至反向横屏。竖屏状态和横屏状态的窗口示意图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/ZdpSvDpITdylgbihiTv9gg/zh-cn_image_0000002522661810.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=06622CCB8EC5EA99E599572CBAF0D6306823DB9D27F5EAF589E83F67EA0DB1AB "点击放大")

当用户点击进入或退出全屏时，应分别触发对应的逻辑处理，所需使用的方向状态如下：

设置为横屏时，对应窗口显示方向设置为USER\_ROTATION\_LANDSCAPE模式，将窗口临时旋转到横屏。例如进入播放页时，进行竖屏 -> 横屏切换。

```
1. SymbolGlyph($r('sys.symbol.arrow_up_left_and_arrow_down_right'))
2. // ...
3. .onClick(() => {
4. if (WindowUtils.isExpandedOrHalfFolded()) {
5. // When the device is folded or half-folded,
6. // the playback mode is set to landscape mode, and the window rotation is set to auto-rotate.
7. this.isLandscape = true;
8. this.setOrientation(window.Orientation.AUTO_ROTATION);
9. } else {
10. // In a non-expanded state, such as when folded, set the window orientation to landscape.
11. this.setOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);
12. }
13. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L256-L279)

设置为竖屏时，对应窗口显示方向设置为USER\_ROTATION\_PORTRAIT模式，将窗口临时旋转到竖屏。例如在返回竖屏状态时，进行横屏 -> 竖屏切换。

```
1. Button({ type: ButtonType.Circle }) {
2. SymbolGlyph($r('sys.symbol.chevron_backward'))
3. .fontColor([$r('sys.color.icon_on_primary')])
4. .fontSize($r('sys.float.Title_M'))
5. }
6. // ...
7. .onClick(() => {
8. // Exit the current page if not in landscape mode
9. if (!this.isLandscape) {
10. this.navStack?.pop();
11. return;
12. }
13. // ...
14. // Set the window orientation to portrait
15. this.setOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
16. // ...
17. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L183-L213)

注意

调用[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)接口会改变窗口的显示方向。因此，如果在进入视频播放页时手动调用此接口，将窗口旋转至横屏，那么在退出页面时也应调用此接口，将窗口恢复为竖屏。

### 监听窗口变化

当传感器变化或用户手动设置窗口方向时，窗口显示和尺寸将发生变化。此时，应使用窗口尺寸对布局进行适配。

在需要进行横竖屏切换的页面，通过window.[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)接口监听窗口尺寸的变化。建议在aboutToAppear()函数中执行，具体措施如下：

```
1. // Listen for window size changes.
2. this.windowClass.on('windowSizeChange', (size) => {
3. // ...
4. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L65-L100)

并在aboutToDisappear()函数中取消监听：

```
1. aboutToAppear(): void {
2. // Remove window size listener
3. WindowUtils.windowClass.off('windowSizeChange');
4. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/pages/Index.ets#L96-L99)

需要注意的是，当应用不随传感器旋转时，如果用户手动触发setOrientation()方法将窗口设置为横屏状态，即使当前手机处于垂直方向，窗口仍会保持横屏状态。此时，窗口的宽度为竖屏状态下的高度，高度则为竖屏状态下的宽度。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/OV8YbPsJRMm3m8zaOk-wIA/zh-cn_image_0000002553741751.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=D008CF05D5238EB60B733FEF65F368709FBC020385EB189FF617AA04539F3487 "点击放大")

进入视频详情页面时，需监听窗口尺寸的变化，并依据状态变化调整XComponent的宽高。

```
1. // Listen for window size changes.
2. this.windowClass.on('windowSizeChange', (size) => {
3. // Detect screen orientation in the window resize listener
4. this.windowHeight = this.getUIContext().px2vp(size.height);
5. this.windowWidth = this.getUIContext().px2vp(size.width);
6. this.setXComponentSize();
7. // ...
8. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L66-L99)

### 进行布局适配

对于视频播放类应用，仅播放窗口需支持横竖屏切换。因此，只需对视频播放组件进行横屏及全屏处理。开发者可利用UI状态更新的特点，使播放窗口切换为全屏。

将播放窗口的尺寸定义为@State状态，并设置到[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件上。

```
1. @State xComponentWidth: number = 0;
2. @State xComponentHeight: number = 0;
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L33-L34)

将状态变量与视频播放组件绑定。

```
1. XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.xComponentController })
2. .onLoad(() => {
3. // ...
4. })
5. // Bind the width and height state variables to the XComponent.
6. .width(this.xComponentWidth)
7. .height(this.xComponentHeight)
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L154-L175)

在监听窗口变化的回调中，动态调整XComponentWidth和XComponentHeight，以适配横屏和竖屏视频播放组件的布局。横屏时，视频播放组件的宽高应与窗口的宽高一致，并进入全屏状态。竖屏时，视频播放组件的宽度与窗口宽度相等，高度则按视频播窗比例乘以窗口宽度，并退出全屏状态。旋转过程宽高属性如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/4VoKg1YdQw-VponlUvJAOg/zh-cn_image_0000002522821802.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=D7F632E68C533076931EC92ED79C20845DC01906AB61EAA0F0F1B729C4351F1F "点击放大")

在监听窗口变化时，可调用[display.getDefaultDisplaySync()](../harmonyos-references/js-apis-display.md#displaygetdefaultdisplaysync9)接口获取屏幕的display对象，依据display对象的Orientation属性决定实际的横竖屏状态。然后根据横竖屏状态和折叠屏的折叠状态设置旋转策略，具体实现如下：

注意

需要注意的是，对于视频全屏效果，建议采用沉浸式开发。沉浸式效果的实现，可参考[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)。

```
1. // Listen for window size changes.
2. this.windowClass.on('windowSizeChange', (size) => {
3. // Detect screen orientation in the window resize listener
4. this.windowHeight = this.getUIContext().px2vp(size.height);
5. this.windowWidth = this.getUIContext().px2vp(size.width);
6. this.setXComponentSize();
7. let displayClass: display.Display = display.getDefaultDisplaySync();
8. let orientation: display.Orientation = displayClass.orientation;

10. if (orientation === display.Orientation.LANDSCAPE || orientation === display.Orientation.LANDSCAPE_INVERTED) {
11. // Set full-screen playback to true in landscape mode
12. this.isLandscape = true;
13. } else {
14. if (!WindowUtils.isExpandedOrHalfFolded() && !this.isVideoLock) {
15. // When not expanded and unlocked, set the fullscreen playback flag to false
16. this.isLandscape = false;
17. this.setOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
18. }
19. }
20. // Folded mode landscape playback, set to auto-rotate with the sensor
21. if (this.isLandscape && WindowUtils.isFolded() && this.isVideoLock) {
22. this.setOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
23. }
24. // Play in full-screen mode and set to rotate automatically according to the sensor
25. if (this.isLandscape && WindowUtils.isExpandedOrHalfFolded()) {
26. this.setOrientation(window.Orientation.AUTO_ROTATION);
27. }
28. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L67-L98)

### 锁定屏幕功能

某些视频应用支持锁定屏幕功能，在全屏状态下，可隐藏功能按钮并临时锁定屏幕旋转，以防止用户误触其他操作按钮。屏幕锁定后，应用可在横屏和反向横屏间切换，但不能从横屏切换至竖屏；解锁后，如果当前屏幕为竖屏，则应恢复为竖屏显示。全屏状态下锁定屏幕功能如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/15SLS60DTOW5KGpuj-DOuA/zh-cn_image_0000002553861705.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=7229878C43024BDFDCCFF0B8E949698755A4308320F92D70E5991F5DD930F3E4 "点击放大")

开发者应考虑以下三种情况以实现上述功能：

1. 判断当前旋转锁定开关的状态，若已开启，则无需进行额外处理。
2. 点击锁定屏幕按钮时，设置旋转策略为AUTO\_ROTATION\_LANDSCAPE，即支持在横屏和反向横屏间切换，不受旋转锁定开关控制。
3. 点击解锁按钮时，需支持在横屏、竖屏和反向横屏间切换，并受旋转锁定开关控制。

可依据上述推断功能实现如下代码：

```
1. Image(this.isVideoLock ? $r('app.media.icon_lock') : $r('app.media.icon_lock_open'))
2. // ...
3. .onClick(() => {
4. // Set video lock status
5. this.isVideoLock = !this.isVideoLock;
6. // ...
7. if (this.isVideoLock) {
8. // If landscape mode is locked, then set to AUTO_ROTATION_LANDSCAPE.
9. this.setOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
10. } else {
11. // Otherwise, set the window orientation to auto-rotate.
12. this.setOrientation(window.Orientation.AUTO_ROTATION);
13. }
14. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L219-L250)

若开发者需对折叠屏的旋转逻辑进行单独处理，可封装如下方法isExpandedOrHalfFolded()，以判断当前设备是否为折叠屏展开态。当设备处于折叠屏展开态时，不触发旋转逻辑。

```
1. static isExpandedOrHalfFolded(): boolean {
2. let isExpandedOrHalfFolded: boolean = false;
3. try {
4. isExpandedOrHalfFolded = display.getFoldStatus() === display.FoldStatus.FOLD_STATUS_EXPANDED ||
5. display.getFoldStatus() === display.FoldStatus.FOLD_STATUS_HALF_FOLDED
6. } catch (err) {
7. let error = err as BusinessError;
8. Logger.error(TAG, `isExpandedOrHalfFolded err, error code: ${error.code}, error message: ${error.message}`);
9. }
10. return isExpandedOrHalfFolded;
11. }
```

[WindowUtils.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/utils/WindowUtils.ets#L79-L89)

当开发者需监听设备控制中心的状态时，可使用[setting.registerKeyObserver()](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)接口。其中，[general](../harmonyos-references/js-apis-settings.md#general).ACCELEROMETER\_ROTATION\_STATUS表示是否启用自动旋转。当返回值为“0”时，即代表旋转锁定开关开启，此时在处理锁定功能的代码中无需执行旋转逻辑。可参考以下代码实现对设备控制中心状态的监听：

```
1. // Monitor the status of the rotation lock switch in the status bar
2. settings.registerKeyObserver(this.context, settings.general.ACCELEROMETER_ROTATION_STATUS,
3. settings.domainName.DEVICE_SHARED, () => {
4. this.orientationLockState =
5. settings.getValueSync(this.context, settings.general.ACCELEROMETER_ROTATION_STATUS,
6. settings.domainName.DEVICE_SHARED);
7. })
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L133-L139)

当控制中心的旋转锁定开关关闭时，可通过应用内的锁定按钮进行逻辑判断。在锁定状态下，调用setOrientation()方法将显示方向设置为AUTO\_ROTATION\_LANDSCAPE模式，此时可旋转至横屏和反向横屏；解锁后，将显示方向设置为AUTO\_ROTATION\_UNSPECIFIED模式，此时可旋转至横屏、竖屏、反向横屏三个方向。

```
1. if (this.isVideoLock) {
2. // If landscape mode is locked, then set to AUTO_ROTATION_LANDSCAPE.
3. this.setOrientation(window.Orientation.AUTO_ROTATION_LANDSCAPE);
4. } else {
5. // Otherwise, set the window orientation to auto-rotate.
6. this.setOrientation(window.Orientation.AUTO_ROTATION);
7. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L242-L248)

## 通过页面跳转实现横竖屏切换

开发者可分别创建竖屏页面和横屏页面，并通过页面级分层旋转的方式实现横竖屏切换。

### 分层旋转的实现原理

在视频类应用中，屏幕最终显示的画面可分为视频图层（视频播放组件）、UI图层（UI组件）和系统图层（状态栏、导航栏）。页面级分层旋转是指通过页面跳转实现横竖屏切换，页面切换时仅旋转视频图层。实现原理如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/r98-yttjR2C1MIV-R4YiAA/zh-cn_image_0000002522661812.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=EDA12C1545CB57F533F28DEC2D6F7BA630DF3D065176F9F8C2CE3E47068BC86A "点击放大")

1. 通过NavDestination的[preferredOrientation](../harmonyos-references/ts-basic-components-navdestination.md#preferredorientation19)属性设置页面的显示方向，并使用[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)实现页面切换。
2. 使用[自定义声明式节点 (BuilderNode)](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)挂载视频播放组件，并通过[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)实现视频节点在页面之间迁移，可参考[实现视频播放节点的迁移](bpta-landscape-and-portrait-development.md#section015175011467)。
3. 通过Navigation的自定义转场动画回调（[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)）配置自定义导航动画，可参考[自定义页面转场动画](bpta-landscape-and-portrait-development.md#section029702318474)。
4. 封装一镜到底转场动画实现视频旋转效果。页面切换时，在页面的转场动画回调中执行视频旋转动画，可参考[实现视频旋转动画](bpta-landscape-and-portrait-development.md#section111189303292)。

本示例通过[共享元素转场（一镜到底）](../harmonyos-guides/arkts-shared-element-transition.md)实现页面转场动画。开发者也可以根据实际场景选择适合的[转场动画](../harmonyos-guides/arkts-animation-transition.md)。

### 实现视频播放节点的迁移

说明

[BuildNode](../harmonyos-guides/arkts-user-defined-arktsnode-buildernode.md)提供了组件预构建的能力，对于初始化耗时较长的声明式组件（如XComponent），可以有效减少初始化时间，提高组件加载效率。因此，推荐使用BuildNode挂载视频播放组件。

为了实现视频在不同页面连续播放，可使用NodeContainer挂载视频播放节点，并通过NodeController移除原页面的视频节点，迁移到新页面。具体实现可分为以下四步：

1. 使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件创建视频播放组件。步骤如下：
   1. 创建[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件和[XComponentController](../harmonyos-references/ts-basic-components-xcomponent.md#xcomponentcontroller)控制器对象，并将控制器对象绑定至XComponent组件。
   2. 在XComponent的[onLoad()](../harmonyos-references/ts-basic-components-xcomponent.md#onload)事件中初始化[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)，并传入XComponent对应Surface的ID，实现视频的播放，可参考[在ArkTS侧使用SurfaceId进行渲染绘制](../harmonyos-guides/napi-xcomponent-guidelines.md#在arkts侧使用surfaceid进行渲染绘制)。
   3. 通过[全局自定义构建函数](../harmonyos-guides/arkts-builder.md#全局自定义构建函数)封装Video自定义组件，创建videoBuilder构建函数。

   ```
   1. @Component
   2. struct VideoNode {
   3. @State videoRatio: number = 16 / 9;
   4. // Create XComponentController object.
   5. private xComponentController: XComponentController = new XComponentController();
   6. private player?: AVPlayerUtil;
   7. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   8. // ...
   9. build() {
   10. XComponent({ id: 'video_player_id1', type: XComponentType.SURFACE, controller: this.xComponentController })
   11. .aspectRatio(this.videoRatio)
   12. .onLoad(() => {
   13. try {
   14. this.player = new AVPlayerUtil(this.context);
   15. // Bind XComponent to AVPlayer using ID.
   16. this.player.setSurfaceId(this.xComponentController.getXComponentSurfaceId());
   17. // Creating an AVPlayer to play video.
   18. this.player.initPlayer('videoTest.mp4', (ratio: number) => {
   19. // Set the video width/height ratio to the global state
   20. AppStorage.setOrCreate('videoRatio', ratio);
   21. })
   22. } catch (err) {
   23. let error = err as BusinessError;
   24. Logger.error(TAG, `initPlayer err, error code: ${error.code}, error message: ${error.message}`);
   25. }
   26. })
   27. }
   28. }
   29. // Build a global video playback component.
   30. @Builder
   31. export function videoBuilder() {
   32. VideoNode()
   33. .id('myVideoComponent')
   34. }
   ```

   [VideoPlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/VideoPlay.ets#L8-L50)
2. 将视频播放组件挂载至BuildNode，并通过[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)管理自定义节点。步骤如下：
   1. 使用[wrapBuilder](../harmonyos-references/ts-universal-wrapbuilder.md)封装videoBuilder构建函数。
   2. 通过调用[BuildNode](../harmonyos-references/js-apis-arkui-buildernode.md)节点的[build()](../harmonyos-references/js-apis-arkui-buildernode.md#build12)接口创建组件树。
   3. 在[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)的[makeNode()](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)回调方法中返回组件树的实体节点（[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)）。当NodeController绑定的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)组件创建时，自动将返回的节点挂载至NodeContainer组件。

   ```
   1. export class VideoNodeController extends NodeController {
   2. private static instance: VideoNodeController;
   3. private rootNode: BuilderNode<[]> | null = null;
   4. // Use wrapBuilder to encapsulate the global @Builder
   5. private wrapBuilder: WrappedBuilder<[]> = wrapBuilder(videoBuilder);
   6. private isRemove: boolean = false;
   7. // ...
   8. // Callback when the NodeContainer bound to the instance is created.
   9. makeNode(uiContext: UIContext): FrameNode | null {
   10. Logger.info(TAG, `makeNode`)
   11. // Wether to remove the node.
   12. if (this.isRemove) {
   13. return null;
   14. }
   15. if (this.rootNode === null) {
   16. this.rootNode = new BuilderNode(uiContext);
   17. // Create a component tree based on the passed wrapBuilder.
   18. this.rootNode.build(this.wrapBuilder);
   19. }
   20. // Returning the entity node of the component tree.
   21. return this.rootNode.getFrameNode();
   22. }
   23. // ...
   24. }
   ```

   [VideoNodeController.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/VideoNodeController.ets#L8-L78)
3. 在竖屏页面中，将NodeController与NodeContainer绑定。

   ```
   1. @Component
   2. export struct DetailPlay {
   3. // ...
   4. @State nodeController: VideoNodeController = VideoNodeController.getInstance();
   5. // ...
   6. build() {
   7. NavDestination() {
   8. Column() {
   9. RelativeContainer() {
   10. // Bind the NodeController to the NodeContainer
   11. NodeContainer(this.nodeController)
   12. // ...
   13. }
   14. // ...
   15. }
   16. // Set the page display orientation portrait.
   17. .preferredOrientation(window.Orientation.PORTRAIT)
   18. // ...
   19. }
   20. }
   ```

   [DetailPlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/DetailPlay.ets#L33-L239)

   在横屏页面中，将NodeController与NodeContainer绑定。

   ```
   1. @Component
   2. export struct MyPageLandscape {
   3. // ...
   4. // Obtaining the VideoNodeController instance
   5. @State nodeController: VideoNodeController = VideoNodeController.getInstance();
   6. // Page display orientation, default is landscape.
   7. @State displayOrientation: window.Orientation = window.Orientation.LANDSCAPE;
   8. // ...
   9. build() {
   10. NavDestination() {
   11. Stack() {
   12. // Bind the NodeController to the NodeContainer
   13. NodeContainer(this.nodeController)
   14. // ...
   15. }
   16. // ...
   17. }
   18. // Set the page display orientation.
   19. .preferredOrientation(this.displayOrientation)
   20. // ...
   21. })
   22. }
   23. }
   ```

   [LandscapePlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/LandscapePlay.ets#L17-L173)
4. 页面切换完成时，调用NodeController的自定义方法onRemove()移除原页面的视频节点。

   ```
   1. // This method is called when the page transition animation is completed.
   2. private doFinishTransition(): void {
   3. // ...
   4. // Remove the video node from the original page.
   5. this.nodeController.onRemove();
   6. }
   ```

   [DetailPlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/DetailPlay.ets#L95-L104)

   在自定义方法onRemove()中，将isRemove标志位设置为true，表示移除节点，然后调用[rebuild()](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)接口通知NodeContainer组件，将null挂载至[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)，实现节点移除。操作完成后，重置isRemove标志位，保证新页面的节点正常生成。

   ```
   1. onRemove(): void {
   2. Logger.info(TAG, 'onRemove')
   3. this.isRemove = true;
   4. // Trigger rebuild when the component is moved out of the node
   5. this.rebuild();
   6. this.isRemove = false;
   7. }
   ```

   [VideoNodeController.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/VideoNodeController.ets#L45-L51)

### 自定义页面转场动画

1. 创建Navigation自定义转场动画配置类CustomTransition，用于注册、获取和删除页面的动画回调，包含以下方法：
   * getInstance()：获取转场动画配置类的实例，使用静态方法在页面间共享。

     ```
     1. static delegate = new CustomTransition();
     2. // Return the CustomTransition instance.
     3. static getInstance() {
     4. return CustomTransition.delegate;
     5. }
     ```

     [CustomTransition.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/CustomTransition.ets#L32-L36)
   * registerNavParam()：当页面加载完成时，注册当前页面的动画回调。

     ```
     1. // Register the transition animation callback of the current page.
     2. registerNavParam(name: string,
     3. animationCallback: (operation: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => void,
     4. timeout: number): void {
     5. // Overwrite if already exists.
     6. if (customTransitionMap.has(name)) {
     7. let param = customTransitionMap.get(name);
     8. if (param !== undefined) {
     9. param.animation = animationCallback;
     10. param.timeout = timeout;
     11. return;
     12. }
     13. }
     14. // Creating a Transition Animation callback when it dose not exist.
     15. let params: AnimateCallback = { timeout: timeout, animation: animationCallback };
     16. customTransitionMap.set(name, params);
     17. }
     ```

     [CustomTransition.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/CustomTransition.ets#L40-L56)
   * unRegisterNavParam()：当页面卸载完成时，删除当前页面的动画回调。

     ```
     1. // Unregister the transition animation callback of the current page.
     2. unRegisterNavParam(name: string): void {
     3. customTransitionMap.delete(name);
     4. }
     ```

     [CustomTransition.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/CustomTransition.ets#L60-L63)
   * getAnimateParam()：在自定义转场动画回调方法中，通过此方法获取原页面和新页面的动画回调。

     ```
     1. // Obtain the transition animation callback.
     2. getAnimateParam(name: string): AnimateCallback {
     3. let result: AnimateCallback = {
     4. animation: customTransitionMap.get(name)?.animation,
     5. timeout: customTransitionMap.get(name)?.timeout,
     6. };
     7. return result;
     8. }
     ```

     [CustomTransition.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/CustomTransition.ets#L67-L74)
2. 在Navigation（导航页面）的[customNavContentTransition()](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)事件中实现自定义转场动画回调方法，自定义竖屏页面与横屏页面的导航转场动画。具体步骤如下：
   1. 检查原页面与新页面是否存在，其中一个不存在则返回undefined。返回值为undefined表示执行默认动画。

      ```
      1. // If the parameters related to jumping are not defined, no custom animation will be performed.
      2. if (!from || !to || !from.name || !to.name || !from.navDestinationId || !to.navDestinationId) {
      3. return undefined;
      4. }

      6. // If it is the homepage, no custom animation will be performed.
      7. if (from.index === -1 || to.index === -1) {
      8. return undefined;
      9. }

      11. // Control custom transition routes using the names of from and to.
      12. if (!isCustomTransitionEnable(from.name, to.name)) {
      13. return undefined;
      14. }
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/pages/Index.ets#L40-L53)
   2. 通过[创建Navigation自定义转场动画配置类](bpta-landscape-and-portrait-development.md#li49791041461)实现的getAnimateParam()方法获取原页面与新页面的动画回调方法。

      ```
      1. // It is necessary to check whether the transition page has registered an animation
      2. // in order to decide whether to perform a custom transition.
      3. let fromParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(from.navDestinationId);
      4. let toParam: AnimateCallback = CustomTransition.getInstance().getAnimateParam(to.navDestinationId);
      5. if (!fromParam.animation || !toParam.animation) {
      6. return undefined;
      7. }
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/pages/Index.ets#L57-L63)
   3. 创建自定义转场动画协议对象（[NavigationAnimatedTransition](../harmonyos-references/ts-basic-components-navigation.md#navigationanimatedtransition11)），定义Navigation路由跳转时的转场动画。

      ```
      1. // After all judgments are made, construct customAnimation for the system to call
      2. // and execute the custom transition animation.
      3. let customAnimation: NavigationAnimatedTransition = {
      4. // Transition Completed Callback
      5. onTransitionEnd: (isSuccess: boolean) => {
      6. Logger.info(`onTransitionEnd success: ${isSuccess}`)
      7. },
      8. // Animation timeout end time
      9. timeout: 1000,
      10. // Custom transition animation execution callback.
      11. // transitionProxy: Custom transition animation delegate object
      12. transition: (transitionProxy: NavigationTransitionProxy) => {
      13. Logger.info('customAnimation transition');
      14. // Run the current page animation
      15. if (fromParam.animation) {
      16. fromParam.animation(operation === NavigationOperation.PUSH, true, transitionProxy)
      17. }

      19. // Execute jump-to-target page animation
      20. if (toParam.animation) {
      21. toParam.animation(operation === NavigationOperation.PUSH, false, transitionProxy)
      22. }
      23. }
      24. }
      25. return customAnimation;
      26. }
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/pages/Index.ets#L67-L92)
   4. 在Navigation（导航页面）的[customNavContentTransition()](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)事件中，传入自定义转场动画回调方法。

      ```
      1. build() {
      2. Navigation(this.pageStack) {
      3. // ...
      4. }
      5. // ...
      6. // Bind custom transition animation.
      7. .customNavContentTransition(this.customTransition)
      8. }
      ```

      [Index.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/pages/Index.ets#L103-L140)

      说明

      当竖屏页面切换至横屏页面时，执行新页面的toParam.animation()动画；当横屏页面切换回竖屏页面时，执行原页面的fromParam.animation()动画。因此，只需实现横屏页面的自定义转场动画。
3. 在NavDestination的[onReady()](../harmonyos-references/ts-basic-components-navdestination.md#onready11)事件中获取[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)对象，并在横屏页面的onReady()事件中注册当前页面的动画回调。

   ```
   1. build() {
   2. // ...
   3. .onReady((ctx: NavDestinationContext) => {
   4. if (ctx.navDestinationId) {
   5. this.pageId = ctx.navDestinationId;
   6. this.stack = ctx.pathStack;
   7. let param = ctx.pathInfo.param as Record<string, object>
   8. this.nodeRectInfo = param.nodeRectInfo as RectInfoInPx;
   9. this.prePageDoFinishTransition = param.DoDefaultTransition as () => void;
   10. // Register the animation callback of the current page.
   11. CustomTransition.getInstance().registerNavParam(this.pageId,
   12. (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
   13. if (WindowUtils.isExpandedOrHalfFolded()) {
   14. // Play animation, foldable screen in unfolded state
   15. this.animationProperties.doAnimationFoldable(this.nodeRectInfo, isPush, isExit, transitionProxy,
   16. this.prePageDoFinishTransition);
   17. } else {
   18. // Perform animation, non-foldable screen expanded state
   19. this.animationProperties.doAnimation(this.nodeRectInfo, isPush, isExit, transitionProxy,
   20. this.prePageDoFinishTransition);
   21. }
   22. }, 2000);
   23. }
   24. })
   25. }
   ```

   [LandscapePlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/LandscapePlay.ets#L86-L171)

### 实现视频旋转动画

1. 使用[animateTo()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口实现旋转动画，通过设置横屏页面的[width](../harmonyos-references/ts-universal-attributes-size.md#width)、[height](../harmonyos-references/ts-universal-attributes-size.md#height)、[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate18)和[rotate](../harmonyos-references/ts-universal-attributes-transformation.md#rotate18)属性来完成，可参考[使用animateTo产生属性动画](../harmonyos-guides/arkts-attribute-animation-apis.md#使用animateto产生属性动画)。关键信息介绍如下：
   * nodeInfoPx为竖屏页面传入的视频节点尺寸信息，包括距离屏幕四周的距离和视频节点的宽高。
   * WindowUtils根据当前页面显示方向获取窗口大小。横屏页面切换至竖屏页面时，获取的是横屏页面的窗口大小，此时，WindowUtils.windowWidthPx获取的值与竖屏页面的窗口高度相等。
   * X值为直板机竖屏时视频节点中心点距离屏幕顶部的距离，Y值为直板机竖屏时视频节点中心点距离屏幕右侧的距离。根据竖屏页面视频中心点与横屏页面视频中心点坐标的差值，得出视频节点在X轴与Y轴的偏移值。如下图所示：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/fqR5WAhhQX-7xrrfSwkBNg/zh-cn_image_0000002553741753.png?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=302C5A9C58E139C60301379681B9AEB83F0E2CEDF5732BB1A35947996FFCF852 "点击放大")

   从竖屏页面切换至横屏页面时，计算可动画属性的初始值，即在竖屏页面的width、height、translateX、translateY和rotate数据。

   ```
   1. // Calculate the center point of the vertical screen
   2. let notFullCenterX: number = nodeInfoPx.top + nodeInfoPx.height / 2;
   3. let notFullCenterY: number = WindowUtils.windowWidthPx - (nodeInfoPx.left + nodeInfoPx.width / 2)
   4. // Calculate the center coordinates after landscape rotation
   5. let fullCenterX: number = WindowUtils.windowHeightPx / 2;
   6. let fullCenterY: number = nodeInfoPx.height / 2;
   7. // Offset position required to calculate the center point
   8. let initTranslateX: number = notFullCenterX - fullCenterX;
   9. let initTranslateY: number = notFullCenterY - fullCenterY;

   11. // Set the video width, height, translation, and rotation angle properties before animation.
   12. this.width = this.uiContext.px2vp(nodeInfoPx.width)
   13. this.height = this.uiContext.px2vp(nodeInfoPx.height)
   14. this.translateX = this.uiContext.px2vp(initTranslateX)
   15. this.translateY = this.uiContext.px2vp(initTranslateY)
   16. this.rotate = -90;

   18. this.uiContext.animateTo({
   19. duration: 500,
   20. curve: Curve.EaseInOut,
   21. onFinish: () => {
   22. if (transitionProxy) {
   23. // Complete transition animation
   24. transitionProxy.finishTransition();
   25. }
   26. AppStorage.setOrCreate('videoBackgroundColor', Color.Black);
   27. }
   28. }, () => {
   29. // Properties after setting the animation
   30. // Changes to properties in a closure function will trigger animation effects
   31. this.width = '100%';
   32. this.height = '100%';
   33. this.translateX = 0;
   34. this.translateY = 0;
   35. this.rotate = 0;
   36. })
   ```

   [AnimationProperties.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/AnimationProperties.ets#L44-L79)

   从横屏页面返回竖屏页面时，计算[animateTo()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)接口闭包内视频节点的可动画属性。动画执行完成后，移除横屏页面的视频节点。

   ```
   1. let notFullCenterX: number = nodeInfoPx.top + nodeInfoPx.height / 2;
   2. let notFullCenterY: number = WindowUtils.windowHeightPx - (nodeInfoPx.left + nodeInfoPx.width / 2);
   3. let fullCenterX: number = WindowUtils.windowWidthPx / 2;
   4. let fullCenterY: number = nodeInfoPx.height / 2;
   5. let initTranslateX: number = notFullCenterX - fullCenterX;
   6. let initTranslateY: number = notFullCenterY - fullCenterY;
   7. this.uiContext.animateTo({
   8. duration: 500,
   9. curve: Curve.EaseInOut,
   10. onFinish: () => {
   11. if (transitionProxy) {
   12. transitionProxy.finishTransition();
   13. }
   14. prePageOnFinish();
   15. }
   16. }, () => {
   17. // Changes to properties in a closure function will trigger animation effects
   18. this.width = this.uiContext!.px2vp(nodeInfoPx.width);
   19. this.height = this.uiContext!.px2vp(nodeInfoPx.height);
   20. this.translateX = this.uiContext!.px2vp(initTranslateX);
   21. this.translateY = this.uiContext!.px2vp(initTranslateY);
   22. this.rotate = -90;
   23. })
   ```

   [AnimationProperties.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/common/AnimationProperties.ets#L84-L106)
2. 在页面的转场动画回调方法中执行视频旋转动画。当设备状态为完全展开或半折叠时，执行doAnimationFoldable()动画，否则，执行doAnimation()动画。

   ```
   1. // Register the animation callback of the current page.
   2. CustomTransition.getInstance().registerNavParam(this.pageId,
   3. (isPush: boolean, isExit: boolean, transitionProxy: NavigationTransitionProxy) => {
   4. if (WindowUtils.isExpandedOrHalfFolded()) {
   5. // Play animation, foldable screen in unfolded state
   6. this.animationProperties.doAnimationFoldable(this.nodeRectInfo, isPush, isExit, transitionProxy,
   7. this.prePageDoFinishTransition);
   8. } else {
   9. // Perform animation, non-foldable screen expanded state
   10. this.animationProperties.doAnimation(this.nodeRectInfo, isPush, isExit, transitionProxy,
   11. this.prePageDoFinishTransition);
   12. }
   13. }, 2000);
   ```

   [LandscapePlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/LandscapePlay.ets#L154-L166)

   直板机实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/XvFg5vDOS9StEHXcBZLd1g/zh-cn_image_0000002522821804.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=86C5D6E873076764891E5083D1CC558E604E17E61DBA5543CD96CC135858CBDB "点击放大")
3. 使用[window.getLastWindow()](../harmonyos-references/arkts-apis-window-f.md#windowgetlastwindow9)接口获取应用内层级最高的窗口对象，通过[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)接口开启窗口尺寸变化的监听。当折叠屏的折叠状态切换时，视频节点宽高同步调整。

   ```
   1. window.getLastWindow(this.getUIContext().getHostContext()).then((windowClass) => {
   2. WindowUtils.windowWidthPx = windowClass.getWindowProperties().windowRect.width;
   3. WindowUtils.windowHeightPx = windowClass.getWindowProperties().windowRect.height;
   4. this.defaultVideoWidth = this.getUIContext().px2vp(WindowUtils.windowWidthPx);
   5. this.defaultVideoHeight = this.getUIContext().px2vp(WindowUtils.windowWidthPx / this.videoRatio);
   6. windowClass.on('windowSizeChange', (data) => {
   7. // ...
   8. // Updating the window size during the orientation switching between landscape and portrait modes.
   9. WindowUtils.windowWidthPx = data.width;
   10. WindowUtils.windowHeightPx = data.height;
   11. // Only dynamically change the size of the video component container
   12. // when the page is displayed, such as when collapsing or expanding.
   13. if (this.isDetailShow) {
   14. this.defaultVideoWidth = this.getUIContext().px2vp(data.width);
   15. this.defaultVideoHeight = this.getUIContext().px2vp(data.width / this.videoRatio);
   16. }
   17. // Foldable screen expanded state settings page video width and height
   18. if (WindowUtils.isExpandedOrHalfFolded() && !this.isDetailShow) {
   19. this.defaultVideoWidth = this.getUIContext().px2vp(data.width);
   20. this.defaultVideoHeight = this.getUIContext().px2vp(data.width / this.videoRatio);
   21. AppStorage.setOrCreate('defaultVideoHeight', this.defaultVideoHeight);
   22. }
   23. });
   ```

   [DetailPlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/DetailPlay.ets#L60-L85)
4. 在横屏页面折叠屏的折叠状态切换时，使用[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)接口监听并适配UI界面。
   * 当折叠屏由展开态切换为折叠态时，调用[pop()](../harmonyos-references/ts-basic-components-navigation.md#pop11)接口返回到竖屏页面，并调用竖屏页面传入的prePageDoFinishTransition()方法移除横屏页面的视频节点。开发者可根据实际业务场景返回到竖屏页面或者将显示方向设置为横屏显示。
   * 当折叠屏由折叠态切换为展开态时，仍使用竖屏的方式播放视频，因此将显示方向设置为PORTRAIT。

   ```
   1. // Handling UI adaptation for video playback with collapse and expand functionality
   2. foldStatusChangeUI() {
   3. try {
   4. let beforeFoldedStatus: display.FoldStatus = display.getFoldStatus();
   5. // Handling UI adaptation for video playback with collapse and expand functionality
   6. let callback: Callback<display.FoldStatus> = (data: display.FoldStatus) => {
   7. // Full-screen playback: Expanded / Semi-expanded -> Collapsed detail page playback
   8. if ((beforeFoldedStatus === display.FoldStatus.FOLD_STATUS_EXPANDED ||
   9. beforeFoldedStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED) &&
   10. data === display.FoldStatus.FOLD_STATUS_FOLDED) {
   11. CustomTransition.getInstance().unRegisterNavParam(this.pageId);
   12. this.stack?.pop(false);
   13. this.prePageDoFinishTransition();
   14. }
   15. // Full-screen playback: collapsed state -> expanded state full playback
   16. if (beforeFoldedStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED &&
   17. data === display.FoldStatus.FOLD_STATUS_EXPANDED) {
   18. this.displayOrientation = window.Orientation.PORTRAIT;
   19. }
   20. beforeFoldedStatus = data;
   21. };
   22. display.on('foldStatusChange', callback);
   23. } catch (err) {
   24. let error = err as BusinessError;
   25. Logger.error(TAG, `on foldStatusChangeUI err, code: ${error.code}, message: ${error.message}`);
   26. }
   27. }
   ```

   [LandscapePlay.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitionbetweenpage/LandscapePlay.ets#L47-L73)

   折叠屏实现效果：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/X24uKZy8TnOzKaaYTsXa6w/zh-cn_image_0000002553861707.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061308Z&HW-CC-Expire=86400&HW-CC-Sign=3AA69C9FAD73194F77A1FE2DD648F8542446731049CE7A005AACC33BED30BC66 "点击放大")

## 性能优化

在窗口旋转时，屏幕尺寸变化会导致界面重新布局。为提高横竖屏切换的流畅度，建议开发者进行性能优化。

**使用自定义组件冻结****功能**

横竖屏切换时，整个窗口一同旋转会导致页面重新布局。然而，实际上需要展示的可能只有播放内容，对于其他组件，可使用自定义组件冻结功能，避免因旋转引发的UI更新操作。例如，视频播放下方的详情内容，可能是单独的组件，无需与视频组件一同旋转。

```
1. @Component({ freezeWhenInactive: true })
2. // Added custom component freezing function
3. struct VideoDetailView {
4. build() {
5. Scroll() {
6. // ...
7. }
8. }
9. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L297-L310)

**对图片使用autoResize**

如果当前旋转页面包含图片，未经适当裁剪，图片过大，可以对图片设置[autoResize](../harmonyos-references/ts-basic-components-image.md#autoresize)属性，使图片裁剪到合适的大小进行绘制。该属性的作用是将组件显示区域作为绘制的图源尺寸，以减少内存占用。例如，原图尺寸为1920\*1080px，而显示区域为200\*100px，在解码时则会将采样编码降至200\*100px。

```
1. @Builder
2. function ImageItem(imageSrc: ResourceStr) {
3. Stack({}) {
4. Image(imageSrc)
5. .width('100%')
6. .height('100%')
7. .autoResize(true)// Use auto_resize attributes on images
8. .borderRadius(8)
9. .objectFit(ImageFit.Fill)
10. .backgroundColor('#1AFFFFFF')
11. }
12. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L314-L326)

**排查耗时操作**

排查当前页面是否存在冗余的OnAreaChange事件、blur模糊或linearGradient属性，这些属性较为耗时，应根据其必要性决定是否进行优化。

## 常见问题

### Tabs栏中的视频横屏播放，无法隐藏Tabs栏

**问题现象**

首页中部分视频可直接播放，无需跳转至详情页。需支持在首页直接旋转视频，当前可通过设置XComponent的宽高实现。然而，视频全屏播放后，Tabs栏不会消失，而是会随页面一同旋转并存在于页面中。

**解决方案**

进入全屏时，隐藏Tabs栏，退出全屏时，展示Tabs栏。

```
1. @Component
2. struct TabsView {
3. @State isLayoutFullScreen: boolean = false

5. build() {
6. Tabs() {
7. // ...
8. }
9. // Hide the height of the Tabs tab bar by whether the user needs to click to enter the full screen and hide it
10. .barHeight(this.isLayoutFullScreen ? 0 : 50)
11. }
12. }
```

[VideoPlayView.ets](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle/blob/master/entry/src/main/ets/transitioninpage/VideoPlayView.ets#L330-L349)

## 示例代码

* [实现视频横竖屏切换功能](https://gitcode.com/HarmonyOS_Samples/LandscapePortraitToggle)
