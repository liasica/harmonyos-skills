---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-vdeocast
title: 视频投播
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 视频投播
category: best-practices
scraped_at: 2026-04-28T08:21:40+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:ad115a764317bba829c161bbf4e443a64e132030cebb73f8495918436e37f2e6
---

## 概述

系统投播功能让用户能够轻松将手机上的音视频投放到其他设备（如PC/2in1设备、华为智慧屏）上继续播放，实现跨设备切换，带来流畅的观影体验。为简化开发流程，系统提供了标准化的音视频投播解决方案，开发者仅需配置资源信息、监听投播状态并实现播放控制（如播放、暂停），即可快速集成该功能。

本文将结合实际案例，详细介绍如何高效利用系统投播组件和接口实现视频投播，帮助开发者提升开发效率，包含如下关键步骤：

* [接入播控中心](bpta-vdeocast.md#section198061041155312)：播控中心系统提供的播放管理模块，可以后台管理应用播放任务，是投播接入的必备条件。
* [本端控制远端设备状态](bpta-vdeocast.md#section1850441982916)：手机端实现遥控器功能，直接控制远端设备的播放状态、进度、音量等。
* [远端视频状态回传本端](bpta-vdeocast.md#section13876193232918)：能够实时同步播放进度至手机端显示。
* [视频资源切换](bpta-vdeocast.md#section1133113013013)和[设备切换](bpta-vdeocast.md#section6237193134112)：支持投播过程中集数的切换及投播设备的切换。

说明

**设备限制：**

详细版本、设备和使用限制见[约束与限制](../harmonyos-guides/distributed-playback-guide.md#约束与限制)。

## 用户体验

**体验视频**

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/23/v3/GACQ4K7HRie0N7KJnirDKg/zh-cn_media_0000002311894292.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=4D7ED4F98CE9717FEEA93E77EABE545CBA772EC9DECFBA3C7B5FC6CF9C86B02C)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 1.45%

0:00

Duration 1:00

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

**用户体验路径**

本文案例提供本端播放和视频投播两种播放模式，体验路径和交互流程图如下。用户可以在本端和远端播放视频，在投播模式下，用户可以通过遥控界面实现快进/快退、切换上下集、音量调节（支持物理键控制）、进度条拖动跳转、选集切换控制功能，应用接入时，可根据实际需求参考本文实现，并按照[应用接入播控自检表](../harmonyos-guides/playback-control-access-checklist.md)完成基础功能验证，确保应用基础体验。

| 用户操作阶段 | 1、本端视频播放与控制 | 2、播控中心控制本端视频 | 3、接入投播 | 4、应用遥控远端设备 |
| --- | --- | --- | --- | --- |
| 预期行为 | 1、本端视频的正常播放。  2、本端视频的控制（切集、倍速、音量、进度等）。 | 1、播控中心状态与本端视频一致。  2、播放中心控制本端视频播放（切集、倍速、音量、进度等）。 | 1、初次链接认证。  2、选择设备。 | 1、本端状态与远端状态一致。  2、本端播控中心遥控远端设备播放（切集、倍速、音量、进度等）。  3、应用遥控远端设备播放（切集、倍速、音量、进度等）。 |
|  |  |  |  |  |

## 实现原理

**名词解释**

| 概念 | 解释 |
| --- | --- |
| **媒体会话（[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)）** | 音视频管控服务，用于对系统中所有音视频行为进行统一的管理。 |
| **投播组件（[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)****）** | 系统级的投播组件，可嵌入应用界面的UI组件。当用户点击该组件后，系统将进行设备发现、连接、认证等流程，应用仅需要通过接口获取投播中相关的回调信息。 |
| **投播控制器（[AVCastController](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)****）** | 在投播后，由应用发起的用于控制远端播放的接口，包括播放、暂停、调节音量、设置播放模式、设置播放速度等能力。 |

投播功能通过AVSession建立设备连接，由AVCastController控制远端播放。详见[运作机制](../harmonyos-guides/distributed-playback-overview.md#运作机制)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/pQpD25_BSXyWHkAeW964vw/zh-cn_image_0000002345973089.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=13E733A85A8F9436F40CF137B09761739B00119DD1B3BA25DF85A8091EB9ABEB "点击放大")

## 模块设计

建议应用封装三个模块：

* VideoPlayerController：应用封装的本地视频控制器，控制本端视频资源的暂停、播放、进度、音量、倍速。
* VideoSessionController：应用封装的媒体会话控制器，本端视频播放时用于本应用与播控中心的同步、切换设备发起投播、结束投播。
* VideoCastController：应用封装的投播视频控制器，控制远端设备视频资源的暂停、播放、进度、音量、倍速。

完成投播功能，建议参考如下流程接入，其中本端视频显示和控制可参考[视频播放组件](../harmonyos-guides/arkts-common-components-video-player.md)、[使用AVPlayer播放视频(ArkTS)](../harmonyos-guides/video-playback.md)、[使用AVPlayer播放视频(C/C++)](../harmonyos-guides/using-ndk-avplayer-for-video-playback.md)等视频实现方案根据功能诉求自行实现，本文从接入播控中心进行介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/o-S9NT9aSPGZ69PJTldS-w/zh-cn_image_0000002345853277.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=3298C8AD1E4E734CB70AE954A67E7B05B1E57B5B052702D6ECDDAB8FB88AC45A "点击放大")

## 接入播控中心

投播功能依赖于播控中心，因此必须接入播控中心才能实现投播功能。播控中心不仅能够控制本端设备的播放，还能控制远端设备的播放。本章节将简要介绍应用接入播控中心的开发流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/cuOiCQFNQ0e9n2BKoT4bzQ/zh-cn_image_0000002346524017.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=32984D0E2429C7DA2977D35D3771DD97CCAC240589E4A5AA98C8003F535CA7E5 "点击放大")

### 媒体会话初始化

1. [avSession.createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建avsession，类型为video。
2. 设置后台长时播放任务，确保应用退至后台后播放不会停止。
3. [videoSession.setLaunchAbility()](../harmonyos-references/arkts-apis-avsession-avsession.md#setlaunchability10)设置一个WantAgent用于拉起会话的Ability。
4. [videoSession.activate()](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)激活videoSession。

```
1. let videoSession = await avSession.createAVSession(context, 'VIDEO_SESSION', 'video');
2. // Set up a background task.
3. BackgroundTaskManager.startContinuousTask(context);
4. const wantAgentInfo: wantAgent.WantAgentInfo = {
5. wants: [
6. {
7. bundleName: context.abilityInfo.bundleName,
8. abilityName: context.abilityInfo.name
9. }
10. ],
11. operationType: wantAgent.OperationType.START_ABILITIES,
12. requestCode: 0,
13. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
14. };
15. let agent = wantAgent.getWantAgent(wantAgentInfo);
16. videoSession.setLaunchAbility(agent);
17. videoSession.activate();
18. return new VideoSessionController(videoSession);
```

[VideoSessionController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoSessionController.ets#L39-L56)

### 设置媒体会话元数据

[videoSession.setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)上传元数据，从而在播控中心界面进行展示。如媒体ID（assetId）、标题（title）、播控中心显示的图片（mediaImage）、媒体时长（duration）。

```
1. let metadata: avSession.AVMetadata = {
2. assetId: `${curSource.index}`,
3. title: curSource.name,
4. mediaImage: headPixel,
5. duration: duration,
6. filter: avSession.ProtocolType.TYPE_DLNA | avSession.ProtocolType.TYPE_CAST_PLUS_STREAM
7. };
8. await this.videoSession.setAVMetadata(metadata);
```

[VideoSessionController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoSessionController.ets#L68-L75)

### 本应用播放状态同步到播控中心

当设置元数据后，播控中心会显示进度条并自动计算播放进度，但播放状态变更（如暂停、播放、进度跳转）、音量调节和倍速设置等操作不会自动同步到播控中心。开发者需要主动监听本地的播放状态变化（包括进度跳转、倍速调整、音量修改等事件），并主动将这些状态同步到播控中心，以确保两端状态一致。

以下是videoSession状态更新的示例代码，特别注意的是，在更新进度状态时，需要传入当前时间戳updateTime和视频播放的时间进度elapsedTime。

```
1. await this.videoSession.setAVPlaybackState({
2. state: state === 'playing' ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
3. avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
4. });
```

[VideoSessionController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoSessionController.ets#L103-L106)

### 播控中心控制应用播放

当用户在播控中心进行操作（如播放、暂停、停止、进度跳转、快进、快退等）时，这些操作不会自动同步到应用端，开发者需要主动通过avCastController.on('controlCommand')监听这些事件，并在回调函数中主动更新应用播放器的状态以保持同步，例如在收到播放指令时调用本地播放器的play()方法，在收到跳转指令时调整播放进度等，确保播控中心与应用端的操作状态完全一致。

```
1. this.videoSession.on('play', () => avPlayerController.setAVPlayerPlaying());
2. this.videoSession.on('pause', () => avPlayerController.setAVPlayerPause());
```

[VideoSessionController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoSessionController.ets#L144-L145)

说明

这里注册的交互监听所有on()事件建议在退出播放页时通过videoSession.off()事件销毁。

## 投播基础功能

为确保投播功能正常使用，应用在发起投播前需要完成播控中心[初始化](bpta-vdeocast.md#section15774202314195)。如未完成此关键步骤，则导致投播功能不可用。

### 创建投播

在完成创建投播后，远端设备即可正常播放视频，本端会停止播放并页面跳转。

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/30/v3/UGQQMvulTzu1k_UOGpThfw/zh-cn_media_0000002311894304.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=E93EF8AE55C7F353EF73A69E94BB0C96372F5EB5946CA9EEFEC934124D6DD5CA)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 4.31%

0:00

Duration 0:13

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

创建投播时需要setExtras()告知系统可投播、绘制AVCastPicker、videosession监听设备改变事件，用户点击AVCastPicker组件后会弹出设备选择半模态，在选择设备后，应用需要设置投播媒体信息，调用prepare、start启动播放。时序图如下，具体实现见开发步骤：

**时序图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/OD2ljnbBRoiyvITFSM4ufw/zh-cn_image_0000002345973101.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=CA9A228E06E78BBC2C01306313A332ABF7CB87379E71EDA15B9F5E46093DE5F1 "点击放大")

**开发步骤**

1. videosession创建后，创建投播前，声明当前应用支持投播。

   ```
   1. await videoSession.setExtras({
   2. 'requireAbilityList': ['url-cast']
   3. })
   ```

   [VideoPlayingView.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/view/VideoPlayingView.ets#L150-L152)
2. 绘制AVCastPicker，AVCastPicker是投播组件，点击后系统会弹出设备选择半模态。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ZAHftCfXQyulHT8kyuozKQ/zh-cn_image_0000002473018785.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=D5569CB7CB8C463B631442858380463E9A3AE0E71BC059DDC8017E1030E04FC7 "点击放大")

   ```
   1. AVCastPicker({
   2. normalColor: Color.White,
   3. pickerStyle: AVCastPickerStyle.STYLE_PANEL,
   4. sessionType: 'video',
   5. // ...
   6. })
   ```

   [VideoPlayingView.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/view/VideoPlayingView.ets#L282-L298)
3. 当用户选择设备并设备切换成功后触发[videoSession.on('outputDeviceChange')](../harmonyos-references/arkts-apis-avsession-avsession.md#onoutputdevicechange10)事件，应用可选择停止本地播放并跳转到遥控页面（或保持本端继续播放），此时播控中心会自动接管远端设备的播放控制，开发者无需额外设置。

   ```
   1. videoSession.on('outputDeviceChange', async (connectState: avSession.ConnectionState,
   2. device: avSession.OutputDeviceInfo) => {
   3. hilog.info(0x0000, TAG, `device ${JSON.stringify(device)}`);
   4. hilog.info(0x0000, TAG, `connectState ${JSON.stringify(connectState)}`);
   5. // The linked device is a remote device.
   6. if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_REMOTE &&
   7. connectState === avSession.ConnectionState.STATE_CONNECTED) {
   8. // Page jump
   9. this.remoteControlPathStack.replacePath({ name: 'detail', param: this.currentTime });
   10. this.castingList.push(this.videoType);
   11. await this.releaseAVPlayer();
   12. // The linked device is the local device.
   13. } else if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_REMOTE &&
   14. connectState === avSession.ConnectionState.STATE_DISCONNECTED) {
   15. if (this.avCastController) {
   16. await this.avCastController.releaseAVCast();
   17. await this.avSessionController!.stopCasting();
   18. this.avCastController = undefined;
   19. }
   20. }
   21. else if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_LOCAL) {
   22. this.remoteControlPathStack.clear();
   23. let videoType = this.castingList[0];
   24. this.castingList = [];
   25. let videoPlayParam = new VideoPlayParam(videoType, 0, this.avplayerContinueIndex);
   26. this.videoPlayPathStack.replacePath({ name: 'detail', param: videoPlayParam });
   27. if (this.avCastController) {
   28. await this.avCastController.releaseAVCast();
   29. await this.avSessionController!.stopCasting();
   30. this.avCastController = undefined;
   31. }
   32. }
   33. })
   ```

   [VideoPlayingView.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/view/VideoPlayingView.ets#L156-L191)
4. 设置avCastController资源，完成以下三步后远端设备即可投播视频，以播放网络资源为例。
   1. 构建[avSession.AVQueueItem](../harmonyos-references/arkts-apis-avsession-i.md#avqueueitem10)。需要传入assetId（播放列表媒体ID，应用自定义）、title（媒体标题）、artist（媒体专辑作者）、mediaUri（媒体URI）、mediaType（媒体类型）、mediaImage（媒体图片像素数据）、duration（媒体播放时长）。
   2. [avCastController.prepare(playItem)](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#prepare10-1)准备播放媒体资源，即进行播放资源的加载和缓冲。
   3. [avCastController.start(playItem)](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#start10-1)启动播放媒体资源。

      ```
      1. let playItem: avSession.AVQueueItem = {
      2. itemId: videoIndex,
      3. description: {
      4. assetId: 'VIDEO-' + JSON.stringify(videoIndex),
      5. title: this.videoDataArray[videoIndex].name,
      6. subtitle: 'video',
      7. mediaUri: this.videoDataArray[videoIndex].url as string,
      8. mediaType: 'VIDEO',
      9. mediaImage: imgPixel,
      10. startPosition: startPosition,
      11. duration: this.videoDataArray[videoIndex].duration
      12. }
      13. };
      14. await this.avCastController.prepare(playItem);
      15. await this.avCastController.start(playItem);
      ```

      [VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L56-L70)

   若需要投播本地资源，需要打开沙箱文件，并在fdSrc中传入文件fd实现。

   ```
   1. let file = await fileIo.open(context.filesDir + '/' + this.videoDataArray[videoIndex].url);
   2. let avFileDescriptor: media.AVFileDescriptor = { fd: file.fd };
   3. let playItem: avSession.AVQueueItem = {
   4. itemId: videoIndex,
   5. description: {
   6. assetId: 'VIDEO-' + JSON.stringify(videoIndex),
   7. title: this.videoDataArray[videoIndex].name,
   8. subtitle: 'video',
   9. mediaType: 'VIDEO',
   10. mediaImage: imgPixel,
   11. fdSrc: avFileDescriptor,
   12. startPosition: startPosition,
   13. duration: this.videoDataArray[videoIndex].duration
   14. }
   15. };
   16. await this.avCastController.prepare(playItem);
   17. await this.avCastController.start(playItem);
   ```

   [VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L76-L92)

### 设备切换

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/1c/v3/q4KviacyR3CYd-ej6F8Bfg/zh-cn_media_0000002312054100.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=114338E70B83E97655A67672FC430D77A5DC3C09152B15802D2017025E0EB1FE)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 7.83%

0:00

Duration 0:09

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

设备切换依赖于videosession监听设备改变事件，可以通过stopCasting终止投播切换设备，也可以通过[avCastPicker.select()](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14)进行切换。均会触发[videoSession.on('outputDeviceChange')](../harmonyos-references/arkts-apis-avsession-avsession.md#onoutputdevicechange10)事件，当切换到远端设备播放，本端应该跳转到遥控器界面，当切换回本端设备播放，应当停止投播并跳转到视频播放页面。应用时序图如下，具体实现见开发步骤。

**时序图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/BxaxvLSbSfKSqxcgobtUuA/zh-cn_image_0000002311894312.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=95A5AAEA1618ECD49972A2CB13499FA94B31FD916B8008F84DAE6C8757940860 "点击放大")

**开发步骤**

可以直接使用AVCastPicker切换设备，系统会自动弹出设备选择半模态弹窗，用户可直接选择目标设备完成切换。开发者无需额外处理弹窗逻辑。也可以使用[avCastPicker.select()](../harmonyos-references/arkts-apis-avsession-avcastpickerhelper.md#select14) 接口切换设备。

当设备切换时，[videoSession.on('outputDeviceChange')](../harmonyos-references/arkts-apis-avsession-avsessioncontroller.md#onoutputdevicechange10)事件将被触发，开发者可在回调中处理设备切换逻辑：若切换至远端设备则跳转至遥控页面，若切回本端设备则恢复本地播放，实现播放控制的无缝切换。

```
1. videoSession.on('outputDeviceChange', async (connectState: avSession.ConnectionState,
2. device: avSession.OutputDeviceInfo) => {
3. hilog.info(0x0000, TAG, `device ${JSON.stringify(device)}`);
4. hilog.info(0x0000, TAG, `connectState ${JSON.stringify(connectState)}`);
5. // The linked device is a remote device.
6. if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_REMOTE &&
7. connectState === avSession.ConnectionState.STATE_CONNECTED) {
8. // Page jump
9. this.remoteControlPathStack.replacePath({ name: 'detail', param: this.currentTime });
10. this.castingList.push(this.videoType);
11. await this.releaseAVPlayer();
12. // The linked device is the local device.
13. } else if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_REMOTE &&
14. connectState === avSession.ConnectionState.STATE_DISCONNECTED) {
15. if (this.avCastController) {
16. await this.avCastController.releaseAVCast();
17. await this.avSessionController!.stopCasting();
18. this.avCastController = undefined;
19. }
20. }
21. else if (device.devices[0].castCategory === avSession.AVCastCategory.CATEGORY_LOCAL) {
22. this.remoteControlPathStack.clear();
23. let videoType = this.castingList[0];
24. this.castingList = [];
25. let videoPlayParam = new VideoPlayParam(videoType, 0, this.avplayerContinueIndex);
26. this.videoPlayPathStack.replacePath({ name: 'detail', param: videoPlayParam });
27. if (this.avCastController) {
28. await this.avCastController.releaseAVCast();
29. await this.avSessionController!.stopCasting();
30. this.avCastController = undefined;
31. }
32. }
33. })
```

[VideoPlayingView.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/view/VideoPlayingView.ets#L156-L191)

### 远端视频状态回传本端

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/62/v3/yblcHlK4QGuJfE4pqLH9Dg/zh-cn_media_0000002345973105.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=C4F01ED2F8B42A571AE0930C9C84F512584EE2FF62C3736DDAA4DBFA36229CDF)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 9.97%

0:00

Duration 0:09

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

当视频在远端设备播放时，为了控制远端视频的播放应用需要监听远端视频播放状态并同步显示本端，通过远端设备或本端播控中心控制，都会直接改变远端设备的播放状态，并触发[avCastController.on('playbackStateChange')](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaybackstatechange10)。应用时序图如下，具体实现见开发步骤。

**时序图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/KVRI0xt2QbCGu23kDzHPVA/zh-cn_image_0000002345853289.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=81209B84FE65E9E95BE12A6B0FBE7337F1306581D9E4E04C66ED7111F16FDF39 "点击放大")

**开发步骤**

当需要在本地遥控界面同步显示远端视频的播放状态时，可通过[avCastController.on('playbackStateChange')](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaybackstatechange10) 监听状态变化，并使用过滤器筛选目标状态。

建议使用@Track修饰器标记这些经常改变的状态变量，以便页面自动响应数据更新。该机制可统一获取播放状态（如播放/暂停）、音量、总时长及倍速等信息，以下代码以获取已播放时长为例：

```
1. @Observed
2. export class VideoCastController {
3. @Track state: avSession.PlaybackState = avSession.PlaybackState.PLAYBACK_STATE_INITIAL;
4. // ...
5. /**
6. * Sets up AV cast playback state change callbacks.
7. * Handles playback completion, position updates, volume changes and errors.
8. */
9. setAVCastCallback() {
10. this.avCastController.on('playbackStateChange', ['state'], async (playbackState: avSession.AVPlaybackState) => {
11. if (playbackState.state) {
12. this.state = playbackState.state;
13. }
14. });
15. // ...
16. }

18. // ...
19. }
```

[VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L29-L232)

### 本端控制远端设备状态

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/c2/v3/xOifsBxDR2SN9BW-erySOA/zh-cn_media_0000002312054104.mp4?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=AA15DF45ED6CDAACCF5BAC2522A0D283112AE3870BD5EC04EE1E79FD2B1BF4F6)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 12.52%

0:00

Duration 0:07

Mute

1x

Playback Rate

* 2x
* 1.8x
* 1.5x
* 1.2x
* 1x, selected

Fullscreen

This is a modal window.

Beginning of dialog window. Escape will cancel and close the window.

TextColorWhiteBlackRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentText BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityOpaqueSemi-TransparentTransparentCaption Area BackgroundColorBlackWhiteRedGreenBlueYellowMagentaCyanOpacityTransparentSemi-TransparentOpaque

Font Size50%75%100%125%150%175%200%300%400%Text Edge StyleNoneRaisedDepressedUniformDrop shadowFont FamilyProportional Sans-SerifMonospace Sans-SerifProportional SerifMonospace SerifCasualScriptSmall Caps

Reset restore all settings to the default valuesDone

Close Modal Dialog

End of dialog window.

**时序图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/FqtwPS5EQNi9s-Nx0IlgbQ/zh-cn_image_0000002311894316.png?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=14DF229F5E400ED08B5A823555C3F75555042D7FE0AB66F858FE4509D4BC7D0F "点击放大")

**开发步骤**

控制远端设备状态可通过[avCastController.sendControlCommand()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#sendcontrolcommand10)接口实现，支持多种播放控制命令，包括：暂停、停止、下一首、上一首、快进、快退、跳转、音量调节和倍速设置。只需修改command字段即可切换不同功能，具体命令与功能的对应关系请参考[AVCastControlCommandType](../harmonyos-references/arkts-apis-avsession-t.md#avcontrolcommandtype10)。

```
1. public async setAVCastPlay() {
2. let avCommand: avSession.AVCastControlCommand = { command: 'play' };
3. await this.avCastController.sendControlCommand(avCommand);
4. }
```

[VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L175-L178)

在控制跳转、音量调节和倍速设置时，需要传入时间（单位ms）、音量、倍速参数。

```
1. public async setAVCastSeek(timeMS: number) {
2. let avCommand: avSession.AVCastControlCommand = { command: 'seek', parameter: timeMS };
3. await this.avCastController.sendControlCommand(avCommand);
4. }

6. public async setAVCastVolume(volume: number) {
7. let avCommand: avSession.AVCastControlCommand = { command: 'setVolume', parameter: volume };
8. await this.avCastController.sendControlCommand(avCommand);
9. }

11. public async setAVCastSpeed(speed: media.PlaybackSpeed) {
12. let avCommand: avSession.AVCastControlCommand = { command: 'setSpeed', parameter: speed };
13. await this.avCastController.sendControlCommand(avCommand);
14. }
```

[VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L205-L218)

### 资源切换

在完成本集播放/用户触发集数切换时不需要断开连接，重新设置资源即可。

1. 构建[avSession.AVQueueItem](../harmonyos-references/arkts-apis-avsession-i.md#avqueueitem10)。
2. [avCastController.prepare(playItem)](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#prepare10-1)。
3. [avCastController.start(playItem)](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#start10-1)。

   ```
   1. let playItem: avSession.AVQueueItem = {
   2. itemId: videoIndex,
   3. description: {
   4. assetId: 'VIDEO-' + JSON.stringify(videoIndex),
   5. title: this.videoDataArray[videoIndex].name,
   6. subtitle: 'video',
   7. mediaUri: this.videoDataArray[videoIndex].url as string,
   8. mediaType: 'VIDEO',
   9. mediaImage: imgPixel,
   10. startPosition: startPosition,
   11. duration: this.videoDataArray[videoIndex].duration
   12. }
   13. };
   14. await this.avCastController.prepare(playItem);
   15. await this.avCastController.start(playItem);
   ```

   [VideoCastController.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/controller/VideoCastController.ets#L56-L70)

## 扩展功能

### 悬浮球快捷控制

建议应用集成悬浮球快捷控制功能，便于用户快速返回投播页面进行操作控制，实现效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/iT05TjVQQAqKMraZG_n1mg/zh-cn_image_0000002346644421.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002136Z&HW-CC-Expire=86400&HW-CC-Sign=3621A010E016CF594C30EC9014D6D8ED1D77CEF151C0105BBB5417EC059C5EDE)

可以通过为页面设置浮层实现。

```
1. .overlay(this.OverlayNode(), {
2. align: Alignment.BottomEnd,
3. offset: { x: -24,
4. y: -136 }
5. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/pages/Index.ets#L256-L260)

```
1. @Builder
2. OverlayNode() {
3. // ...
4. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/pages/Index.ets#L52-L139)

### 手机物理音量键同步远端

音量同步需要通过遥控器页面的焦点管理和按键监听实现，具体流程为：当遥控器页面获焦时，监听音量加减按键事件，在事件回调中调用音量调节函数并同步更新播控中心状态。典型实现示例如下：

```
1. let upOptions: inputConsumer.KeyPressedConfig = {
2. key: KeyCode.KEYCODE_VOLUME_UP,
3. action: 1,
4. isRepeat: true,
5. }
6. inputConsumer.on('keyPressed', upOptions, async () => {
7. if (this.avCastPlayerController) {
8. console.log('currentVolume' + JSON.stringify(this.currentVolume));
9. let volume = this.currentVolume + 10;
10. await this.avCastPlayerController.setAVCastVolume(volume);
11. }
12. })
13. let downOptions: inputConsumer.KeyPressedConfig = {
14. key: KeyCode.KEYCODE_VOLUME_DOWN,
15. action: 1,
16. isRepeat: true,
17. }
18. inputConsumer.on('keyPressed', downOptions, async () => {
19. if (this.avCastPlayerController) {
20. let volume = this.currentVolume - 10;
21. if (volume < 0) {
22. await this.avCastPlayerController.setAVCastVolume(0);
23. }
24. await this.avCastPlayerController.setAVCastVolume(volume);
25. }
26. })
```

[RemoteControlPage.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/pages/RemoteControlPage.ets#L75-L100)

### 投屏转投播

用户通过“无线投屏”功能实现手机等设备和大屏等的镜像投屏，然后打开视频应用进入视频播放，此时会自动切换为资源投播，详见[镜像投屏自动切换资源投播](../harmonyos-guides/distributed-playback-guide.md#镜像投屏自动切换资源投播)。目前投播暂不支持视频弹幕功能，若应用想优先保证弹幕体验，可不接入此功能。

## 常见问题

### 播控中心、本端应用、远端投播三端进度不一致

**问题现象**

在投播时，应用在本端、远端、播控中心均有进度条显示，三个进度条进度显示不一致。

**解决措施**

1、远端和播控中心进度自动保持一致，应用无需进行设置。

2、本端应通过监听远端设备的进度条进行更新同步，在控制时调用avCastController.sendControlCommand(avCommand)改变播放状态、进度，不主动改变本端显示的状态。

**参考链接**

[远端视频状态回传本端](bpta-vdeocast.md#section13876193232918)

### 投播时AVcastPicker无法搜索到设备

**问题现象**

使用AVCastPicker投播时，无法搜索到目标设备。

**解决措施**

1. 确认远端设备状态，锁屏、息屏时无法搜索到设备。
2. AVSession接入。
3. 应用是否设置媒体信息。
4. AVCastPicker显示期间AVSession没有销毁重建。
5. AVSession接入后告知当前应用支持投播。

   ```
   1. await videoSession.setExtras({
   2. 'requireAbilityList': ['url-cast']
   3. })
   ```

   [VideoPlayingView.ets](https://gitcode.com/HarmonyOS_Samples/VideoCast/blob/master/entry/src/main/ets/view/VideoPlayingView.ets#L150-L152)
6. 确认filter是否过滤掉设备。

### 投播后远端黑屏

**问题现象**

投播后远端黑屏，无法播放视频。

**解决措施**

1、是否正确配置元数据。

2、调用prepare()和start()。

### 投播后，播控中心按钮置灰

**问题现象**

投播后，播控中心按钮灰色无法点击调控。

**解决措施**

播放、暂停、音量变化：监听AVCastController.on('playbackStateChange')。

上一集：监听AVCastController.on('playPrevious')。

下一集：监听AVCastController.on('playNext')。

快进、快退、进度条：监听AVCastController.on('seekDone')。

### AVCastPicker无法直接切换资源

**问题现象**

A视频投播成功后，在B视频播放的页面点击AVCastPicker切集，调起的半模态只可以切换A视频的播放设备。

**解决措施**

在本应用正在投播时，应用可自绘制AVCastPicker按钮，在点击事件中调用[资源切换](bpta-vdeocast.md#section1133113013013)函数实现。

## 示例代码

* [实现视频投播功能](https://gitcode.com/harmonyos_samples/VideoCast)
