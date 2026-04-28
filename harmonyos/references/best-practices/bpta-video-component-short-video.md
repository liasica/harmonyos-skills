---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-video-component-short-video
title: 基于Video组件播放短视频
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于Video播放视频系列开发实践 > 基于Video组件播放短视频
category: best-practices
scraped_at: 2026-04-28T08:20:45+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:a6a867b95375d7453cafe79b06d9c14446976dd1431e0767303affd020e0dc1b
---

## 概述

短视频通常以移动智能终端为播放载体，通过社交或视频平台快速传播。本文围绕主流短视频应用的常见场景，包括基础播控、横竖屏切换与旋转感知、长按视频倍速播放、前后台感知、自动连播等，指导开发者基于[Video](../harmonyos-references/ts-media-components-video.md)组件实现短视频播放功能。

* [基础播控](bpta-video-component-short-video.md#section8262152281415)
* [横竖屏切换与旋转感知](bpta-video-component-short-video.md#section10921503198)
* [短视频列表流畅切换](bpta-video-component-short-video.md#section68130286511)
* [长按视频倍速播放](bpta-video-component-short-video.md#section107981344143717)
* [前后台感知](bpta-video-component-short-video.md#section7933653553)
* [音量设置](bpta-video-component-short-video.md#section1611719321814)
* [自动连播](bpta-video-component-short-video.md#section25891771761)

## 基础播控

### 场景描述

通过Video组件实现视频基础播放控制能力，包括播放视频、暂停播放等操作。实现效果如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/gaFRQ5mJSUy9FdcnbkAi1g/zh-cn_image_0000002555239530.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=55C8584291CDEC28B21BF07A0B8079BE18E688AA631DE8D01EAC322DCB492E2E "点击放大")

### 实现原理

具体实现原理可参考《基于Video组件播放长视频》的[基础播控实现原理](bpta-video-component-long-video.md#section1669421012353)。

### 开发步骤

具体开发步骤可参考《基于Video组件播放长视频》的[基础播控开发步骤](bpta-video-component-long-video.md#section18477202813352)。

## 横竖屏切换与旋转感知

### 场景描述

当用户需要全屏播放视频时，可以通过点击按钮全屏播放，或通过旋转设备进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/-tP96e4iQ_i-whGjd-grIg/zh-cn_image_0000002585679465.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=3804D6C7879E803A4EA0DC1120099FF28C833AA3E5B59713E2D83E4B694588EE "点击放大")

### 实现原理

* 自动旋转：在[model.json5配置文件](../harmonyos-guides/module-configuration-file.md)中配置"orientation"字段，设置orientation为[AUTO\_ROTATION\_RESTRICTED](../harmonyos-guides/window-rotation.md#自动旋转方向类型)，应用会跟随传感器自动旋转。

  说明

  须提前打开设备的控制中心，取消旋转锁定，否则自动旋转不生效。
* 手动切换：通过[setPreferredOrientation()](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)设置应用的主窗口显示方向[Orientation](../harmonyos-references/arkts-apis-window-e.md#orientation9)：
  + USER\_ROTATION\_LANDSCAPE：旋转到横屏。
  + USER\_ROTATION\_PORTRAIT：旋转到竖屏。

### 开发步骤

开发步骤详情可参考《基于Video组件播放长视频》的[横竖屏切换和旋转感知开发步骤](bpta-video-component-long-video.md#section3703101910168)。

## 短视频列表流畅切换

### 场景描述

在用户上下滑动时，视频能快速切换到下一个或上一个，且加载和播放流畅、无卡顿。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WJER457QStKqBFY3m5lY1w/zh-cn_image_0000002555079910.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=85787FC73101880763CA7C108A1FA3AD4334BE9CA79EEA5400292196D1B5390C "点击放大")

### 实现原理

设置[Swiper](../harmonyos-references/ts-container-swiper.md)组件的[cachedCount](../harmonyos-references/ts-container-swiper.md#cachedcount15)属性预加载子组件个数，提前加载并缓存下一个视频内容，确保滑动时无卡顿，提升短视频切换的流畅性。

### 开发步骤

1. 设置Swiper组件预加载子组件个数cachedCount为1，预加载当前、上一个和下一个视频。

   ```
   1. Swiper(this.swiperController) {
   2. LazyForEach(new MyDataSource(this.videoInfoList), (item: VideoDataModel, index: number) => {
   3. VideoPlayer({
   4. isFullLandscapeScreen: this.isFullLandscapeScreen, // fullLandscapeScreen state
   5. videoIndex: index, // Video index
   6. activeIndex: this.currentIndex, // Index of the currently playing video
   7. screenWidth: this.screenWidth // Screen width
   8. })
   9. }, (item: string) => item)
   10. }
   11. .cachedCount(CommonConstants.CACHED_COUNT)
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/pages/Index.ets#L75-L86)
2. 滑动切换视频时，同步更新当前视频的索引值currentIndex，具体步骤请参考[自动连播开发步骤](bpta-video-component-short-video.md#section6406358972)的2、3、4。

## 长按视频倍速播放

### 场景描述

通过长按屏幕实现视频2倍速播放。如下图所示，长按触屏时，显示"2.0X快进中"，同时视频以2倍速进行播放；抬起后，视频以默认的1倍速进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/bd_8yZFFRzeizE-2xP7pxA/zh-cn_image_0000002585799527.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=ED240603E7200A846EADF6F98EA42522B3449571F1BF42F0322F29B5EAFA99E3 "点击放大")

### 实现原理

绑定长按手势事件[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)，当用户长按视频边缘时，动态设置[VideoOptions](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)中的视频播放倍速currentProgressRate，从而实现视频倍速播放功能。

### 开发步骤

1. 绑定LongPressGesture长按手势事件，在[onAction()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onaction)方法中设置视频播放倍速值为2倍速，即PlaybackSpeed.Speed\_Forward\_2\_00\_X，在[onActionEnd()](../harmonyos-references/ts-basic-gestures-longpressgesture.md#onactionend)方法中，恢复初始播放速度为PlaybackSpeed.Speed\_Forward\_1\_00\_X。具体视频播放倍速选项请参考[PlaybackSpeed枚举说明](../harmonyos-references/ts-media-components-video.md#playbackspeed8枚举说明)。

   ```
   1. Column()
   2. .width('20%')
   3. .height('100%')
   4. .gesture(
   5. LongPressGesture({ repeat: true })
   6. .onAction((event: GestureEvent | undefined) => {
   7. // The fast forward icon changes between visible and invisible states.
   8. this.leftRateOpacity = 1;
   9. this.rightRateOpacity = 0;
   10. if (!event) {
   11. return;
   12. }
   13. if (event.repeat) {
   14. this.isAccelerate = true;
   15. this.curRate = PlaybackSpeed.Speed_Forward_2_00_X;
   16. if (!this.isStart) {
   17. this.isStart = true;
   18. this.controller.start();
   19. }
   20. }
   21. })
   22. .onActionEnd(() => {
   23. this.isAccelerate = false;
   24. this.curRate = PlaybackSpeed.Speed_Forward_1_00_X;
   25. })
   26. );
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L115-L140)
2. 同步更新Video组件的currentProgressRate参数，设置视频播放倍速。

   ```
   1. Video({
   2. src: this.videoInfoList[this.activeIndex].uri,
   3. controller: this.controller,
   4. currentProgressRate: this.curRate
   5. })
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L263-L267)

## 前后台感知

### 场景描述

应用从前台切到后台，再从后台切回前台时，能够保持原有进度继续播放原视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/6wwx-yR3T7O9ongGyxvSIg/zh-cn_image_0000002555239532.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=6FFCA01E72D16B417F3E4099E0D97D96E2924B6B4913BFA76328AC58ECEADFD5 "点击放大")

### 实现原理

通过[onForeground()](../harmonyos-guides/uiability-lifecycle.md#onforeground)和[onBackground()](../harmonyos-guides/uiability-lifecycle.md#onbackground)生命周期方法监听应用前后台状态变化，根据状态变化播放或暂停视频：

* 当应用从前台切到后台时，调用[VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)的[pause()](../harmonyos-references/ts-media-components-video.md#pause)方法暂停视频；
* 当应用回到前台时，调用VideoController的[start()](../harmonyos-references/ts-media-components-video.md#start)方法继续播放视频。

### 开发步骤

1. 在EntryAbility.ets文件中，使用[AppStorage.setOrCreate()](../harmonyos-references/ts-state-management.md#setorcreate10)设置并缓存应用前后台状态isForeGround：
   * 当应用处于前台时，isForeGround为true。
   * 当应用处于后台时，isForeGround为false。

   ```
   1. onForeground(): void {
   2. // Ability has brought to foreground
   3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
   4. AppStorage.setOrCreate('isForeGround', true);
   5. }

   7. onBackground(): void {
   8. // Ability has back to background
   9. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
   10. AppStorage.setOrCreate('isForeGround', false);
   11. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/entryability/EntryAbility.ets#L64-L75)
2. 在VideoPlayer自定义组件里对状态变量isForeGround添加[@Watch装饰器](../harmonyos-guides/arkts-watch.md)，通过回调函数foregroundStatus监听状态变量的变化。

   ```
   1. @Watch('foregroundStatus') @StorageLink('isForeGround') isForeGround: boolean = false;
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L29-L29)
3. 在回调函数foregroundStatus中调用Video组件的播放/暂停方法，以实现切换到后台时视频暂停播放、切回前台时视频恢复播放。

   ```
   1. // Perception of foreground and background.
   2. foregroundStatus() {
   3. if (this.isForeGround) {
   4. this.controller.start(); // Start playing when in the foreground.
   5. this.isStart = true;
   6. } else {
   7. this.controller.pause(); // Pause playback when in the background.
   8. this.isStart = false;
   9. }
   10. }
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L69-L79)

## 音量设置

### 场景描述

滑动调节音量在视频应用中是一种常见功能，允许用户在不离开视频播放界面的情况下，通过长按结合滑动手势即可调节音量，以获得更佳的观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/meq7Hk57TkinOoJpIv5dRg/zh-cn_image_0000002585679469.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=95B2E3D3EC3973E2DAE4B130152B01D23FA3963FE28358A445C03AB009A299DC "点击放大")

### 实现原理

系统音量面板[AVVolumePanel](../harmonyos-references/ohos-multimedia-avvolumepanel.md)提供了展示和调节系统音量的功能。结合[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)长按手势事件和[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，设置滑动方向为竖直方向，长按触屏后，上滑增大音量，下滑减小音量，实现控制系统音量功能。

### 开发步骤

1. 创建AVVolumePanel系统音量面板。

   ```
   1. @Prop volume: number = CommonConstants.INITIAL_VOLUME; // volume level
   2. @Prop volumeVisible: boolean = false; // Whether to show the volume component.
   3. @Prop isFullLandscapeScreen: boolean = false; // FullLandscapeScreen or not

   5. build() {
   6. Column() {
   7. AVVolumePanel({
   8. volumeLevel: this.volume,
   9. volumeParameter: {
   10. position: {
   11. x: this.isFullLandscapeScreen ? CommonConstants.AV_VOLUME_PANEL_X_IN_FULL :
   12. CommonConstants.AV_VOLUME_PANEL_X,
   13. y: this.isFullLandscapeScreen ? CommonConstants.AV_VOLUME_PANEL_Y_IN_FULL :
   14. CommonConstants.AV_VOLUME_PANEL_Y
   15. }
   16. }
   17. })
   18. .width(10)
   19. }
   20. .visibility(this.volumeVisible ? Visibility.Visible : Visibility.Hidden)
   21. .height('50%')
   22. }
   ```

   [SetVolume.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/SetVolume.ets#L22-L44)
2. 绑定[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)和[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)组合而成的Sequence组合手势。
   * 长按触发LongPressGesture时，显示AVVolumePanel音量调节组件。

     ```
     1. LongPressGesture({ repeat: true })
     2. .onAction((event: GestureEvent | undefined) => {
     3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'LongPressGesture:' + event);
     4. if (event) {
     5. this.volumeVisible = true;
     6. }
     7. })
     8. .onActionEnd(() => {
     9. this.volumeVisible = false;
     10. }),
     ```

     [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L381-L390)
   * 长按后滑动触发PanGesture时，根据手势滑动距离计算并同步刷新音量值volume。

     ```
     1. // When dragging after a long press, the PanGesture gesture is triggered.
     2. PanGesture({ direction: PanDirection.Vertical })
     3. .onActionUpdate((event: GestureEvent) => {
     4. let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.windowHeight;
     5. curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
     6. curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
     7. this.volume = curVolume;
     8. })
     9. .onActionEnd(() => {
     10. setTimeout(() => {
     11. this.volumeVisible = false;
     12. }, 5000)
     13. })
     ```

     [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L393-L405)

## 自动连播

### 场景描述

当前视频播放结束后，播放器将自动加载并播放下一个视频，无需用户手动操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/X3Pg4m8ESBu7PrJbL8Xnsg/zh-cn_image_0000002555079912.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002040Z&HW-CC-Expire=86400&HW-CC-Sign=2A436592B772716D3D09980758A1EFBAC0787CF971176B762EA18730F6C5CA3C "点击放大")

### 实现原理

1. 在视频播放结束时，触发[onFinish()](../harmonyos-references/ts-media-components-video.md#onfinish)事件，通过Swiper组件的[showNext()](../harmonyos-references/ts-container-swiper.md#shownext)切换下一个视频。
2. 在Swiper的[onAnimationStart()](../harmonyos-references/ts-container-swiper.md#onanimationstart9)回调中更新视频索引值。
3. 监听视频索引值变化，使用[reset()](../harmonyos-references/ts-media-components-video.md#reset12)、start()分别重置和播放视频。

### 开发步骤

1. 在Video组件的onFinish()事件中，调用Swiper组件的showNext()方法。

   ```
   1. .onFinish(() => {
   2. hilog.info(DOMAIN, 'testTag', '%{public}s', 'onFinish and showNext.');
   3. this.swiperController?.showNext();
   4. })
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L286-L289)
2. 在Swiper组件的onAnimationStart()回调中，更新当前视频的索引值currentIndex。

   ```
   1. Swiper(this.swiperController) {
   2. LazyForEach(new MyDataSource(this.videoInfoList), (item: VideoDataModel, index: number) => {
   3. VideoPlayer({
   4. isFullLandscapeScreen: this.isFullLandscapeScreen, // fullLandscapeScreen state
   5. videoIndex: index, // Video index
   6. activeIndex: this.currentIndex, // Index of the currently playing video
   7. screenWidth: this.screenWidth // Screen width
   8. })
   9. }, (item: string) => item)
   10. }
   11. // ...
   12. .onAnimationStart((index: number, targetIndex: number) => {
   13. hilog.info(DOMAIN, 'testTag', '%{public}s',
   14. `onAnimationStart index:${index} , targetIndex: ${targetIndex}`);
   15. this.currentIndex = targetIndex; // Update current video index.
   16. })
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/pages/Index.ets#L74-L99)
3. 在VideoPlayer自定义组件里对状态变量activeIndex添加@Watch装饰器，通过回调函数activeIndexChange监听当前视频的索引值的变化。

   ```
   1. @Prop @Watch('activeIndexChange') activeIndex: number = 0; // Index of the currently playing video
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L32-L32)
4. 在回调函数activeIndexChange中重置播放进度显示值为0，然后依次调用Video组件的reset()、start()方法重置和播放下一个视频。

   ```
   1. // Monitor the change of activeIndex when the onchange event occurs.
   2. activeIndexChange() {
   3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'activeIndexChange.' + this.activeIndex);
   4. this.currentTime = 0; // Reset currentTime
   5. this.controller.reset(); // Reset VideoController
   6. this.controller.start(); // Start playing
   7. }
   ```

   [VideoPlayer.ets](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent/blob/master/entry/src/main/ets/view/VideoPlayer.ets#L58-L65)

## 示例代码

* [基于Video组件播放短视频](https://gitcode.com/HarmonyOS_Samples/PlayShortVideosBasedOnVideoComponent)
