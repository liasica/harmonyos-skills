---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-long-video
title: 基于AVPlayer播放长视频实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AVPlayer播放视频系列开发实践 > 基于AVPlayer播放长视频实践
category: best-practices
scraped_at: 2026-04-28T08:20:30+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:59b7579fff3cf0ea72f9fec89b4b1e5f22ee55ea78118d0b417815bc36defe3c
---

## 概述

本文适用于视频播放类应用的开发，针对市场上主流视频播放类应用的常见场景，介绍了如何基于AVPlayer系统播放器实现长视频播放。本文指导开发者实现基本播控、精准跳转、静音播放、窗口缩放模式设置、倍速播放、音量控制、亮度控制、焦点管理、前后台感知、弹幕发送与显示、字幕挂载、视频截图、画中画播放、后台播放与接入播控中心、视频首帧显示等开发场景。

* [亮度控制](bpta-avplayer-long-video.md#section512331617222)
* [焦点管理](bpta-avplayer-long-video.md#section745373252219)
* [前后台感知](bpta-avplayer-long-video.md#section141437368229)
* [弹幕发送与显示](bpta-avplayer-long-video.md#section28801440152211)
* [视频截图](bpta-avplayer-long-video.md#section3655185020221)
* [画中画播放](bpta-avplayer-long-video.md#section16229471226)
* [接入播控中心](bpta-avplayer-long-video.md#section1489902163313)
* [后台播放](bpta-avplayer-long-video.md#section19176174913234)
* [视频首帧显示](bpta-avplayer-long-video.md#section96024162316)
* [横竖屏切换与旋转感知](bpta-avplayer-long-video.md#section178071122418)
* [视频无缝转场播放](bpta-avplayer-long-video.md#section86364193363)

## 基本播控

基本播控、精准跳转、静音播放、窗口缩放设置、倍速播放、音量控制、字幕挂载场景参见[《基于AVPlayer基础播控实践》](bpta-avplayer-basic-control.md)。

## 亮度控制

### 场景描述

用户在横屏播放视频时可通过手势滑动调节屏幕亮度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/BfNfT-TMSIa4HL9oLs0FVQ/zh-cn_image_0000002485889645.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=C2BB9F87FFCF4C873952B5FE7FA845DA70C64A036CA0C93F45E0DFC1C5E31ACB "点击放大")

### 实现原理

使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)设置亮度面板，绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，当Pan手势在移动过程中调用[setWindowBrightness()](../harmonyos-references/arkts-apis-window-window.md#setwindowbrightness9)方法，实现上滑增加亮度、下滑减少亮度的功能。

### 开发步骤

1. 当进入全屏播放模式时，在视频播放界面右侧区域添加Slider组件，用来展示屏幕亮度变化情况。

   ```
   1. Column() {
   2. Stack() {
   3. Slider({
   4. value: this.screenBrightness,
   5. min: 0,
   6. max: 1,
   7. step: 0.05,
   8. style: SliderStyle.NONE,
   9. direction: Axis.Vertical,
   10. reverse: true
   11. })
   12. .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
   13. .height(160)
   14. .selectedColor(Color.White)
   15. .trackColor(Color.Black)
   16. .trackThickness(40)

   18. Image($r('app.media.sun_max_fill'))
   19. .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
   20. .margin({ top: 120 })
   21. .width(20)
   22. .height(20)
   23. }
   24. .margin({
   25. top: 0,
   26. right: 0
   27. })
   28. }
   29. .width('50%')
   30. .alignItems(HorizontalAlign.End)
   31. .justifyContent(FlexAlign.Center)
   32. .padding({
   33. right: 30,
   34. bottom: 20
   35. })
   ```

   [VolumeAndBrightnessView.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/VolumeAndBrightnessView.ets#L27-L62)
2. 在视频播放界面绑定PanGesture滑动手势事件，设置触发条件为仅在屏幕右侧区域且垂直方向滑动Pan手势时，调用setWindowBrightness()方法，实现亮度的调节。

   补充说明：此处setScreenBrightness()为setWindowBrightness()的封装。

   ```
   1. .gesture(
   2. // Sliding in the vertical direction
   3. PanGesture({ direction: PanDirection.Vertical })
   4. .onActionStart(() => {
   5. })
   6. .onActionUpdate((event: GestureEvent) => {
   7. // The area on the right side of the screen
   8. if (event.fingerList[0].globalX > (this.screenWidth / 2)) {
   9. if (this.isInputtingBulletComment) {
   10. return; // When inputting bullet comment, disable screen brightness change
   11. }
   12. this.visible = true;
   13. let curBrightness = this.screenBrightness -
   14. this.getUIContext().vp2px(event.offsetY) / this.getUIContext().vp2px(this.screenHeight);
   15. curBrightness = this.getValidValue(curBrightness, 0.0, 1.0);
   16. this.screenBrightness = curBrightness;
   17. this.setScreenBrightness(this.screenBrightness);
   18. } else {
   19. this.visible = false;
   20. let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
   21. curVolume = this.getValidValue(curVolume, 0.0, 15.0);
   22. this.volume = curVolume;
   23. }
   24. })
   25. .onActionEnd(() => {
   26. setTimeout(() => {
   27. this.visible = false;
   28. }, 3000)
   29. })
   30. )
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L660-L690)

## 焦点管理

### 场景描述

通过正确设置音频流类型、中断事件处理和自定义焦点策略，完成播放过程音频焦点管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/qhYS0UG7Qtuz_GLi5zWCNw/zh-cn_image_0000002452849926.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=98F53D5038B977237B197C39C2CE83727783155990D6B818BFE198E331504F36 "点击放大")

### 实现原理

通过AVPlayer的[on('audioInterrupt')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiointerrupt9)方法，监听音频焦点变化，根据不同的[打断类型](../harmonyos-references/arkts-apis-audio-e.md#interruptforcetype9)和[中断提示](../harmonyos-references/arkts-apis-audio-e.md#interrupthint)作相应的处理，更多焦点管理相关说明可参考[音频焦点管理](bpta-audio-focus-management.md)。

* 当闹钟或电话等外部打断事件发生时，打断类型为强制打断（INTERRUPT\_FORCE），视频会自动中断播放。
* 当闹钟或电话的提示音结束后，系统将发送打断类型为共享打断类型(INTERRUPT\_SHARE)、中断提示为音频可继续播放(INTERRUPT\_HINT\_RESUME)的事件，应用在监听到该事件时调用AVPlayer的play()函数恢复播放。

### 开发步骤

1. 通过AVPlayer实例注册[on('audioInterrupt')](../harmonyos-references/arkts-apis-media-avplayer.md#onaudiointerrupt9)方法，监听外部打断事件，当打断类型为INTERRUPT\_FORCE时，视频会自动中断播放。
2. 当打断类型为INTERRUPT\_SHARE、中断提示为INTERRUPT\_HINT\_RESUME时，调用videoPlay()函数恢复播放视频。

   补充说明：此处videoPlay()为[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)的封装。

   ```
   1. private setInterruptCallback() {
   2. if (!this.avPlayer) {
   3. return;
   4. }
   5. this.avPlayer.on('audioInterrupt', async (interruptEvent: audio.InterruptEvent) => {
   6. if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_FORCE) {
   7. // For the INTERRUPT_FORCE type: Audio-related processing has been performed by the system, and the
   8. // application needs to update its own state and make the corresponding adjustments.
   9. switch (interruptEvent.hintType) {
   10. // This branch indicates that the system has paused the audio stream (temporarily lost focus).
   11. case audio.InterruptHint.INTERRUPT_HINT_PAUSE:
   12. // This branch indicates that the system has stopped the audio stream (permanently lost focus).
   13. case audio.InterruptHint.INTERRUPT_HINT_STOP:
   14. this.isPlaying = false;
   15. this.updateIsPlay();
   16. break;
   17. // This branch indicates that the system has reduced the audio volume (default to 20% of the normal volume).
   18. case audio.InterruptHint.INTERRUPT_HINT_DUCK:
   19. // This branch indicates that the system has restored the audio volume to normal.
   20. case audio.InterruptHint.INTERRUPT_HINT_UNDUCK:
   21. break;
   22. default:
   23. break;
   24. }
   25. } else if (interruptEvent.forceType === audio.InterruptForceType.INTERRUPT_SHARE) {
   26. // For the INTERRUPT_SHARE type: The application can choose to perform related actions or ignore the
   27. // audio interruption event.
   28. switch (interruptEvent.hintType) {
   29. // This branch indicates that the audio stream, which was paused due to temporary loss of focus,
   30. // can resume playing.
   31. case audio.InterruptHint.INTERRUPT_HINT_RESUME:
   32. this.videoPlay();
   33. break;
   34. default:
   35. break;
   36. }
   37. }
   38. })
   39. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L159-L198)

## 前后台感知

### 场景描述

应用从前台切到后台，再从后台切回前台时，能够保持原有进度继续播放原视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/9oC4EnDJQwqDlgKCmMI2tw/zh-cn_image_0000002486049697.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=A55175EFEBEA98DEB09A401EB555E85E0AE06C1A27CAE40F84F0B9791C137D4E "点击放大")

### 实现原理

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)。

### 开发步骤

1. 在主页面的onPageShow()和onPageHide()里变更状态变量。

   ```
   1. onPageHide(): void {
   2. this.isPageShow = false;
   3. }
   ```

   [IndexPage.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/pages/IndexPage.ets#L75-L78)

   ```
   1. onPageShow(): void {
   2. this.isPageShow = true;
   3. }
   ```

   [IndexPage.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/pages/IndexPage.ets#L82-L85)
2. 在视频播放组件里对该状态变量添加@Watch装饰器。

   ```
   1. @Prop @Watch('onPageShowChange') isPageShow: boolean = false; // Whether the app is on the front end or back end
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L43-L43)
3. 通过监听事件onPageShowChange调用AVPlayer的播放/暂停方法，以实现切换到后台时视频暂停播放、切回前台时视频恢复播放。

   补充说明：此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，resumePlayback()和pausePlay()分别为[play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)和[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)的封装。

   ```
   1. onPageShowChange() {
   2. if (!this.isPIPShow && this.curIndex === this.index) {
   3. this.isPageShow ? this.resumePlayback() : this.pausePlay();
   4. }
   5. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L161-L166)

   ```
   1. private resumePlayback() {
   2. if (!this.avPlayerController.isPlaying) {
   3. this.avPlayerController.videoPlay();
   4. }
   5. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L498-L503)

   ```
   1. private pausePlay() {
   2. if (this.avPlayerController.isPlaying) {
   3. this.avPlayerController.videoPause();
   4. }
   5. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L489-L494)

## 弹幕发送与显示

### 场景描述

视频弹幕发送与显示是影音娱乐类应用中的高频使用场景之一，如用户在播放视频、观看直播时可以发送弹幕，实时评论互动，增强用户参与度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/Y9Y4hMOdTKKoxNrnjtBu7w/zh-cn_image_0000002452690354.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=2E49EC8CEB89AEDDAA0E695B94A5F00E7E68035FE000CB8590A212AB21ECFF71 "点击放大")

### 实现原理

通过数组保存实现弹幕发送，基于[setInterval()](../harmonyos-references/js-apis-timer.md#setinterval)函数和[translate](../harmonyos-references/ts-page-transition-animation.md#translate)属性实现弹幕水平移动的动画效果。

### 开发步骤

1. 在视频播放组件里定义一个空数组，用来保存发送的弹幕，用户输入弹幕点击发送后将输入内容存入当前数组中。

   ```
   1. private sendBulletComment() {
   2. if (this.bulletCommentInput.trim()) {
   3. this.bulletComments = [...this.bulletComments, new BulletComment(this.bulletCommentInput, true)];
   4. this.bulletCommentInput = '';
   5. if (this.bulletComments.length > 50) {
   6. this.bulletComments = this.bulletComments.slice(1);
   7. }
   8. }
   9. this.resumePlayback(); // Resume video playback after sending
   10. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L507-L517)
2. 在弹幕展示组件中，通过调用[setInterval](../harmonyos-references/js-apis-timer.md#setinterval)函数设置定时器，定时器定时刷新承载弹幕内容的Text组件的[translate](../harmonyos-references/ts-page-transition-animation.md#translate)属性，刷新所有弹幕位置。

   ```
   1. // Start bullet comment animation
   2. private startAnimation() {
   3. if (this.timerId > 0) {
   4. clearInterval(this.timerId);
   5. }
   6. // Refresh the postion of bullet comments by timer
   7. this.timerId = setInterval(() => {
   8. let needUpdate = false;
   9. this.bulletComments.forEach(item => {
   10. const positionX = item.translateX - item.speed;
   11. if (positionX !== item.translateX) {
   12. item.translateX = positionX; // Set new X position of bullet comment
   13. needUpdate = true;
   14. }
   15. });
   16. const beforeLength = this.bulletComments.length;
   17. this.bulletComments =
   18. this.bulletComments.filter(item => item.translateX > -20); // Remove the bullet comment which beyond the screen
   19. if (needUpdate || this.bulletComments.length !== beforeLength) {
   20. this.forceUpdate = !this.forceUpdate; // Trigger ui refresh
   21. }
   22. }, 16);
   23. }
   ```

   [BulletCommentView.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/BulletCommentView.ets#L36-L59)

## 视频截图

### 场景描述

视频截图是影音娱乐类应用中的典型场景之一，如用户可在观看视频时截取画面，并对截图的前后帧进行微调，避免所截图片与预期不符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Vqcj_TAESpy1vMBCjQMcFw/zh-cn_image_0000002485889761.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=4539655574B750B36B7B8FA1C21C8EAAFF1247D352F1324CB6683821BF046BC1 "点击放大")

### 实现原理

以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件，通过[ComponentSnapshot](../harmonyos-guides/arkts-uicontext-component-snapshot.md)对象获取组件截图的能力。

### 开发步骤

1. 通过getUIContext().getComponentSnapshot().get()方法获取视频播放组件XComponent当前截图。

   ```
   1. private async screenshot() {
   2. try {
   3. this.pixmap = await this.getUIContext().getComponentSnapshot().get(`videoXComponent_${this.curSource.index}`);
   4. } catch (exception) {
   5. hilog.error(0x0000, TAG, `screenshot failed: code: ${exception.code}, message: ${exception.message}`);
   6. }
   7. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L539-L546)
2. 调用AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)方法跳转到视频播放的上一秒或下一秒，再次通过步骤1的方法获取当前截图。

   补充说明：此处avPlayerController为基于AVPlayer实现基本播控的控制器实例，videoSeek()为seek()的封装。

   ```
   1. private async clickPreviousFrame() {
   2. this.avPlayerController?.videoSeek(this.screenshotTime - 1000 / ScreenShotConstants.FRAME_RATE);
   3. this.pausePlay();
   4. setTimeout(() => {
   5. this.screenshot()
   6. }, 500)
   7. this.screenshotTime -= 1000 / ScreenShotConstants.FRAME_RATE
   8. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L550-L558)

   ```
   1. private async clickNextFrame() {
   2. this.avPlayerController?.videoSeek(this.screenshotTime + 1000 / ScreenShotConstants.FRAME_RATE);
   3. this.pausePlay();
   4. setTimeout(() => {
   5. this.screenshot()
   6. }, 500)
   7. this.screenshotTime += 1000 / ScreenShotConstants.FRAME_RATE
   8. }
   ```

   [AVPlayer.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/view/AVPlayer.ets#L562-L570)

## 画中画播放

### 场景描述

应用在视频播放时，可以使用画中画能力将视频内容以小窗（画中画）模式呈现。切换为小窗（画中画）模式后，用户可以进行其他界面操作，提升使用体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/QW_xRSf4TOCJgD3PHpIBtw/zh-cn_image_0000002452850030.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=21746806702DAAB768DE664600B7C8B69FC596A1E5C0225C729CF46F9C82D9E2 "点击放大")

### 实现原理

以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件，通过[PiPWindow](../harmonyos-references/js-apis-pipwindow.md#导入模块)模块实现画中画基础功能。

说明

* 仅支持以XComponent作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。
* 在API version 20之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从API version 20开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。

### 开发步骤

1. 创建画中画控制器，设置[setAutoStartEnabled()](../harmonyos-references/js-apis-pipwindow.md#setautostartenabled)为true以在应用返回桌面时启动画中画。

   ```
   1. // Create PIPWindows
   2. async createPipController() {
   3. if (!this.pipController) {
   4. try {
   5. this.pipController = await PiPWindow.create({
   6. context: this.context,
   7. componentController: this.xComponentController,
   8. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY
   9. });
   10. } catch (exception) {
   11. Logger.error(TAG,
   12. `pipController init failed, Code:${exception.code}, message:${exception.message}`);
   13. }
   14. }
   15. this.pipController?.on('stateChange', (State: PiPWindow.PiPState, reason: string) => {
   16. this.onStateChange(State, reason);
   17. })

   19. this.pipController?.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
   20. this.onActionEvent(event, status);
   21. })
   22. this.pipController?.setAutoStartEnabled(true); // Key point:  Set the animation to start when the application returns to the desktop
   23. }
   ```

   [PipWindowController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/PipWindowController.ets#L37-L60)
2. 注册生命周期事件和控制事件回调。

   ```
   1. onStateChange(state: PiPWindow.PiPState, reason: string) {
   2. switch (state) {
   3. case PiPWindow.PiPState.ABOUT_TO_START:
   4. this.curState = 'ABOUT_TO_START';
   5. break;
   6. case PiPWindow.PiPState.STARTED:
   7. this.curState = 'STARTED';
   8. let status: PiPWindow.PiPControlStatus =
   9. this.avPlayerController?.isPlaying ? PiPWindow.PiPControlStatus.PLAY : PiPWindow.PiPControlStatus.PAUSE;
   10. this.pipController?.updatePiPControlStatus(PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE, status);
   11. break;
   12. case PiPWindow.PiPState.ABOUT_TO_STOP:
   13. this.curState = 'ABOUT_TO_STOP';
   14. break;
   15. case PiPWindow.PiPState.STOPPED:
   16. this.curState = 'STOPPED';
   17. break;
   18. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
   19. this.curState = 'ABOUT_TO_RESTORE';
   20. break;
   21. case PiPWindow.PiPState.ERROR:
   22. this.curState = 'ERROR';
   23. break;
   24. default:
   25. break;
   26. }
   27. }
   ```

   [PipWindowController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/PipWindowController.ets#L78-L105)

   ```
   1. onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
   2. switch (event) {
   3. case 'playbackStateChanged':
   4. if (status === 0) {
   5. this.avPlayerController?.videoPause();
   6. } else {
   7. this.avPlayerController?.videoPlay();
   8. }
   9. break;
   10. default:
   11. break;
   12. }
   13. }
   ```

   [PipWindowController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/PipWindowController.ets#L109-L122)
3. 销毁画中画控制器，设置setAutoStartEnabled()为false以关闭画中画。

   ```
   1. // Destroy PIPWindows
   2. destroyPipController() {
   3. if (!this.pipController) {
   4. return;
   5. }
   6. this.pipController.setAutoStartEnabled(false);
   7. this.pipController.off('stateChange');
   8. this.pipController.off('controlPanelActionEvent');
   9. this.pipController = undefined;
   10. }
   ```

   [PipWindowController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/PipWindowController.ets#L64-L74)

## 接入播控中心

### 场景描述

通过播控中心，控制播放、暂停、切换上下视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/ba6kgD1MTR-C9H0tKjhIjw/zh-cn_image_0000002486049849.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=F3E8EDB4614F6005801A529291F3AB6B042AA2ED9F6F764252C94A3F51E6122D "点击放大")

### 实现原理

通过[AVSessionKit](../harmonyos-guides/avsession-kit.md)音频播控服务实现视频应用接入播控中心。

### 开发步骤

1. 通过[createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建AVSession实例并激活媒体会话，[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)设置为video。

   ```
   1. public initAvSession() {
   2. this.context = AppStorage.get('context');
   3. if (!this.context) {
   4. Logger.error(TAG, 'session create failed : context is undefined');
   5. return;
   6. }
   7. avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
   8. this.avSession = avSession;
   9. BackgroundTaskManager.startContinuousTask(this.context);
   10. this.setLaunchAbility();
   11. this.avSession.activate().catch((err: BusinessError) => {
   12. Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
   13. });
   14. }).catch((err: BusinessError) => {
   15. Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
   16. });
   17. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L43-L60)
2. 通过[setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)把会话的一些元数据信息设置给系统，从而在播控中心界面进行展示。如媒体ID（assetId）、标题（title）、播控中心显示的图片（mediaImage）、媒体时长（duration）等。

   ```
   1. // Set video session metadata
   2. public async setAVMetadata(curSource: VideoData, duration: number) {
   3. if (curSource === undefined) {
   4. Logger.error(TAG, 'SetAVMetadata Error, curSource is null');
   5. return;
   6. }
   7. let metadata: avSession.AVMetadata = {
   8. assetId: `${curSource.index}`,
   9. title: curSource.name,
   10. duration: duration // Video duration
   11. };
   12. if (this.avSession) {
   13. this.avSession.setAVMetadata(metadata).then(() => {
   14. this.avSessionMetadata = metadata;
   15. }).catch((err: BusinessError) => {
   16. Logger.error(TAG, `SetAVMetadata BusinessError: code: ${err.code}, message: ${err.message}`);
   17. });
   18. }
   19. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L72-L91)
3. 设置用于被播控中心拉起的UIAbility。

   ```
   1. private setLaunchAbility() {
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
   12. operationType: wantAgent.OperationType.START_ABILITIES,
   13. requestCode: 0,
   14. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   15. };
   16. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
   17. if (this.avSession) {
   18. this.avSession.setLaunchAbility(agent).catch((err: BusinessError) => {
   19. Logger.error(TAG, `setLaunchAbility failed: code: ${err.code}, message: ${err.message}`);
   20. });
   21. }
   22. }).catch((err: BusinessError) => {
   23. Logger.error(TAG, `getWantAgent failed: code: ${err.code}, message: ${err.message}`);
   24. });
   25. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L95-L120)
4. 注册播控命令事件监听，便于响应用户通过播控中心下发的播控命令，比如播放[on('play')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplay10)、暂停[on('pause')](../harmonyos-references/arkts-apis-avsession-avsession.md#onpause10)、上一曲[on('playPrevious')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplayprevious10)、下一曲[on('playNext')](../harmonyos-references/arkts-apis-avsession-avsession.md#onplaynext10)等。

   ```
   1. // Set background control monitor the callback events
   2. public async setAvSessionListener() {
   3. if (!this.avSessionController) {
   4. return;
   5. }
   6. try {
   7. this.avSessionController.getAvSession()?.on('play', () => this.sessionPlayCallback());
   8. this.avSessionController.getAvSession()?.on('pause', () => this.sessionPauseCallback());
   9. this.avSessionController.getAvSession()?.on('seek', (seekTime: number) => this.sessionSeekCallback(seekTime));
   10. this.avSessionController.getAvSession()?.on('setLoopMode', (mode: avSession.LoopMode) => {
   11. Logger.info(`on setLoopMode: ${mode}`)
   12. });
   13. this.avSessionController.getAvSession()?.on('playPrevious', () => {
   14. this.sessionPlayPreviousCallback();
   15. });
   16. this.avSessionController.getAvSession()?.on('playNext', () => {
   17. this.sessionPlayNextCallback();
   18. });
   19. } catch (exception) {
   20. Logger.error(TAG,
   21. `Invoke setAvSessionListener failed, code is ${exception.code}, message is ${exception.message}`);
   22. }
   23. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L306-L329)
5. 应用状态上报播控中心，当视频状态发生改变时，需要通过[setAVPlaybackState()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)向播控中心上报视频状态，来达到播控中心与应用的状态同步，包括播放状态（state）、播放位置（position）、当前媒体播放时长（duration）等。

   ```
   1. // Report the video state to background control
   2. private updateIsPlay() {
   3. this.avSessionController.setAvSessionPlayState({
   4. state: this.isPlaying ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
   5. avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
   6. position: {
   7. elapsedTime: this.currentTime,
   8. updateTime: new Date().getTime()
   9. },
   10. duration: this.currentTime
   11. });
   12. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L333-L345)

   ```
   1. public setAvSessionPlayState(playbackState: avSession.AVPlaybackState) {
   2. if (this.avSession) {
   3. this.avSession.setAVPlaybackState(playbackState, (err: BusinessError) => {
   4. if (err) {
   5. Logger.error(TAG, `SetAVPlaybackState BusinessError: code: ${err.code}, message: ${err.message}`);
   6. } else {
   7. Logger.info(TAG, 'SetAVPlaybackState successfully');
   8. }
   9. });
   10. }
   11. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L124-L135)

## 后台播放

### 场景描述

视频切换到后台播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/JnbH185vR8e6-6rknOl4YQ/zh-cn_image_0000002452690518.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=3C385A7AF820B94D1C187CF87286A301CC2ED23BEF018E4217342027B8BDC138 "点击放大")

### 实现原理

首先需实现播控中心的接入，在此基础上申请后台运行权限并设置后台模式，同时为视频应用创建长时后台任务，从而实现视频在后台持续播放的功能。

说明

后台播放的实现依赖于播控中心，建议开发者先完成[接入播控中心](bpta-avplayer-long-video.md#section1489902163313)章节的学习。

### 开发步骤

1. 在module.json5配置文件中配置ohos.permission.KEEP\_BACKGROUND\_RUNNING权限和后台模式audioPlayback。

   ```
   1. "requestPermissions": [
   2. {
   3. "name": "ohos.permission.KEEP_BACKGROUND_RUNNING",
   4. "reason": "$string:reason_background",
   5. "usedScene": {
   6. "abilities": [
   7. "EntryAbility"
   8. ],
   9. "when": "always"
   10. }
   11. }
   12. ],
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/module.json5#L45-L56)

   ```
   1. "backgroundModes": [
   2. "audioPlayback"
   3. ],
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/module.json5#L28-L30)
2. 创建后台任务管理类，实现后台任务的申请（startContinuousTask）与取消（stopContinuousTask），长时任务类型选择[AUDIO\_PLAYBACK](../harmonyos-references/js-apis-resourceschedule-backgroundtaskmanager.md#backgroundmode)，表示视频后台播放。

   ```
   1. public static startContinuousTask(context?: common.UIAbilityContext): void {
   2. if (!context) {
   3. return;
   4. }
   5. let wantAgentInfo: wantAgent.WantAgentInfo = {
   6. wants: [
   7. {
   8. bundleName: context.abilityInfo.bundleName,
   9. abilityName: context.abilityInfo.name
   10. }
   11. ],
   12. operationType: wantAgent.OperationType.START_ABILITY,
   13. requestCode: 0,
   14. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   15. };
   16. wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
   17. if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
   18. backgroundTaskManager.startBackgroundRunning(context,
   19. backgroundTaskManager.BackgroundMode.AUDIO_PLAYBACK, wantAgentObj).then(() => {
   20. }).catch((err: BusinessError) => {
   21. Logger.error(TAG, `startBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
   22. });
   23. }
   24. }).catch((err: BusinessError) => {
   25. Logger.error(TAG, `getWantAgent failed, code is ${err.code}, message is ${err.message}`);
   26. });
   27. }
   ```

   [BackgroundTaskManager.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/common/utils/BackgroundTaskManager.ets#L25-L52)

   ```
   1. public static stopContinuousTask(context?: common.UIAbilityContext): void {
   2. if (!context) {
   3. return;
   4. }
   5. if (canIUse('SystemCapability.ResourceSchedule.BackgroundTaskManager.Core')) {
   6. backgroundTaskManager.stopBackgroundRunning(context).then(() => {
   7. }).catch((err: BusinessError) => {
   8. Logger.error(TAG, `stopBackgroundRunning failed, code is ${err.code}, message is ${err.message}`);
   9. });
   10. }
   11. }
   ```

   [BackgroundTaskManager.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/common/utils/BackgroundTaskManager.ets#L56-L67)
3. 在AVSession创建和释放时，分别申请和销毁后台长时任务。

   ```
   1. public initAvSession() {
   2. this.context = AppStorage.get('context');
   3. if (!this.context) {
   4. Logger.error(TAG, 'session create failed : context is undefined');
   5. return;
   6. }
   7. avSession.createAVSession(this.context, 'LONG_VIDEO_SESSION', 'video').then(async (avSession) => {
   8. this.avSession = avSession;
   9. BackgroundTaskManager.startContinuousTask(this.context);
   10. this.setLaunchAbility();
   11. this.avSession.activate().catch((err: BusinessError) => {
   12. Logger.error(TAG, `avSession activate failed, code is ${err.code}, message is ${err.message}`);
   13. });
   14. }).catch((err: BusinessError) => {
   15. Logger.error(TAG, `createAVSession failed, code is ${err.code}, message is ${err.message}`);
   16. });
   17. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L43-L60)

   ```
   1. async unregisterSessionListener() {
   2. if (!this.avSession) {
   3. return;
   4. }
   5. try {
   6. this.avSession.off('play');
   7. this.avSession.off('pause');
   8. this.avSession.off('playNext');
   9. this.avSession.off('playPrevious');
   10. this.avSession.off('setLoopMode');
   11. this.avSession.off('seek');
   12. } catch (exception) {
   13. Logger.error(TAG, `unregisterSessionListener failed: code: ${exception.code}, message: ${exception.message}`);
   14. }
   15. BackgroundTaskManager.stopContinuousTask(this.context);
   16. }
   ```

   [AvSessionController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvSessionController.ets#L139-L155)

## 视频首帧显示

### 场景描述

在播放列表或者窗口中显示视频的首帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ntZQ6k4CSkOO5ZyC5Ff_bQ/zh-cn_image_0000002485889933.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=6AB6F4B20A26B86CDE2CE71FF8CC2E3044132DCD209C067D5F70EC93307F250B "点击放大")

### 实现原理

* 通过[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12)方法获取本地视频的首帧图片在视频列表展示。
* 通过设置播放策略[setPlaybackStrategy](../harmonyos-references/arkts-apis-media-avplayer.md#setplaybackstrategy12)的showFirstFrameOnPrepare属性为true来实现AVPlayer显示视频起播首帧。

### 开发步骤

播放列表中显示视频首帧的实现步骤：

1. 使用media.AVImageGenerator实例的[fetchFrameByTime()](../harmonyos-references/arkts-apis-media-avimagegenerator.md#fetchframebytime12)方法获取本地视频的首帧图片在列表展示。

   ```
   1. public static async getThumbnailFromVideo(src: string, timeUs: number) {
   2. let pixelMap: image.PixelMap | undefined = undefined;
   3. let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
   4. let param: media.PixelMapParams = {
   5. width: 540,
   6. height: 304
   7. };
   8. try {
   9. let generator: media.AVImageGenerator = await media.createAVImageGenerator();
   10. let fileDescriptor = await uiContext?.getHostContext()?.resourceManager?.getRawFd(src);
   11. generator.fdSrc = fileDescriptor;
   12. pixelMap = await generator.fetchFrameByTime(timeUs, queryOption, param);
   13. } catch (exception) {
   14. hilog.error(0x0000, 'ImageUtil',
   15. `getThumbnailFromVideo failed, code is ${exception.code}, message is ${exception.message}`)
   16. }
   17. return pixelMap;
   18. }
   ```

   [ImageUtil.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/common/utils/ImageUtil.ets#L24-L42)

播放窗口中显示视频首帧的实现步骤：

1. 确认AVPlayer实例中的[on('stateChange')](../harmonyos-references/arkts-apis-media-avplayer.md#onstatechange9)方法在prepared状态下没有调用this.avPlayer.play()，如有调用，则去掉，避免视频在加载完毕后自动播放。
2. 在on('stateChange')方法中initialized状态下，设置播放策略[setPlaybackStrategy](../harmonyos-references/arkts-apis-media-i.md#playbackstrategy12)的showFirstFrameOnPrepare为true。

   ```
   1. case 'initialized': // This status is reported after the playback source is set on the AVPlayer.
   2. Logger.info(TAG, 'setAVPlayerCallback AVPlayerState initialized called.');
   3. // Set the display screen. This parameter is not required when the resource to be played is audio-only.
   4. this.avPlayer.surfaceId = this.surfaceID;

   6. try {
   7. await this.avPlayer.setPlaybackStrategy({
   8. preferredBufferDuration: 20,
   9. showFirstFrameOnPrepare: true
   10. });
   11. } catch (exception) {
   12. Logger.error(TAG,
   13. `setPlaybackStrategy failed. Cause code: ${exception.code}, message: ${exception.message}`);
   14. }
   15. this.avPlayer.prepare().catch((err: BusinessError) => {
   16. Logger.error(TAG, `prepare failed. Code:${err.code}, message:${err.message}`);
   17. });
   18. break;
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L215-L232)

## 横竖屏切换与旋转感知

### 场景描述

用户播放视频时可以根据实际需求进行横竖屏切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/3HSYkg4CT7Sst3iu0Ck7pA/zh-cn_image_0000002452850190.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=2FEE0E08C12D06E02824E9298AAAA1C3DFA4081D96117CDB4411294C355BB26B "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/JC98a76-TCWTJKSw93-w-Q/zh-cn_image_0000002486049953.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=BD837AF833B7AA5FF8CC8244408AC6979408143EB28329DB4DA363DC28B3925A "点击放大")

### 实现原理

* 通过设置orientation为auto\_rotation\_restricted实现传感器自动感知。
* 通过设置window.Orientation为USER\_ROTATION\_LANDSCAPE/USER\_ROTATION\_PORTRAIT实现横竖屏的手动切换。

### 开发步骤

通过传感器旋转自动感知切换：

1. 在模块级配置文件module.json5中设置[窗口显示方向](../harmonyos-references/arkts-apis-window-e.md#orientation9)为AUTO\_ROTATION\_RESTRICTED。

   ```
   1. "orientation": "auto_rotation_restricted",
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/module.json5#L25-L25)

通过点击按钮实现横竖屏切换：

1. 封装横竖屏切换的实现方法。

   ```
   1. setMainWindowOrientation(orientation: window.Orientation, callback?: Function): void {
   2. if (this.mainWindowClass === undefined) {
   3. hilog.error(0x0000, TAG, 'MainWindowClass is undefined');
   4. return;
   5. }
   6. this.mainWindowClass.setPreferredOrientation(orientation).then(() => {
   7. callback?.();
   8. }).catch((err: BusinessError) => {
   9. hilog.error(0x0000, TAG,
   10. `Failed to set the ${orientation} of main window. Code:${err.code}, message:${err.message}`);
   11. });
   12. }
   ```

   [WindowUtil.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/common/utils/WindowUtil.ets#L60-L72)
2. 点击横屏播放按钮时，设置window.Orientation为USER\_ROTATION\_LANDSCAPE。

   ```
   1. this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_LANDSCAPE);
   ```

   [IndexPage.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/pages/IndexPage.ets#L161-L161)
3. 点击返回按钮时，设置window.Orientation为USER\_ROTATION\_PORTRAIT。

   ```
   1. this.windowUtil.setMainWindowOrientation(window.Orientation.USER_ROTATION_PORTRAIT);
   ```

   [IndexPage.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-long-video/blob/master/entry/src/main/ets/pages/IndexPage.ets#L94-L94)

## 视频无缝转场播放

### 场景描述

用户在横竖屏切换后，视频保持原有进度继续播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/dGzg7se9RyGuhh5Ayq1pJg/zh-cn_image_0000002452690582.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=1C829F5BCEB14739F93A70C1B05548A7A1F766A9B364A4E30D637D3F20E38856 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/hfWvuyaGS6-UhNzgjF6fbA/zh-cn_image_0000002485889989.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002025Z&HW-CC-Expire=86400&HW-CC-Sign=B837BC9A8F1E404E5CB890C47024DB67F203FDAD72823529C355EC256C909108 "点击放大")

### 实现原理

基于[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)与[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)实现视频播放，在横竖屏来回切换时，[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)本身具有保持原有进度继续播放的特性，开发者无需进行额外开发。

## 示例代码

[基于AVPlayer实现长视频播放](https://gitcode.com/harmonyos_samples/avplayer-long-video)
