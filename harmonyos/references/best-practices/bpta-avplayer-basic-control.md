---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-basic-control
title: 基于AVPlayer基础播控实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 基于AVPlayer播放视频系列开发实践 > 基于AVPlayer基础播控实践
category: best-practices
scraped_at: 2026-04-29T14:11:16+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:8f3a5302a80d822901f5555ac47d836cd46519cf2b9afb1c7bd941ba59fd0d55
---

## 概述

本文适用于视频播放类应用的开发，针对市场上主流视频播放类应用的常见场景，介绍了如何基于AVPlayer系统播放器实现视频播放应用。

本文指导开发者基于HarmonyOS提供的媒体和ArkUI等能力，实现视频播放、暂停、跳转播放、静音播放、循环播放、窗口缩放模式设置、倍速设置、音量设置等基本开发场景，可以为视频播放应用提供灵活的交互体验和良好的观看效果。

说明

在阅读本文之前，建议开发者先熟悉视频播放器[《使用AVPlayer播放视频(ArkTS)》](../harmonyos-guides/video-playback.md)。

## 场景分析

| 场景名称 | 描述 | 实现方案 |
| --- | --- | --- |
| [基础播控](bpta-avplayer-basic-control.md#section169581112135319) | 视频资源的加载、播放、暂停、退出等操作。 | 使用[AVPlayer接口](../harmonyos-references/arkts-apis-media-avplayer.md)实现。 |
| [跳转播放](bpta-avplayer-basic-control.md#section1897734041617) | 滑动进度条精准跳转到指定时间进行播放。 | 使用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条，在其onChange回调中触发进度调节。 |
| [静音播放](bpta-avplayer-basic-control.md#section15152110181715) | 点击按钮设置静音播放。 | 使用AVPlayer的[setMediaMuted()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)控制静音状态。 |
| [循环播放](bpta-avplayer-basic-control.md#section09619253174) | 视频播放结束后会从初始位置再次播放。 | 通过在prepared状态下，设置视频播放器AVPlayer的[loop属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)值为true，实现视频循环播放。 |
| [窗口缩放模式设置](bpta-avplayer-basic-control.md#section18974144910175) | 设置窗口缩放模式体验不同的缩放效果。 | 通过设置AVPlayer的[videoScaleType属性](../harmonyos-references/arkts-apis-media-e.md#videoscaletype9)设置窗口缩放模式。 |
| [倍速设置](bpta-avplayer-basic-control.md#section1333481316184) | 可以通过[点击按钮选择倍速](bpta-avplayer-basic-control.md#section1333481316184)或者通过[长按手势调节倍速](bpta-avplayer-basic-control.md#section364983943913)。 | 使用AVPlayer的[setSpeed()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)设置倍速。通过添加按钮和弹窗实现通过按钮调节倍速；通过给组件绑定[长按手势](../harmonyos-references/ts-basic-gestures-longpressgesture.md)实现长按倍速。 |
| [音量设置](bpta-avplayer-basic-control.md#section74003157187) | 可以滑动屏幕调节音量。 | 使用[AVVolumePanel组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)显示音量，通过给组件绑定[手势滑动监听](../harmonyos-references/ts-basic-gestures-pangesture.md)实现调节音量。 |
| [字幕挂载与切换](bpta-avplayer-basic-control.md#section627701016296) | 视频下方显示字幕。 | 使用AVPlayer的[addSubtitleFromFd()方法](../harmonyos-references/arkts-apis-media-avplayer.md#addsubtitlefromfd12)设置外挂字幕资源，并通过AVPlayer实例注册字幕回调函数[on('subtitleUpdate')](../harmonyos-references/arkts-apis-media-avplayer.md#onsubtitleupdate12)；通过切换字幕资源并使用AVPlayer的[reset()方法](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)重置播放实现切换字幕。 |

## 基础播控

### 场景描述

通过[AVPlayer](../harmonyos-guides/video-playback.md)实现核心视频播放控制能力，包括视频资源加载、播放、暂停、停止及退出等操作。

### 实现原理

本开发指导将介绍如何使用AVPlayer开发视频播放功能，以完整地播放一个视频作为示例，实现端到端播放原始媒体资源。

播放的全流程包含：创建AVPlayer，设置播放资源和窗口，设置播放参数（音量/倍速/缩放模式），播放控制（播放/暂停/跳转/停止），重置，销毁资源。在进行应用开发的过程中，开发者可以通过AVPlayer的state属性主动获取当前状态或使用on('stateChange')方法监听状态变化。如果应用在视频播放器处于错误状态时执行操作，系统可能会抛出异常或生成其他未定义的行为。

原理详情可查看[《使用AVPlayer播放视频(ArkTS)》](../harmonyos-guides/video-playback.md)。

### 开发步骤

1. 创建实例：调用createAVPlayer()接口创建AVPlayer实例，初始化进入idle状态。
2. 设置视频资源：设置AVPlayer实例的url或者fdSrc属性值，进入initialized状态。
3. 准备播放：调用prepare()接口，进入prepared状态。
4. 播放：调用play()接口，进入playing状态。
5. 暂停：调用pause()接口，进入paused状态。
6. 停止：调用stop()接口，进入stopped状态。
7. 销毁实例：调用release()接口销毁实例，AVPlayer进入released状态，退出播放。

## 跳转播放

### 场景描述

进度条是视频应用的一个基础能力，可以通过点击或拖动进度条精准跳转到指定时间进行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/POkJC9zsTBCX_sot1QJFnw/zh-cn_image_0000002453067562.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=5EF1AEA2BB9EB95A389F4742F0569DE62792F4F6FD01ED750FA192B02D4CB01F "点击放大")

### 实现原理

基于[Slider组件](../harmonyos-references/ts-basic-components-slider.md)和视频播放器AVPlayer的[seek()方法](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)实现跳转播放。

### 开发步骤

采用[Slider组件](../harmonyos-references/ts-basic-components-slider.md)实现进度条功能，根据Slider组件属性设置进度条样式，并在其onChange()事件中触发视频播放器AVPlayer的[seek()方法](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)跳转到指定播放位置，实现视频进度的控制。

```
1. /**
2. * Progress slider
3. */
4. Slider({
5. value: this.currentTime,
6. min: 0,
7. max: this.durationTime,
8. style: SliderStyle.OutSet
9. })
10. .id('Slider')
11. .blockColor(Color.White)
12. .trackColor(Color.Gray)
13. .selectedColor($r('app.color.slider_selected'))
14. .showTips(false)
15. .onChange((value: number, mode: SliderChangeMode) => {
16. if (mode === SliderChangeMode.Begin) {
17. this.isSwiping = true;
18. this.avPlayerController.videoPause();
19. }
20. this.avPlayerController.videoSeek(value);
21. this.currentTime = value;
22. if (mode === SliderChangeMode.End) {
23. this.isSwiping = false;
24. this.flag = true;
25. this.avPlayerController.videoPlay();
26. }
27. })
```

[VideoOperate.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/views/VideoOperate.ets#L106-L132)

## 静音播放

### 场景描述

通过界面按钮快捷切换视频播放静音状态，实现一键开启或关闭静音，提升媒体播放的交互便捷性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/mQBYdXjwSMu-E83xNPo34g/zh-cn_image_0000002486107325.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=E9F808FBA5F04461718044E3E4AA33423080854AE3E27B72459E9B368B9E0BB0 "点击放大")

### 实现原理

通过视频播放器AVPlayer的[setMediaMuted()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)，实现控制视频静音状态。

### 开发步骤

1. 在底部操作栏添加[Button组件](../harmonyos-references/ts-basic-components-button.md)，按钮显示为icon图标；根据Button组件属性设置按钮样式，并在其onClick()事件中触发视频管理接口AvPlayerController.ets文件中封装的videoMuted()方法。

   ```
   1. /**
   2. * Video Muted Button
   3. */
   4. Button() {
   5. Image(this.isMuted ? $r('app.media.ic_video_speaker_slash') : $r('app.media.ic_video_speaker'))
   6. .width($r('app.float.size_30'))
   7. .height($r('app.float.size_30'))
   8. }
   9. .type(ButtonType.Normal)
   10. .width($r('app.float.size_30'))
   11. .height($r('app.float.size_30'))
   12. .borderRadius($r('app.float.size_20'))
   13. .backgroundColor('rgba(0, 0, 0, 0)')
   14. .margin({ left: $r('app.float.size_5') })
   15. .fontColor(Color.White)
   16. .onClick(() => {
   17. this.isMuted = !this.isMuted;
   18. this.avPlayerController.videoMuted(this.isMuted)
   19. })
   ```

   [VideoOperate.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/views/VideoOperate.ets#L162-L181)
2. videoMuted()方法中调用了视频播放器AVPlayer的[setMediaMuted()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)，实现控制视频静音状态，其中第一个参数[mediaType](../harmonyos-references/arkts-apis-media-e.md#mediatype8)选择媒体类型为MEDIA\_TYPE\_AUD表示音频，第二个参数是静音开关。

   ```
   1. /**
   2. * Video muted
   3. * @param isMuted
   4. * @returns
   5. */
   6. async videoMuted(isMuted: boolean): Promise<void> {
   7. if (this.avPlayer) {
   8. try {
   9. this.isMuted = isMuted;
   10. await this.avPlayer!.setMediaMuted(media.MediaType.MEDIA_TYPE_AUD, isMuted)
   11. } catch (err) {
   12. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   13. `videoMuted failed, code is ${err.code}, message is ${err.message}`);
   14. }
   15. }
   16. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L321-L337)

## 循环播放

### 场景描述

本功能可以用于在视频播放结束后自动将播放器重置至初始状态，使用户能够立即重新开始播放视频内容，实现无缝循环观看体验。

### 开发步骤

在视频prepared状态下，设置视频播放器AVPlayer的[loop属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)值为true，实现视频循环播放。

```
1. // Callback function for state machine changes
2. this.avPlayer.on('stateChange', async (state) => {
3. if (!this.avPlayer) {
4. return;
5. }
6. switch (state) {
7. // ...
8. case 'prepared': // This state machine is reported after the prepare interface is successfully invoked.
9. this.isReady = true;
10. this.avPlayer.loop = true
11. // ...
12. break;
13. // ...
14. }
15. });
```

[AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L168-L253)

## 窗口缩放模式设置

### 场景描述

通过窗口缩放模式设置功能，用户可根据实际观看需求灵活调整视频内容的显示方式。该功能在未设置视频固定宽高时，在窗口尺寸频繁调整、不同宽高比视频源适配、全屏/窗口模式切换及多屏协作等场景下较为重要。

点击按钮即可弹出设置弹窗，可选择"拉伸至与窗口等大"模式，视频拉伸至与窗口等大，适合需要充分利用显示区域且对比例变化不敏感的场景；选择"缩放至最短边填满窗口"模式，视频将保持原始宽高比并以最短边为基准进行缩放，适合需要保持画面比例不变的场景。

**图1** 拉伸至与窗口等大模式  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/iNIVJ5-xSOO78f6YyHVDTg/zh-cn_image_0000002452907970.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=69792B3A6131C4E808698091EDFFF8BE1E38A4DBF3B682764A8EE5EC7FA97EC7 "点击放大")

**图2** 缩放至最短边填满窗口  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/lk5eqzsITgCaCyjuh8E5HA/zh-cn_image_0000002485947349.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=2E7B1B2429AA1D97D751E730AED84C7527B123F075CE4B050CA4C0DFAC9DB776 "点击放大")

### 实现原理

通过设置视频播放器AVPlayer的[videoScaleType](../harmonyos-references/arkts-apis-media-e.md#videoscaletype9)属性值，实现窗口缩放模式的切换。由于VIDEO\_SCALE\_TYPE\_SCALED\_ASPECT（缩放至长边填满窗口）属性值从APIversion20开始才支持在元服务中使用，因此在这之前的版本中可根据屏幕大小为视频设置固定宽高来实现。

说明

在未设置视频固定宽高的情况下，即未设置XComponent的height和width为固定值时，设置AVPlayer的videoScaleType属性值才能生效。

### 开发步骤

1. 可选择拉伸至与窗口等大/缩放至最短边填满窗口模式，选择后调用封装的videoScaleFit()/videoScaleFitCrop()方法。

   ```
   1. List() {
   2. ForEach(this.scaleList, (item: Resource, index) => {
   3. ListItem() {
   4. Column() {
   5. Row() {
   6. Text(item)
   7. // ...
   8. Blank()
   9. Image(this.windowScaleSelect === index ? $r('app.media.ic_radio_selected') :
   10. $r('app.media.ic_radio'))
   11. // ...
   12. }
   13. // ...
   14. }
   15. .width('90%')
   16. }
   17. .width('100%')
   18. .height($r('app.float.size_48'))
   19. .onClick(() => {
   20. this.windowScaleSelect = index;
   21. switch (this.windowScaleSelect) {
   22. case ZERO:
   23. this.avPlayerController.videoScaleFit();
   24. break;
   25. case ONE:
   26. this.avPlayerController.videoScaleFitCrop();
   27. break;
   28. default:
   29. break;
   30. }
   31. this.controller.close();
   32. })
   33. })
   34. }
   ```

   [ScaleDialog.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/views/ScaleDialog.ets#L48-L101)
2. videoScaleFit()/videoScaleFitCrop()方法内设置视频播放器AVPlayer的[videoScaleType](../harmonyos-references/arkts-apis-media-e.md#videoscaletype9)属性值。VIDEO\_SCALE\_TYPE\_FIT表示拉伸至与窗口等大；VIDEO\_SCALE\_TYPE\_FIT\_CROP表示缩放至最短边填满窗口。

   ```
   1. /**
   2. * Set window scale mode
   3. */
   4. videoScaleFit(): void {
   5. if (this.avPlayer) {
   6. try {
   7. this.avPlayer.videoScaleType = media.VideoScaleType.VIDEO_SCALE_TYPE_FIT
   8. } catch (err) {
   9. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   10. `videoScaleType_0 failed, code is ${err.code}, message is ${err.message}`);
   11. }
   12. }
   13. }

   15. videoScaleFitCrop(): void {
   16. if (this.avPlayer) {
   17. try {
   18. this.avPlayer.videoScaleType = media.VideoScaleType.VIDEO_SCALE_TYPE_FIT_CROP
   19. } catch (err) {
   20. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   21. `videoScaleType_1 failed, code is ${err.code}, message is ${err.message}`);
   22. }
   23. }
   24. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L400-L424)

## 点击按钮选择倍速

### 场景描述

通过点击按钮选择预设倍速实现倍速设置，为用户提供灵活的视频播放速率控制。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/GgmIbrGfRqKKnI61F_U-uQ/zh-cn_image_0000002453067566.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=C71BDEB054AFA250F4B564E4667ADF40C58ACD2D3ADEF50095D6188D103E4B3D "点击放大")

### 实现原理

根据选择的倍速调用视频播放器AVPlayer的[setSpeed()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)设置对应值，实现视频播放倍速设置。

### 开发步骤

1. 可选择1.0X、1.25X、1.75X、2.0X，选择后调用对应的设置倍速方法。

   ```
   1. ForEach(this.speedList, (item: Resource, index) => {
   2. ListItem() {
   3. Column() {
   4. Row() {
   5. Text(item)
   6. // ...
   7. Blank()
   8. Image(this.speedSelect === index ? $r('app.media.ic_radio_selected') :
   9. $r('app.media.ic_radio'))
   10. // ...
   11. }
   12. // ...
   13. }
   14. .width('90%')
   15. }
   16. .width('100%')
   17. .height($r('app.float.size_48'))
   18. .onClick(() => {
   19. this.speedSelect = index;
   20. switch (this.speedSelect) {
   21. case ZERO:
   22. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
   23. break;
   24. case ONE:
   25. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_25_X);
   26. break;
   27. case TWO:
   28. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_75_X);
   29. break;
   30. case THREE:
   31. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
   32. break;
   33. default:
   34. break;
   35. }
   36. this.controller.close();
   37. })
   38. }, (item: Resource, index) => index + '_' + JSON.stringify(item))
   39. }
   ```

   [SpeedDialog.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/views/SpeedDialog.ets#L55-L113)
2. 设置倍速方法内调用视频播放器AVPlayer的[setSpeed()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)实现设置倍速。

   ```
   1. videoSpeed(speed: number): void {
   2. if (this.avPlayer) {
   3. try {
   4. this.avPlayer.setSpeed(speed);
   5. } catch (err) {
   6. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   7. `videoSpeed failed, code is ${err.code}, message is ${err.message}`);
   8. }
   9. }
   10. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L341-L351)

## 长按手势调节倍速

### 场景描述

通过长按手势实现长按屏幕时2倍速播放，长按结束时恢复1倍速播放。

### 实现原理

通过为元素绑定[长按手势](../harmonyos-references/ts-basic-gestures-longpressgesture.md)事件，在长按手势开始时调用视频播放器AVPlayer的[setSpeed()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)设置值为media.[PlaybackSpeed](../harmonyos-references/arkts-apis-media-e.md#playbackspeed8).SPEED\_FORWARD\_2\_00\_X，实现长按时2倍速播放；长按结束后调用视频播放器AVPlayer的setSpeed()方法设置值为media.PlaybackSpeed.SPEED\_FORWARD\_1\_00\_X，恢复播放速度为1倍速。

### 开发步骤

1. 为元素绑定[长按手势LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)事件，并调用封装的videoSpeed()方法，长按手势开始时传递参数为media.PlaybackSpeed.SPEED\_FORWARD\_2\_00\_X，设置播放速度为2倍速；长按手势结束时传递参数为media.PlaybackSpeed.SPEED\_FORWARD\_1\_00\_X，恢复播放速度为1倍速。

   ```
   1. .gesture(
   2. LongPressGesture({ repeat: true })
   3. .onAction(() => {
   4. this.speedSelect = CASE_THREE
   5. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
   6. })
   7. .onActionEnd(() => {
   8. this.speedSelect = CASE_ZERO
   9. this.avPlayerController.videoSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
   10. })
   11. )
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/pages/Index.ets#L331-L341)
2. 设置倍速方法内调用视频播放器AVPlayer的[setSpeed()方法](../harmonyos-references/arkts-apis-media-avplayer.md#setspeed9)实现设置倍速。

   ```
   1. videoSpeed(speed: number): void {
   2. if (this.avPlayer) {
   3. try {
   4. this.avPlayer.setSpeed(speed);
   5. } catch (err) {
   6. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   7. `videoSpeed failed, code is ${err.code}, message is ${err.message}`);
   8. }
   9. }
   10. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L341-L351)

## 音量设置

### 场景描述

滑动调节音量是一项非常实用的功能，它允许用户在不离开视频播放界面的情况下快速调整音量，以获得更好的观看体验。该功能位于窗口左侧，通过上下滑动手势即可调整音量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/IEhwWyAbTUCLY039HXbdpQ/zh-cn_image_0000002486107329.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=CF7C08250A86080AB099D74DBB690439E944D3DAE6C7DD68280F650E2811AC57 "点击放大")

### 实现原理

用[AVVolumePanel组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)显示系统音量面板，为元素绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，设置滑动方向为竖直方向，当手势在移动时，上滑增加音量，下滑减少音量，实现控制系统音量功能。

### 开发步骤

1. 添加[AVVolumePanel组件](../harmonyos-references/ohos-multimedia-avvolumepanel.md)显示系统音量面板。

   ```
   1. import { AVVolumePanel } from '@kit.AudioKit';

   3. @Component
   4. export struct SetVolume {
   5. @Prop volume: number = 5
   6. @Prop volumeVisible: boolean = false

   8. build() {
   9. Column() {
   10. AVVolumePanel({
   11. volumeLevel: this.volume,
   12. volumeParameter: {
   13. position: {
   14. x: 50,
   15. y: 1000
   16. }
   17. }
   18. })
   19. .width(10)
   20. }
   21. .visibility(this.volumeVisible ? Visibility.Visible : Visibility.Hidden)
   22. .height('50%')
   23. }
   24. }
   ```

   [SetVolume.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/views/SetVolume.ets#L17-L40)
2. 为元素绑定[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)滑动手势事件，并根据手势滑动距离计算音量值volume。

   ```
   1. .gesture(
   2. PanGesture({ direction: PanDirection.Vertical })
   3. .onActionStart(() => {
   4. })
   5. .onActionUpdate((event: GestureEvent) => {
   6. this.volumeVisible = true;
   7. let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.windowHeight;
   8. curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
   9. curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
   10. this.volume = curVolume;
   11. })
   12. .onActionEnd(() => {
   13. this.setVolumeTimer();
   14. })
   15. )
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/pages/Index.ets#L251-L265)

## 字幕挂载与切换

### 场景描述

在视频播放前，用户可设置外挂字幕文件，字幕将精准同步显示于视频画面下方，并可以通过按钮切换字幕语言，提升观看体验。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/jQ1PoR6NRvaI7kqxoLcTcA/zh-cn_image_0000002452907974.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061109Z&HW-CC-Expire=86400&HW-CC-Sign=FDF0D1033D4B35C08F987D50AB08A973526477D0B0404D3B0C530C9F033EF8EF "点击放大")

### 实现原理

通过AVPlayer视频播放器的[addSubtitleFromFd()](../harmonyos-references/arkts-apis-media-avplayer.md#addsubtitlefromfd12)方法加载外挂字幕，并使用[on('subtitleUpdate')](../harmonyos-references/arkts-apis-media-avplayer.md#onsubtitleupdate12)方法注册字幕回调函数。在回调函数中获取字幕文本，通过状态变量刷新[Text组件](../harmonyos-references/ts-basic-components-text.md)显示内容。使用Text组件显示字幕并设置字体格式。

切换字幕语言需依据所选语言加载相应的字幕资源，然后调用AVPlayer的[reset()方法](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)重置播放器并重新初始化。

### 开发步骤

1. 使用AVPlayer实例的[addSubtitleFromFd()](../harmonyos-references/arkts-apis-media-avplayer.md#addsubtitlefromfd12)方法为视频添加外挂字幕资源。

   ```
   1. if (this.curSource.caption) {
   2. let fileDescriptorSub = await this.context.resourceManager.getRawFd(this.curSource.caption);
   3. this.avPlayer.addSubtitleFromFd(fileDescriptorSub.fd, fileDescriptorSub.offset, fileDescriptorSub.length)
   4. .catch((err: BusinessError) => {
   5. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   6. `addSubtitleFromFd failed, code is ${err.code}, message is ${err.message}`);
   7. });
   8. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L109-L116)
2. 通过AVPlayer的[on('subtitleUpdate')](../harmonyos-references/arkts-apis-media-avplayer.md#onsubtitleupdate12)方法订阅获取外挂字幕事件，当有外挂字幕时，会通过订阅的回调方法通知用户。用户只能订阅一个外挂字幕事件的回调方法，若用户重复订阅，则以最后一次订阅的回调接口为准。回调中可以获取字幕文本、当前时间等信息，从而可以通过状态变量刷新Text组件显示的内容。

   ```
   1. this.avPlayer.on('subtitleUpdate', (info: media.SubtitleInfo) => {
   2. if (info) {
   3. let text = (!info.text) ? '' : info.text;
   4. this.currentCaption = text; //update current caption content
   5. } else {
   6. this.currentCaption = '';
   7. hilog.error(CommonConstants.LOG_DOMAIN, TAG, 'subtitleUpdate info is null');
   8. }
   9. });
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L430-L438)
3. 使用状态变量刷新[Text组件](../harmonyos-references/ts-basic-components-text.md)的内容，并通过修改Text属性调整字幕字体格式。

   ```
   1. Stack({ alignContent: Alignment.Center }) {
   2. Text(this.avPlayerController.currentCaption)
   3. .fontColor(Color.White)
   4. .fontSize($r('app.float.size_20'))
   5. .fontFamily('Sans')
   6. }
   7. .width('100%')
   8. .position({ x: $r('app.float.size_zero'), y: $r('app.float.size_216') })
   9. .zIndex(1)
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/pages/Index.ets#L236-L245)
4. 根据所选语言切换对应字幕资源，并调用AVPlayer的[reset()方法](../harmonyos-references/arkts-apis-media-avplayer.md#reset9-1)重置播放器并重新初始化。

   ```
   1. async languageChange(languageSelect: number = 0): Promise<void> {
   2. if (this.avPlayer) {
   3. try {
   4. if (this.curSource && this.curSource.caption) {
   5. this.curSource.caption = languageSelect === 0 ? 'captions.srt' : 'en_captions.srt'
   6. this.curSource.seekTime = this.avPlayer.currentTime;
   7. await this.avPlayer.reset();
   8. this.initAVPlayer(this.curSource, this.surfaceID, this.avPlayer);
   9. }
   10. } catch (err) {
   11. hilog.error(CommonConstants.LOG_DOMAIN, TAG,
   12. `languageChange failed, code is ${err.code}, message is ${err.message}`);
   13. }
   14. }
   15. }
   ```

   [AvPlayerController.ets](https://gitcode.com/HarmonyOS_Samples/avplayer-basic-control/blob/master/entry/src/main/ets/controller/AvPlayerController.ets#L448-L463)

## 示例代码

* [基于AVPlayer实现视频基础播控功能](https://gitcode.com/harmonyos_samples/avplayer-basic-control)
