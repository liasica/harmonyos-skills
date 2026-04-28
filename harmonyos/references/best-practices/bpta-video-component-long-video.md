---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-component-long-video
title: 基于Video组件播放长视频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于Video播放视频系列开发实践 > 基于Video组件播放长视频
category: best-practices
scraped_at: 2026-04-28T08:20:43+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:5265170ec56a9f3c4859d33c6f283dd9197bef2fcec5ecfec7373059f136f010
---

## 概述

Video组件可用于播放视频文件并控制其播放状态。本文针对市场上主流视频播放类应用的常见场景，介绍如何基于Video组件实现长视频播放，指导开发者实现基本播控、视频首帧显示、全屏播放、跳转播放、前台小窗播放、点击按钮选择倍速、长按视频倍速、循环播放、音量设置、接入播控中心等功能。

本文主要面向初级开发者，在阅读内容前，建议先了解[视频播放 (Video)](../harmonyos-guides/arkts-common-components-video-player.md)、[Slider](../harmonyos-references/ts-basic-components-slider.md)、[基础手势](../harmonyos-references/basic-gestures.md)、[AVSession Kit](../harmonyos-guides/avsession-kit.md)相关知识。

本文主要介绍以下场景的实现：

* [基础播控](bpta-video-component-long-video.md#section42611837143314)
* [视频首帧显示](bpta-video-component-long-video.md#section144531238153517)
* [横竖屏切换和旋转感知](bpta-video-component-long-video.md#section1047075173619)
* [跳转播放](bpta-video-component-long-video.md#section15644530123614)
* [前台小窗播放](bpta-video-component-long-video.md#section1141713610409)
* [点击按钮选择倍速](bpta-video-component-long-video.md#section738062610377)
* [长按视频倍速](bpta-video-component-long-video.md#section107981344143717)
* [循环播放](bpta-video-component-long-video.md#section1024864191117)
* [音量设置](bpta-video-component-long-video.md#section131242023153813)
* [接入播控中心](bpta-video-component-long-video.md#section156851949193813)

## 基础播控

### 场景描述

通过Video组件实现视频基础播放控制能力，包括播放视频、暂停播放等操作。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/cX8J3JLRRiejlJYwicBJgg/zh-cn_image_0000002555237888.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=68FEC8A84BBDE8AC3DD405541AE6CA020456A54093AF39DD304213C44745BE07 "点击放大")

### 实现原理

通过Video组件的[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)对象控制视频播放，VideoController在底层调用[start()](../harmonyos-references/ts-media-components-video.md#start)和[pause()](../harmonyos-references/ts-media-components-video.md#pause)等方法切换视频的播放状态。

Video组件的接口和状态变化关系如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/HpgE3rYsSRufLBV_jGagJQ/zh-cn_image_0000002555078262.png?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=90E576BAE3A87AD40CB3C0B24ABB540BFB270371F0AA7A5F1EC114ECE550B61A "点击放大")

### 开发步骤

1. 创建Video视频组件。
2. 加载视频资源：设置Video的src参数，配置视频的数据源。
3. 准备视频：通过[onPrepared()](../harmonyos-references/ts-media-components-video.md#onprepared)事件，监听视频完成加载。
4. 创建Video控制器[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)。
5. 播放视频：调用VideoController的start()方法进行视频播放。
6. 暂停播放：调用VideoController的pause()方法暂停视频播放。

Video组件和Video控制器的基础使用请参考：[视频播放 (Video)](../harmonyos-guides/arkts-common-components-video-player.md)。

## 视频首帧显示

### 场景描述

长视频未播放时，显示视频资源的首帧画面或特定画面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/c_F5dnRUTTqIUTo70opp2w/zh-cn_image_0000002585797859.png?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=0BD48DEC98BE7A57EA30EBE8C11B3E20A5443A3D8DF0AE3839E5F3982BE8A5D9 "点击放大")

### 实现原理

Video组件要实现视频未播放时显示预览画面，设置方式有如下两种：

* 方案一：通过设置previewUri显示视频未播放时的预览画面，参数说明请参考：[VideoOptions对象说明](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)。

  previewUri属性设置预览画面时，在视频实际播放前，系统会优先渲染previewUri指定的图像资源，将该图像作为预览图直接渲染到Video组件显示区域，避免播放启动前的黑屏或白屏状态。
* 方案二：通过设置showFirstFrame显示视频首帧画面，参数说明请参考：[PosterOptions对象说明](../harmonyos-references/ts-media-components-video.md#posteroptions18对象说明)。

  当showFirstFrame属性设置为true时（showFirstFrame的优先级高于previewUri，此时previewUri字段不生效），系统会在初始化播放器阶段异步解码视频文件，提取时间戳为0（即首帧）的视频帧数据，作为视频首帧画面显示。

| 实现方案 | 优点 | 缺点 | 适用场景 |
| --- | --- | --- | --- |
| previewUri | 1. 灵活性高，可自定义图片内容，不依赖视频首帧。 2. 通过静态图片替代视频首帧解码，减少初始化资源消耗。 3. 支持复用已有图片资源。 | 1. 需要手动处理预览画面，代码复杂度相对较高。 2. 开发和维护的复杂性相对较高。 3. 预览图需要单独存储和加载，消耗额外存储空间。 | 适用于自定义视频封面、网络视频预加载优化或需缓存首帧图片的场景。 |
| showFirstFrame | 1. 简单易用，通过布尔值即可控制是否显示视频首帧。 2. 无需手动处理代码逻辑。 3. 只加载显示视频第一帧，资源占用相对较低。 | 1. 定制性弱，无法自定义首帧画面。 2. 当视频第一帧为空白或黑屏时，影响用户体验。 3. 网络视频需等待下载完成后才能解码显示首帧。 | 适合本地视频，对首帧实时性要求高，且希望简化代码逻辑的场景。 |

### 开发步骤

本场景以showFirstFrame为例，设置视频视频未播放时显示视频首帧画面：

```
1. Video({
2. src: this.videoSrc,
3. controller: this.videoController,
4. currentProgressRate: this.curRate, // Set playback speed.
5. posterOptions: {
6. showFirstFrame: true,
7. }
8. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L406-L417)

previewUri使用示例请参考：[视频播放基础用法](../harmonyos-references/ts-media-components-video.md#示例1视频播放基础用法)。

## 横竖屏切换和旋转感知

### 场景描述

播放视频时，可通过点击全屏图标按钮实现全屏播放，或通过旋转设备进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/KTNw5fcTRXy5tXEPO7ctng/zh-cn_image_0000002585677821.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=E2946B3B500FC575607A6427C0A097A38D109F8C14CB2BC035E62D89E2EB58A6 "点击放大")

### 实现原理

* 自动旋转：在设备控制面板中取消旋转锁定，并将orientation设置为AUTO\_ROTATION\_RESTRICTED时，应用会跟随传感器自动旋转。

  说明

  须提前打开设备的控制中心，取消旋转锁定，否则自动旋转不生效。
* 手动切换：通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置应用的主窗口显示方向：
  + USER\_ROTATION\_LANDSCAPE：旋转到横屏。
  + USER\_ROTATION\_PORTRAIT：旋转到竖屏。

### 开发步骤

通过传感器自动旋转：

1. 在模块级配置文件module.json5中，设置窗口显示方向[orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)的字段值为AUTO\_ROTATION\_RESTRICTED。

   ```
   1. "orientation": "auto_rotation_restricted",
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/module.json5#L25-L25)

手动切换：

1. 通过setPreferredOrientation()方法，设置主窗口的显示方向。

   ```
   1. public setMainWindowOrientation(orientation: window.Orientation) {
   2. if (!this.mainWindowClass) {
   3. return;
   4. }
   5. this.mainWindowClass.setPreferredOrientation(orientation)
   6. .then(() => {
   7. Logger.info('setPreferredOrientation succeed.');
   8. })
   9. .catch((err: BusinessError) => {
   10. Logger.error(TAG, `setPreferredOrientation failed. code: ${err.code}, message: ${err.message}`);
   11. })
   12. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/utils/WindowUtil.ets#L56-L67)
2. 通过[setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)方法，设置主窗口状态栏、底部导航的可见模式。

   ```
   1. // Display the status bar of the main window and the bottom navigation.
   2. public enableWindowSystemBar(): void {
   3. if (!this.mainWindowClass) {
   4. return;
   5. }
   6. this.mainWindowClass.setWindowSystemBarEnable(['status', 'navigation'])
   7. .catch((err: BusinessError) => {
   8. Logger.error(TAG, `setWindowSystemBarEnable failed. code: ${err.code}, message: ${err.message}`);
   9. })
   10. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/utils/WindowUtil.ets#L71-L80)

   ```
   1. // Disable the status bar and bottom navigation of the main window.
   2. public disableWindowSystemBar(): void {
   3. if (!this.mainWindowClass) {
   4. return;
   5. }
   6. this.mainWindowClass.setWindowSystemBarEnable([])
   7. .catch((err: BusinessError) => {
   8. Logger.error(TAG, `setWindowSystemBarEnable failed. code: ${err.code}, message: ${err.message}`);
   9. })
   10. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/utils/WindowUtil.ets#L84-L93)
3. 点击全屏按钮，设置window.Orientation为USER\_ROTATION\_LANDSCAPE，并设置状态栏和底部导航区域不可见。

   ```
   1. this.windowUtil.disableWindowSystemBar();
   2. this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L311-L312)
4. 点击缩放按钮，设置window.Orientation为USER\_ROTATION\_PORTRAIT，并设置显示状态栏和底部导航区域。

   ```
   1. this.windowUtil.enableWindowSystemBar();
   2. this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L377-L378)

## 跳转播放

### 场景描述

通过点击或拖动自定义进度条，实现视频跳转至指定时间进行播放功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/IeOH_SHNQtaY9Ms-nLnHmA/zh-cn_image_0000002555237890.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=A46653AFD4FD239A7D89998188B6EC094533F20F1C79998163BD447EDCA305EC "点击放大")

### 实现原理

Video组件自带的控制栏由[controls](../harmonyos-references/ts-media-components-video.md#controls)属性进行控制。当controls属性设置为false时，控制栏隐藏，此时可基于[Slider](../harmonyos-references/ts-basic-components-slider.md)组件实现自定义播放进度条，并通过[setCurrentTime()](../harmonyos-references/ts-media-components-video.md#setcurrenttime8)方法，指定视频播放进度，实现跳转播放。

### 开发步骤

1. controls属性设置为false，禁用Video控制栏。

   ```
   1. Video({
   2. src: this.videoSrc,
   3. controller: this.videoController,
   4. currentProgressRate: this.curRate, // Set playback speed.
   5. posterOptions: {
   6. showFirstFrame: true,
   7. }
   8. })
   9. // ...
   10. .controls(false)
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L407-L429)
2. 在Slider组件的[onChange()](../harmonyos-references/ts-basic-components-slider.md#onchange)事件中，调用VideoController的setCurrentTime()方法传入Slider组件进度值，并设置[SeekMode](../harmonyos-references/ts-media-components-video.md#seekmode8枚举说明)跳转模式为Accurate精准跳转，实现视频跳转播放。

   ```
   1. Slider({
   2. value: this.currentTime,
   3. max: this.durationTime,
   4. step: 1
   5. })
   6. // ...
   7. .onChange((value) => {
   8. this.videoController.setCurrentTime(value, SeekMode.Accurate);
   9. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L287-L298)

## 前台小窗播放

### 场景描述

播放视频时，向下滑动视频列表，Video组件从页面消失后，视频以小窗口模式进行播放，同时用户可以进行其它操作，提升使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/tX45XibeR5-R4qQREWS3SA/zh-cn_image_0000002555078264.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=4DAD312DEE46DE31ABD94A473C6EFE6CF3F839CDB587DAF9DE656B284C6E1DD1 "点击放大")

### 实现原理

Video通过自定义组件实现小窗口播放视频，通过[onWillScroll()](../harmonyos-references/ts-container-scroll.md#onwillscroll12)计算Scroll组件在竖直方向的偏移量，当偏移量超过Video组件自身高度时，通过自定义组件实现小窗口播放视频。

说明

Video组件不支持视频以画中画模式播放，如需使用画中画模式，请参考基于AVPlayer播放长视频实践[画中画播放](bpta-avplayer-long-video.md#section16229471226)小节。

### 开发步骤

1. 自定义SmallWindowVideo组件，用于小窗播放视频。

   ```
   1. @Component
   2. export struct SmallWidnowVideo {
   3. // ...

   5. build() {
   6. Column() {
   7. Video({
   8. src: this.videoSrc,
   9. controller: this.videoController,
   10. currentProgressRate: this.curRate, // Set playback speed.
   11. posterOptions: {
   12. showFirstFrame: true,
   13. }
   14. })
   15. // ...
   16. .onPrepared((event) => {
   17. this.videoController.start();
   18. if (event) {
   19. this.videoController.setCurrentTime(this.currentTime, SeekMode.Accurate);
   20. }
   21. })
   22. .onUpdate((event) => {
   23. if (event) {
   24. this.currentTime = event.time;
   25. }
   26. })
   27. Image($r('app.media.video_close'))
   28. // ...
   29. }
   30. // ...
   31. }
   32. }
   ```

   [SmallWidnowVideo.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/view/SmallWidnowVideo.ets#L17-L85)
2. 在Scroll组件的onWillScroll()事件中，计算偏移量，通过偏移量判断是否显示小窗。

   ```
   1. Scroll() {
   2. // ...
   3. }
   4. // ...
   5. .onWillScroll((_xOffset: number, yOffset: number) => {
   6. this.scrollVal += yOffset;
   7. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L401-L553)

   ```
   1. // Play in a small window.
   2. if (this.scrollVal >= 240 && this.isPlaying && !this.isFullScreen) {
   3. SmallWidnowVideo({
   4. videoSrc: this.videoSrc,
   5. curRate: this.curRate,
   6. isMute: this.isMute,
   7. currentTime: this.currentTime,
   8. isPlaying: this.isPlaying,
   9. videoController: this.videoController,
   10. })
   11. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L557-L567)

## 点击按钮选择倍速

### 场景描述

视频横屏时，通过点击按钮选择预设播放速度，实现视频倍速（1.0、1.25、1.75或2.0速度）播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/FbT4wShfSB6l4f_c0dXTHw/zh-cn_image_0000002585797861.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=87A7BB2ACA24A4FB401279D2B6944304EF192D5C663F3BA622CE5391F409D29D "点击放大")

### 实现原理

Video组件支持通过[currentProgressRate](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)参数设置视频播放倍速。同时，结合[Menu](../harmonyos-references/ts-basic-components-menu.md)组件预设视频播放速度，实现点击按钮后倍速播放视频。

### 开发步骤

1. 在Menu中，预设视频播放速度，并在点击事件中修改播放倍速的值。

   ```
   1. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X; // Playback speed.
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L49-L49)

   ```
   1. // Playback speed setting.
   2. @Builder
   3. SpeedMenu() {
   4. Menu() {
   5. MenuItem({ content: '2.0X' })
   6. .width('100%')
   7. .onClick(() => {
   8. this.playbackSpeed = '2.0X';
   9. this.curRate = PlaybackSpeed.Speed_Forward_2_00_X;
   10. })
   11. MenuItem({ content: '1.75X' })
   12. .width('100%')
   13. .onClick(() => {
   14. this.playbackSpeed = '1.75X';
   15. this.curRate = PlaybackSpeed.Speed_Forward_1_75_X;
   16. })
   17. MenuItem({ content: '1.25X' })
   18. .width('100%')
   19. .onClick(() => {
   20. this.playbackSpeed = '1.25X';
   21. this.curRate = PlaybackSpeed.Speed_Forward_1_25_X;
   22. })
   23. MenuItem({ content: '1.0X' })
   24. .width('100%')
   25. .onClick(() => {
   26. this.playbackSpeed = '1.0X';
   27. this.curRate = PlaybackSpeed.Speed_Forward_1_00_X;
   28. })
   29. }
   30. // ...
   31. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L234-L276)
2. 为Video组件配置currentProgressRate参数，并赋值为预设的播放倍速。

   ```
   1. Video({
   2. src: this.videoSrc,
   3. controller: this.videoController,
   4. currentProgressRate: this.curRate, // Set playback speed.
   5. posterOptions: {
   6. showFirstFrame: true,
   7. }
   8. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L408-L416)

## 长按视频倍速

### 场景描述

视频横屏时，长按屏幕可实现2倍速播放，离手后视频恢复至默认1倍速播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/1cbuuehLStuRi_zMUUWDIA/zh-cn_image_0000002585677825.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=92D8A1B7C2F4AA3DC5645B0622A84B748C4D7EF83B506BA3BC9D8B90F0A5655D "点击放大")

### 实现原理

通过绑定长按手势事件[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)，实现长按屏幕边缘视频倍速播放。

### 开发步骤

1. 绑定LongPressGesture长按手势事件，在[onAction()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onaction)方法中设置预设倍速值，在[onActionEnd()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onactionend)方法中，恢复初始播放速度。

   ```
   1. LongPressGesture({ repeat: true })
   2. .onAction(() => {
   3. this.playbackSpeed = '2.0X';
   4. this.curRate = PlaybackSpeed.Speed_Forward_2_00_X;
   5. })
   6. .onActionEnd(() => {
   7. this.playbackSpeed = '1.0X';
   8. this.curRate = PlaybackSpeed.Speed_Forward_1_00_X;
   9. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L498-L506)
2. 为Video组件配置currentProgressRate参数，并重新赋值。

   ```
   1. Video({
   2. src: this.videoSrc,
   3. controller: this.videoController,
   4. currentProgressRate: this.curRate, // Set playback speed.
   5. posterOptions: {
   6. showFirstFrame: true,
   7. }
   8. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L408-L416)

## 循环播放

### 场景描述

视频播放结束后，立即重新开始播放，以实现无缝循环播放的效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/ZeaNPgAPTvSkeguy3KEP3A/zh-cn_image_0000002555237894.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=B50F6E41CC981495F1E74641B4B79CFAA622237F5220460788D405556DC21F3E "点击放大")

### 实现原理

Video组件的[loop](../harmonyos-references/ts-media-components-video.md#loop)属性支持设置单个视频循环播放，当视频播放结束时，系统自动触发onFinish()回调。在回调中，播放器通过setCurrentTime(0)重置进度到起始位置，并调用start()重新播放。此过程通过VideoController控制，无需开发者手动干预。

### 开发步骤

将Video组件的loop属性设置为true，即可实现视频无缝循环播放。

```
1. Video({
2. src: this.videoSrc,
3. controller: this.videoController,
4. currentProgressRate: this.curRate, // Set playback speed.
5. posterOptions: {
6. showFirstFrame: true,
7. }
8. })
9. // ...
10. .loop(true)
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L409-L426)

## 音量设置

### 场景描述

滑动调节音量是视频应用中的常见交互：在播放界面左侧上下滑动，即可快速调节音量，无需中断观看，从而提升用户的观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/e5YLykdRTTWpBqUitWxc2A/zh-cn_image_0000002555078268.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=0DCF8240CFBED1D57D563FD780E496A0A2F65390F2BEF009D7032367E442EFA2 "点击放大")

### 实现原理

系统音量面板[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)提供了展示和调节系统音量的功能，结合[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，设置滑动方向为竖直方向，当手势移动时，上滑增加音量，下滑减少音量，实现控制系统音量功能。

### 开发步骤

1. 创建AVVolumePanel，显示系统音量面板。

   ```
   1. AVVolumePanel({
   2. volumeLevel: this.volume,
   3. volumeParameter: {
   4. position: {
   5. x: 150,
   6. y: 300
   7. }
   8. }
   9. })
   ```

   [VolumeView.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/view/VolumeView.ets#L28-L36)
2. 为元素绑定PanGesture滑动手势事件，根据手势滑动距离计算并设置音量值volume。

   ```
   1. // Bind the swipe gesture event.
   2. PanGesture({ direction: PanDirection.Vertical })
   3. .onActionStart(() => {
   4. })
   5. .onActionUpdate((event: GestureEvent) => {
   6. this.visible = false;
   7. // Current Volume value = Volume value - Vertical offset (physical pixels) of the gesture / Screen height.
   8. let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
   9. // Limit the volume range between 0 and 15.
   10. curVolume = this.getValidValue(curVolume, CommonConstants.MIN_VOLUME, CommonConstants.MAX_VOLUME);
   11. if(curVolume === 0) {
   12. this.isMute = true;
   13. } else {
   14. this.isMute = false;
   15. }
   16. this.volume = curVolume;
   17. })
   18. .onActionEnd(() => {
   19. setTimeout(() => {
   20. this.visible = false;
   21. }, 1500)
   22. }),
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L474-L495)

## 接入播控中心

### 场景描述

Video组件播放视频时，可以通过控制中心，实现视频的播放、暂停、切换视频、跳转播放、点击拉起应用等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/HGabfaAeTlu0ndacbuWVLQ/zh-cn_image_0000002585797863.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002039Z&HW-CC-Expire=86400&HW-CC-Sign=1CD9C9AEADA3CD94E60C0A47EDDE6142AF4287B4D0E13C07AA99DE89216DD7A5 "点击放大")

### 实现原理

通过AVSession Kit实现应用接入播控中心，AVSession Kit是系统提供的音视频管控服务，可用于统一管理系统中所有音视频行为，帮助开发者快速构建音视频统一展示和控制能力。

### 开发步骤

1. 通过[createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建AVSession实例，并指定[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)为video类型。创建成功后，通过[activate()](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)方法激活会话。

   ```
   1. public initAVSession() {
   2. if (!this.context) {
   3. return;
   4. }
   5. // Create a session object of video type.
   6. avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video')
   7. .then((data: avSession.AVSession) => {
   8. this.avSession = data;
   9. this.setLaunchAbility();
   10. BackgroundTaskManager.startContinuousTask(this.context);
   11. // Activate session.
   12. this.avSession.activate()
   13. .then(() => {
   14. Logger.info(TAG, `AVSession activate successed`);
   15. })
   16. .catch((err: BusinessError) => {
   17. BackgroundTaskManager.stopContinuousTask(this.context);
   18. Logger.error(TAG, `AVSession activate failed. code: ${err.code}, message: ${err.message}`);
   19. })
   20. })
   21. .catch((err: BusinessError) => {
   22. Logger.error(TAG, `Create AVSession failed. code: ${err.code}, message: ${err.message}`);
   23. })
   24. }
   ```

   [AVSessionController.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L41-L64)
2. 通过[setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)设置会话元数据，如：媒体ID（assetId）、标题（title）、媒体时长（duration）等，从而在播控中心界面进行展示。

   ```
   1. public setAVMetadata(curSource: VideoInfo, duration: number) {
   2. if (!curSource) {
   3. return;
   4. }
   5. try {
   6. // Set session metadata.
   7. let metadata: avSession.AVMetadata = {
   8. assetId: `${curSource.index}`, // Media ID
   9. title: this.context?.resourceManager.getStringSync(curSource.name.id), // Title
   10. duration: duration // Media duration
   11. }
   12. if (this.avSession) {
   13. this.avSession.setAVMetadata(metadata)
   14. .catch((err: BusinessError) => {
   15. Logger.error(TAG, `Set AVMetadata failed. code: ${err.code}, message: ${err.message}`);
   16. })
   17. }
   18. } catch (error) {
   19. let err = error as BusinessError;
   20. Logger.error(TAG, `getStringSync failed. code: ${err.code}, message: ${err.message}`);
   21. }
   22. }
   ```

   [AVSessionController.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L72-L93)
3. 通过[setAVPlaybackState()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)设置会话播放状态。

   ```
   1. // Set session playback status.
   2. public setAVSessionPlayState(playbackState: avSession.AVPlaybackState) {
   3. if (!this.avSession) {
   4. return;
   5. }
   6. this.avSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
   7. if (err) {
   8. Logger.error(TAG, `SetAVPlaybackState failed. code: ${err.code}, message: ${err.message}`);
   9. } else {
   10. Logger.info('SetAVPlaybackState successfully');
   11. }
   12. })
   13. }
   ```

   [AVSessionController.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L130-L142)
4. 通过[getWantAgent()](../harmonyos-references/js-apis-app-ability-wantagent.md#wantagentgetwantagent)创建WantAgent，并通过[setLaunchAbility()](../harmonyos-references/arkts-apis-avsession-avsession.md#setlaunchability10)设置用于被播控中心拉起的UIAbility。

   ```
   1. public setLaunchAbility() {
   2. if (!this.context) {
   3. return;
   4. }
   5. const wantAgentInfo: wantAgent.WantAgentInfo = {
   6. wants: [
   7. {
   8. bundleName: this.context.abilityInfo.bundleName,
   9. abilityName: this.context.abilityInfo.name
   10. }
   11. ],
   12. actionType: wantAgent.OperationType.START_ABILITIES, // Enable multiple Abilities with pages.
   13. requestCode: 0,
   14. actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   15. };
   16. // Create WantAgent
   17. wantAgent.getWantAgent(wantAgentInfo)
   18. .then((agent: WantAgent) => {
   19. if (this.avSession) {
   20. // Set up a WantAgent to initiate the Ability of the session.
   21. this.avSession.setLaunchAbility(agent)
   22. .catch((err: BusinessError) => {
   23. Logger.error(TAG, `SetLaunchAbility failed. code: ${err.code}, message: ${err.message}`);
   24. })
   25. }
   26. })
   27. .catch((err: BusinessError) => {
   28. Logger.error(TAG, `Get wantAgent failed. code: ${err.code}, message: ${err.message}`);
   29. })
   30. }
   ```

   [AVSessionController.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L97-L126)
5. 注册播控命令事件监听，以响应用户通过播控中心触发的操作，如：播放[on('play')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)、暂停[on('pause')](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10)、切换上一个视频[on('playPrevious')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplayprevious10)、切换下一个视频[on('playNext')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaynext10)等。

   ```
   1. // Set AVSession to listen.
   2. public async setAVSessionListener() {
   3. if (!this.avSessionController) {
   4. return;
   5. }
   6. try {
   7. this.avSessionController.getAVSession()?.on('play', () => this.sessionPlay());
   8. this.avSessionController.getAVSession()?.on('pause', () => this.sessionPause());
   9. this.avSessionController.getAVSession()?.on('seek', (msTime: number) => {
   10. this.sessionSeek(msTime);
   11. });
   12. this.avSessionController.getAVSession()?.on('setLoopMode', () => {
   13. });
   14. this.avSessionController.getAVSession()?.on('playPrevious', () => this.changePlayVideo(true));
   15. this.avSessionController.getAVSession()?.on('playNext', () => this.changePlayVideo(false));
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. Logger.error(TAG, `Set AVSession listener failed. code: ${err.code}, message: ${err.message}`);
   19. }
   20. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L135-L154)
6. 视频播放状态需要上报播控中心。当视频状态发生改变时，通过setAVPlaybackState()向播控中心上报视频状态，实现播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。

   ```
   1. // Update AVSession playback status.
   2. updateIsPlay() {
   3. this.avSessionController.setAVSessionPlayState({
   4. state: this.isPlaying ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
   5. avSession.PlaybackState.PLAYBACK_STATE_PAUSE, // Playback status.
   6. position: {
   7. elapsedTime: this.currentTime * 1000, // Elapsed time.
   8. updateTime: new Date().getTime() // Update time.
   9. },
   10. duration: this.durationTime * 1000, // The duration of current media resources.
   11. speed: this.curRate
   12. })
   13. }
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/video-show/blob/master/entry/src/main/ets/pages/Index.ets#L218-L230)

## 示例代码

* [基于Video组件播放长视频](https://gitcode.com/HarmonyOS_Samples/video-show)
