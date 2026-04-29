---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-cast
title: 音频投播
breadcrumb: 最佳实践 > 自由流转 > 多端协同 > 音频投播
category: best-practices
scraped_at: 2026-04-29T14:12:44+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:682c81b512a95d05659c9ab851fb2a5a711d3b8ae0ffb4caae56038d18637dc6
---

## 概述

系统投播功能支持用户将手机上的音视频无缝流转到其他设备（如PC/2in1设备、华为智慧屏）上继续播放，实现跨终端自由切换，无需受到有线设备的束缚。为简化开发流程，系统提供了标准化的音视频投播解决方案，开发者仅需配置资源信息、监听投播状态并实现播放控制（如播放、暂停等），即可快速集成该功能。

本文将结合实际案例，详细介绍如何高效利用系统投播组件和接口实现音频投播，帮助开发者提升开发效率，包含如下关键步骤：

* [接入播控中心](bpta-audio-cast.md#section157951042142811)：播控中心提供音视频统一管控能力和音频后台约束能力，是投播接入的必备条件。
* [创建投播](bpta-audio-cast.md#section148446619451)：通过调用投播组件的设备选择接口，并注册媒体会话的设备改变事件监听，可以将手机端音视频无缝迁移到指定远端设备上继续播放。
* [本端控制远端音频播放](bpta-audio-cast.md#section23051450141317)：通过手机端可以直接控制远端设备的音频播放状态，包括播放、暂停和播放进度等。
* [远端音频状态回传本端](bpta-audio-cast.md#section178775217533)：将远端设备的播放状态实时同步到手机端显示，包括播放、暂停和播放进度等。
* [资源切换](bpta-audio-cast.md#section153951118172510)和[投播音质切换](bpta-audio-cast.md#section10877141421614)：支持投播过程中不同音频的切换及不同音质的切换。

说明

支持投播的设备规格和使用限制参见[约束与限制](../harmonyos-guides/distributed-playback-guide.md#约束与限制)。

## 用户体验

**体验视频**

**图1** 音频投播流程体验视频

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/b9/v3/gvmGdOPJTZqrt5sSFklhuw/zh-cn_media_0000002421894784.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=7095DAD584D7E712C32550767F152F4E0564CAD1B67F1288BC01E6D64EAEC5E6)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 4.50%

0:00

Duration 0:31

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

本文案例提供本端播放和音频投播两种播放模式，体验路径和交互流程图如下。在投播模式下，可以通过本端的播放界面或播控中心对远端的音频进行播放控制，如播放、暂停、播放进度跳转、上一首/下一首切换和点击切换音频。应用接入音频投播时，可根据实际需求参考本文实现相关功能，并按照[应用接入播控自检表](../harmonyos-guides/playback-control-access-checklist.md)完成基础功能验证，确保应用基础体验。

**表1** 音频投播体验路径和交互流程

| 用户操作阶段 | 本端音频播放与控制 | 播控中心控制本端音频 | 接入音频投播 | 本端控制远端音频播放 |
| --- | --- | --- | --- | --- |
| 预期行为 | 1. 本端音频正常播放 2. 通过播放页面控制本端音频播放 | 1. 播控中心与本端音频播放状态一致 2. 通过播控中心控制本端音频播放 | 1. 初次连接认证 2. 选择投播设备 | 1. 本端与远端播放状态一致 2. 通过播放页面控制远端音频播放 3. 通过播控中心控制远端音频播放 |
| 操作示意图 | **图2** | **图3** | **图4** | **图5** |

## 实现原理

**名词解释**

**表2** 音视频投播相关名词解释

| 概念 | 解释 |
| --- | --- |
| **媒体会话（[AVSession](../harmonyos-references/arkts-apis-avsession-avsession.md)）** | 音视频管控服务，用于统一管理系统中接入播控中心的音视频行为。 |
| **投播组件（[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md)）** | 可嵌入应用UI界面的系统级投播组件。用户点击该组件后，系统将执行设备发现、连接和认证等流程，应用仅需通过接口获取投播中的相关回调信息。 |
| **投播控制器（[AVCastController](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md)）** | 在投播建立后，由应用发起的用于控制远端播放的接口，包括播放、暂停、上一首/下一首切换和播放进度跳转等能力。 |

投播功能的实现基于AVSession媒体会话和AVCastController投播控制器的协同工作，系统通过AVSession建立设备连接，由AVCastController向Cast+服务发送控制指令。开发者需要聚焦两个核心环节——通过AVSession实现监听设备连接，以及使用AVCastController控制远端播放并同步状态，详见[运作机制](../harmonyos-guides/distributed-playback-overview.md#运作机制)。

**图6** 音视频投播运作机制示意图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/dvKpX43-S_-02cEqHQi7ig/zh-cn_image_0000002422054660.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=5D54F4FC612E9E89048415F550FEFD0429D4B8CC29F050E83C1E1EB96B5CEC36 "点击放大")

## 模块设计

建议应用实现音频投播时，封装如下三个模块：

* 本端音频控制器：控制本端音频资源的播放、暂停、上一首/下一首切换和播放进度等。
* 媒体会话控制器：将本端播放的音频接入播控中心，用于本应用发起投播、结束投播、与播控中心的播放状态同步。
* 音频投播控制器：控制远端设备音频资源的播放、暂停、上一首/下一首切换和播放进度等。

实现音频投播功能，建议参考如下流程接入，其中本端音频的播放和控制可参考[使用AVPlayer播放音频](../harmonyos-guides/using-avplayer-for-playback.md)、[音频播放交互场景](bpta-audio-interaction-practice.md)、[使用AudioRenderer开发音频播放功能](../harmonyos-guides/using-audiorenderer-for-playback.md)等方案根据功能诉求自行实现，本文将从接入播控中心开始进行详细介绍。

**图7** 接入音频投播流程图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/mPkL_mTgSVuyDdflk304Fw/zh-cn_image_0000002455573521.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=8F5CC50D5346CB450F7ED4BD323FB1DE2027F7296C394E5AE2727E0E83682333 "点击放大")

## 接入播控中心

[音视频播控服务](../harmonyos-guides/avsession-overview.md)用于统一管理系统中所有音视频行为，开发者须接入播控中心才能实现投播功能。播控中心不仅能控制本端设备的播放，还能控制远端设备的播放。

**图8** 播控中心控制音频播放   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/PcZrGXy_T2-J_2f8U3kyzw/zh-cn_image_0000002455453641.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=6BEC4967BD260C79D746D8D52050E2CD59F2530568B5E9322550E4AB1802DF6A "点击放大")

本应用与系统播控中心通过媒体会话AVSession进行信息交互。创建并初始化媒体会话实例后，应用需要通过[setAVMetaData()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)接口设置会话元数据，同时使用[setAVPlaybackState()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavplaybackstate10)接口主动向播控中心同步当前播放状态，并通过on('controlCommand')注册事件监听实时响应播控中心的音频操作事件，最终实现本应用与播控中心的双向状态同步，确保两端数据的一致性。下面为应用接入播控中心的简要开发流程。

### 媒体会话初始化

1. 通过[avSession.createAVSession()](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建会话类型为'audio'（音频）的会话实例AVSession。

   ```
   1. this.AVSession = await avSession.createAVSession(this.context, "PLAY_AUDIO", 'audio');
   ```

   [AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L61-L61)
2. 通过[AVSession.setLaunchAbility()](../harmonyos-references/arkts-apis-avsession-avsession.md#setlaunchability10)设置一个WantAgent用于拉起会话的Ability。

   ```
   1. let wantAgentInfo: wantAgent.WantAgentInfo = {
   2. wants: [
   3. {
   4. bundleName: this.context.abilityInfo.bundleName,
   5. abilityName: this.context.abilityInfo.name
   6. }
   7. ],
   8. actionType: wantAgent.OperationType.START_ABILITIES,
   9. requestCode: 0,
   10. wantAgentFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
   11. };
   12. wantAgent.getWantAgent(wantAgentInfo).then((agent) => {
   13. if (this.AVSession) {
   14. this.AVSession.setLaunchAbility(agent);
   15. }
   16. }).catch(() => {
   17. hilog.error(0x0000, TAG, `getWantAgent failed.`);
   18. });
   ```

   [AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L83-L100)
3. 通过[AVSession.activate()](../harmonyos-references/arkts-apis-avsession-avsession.md#activate10)激活音频会话AVSession。

   ```
   1. await this.AVSession.activate();
   ```

   [AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L65-L65)

### 设置媒体会话元数据

通过[AVSession.setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)上传元数据，从而在播控中心展示音频相关信息，如媒体ID（assetId）、媒体标题（title）、媒体图片（mediaImage）、媒体时长（duration）等。

```
1. let metadata: avSession.AVMetadata;
2. // ...
3. metadata = {
4. assetId: 'AUDIO-' + JSON.stringify(this.musicIndex),
5. title: this.songList[this.musicIndex].title,
6. artist: this.songList[this.musicIndex].singer,
7. filter: avSession.ProtocolType.TYPE_DLNA | avSession.ProtocolType.TYPE_CAST_PLUS_STREAM,
8. mediaImage: mediaImage,
9. duration: this.getDuration(),
10. };
11. // ...
12. if (this.AVSession) {
13. await this.AVSession.setAVMetadata(metadata);
14. }
```

[AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L124-L150)

### 本应用播放状态同步到播控中心

设置元数据后，开发者需要主动监听本地音频播放状态的变化（如播放、暂停、上一首/下一首切换和进度跳转等事件），并将其同步到播控中心，以确保两端播放状态一致。

以下为应用端调用本地播放器的播放/暂停方法时，通过AVSession更新播控中心的播放/暂停状态进行双端播放状态同步的示例代码：

```
1. await this.AVSession?.setAVPlaybackState({
2. state: isPlay ? avSession.PlaybackState.PLAYBACK_STATE_PLAY :
3. avSession.PlaybackState.PLAYBACK_STATE_PAUSE,
4. });
```

[AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L228-L231)

需要注意的是，在更新播放进度时，需要同时传入音频播放的时间进度（elapsedTime）和当前时间戳（updateTime），以下为示例代码：

```
1. await this.AVSession?.setAVPlaybackState({
2. position: {
3. elapsedTime: position,
4. updateTime: new Date().getTime()
5. }
6. });
```

[AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L245-L250)

### 播控中心控制应用播放

当用户在播控中心操作音频（如播放、暂停、上一首/下一首切换和进度跳转等事件）时，这些操作不会自动同步到应用端。开发者需要通过AVSession.on('controlCommand')监听这些操作事件，并在回调函数中主动更新应用的播放状态，以确保应用端与播控中心的播放状态一致。

以下为应用端监听到播控中心的播放/暂停操作事件时，主动调用本地播放器的播放/暂停方法进行双端播放状态同步的示例代码：

```
1. this.AVSession?.on('play', () => controller?.setPlaying());
2. this.AVSession?.on('pause', () => controller?.setPause());
```

[AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L175-L176)

说明

建议在音频不需要与播控中心进行交互时，通过AVSession.off()销毁使用AVSession.on()注册的播控中心交互事件监听。

## 投播基础功能

为确保投播功能正常使用，应用在发起投播前需要接入播控中心。如未完成此关键步骤，将导致投播功能不可用。

### 创建投播

**图9** 本端播放的音频投播到远端

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/e0/v3/PU1OkzSJQ1iNKaPYrUxXaQ/zh-cn_media_0000002421894824.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=029FC4D35B1CD34459D58808223CA01408D7820C143F52F0A882EA5517634679)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 12.39%

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

创建投播需要通过setExtras()声明应用支持投播功能，初始化投播组件AVCastPicker，同时通过媒体会话注册设备改变事件监听。用户交互时，触发AVCastPicker组件弹出设备选择的半模态弹窗，待设备选定后，应用需依次执行投播媒体信息设置、投播媒体资源准备（prepare）和投播媒体资源播放启动（start）来将本端音视频资源投播到远端继续播放。

**时序图**

**图10** 创建投播时序图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/BKOjv4PsTZeYJQiFmN6fVQ/zh-cn_image_0000002422054684.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=B211CAC4457F07BA8972DD6B8853CAA3F3E03FDF470392629CFF6C38201A4DD0 "点击放大")

**开发步骤**

1. 接入播控中心后，在创建投播前，需要通过AVSession.setExtras({requireAbilityList: ['url-cast']})告知系统应用当前支持投播功能，才能成功发起投播。

   ```
   1. await this.AVSession.setExtras({
   2. 'requireAbilityList': ['url-cast']
   3. });
   ```

   [AVSessionController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AVSessionController.ets#L68-L70)
2. 在音频播放页绘制投播组件[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)，用于拉起半模态弹窗选择投播设备。

   **图11** 发起投播界面   
   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/KpyjzlASRM6bAc5995K19Q/zh-cn_image_0000002455573541.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=FD8B598961B935879F1F513AFCB6CE83E4E9963AB41C49778ECF2222690D5659 "点击放大")

   ```
   1. AVCastPicker({
   2. normalColor: this.color, activeColor: this.color,
   3. })
   ```

   [TopAreaComponent.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/component/TopAreaComponent.ets#L87-L89)
3. 设置播放设备变化的监听事件[AVSession.on('outputDeviceChange')](../harmonyos-references/arkts-apis-avsession-avsession.md#onoutputdevicechange10)，当用户选择投播设备并切换成功后，播控中心会自动接管远端设备的播放控制，无需开发者额外设置。开发者只需在相应的回调函数中实现本端音频的播放控制逻辑即可。

   ```
   1. this.avSessionController?.AVSession?.on('outputDeviceChange', async (connectState: avSession.ConnectionState,
   2. device: avSession.OutputDeviceInfo) => {
   3. let currentDevice: avSession.DeviceInfo = device?.devices?.[0];
   4. this.deviceInfo = currentDevice;
   5. if (currentDevice.castCategory === avSession.AVCastCategory.CATEGORY_REMOTE &&
   6. connectState === avSession.ConnectionState.STATE_CONNECTED) {
   7. // ...
   8. this.isCasting = true;
   9. this.startCast(this.currentTime, this.selectIndex);
   10. }
   11. // ...
   12. })
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/component/ControlAreaComponent.ets#L92-L124)
4. 设置投播媒体资源，以投播本地资源为例，具体步骤如下：

   a.构建播放列表项[avSession.AVQueueItem](../harmonyos-references/arkts-apis-avsession-i.md#avqueueitem10)。需要传入的媒体元数据为assetId（播放列表媒体ID，应用自定义）、title（媒体标题）、artist（媒体专辑作者）、subtitle（播放列表媒体子标题）、mediaType（媒体类型）、mediaImage（媒体图片像素数据）、fdSrc（播放列表媒体本地文件的句柄，系统通过该标识符定位具体的媒体文件）、startPosition（播放列表媒体起始播放位置）、duration（媒体播放时长）、lyricContent（播放列表媒体歌词内容）。

   b.通过[avCastController.prepare()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#prepare10)准备媒体播放资源，即进行播放资源的加载和缓冲。

   c.通过[avCastController.start()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#start10)启动播放媒体资源。

   ```
   1. let playItem: avSession.AVQueueItem;
   2. if (this.context && songItem.lyric) {
   3. lyricContent = await getRawStringData(this.context, songItem.lyric);
   4. }
   5. try {
   6. let file = await fileIo.open(this.context?.filesDir + '/' + curSrc);
   7. let avFileDescriptor: media.AVFileDescriptor = { fd: file.fd };
   8. playItem = {
   9. itemId: this.musicIndex,
   10. description: {
   11. assetId: 'AUDIO-' + JSON.stringify(this.musicIndex),
   12. title: songItem.title,
   13. artist: songItem.singer,
   14. subtitle: 'audio',
   15. mediaType: 'AUDIO',
   16. albumCoverUri: songItem.albumCoverUri,
   17. fdSrc: avFileDescriptor,
   18. startPosition: startPosition,
   19. duration: AppStorage.get('durationTime'),
   20. lyricContent: lyricContent,
   21. }
   22. };
   23. await this.avCastController?.prepare(playItem);
   24. await this.avCastController?.start(playItem);
   25. } catch (err) {
   26. hilog.error(0x0000, TAG, `open file ${err}`);
   27. }
   ```

   [AudioCastController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AudioCastController.ets#L58-L84)

### 本端控制远端音频播放

**图12** 本端控制远端音频播放

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/6c/v3/7VxwzRoRToqM68DpZyawHA/zh-cn_media_0000002455453669.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=9DCD1E875E4DDD84A3954D1D8B22F7332BEC10B8C79015675453440DE517425F)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 100.00%

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

开发者可以采用[avCastController.sendControlCommand()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#sendcontrolcommand10)接口控制远端设备的播放状态，通过在command参数中传入不同的投播控制指令并设置相关参数，可以控制远端播放、暂停、播放进度、音量和循环模式等。具体指令与功能的对应关系可参考[AVCastControlCommandType](../harmonyos-references/arkts-apis-avsession-t.md#avcastcontrolcommandtype10)。

**时序图**

**图13** 本端控制远端音频播放时序图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/bt1PSWzRQSSJDy_0D8Rp5g/zh-cn_image_0000002421894848.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=BFDAD9202229757E5D7122D94330808744A860544836942D8062432DE7A1892F "点击放大")

**开发步骤**

以下为通过传入'play'指令在本端控制远端设备播放的示例代码：

```
1. let avCommand: avSession.AVCastControlCommand = { command: 'play' };
2. await this.avCastController?.sendControlCommand(avCommand);
```

[AudioCastController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AudioCastController.ets#L149-L150)

需要注意的是，在播放进度跳转、音量调节和循环模式设置时，需要传入时间（单位ms）、音量和循环模式参数。

```
1. public async seek(timeMS: number) {
2. let avCommand: avSession.AVCastControlCommand = { command: 'seek', parameter: timeMS };
3. try {
4. await this.avCastController?.sendControlCommand(avCommand);
5. } catch (error) {
6. hilog.error(0x0000, TAG, `avCastController sendControlCommand failed, the error is: ${JSON.stringify(error)}`);
7. }
8. }

10. public async setAVCastVolume(volume: number) {
11. let avCommand: avSession.AVCastControlCommand = { command: 'setVolume', parameter: volume };
12. try {
13. await this.avCastController?.sendControlCommand(avCommand);
14. } catch (error) {
15. hilog.error(0x0000, TAG, `avCastController sendControlCommand failed, the error is: ${JSON.stringify(error)}`);
16. }
17. }

19. public async setPlayModel(mode: number) {
20. let avCommand: avSession.AVCastControlCommand = { command: 'setLoopMode', parameter: mode };
21. try {
22. await this.avCastController?.sendControlCommand(avCommand);
23. } catch (error) {
24. hilog.error(0x0000, TAG, `avCastController sendControlCommand failed, the error is: ${JSON.stringify(error)}`);
25. }
26. }
```

[AudioCastController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AudioCastController.ets#L166-L191)

### 远端音频状态回传本端

**图14** 远端音频状态回传本端

[](https://contentcenter-videovali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_300_3/96/v3/xyOzZCP_SUCKwYT_i3OEVQ/zh-cn_media_0000002422054696.mp4?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=F0BBD10239391001B73D4790C8C35C6D5089FDEA04A4F4C97F37C16EA420535B)

Video Player is loading.

Play Video

Play

Current Time 0:00

Loaded: 9.97%

0:00

Duration 0:08

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

开发者可以采用[avCastController.on('playbackStateChange')](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaybackstatechange10)接口监听远端设备播放状态的变化，通过在filter参数中传入不同的播放状态字段和callback参数设置相应的回调函数，可以将远端的播放状态（播放、暂停、上一首/下一首切换和播放进度等信息）同步到本端。具体的播放状态属性可参考[AVPlaybackState](../harmonyos-references/arkts-apis-avsession-i.md#avplaybackstate10)。

**时序图**

**图15** 远端音频状态回传本端时序图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SRFPw0fTTCm7KDxaDHadaw/zh-cn_image_0000002455573553.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=DD771D27DABF9EF3551DC71EB05C00B9B782E1EF2F721C119942BE3E7A98B96D "点击放大")

**开发步骤**

开发者可以使用[@Track](../harmonyos-guides/arkts-track.md)装饰器管理这些经常被改变的状态变量，以便在远端播放状态变化时，实时响应并自动刷新本端音频状态。以下为获取远端已播放时长并同步给本端的示例代码：

```
1. export class AudioCastController implements Controller {
2. // ...
3. @Track elapsedTime: number = 0;
4. // ...
5. setAVCastCallback() {
6. this.unregisterCastListener();
7. try {
8. // ...
9. this.avCastController?.on('playbackStateChange', ['position'], (playbackState: avSession.AVPlaybackState) => {
10. if (playbackState.position) {
11. this.elapsedTime = playbackState.position.elapsedTime;
12. }
13. });
14. // ...
15. } catch (error) {
16. hilog.error(0x0000, TAG, `avCastController on event failed, the error is: ${JSON.stringify(error)}`);
17. }
18. }
19. // ...
20. }
```

[AudioCastController.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/controller/AudioCastController.ets#L30-L226)

### 资源切换

投播过程中，在完成本首播放或用户触发音频切换时，只需重新设置音频资源即可实现音频切换，无需断开投播连接。

**开发步骤**

1. 当切换音频时，触发音频资源的重新设置，设置资源的具体方法可参考[创建投播](bpta-audio-cast.md#section148446619451)。
2. 在本端通过点击播放页面列表中的音频和上一首/下一首操作按钮的方式，或通过点击播控中心上一首/下一首操作按钮的方式来触发音频资源的重新设置。

   通过播放页切换音频：

   ```
   1. Image($r('app.media.ic_public_previous'))
   2. // ...
   3. .onClick(() => {
   4. this.playNextOrPrevious('previous');
   5. })
   6. // ...
   7. Image($r('app.media.ic_public_next'))
   8. // ...
   9. .onClick(() => {
   10. this.playNextOrPrevious('next');
   11. })
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/component/ControlAreaComponent.ets#L473-L502)

   通过播控中心切换音频：

   ```
   1. this.avSessionController.AVSession?.on('playNext', () => {
   2. this.playNextOrPrevious('next');
   3. });
   4. this.avSessionController.AVSession?.on('playPrevious', () => {
   5. this.playNextOrPrevious('previous');
   6. });
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/component/ControlAreaComponent.ets#L245-L250)
3. 采用[avCastController.on('playPrevious')](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplayprevious10)和[avCastController.on('playNext')](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#onplaynext10)接口监听远端上一首/下一首切换事件，并在回调函数中重新设置音频资源。

   ```
   1. this.audioCastController.avCastController?.on('playNext', () => {
   2. this.playNextOrPrevious('next');
   3. });
   4. this.audioCastController.avCastController?.on('playPrevious', () => {
   5. this.playNextOrPrevious('previous');
   6. });
   ```

   [ControlAreaComponent.ets](https://gitcode.com/harmonyos_samples/AudioCast/blob/master/entry/src/main/ets/component/ControlAreaComponent.ets#L214-L219)

### 投播音质切换

**时序图**

**图16** 切换投播音质时序图   
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/_V4zy8A-QxqEEsQrO3OPNw/zh-cn_image_0000002455453673.png?HW-CC-KV=V1&HW-CC-Date=20260429T061239Z&HW-CC-Expire=86400&HW-CC-Sign=7FBAD5A0F8A437E33D48FA088C108DBC2EB376A4129F9E26E67E53FD9831B8B2 "点击放大")

投播过程中，当用户触发音质切换功能时，开发者只需根据对应音质重新设置不同的投播资源即可实现音质的切换，无需断开投播连接。设置资源的具体方法可参考[创建投播](bpta-audio-cast.md#section148446619451)。

说明

需要注意的是，要将当前音频的播放进度（startPosition）同步设置给新的音频资源，以确保切换前后音频状态的同步。

## 常见问题

### 创建AVCastPicker后应用界面未显示

**问题现象**

打开音乐播放页，右上角的投播组件没有显示。

**可能原因**

1. 未初始化媒体会话AVSession。
2. 未配置媒体会话元数据AVMetaDate。
3. 未声明当前应用支持投播功能。

**解决措施**

1. 创建并激活媒体会话AVSession。
2. 通过[AVSession.setAVMetadata()](../harmonyos-references/arkts-apis-avsession-avsession.md#setavmetadata10)设置媒体会话元数据AVMetaData。
3. 通过[AVSession.setExtras()](../harmonyos-references/arkts-apis-avsession-avsession.md#setextras10)声明当前应用支持投播功能。

**参考链接**

* [媒体会话初始化](bpta-audio-cast.md#section641024718268)
* [设置媒体会话元数据](bpta-audio-cast.md#section343315312467)
* [创建投播](bpta-audio-cast.md#section148446619451)

### 投播后远端黑屏，无音频播放

**问题现象**

投播后，本端显示已切换到远端设备，但是远端黑屏，无音频播放。

**可能原因**

1. 未配置投播媒体元数据。
2. 未加载或启动媒体资源的播放。
3. 远端设备不支持当前投播的音频类型。

**解决措施**

1. 配置投播媒体元数据[avSession.AVQueueItem](../harmonyos-references/arkts-apis-avsession-i.md#avqueueitem10)。
2. 依次调用[avCastController.prepare()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#prepare10)和[avCastController.start()](../harmonyos-references/arkts-apis-avsession-avcastcontroller.md#start10)接口加载并启动媒体资源的播放。
3. 检查远端设备是否支持当前投播的音频类型。

## 示例代码

* [实现音频投播功能](https://gitcode.com/harmonyos_samples/AudioCast)
