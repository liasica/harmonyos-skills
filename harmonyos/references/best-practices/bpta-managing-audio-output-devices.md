---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-managing-audio-output-devices
title: 管理音频输出设备开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 管理音频输出设备开发实践
category: best-practices
scraped_at: 2026-04-28T08:20:50+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:6bea2431a8ed5c040fcf8aacce994b22ecbef482aaeb993434e545bd1bf029cf
---

## 概述

在播放音乐、播放语音消息、语音通话等场景下，经常需要切换输出设备，例如在音乐播放过程中，断开蓝牙耳机连接后输出设备将从耳机切换至手机扬声器，如果不进行设备管理，就会出现断开连接后音乐在扬声器继续播放，造成不良体验。因此，开发者需要对系统的音频输出设备进行管理。开发者可使用以下模块实现音频输出设备的管理功能：

| **模块** | **应用场景** |
| --- | --- |
| [AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md) | 管理全局音频输出设备，提供系统输出设备查询及状态变化的监听接口 |
| [AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md) | 管理应用音频输出设备，当应用不持有AudioRenderer对象时，管理应用的音频输出设备 |
| [AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md) | 管理音频流输出设备，提供音频流输出设备的切换接口及设备变化的监听接口 |
| [AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker) | 切换音频输出设备的系统组件 |

本文基于上述模块提供的能力，指导开发者实现获取输出设备信息、切换输出设备、响应设备变更等场景，并对开发过程中的常见问题提供解决方案。

## 获取输出设备信息

### 场景描述

在开始播放音频前，获取系统的输出设备信息并展示。当设备发生变化时，同步更新设备列表。例如，当蓝牙耳机上线时，将蓝牙耳机添加到设备列表中；当蓝牙耳机下线时，将蓝牙耳机从设备列表中移除。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/WQmYCI1TRj2bpVkdxTh62A/zh-cn_image_0000002548392057.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=BA966F39E0E1F14A4431A022FA9AA95A7BD4E296EA73BA46F6C8D48E5F4E45C4 "点击放大")

### 实现原理

[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)提供管理全局音频输出设备的能力，包括查询设备信息、监听设备连接状态变化等。

整体流程如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/LGkZDVjiTxadrQbIndWdSA/zh-cn_image_0000002548512059.png?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=86C1B6BDF8F9B6D9E8E17CEDDD6977C2CDC81E7A5D2882C4A5D7AF37169C3705)

### 开发步骤

1. 创建AudioRoutingManager实例。

   ```
   1. private audioManager = audio.getAudioManager();
   2. // ...
   3. private audioRoutingManager: audio.AudioRoutingManager = this.audioManager.getRoutingManager();
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L26-L32)
2. 使用[AudioRoutingManager.getDevices(deviceFlag: DeviceFlag)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9-1)获取所有已连接的输出设备。设置deviceFlag参数为[OUTPUT\_DEVICES\_FLAG](../harmonyos-references/arkts-apis-audio-e.md#deviceflag)，表示获取输出设备。

   ```
   1. // Get all output devices and display them.
   2. async getDevices() {
   3. this.sceneType = AppStorage.get('outputDeviceType') as string;
   4. this.audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG)
   5. .then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s',
   7. `Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
   8. this.getAvailableDevices();
   9. this.watchDeviceChange(); // Get changes in the status of audio devices.
   10. this.watchCurrentOutputDeviceChanged(); // Monitor current output device change events.
   11. let deviceUsage = this.sceneType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_OUTPUT_DEVICES :
   12. audio.DeviceUsage.CALL_OUTPUT_DEVICES;
   13. this.watchSessionAvailableDeviceChange(deviceUsage); // Available device connection status change events.
   14. this.watchRoutingAvailableDeviceChange(deviceUsage); // Available device connection status change events.
   15. this.watchAudioSessionDeactivated();
   16. })
   17. .catch((err: BusinessError) => {
   18. hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to get devices. error: ${err.code}, ${err.message}`);
   19. });
   20. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L36-L56)
3. 使用[AudioRoutingManager.on('deviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#ondevicechange9)监听输出设备连接状态的变化。

   ```
   1. // Get changes in the status of audio devices.
   2. watchDeviceChange() {
   3. try {
   4. this.audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG,
   5. (deviceChanged: audio.DeviceChangeAction) => {
   6. if (deviceChanged.deviceDescriptors.length > 0) {
   7. // The device connection status changes, with 0 indicating connection and 1 indicating disconnection.
   8. if (deviceChanged.type === audio.DeviceChangeType.CONNECT) {
   9. hilog.info(DOMAIN, 'testTag', '%{public}s',
   10. 'device connected : ' + deviceChanged.deviceDescriptors[0].name);
   11. } else if (deviceChanged.type === audio.DeviceChangeType.DISCONNECT) {
   12. hilog.info(DOMAIN, 'testTag', '%{public}s',
   13. 'device disconnected : ' + deviceChanged.deviceDescriptors[0].name);
   14. }
   15. }
   16. });
   17. } catch (err) {
   18. hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to deviceChange. error: ${err.code}, ${err.message}`);
   19. }
   20. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L236-L256)
4. 使用[AudioRoutingManager.getAvailableDevices(deviceUsage: DeviceUsage)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getavailabledevices12)获取可用输出设备。通过[DeviceUsage](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)参数区分不同的使用场景，[MEDIA\_OUTPUT\_DEVICES](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)表示媒体输出设备，[CALL\_OUTPUT\_DEVICES](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)表示通话输出设备。

   ```
   1. // Get the current list of available audio output devices.
   2. getAvailableDevices() {
   3. let data: audio.AudioDeviceDescriptors = [];
   4. // Distinguish between media and calling devices.
   5. let deviceUsage = this.sceneType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_OUTPUT_DEVICES :
   6. audio.DeviceUsage.CALL_OUTPUT_DEVICES;
   7. try {
   8. data = this.audioRoutingManager.getAvailableDevices(deviceUsage);
   9. hilog.info(DOMAIN, 'testTag', '%{public}s',
   10. `Succeeded in getting availableDevices: ${JSON.stringify(data)}.`);
   11. AppStorage.setOrCreate('availableDevices', data);
   12. // ...
   13. } catch (err) {
   14. let error = err as BusinessError;
   15. hilog.error(DOMAIN, 'testTag', '%{public}s',
   16. `Failed to getAvailableDevices. error: ${error.code}, ${error.message}`);
   17. }
   18. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L60-L85)
5. 使用[AudioRoutingManager.on('availableDeviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onavailabledevicechange12)监听可用输出设备的变化，并在设备变化时更新设备列表。

   ```
   1. // Available device connection status change events.
   2. watchRoutingAvailableDeviceChange(deviceUsage: audio.DeviceUsage) {
   3. let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
   4. let data: audio.AudioDeviceDescriptors = deviceChanged.deviceDescriptors;
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. `Get available device audioRoutingManager ChangeCallback, AudioDeviceDescriptors: ${data}.` +
   7. JSON.stringify(data));
   8. this.getAvailableDevices();
   9. };
   10. try {
   11. this.audioRoutingManager.on('availableDeviceChange', deviceUsage, availableDeviceChangeCallback);
   12. } catch (err) {
   13. hilog.error(DOMAIN, 'testTag', '%{public}s',
   14. `Failed to availableDeviceChange. error: ${err.code}, ${err.message}`);
   15. }
   16. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L216-L232)
6. 使用[AudioRoutingManager.getPreferOutputDeviceForRendererInfo()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferoutputdeviceforrendererinfo10-1)获取播放使用的设备。通过[AudioRendererInfo.usage](../harmonyos-references/arkts-apis-audio-i.md#audiorendererinfo8)参数区分不同的使用场景，例如STREAM\_USAGE\_MUSIC表示音乐播放，STREAM\_USAGE\_VOICE\_COMMUNICATION表示语音通话。

   ```
   1. // Get default or preferred output device.
   2. getPreferredOutputDevice() {
   3. try {
   4. this.deviceDesc = this.audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo);
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. `Succeeded in getting prefer output device: ${JSON.stringify(this.deviceDesc)}.`);
   7. } catch (err) {
   8. let error = err as BusinessError;
   9. hilog.error(DOMAIN, 'testTag', '%{public}s',
   10. `Failed to get prefer output device. Code: ${error.code}, message: ${error.message}`);
   11. }
   12. if (this.deviceDesc?.length) {
   13. AppStorage.setOrCreate('selectedDeviceType', this.deviceDesc[0].deviceType);
   14. }
   15. // ...
   16. }
   ```

   [AudioRendering.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AudioRendering.ets#L116-L139)
7. 使用[AudioRoutingManager.on('preferOutputDeviceChangeForRendererInfo')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onpreferoutputdevicechangeforrendererinfo10)监听播放设备的变化，并在变化时弹框提示用户。

   ```
   1. // Monitor the status changes of preferred output device.
   2. watchPreferredOutputDeviceChange() {
   3. try {
   4. this.audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo,
   5. (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s',
   7. `AudioDeviceDescriptors watchPreferredOutputDeviceChange: ${JSON.stringify(audioDeviceDescriptors)}.`);
   8. AppStorage.setOrCreate('selectedDeviceType', audioDeviceDescriptors[0].deviceType);
   9. // ...
   10. });
   11. } catch (err) {
   12. let error = err as BusinessError;
   13. hilog.error(DOMAIN, 'testTag', '%{public}s',
   14. `Failed to preferOutputDeviceChangeForRendererInfo. error: ${error.code}, ${error.message}`);
   15. }
   16. }
   ```

   [AudioRendering.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AudioRendering.ets#L143-L164)

## 通过系统组件切换输出设备

### 场景描述

音频流类型对输出设备的选择具有决定性影响，对于不同类型的音频流，系统会自动选择相应的输出设备。例如音频流类型是STREAM\_USAGE\_VOICE\_COMMUNICATION时，系统使用听筒作为音频输出设备。为了提升交互的灵活性，应用可以提供主动切换播放设备的交互入口。下图中底部右侧的按钮，用于展示系统组件的使用方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/r2JCY4JISVeSvZ-S0KDfUA/zh-cn_image_0000002516872178.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=A505EC3535D1CE4EA27D9179FF17184247A098C424569EBBA55B2A4DB9B2016D "点击放大")

### 实现原理

系统提供播放设备选择组件[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)，作为音频输出设备发现与连接的统一入口。点击组件图标时，如果输出设备只有听筒和扬声器，可直接切换设备；否则将弹出可选设备列表，从列表中选择设备后，即可切换至相应设备。

### 开发步骤

1. 使用[AVSession.createAVSession(context: Context, tag: string, type: AVSessionType)](../harmonyos-references/arkts-apis-avsession-f.md#avsessioncreateavsession10)创建AVSession。通过[AVSessionType](../harmonyos-references/arkts-apis-avsession-t.md#avsessiontype10)区分不同的使用场景，audio表示音乐播放，voice\_call表示语音通话。

   ```
   1. // Create AVSession.
   2. try {
   3. this.AVSession = await avSession.createAVSession(this.context, 'PLAY_AUDIO', this.sessionType);
   4. hilog.info(DOMAIN, 'testTag', '%{public}s', `session create successed : sessionId : ${this.AVSession.sessionId}`);
   5. } catch (error) {
   6. hilog.error(DOMAIN, 'testTag',
   7. `avSession.createAVSession failed, code: ${error.code}, message: ${error.message}`);
   8. }
   ```

   [AVSessionController.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AVSessionController.ets#L79-L86)
2. 在需要切换设备的界面创建[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)组件。

   ```
   1. AVCastPicker({
   2. normalColor: this.avCastPickerColor,
   3. activeColor: this.avCastPickerColor,
   4. onStateChange: (state: AVCastPickerState) => {
   5. hilog.info(DOMAIN, 'testTag', '%{public}s', `change avcastpicker: ${state}`);
   6. }
   7. })
   ```

   [CallEquipment.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/view/CallEquipment.ets#L225-L231)
3. 手动点击AVCastPicker组件，如果输出设备只有听筒和扬声器，可直接切换；否则，需在弹框中选择目标设备，以完成输出设备的切换。

## 通过API切换输出设备

### 场景描述

当应用不希望用户通过系统组件手动切换输出设备时，可以使用AudioRenderer API实现设备的切换。例如在应用需要根据使用场景自动切换输出设备或自动设置不同的默认设备时。下图中底部右侧的按钮，在不选择AVCastPicker系统组件时，用于展示AudioRenderer API的使用方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/oOl-X3FxTBeBi5Rrm9pCcw/zh-cn_image_0000002516712260.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=EC80AEA87FB62B67A20E7145EA877082F308DFEDC75ED632586A2945C262E002 "点击放大")

### 实现原理

当音频流类型为语音消息、VoIP语音通话或VoIP视频通话时，可以使用[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)的接口切换播放设备。支持听筒、扬声器和系统默认设备间的切换。

### 开发步骤

1. 通过[audio.createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)创建AudioRenderer实例。
2. 使用[AudioRenderer.setDefaultOutputDevice(deviceType: DeviceType)](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)切换输出设备。通过[DeviceType](../harmonyos-references/arkts-apis-audio-e.md#devicetype)参数指定输出设备。

   ```
   1. // Set default output device.
   2. async setOutputDevice(deviceType: audio.DeviceType) {
   3. this.audioRenderer?.setDefaultOutputDevice(deviceType).then(() => {
   4. hilog.info(DOMAIN, 'testTag', '%{public}s', 'audioRenderer setDefaultOutputDevice Success.');
   5. }).catch((err: BusinessError) => {
   6. hilog.error(DOMAIN, 'testTag', '%{public}s', `audioRenderer setDefaultOutputDevice Fail: ${err}`);
   7. });
   8. }
   ```

   [AudioRendering.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AudioRendering.ets#L257-L265)

## 响应音频流输出设备变更

### 场景描述

当系统出现音频输出设备的上下线、用户主动切换设备、设备抢占或设备选择策略变更等场景，导致音频流输出设备变更时，应用可以根据需要做出对应的处理。例如，在音乐播放过程中摘下耳机，输出设备将从蓝牙耳机切换至手机扬声器，此时应暂停播放，以避免音乐外放。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/3NAF3_GYRPCjH44OHCl_Ew/zh-cn_image_0000002548392059.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=F45DAD7ABCCFDCCCB5CBCE08A6198A541FD5E597C29123046BE87B5A3A3D9E02 "点击放大")

### 实现原理

[AudioRenderer.on('outputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)可以监听音频流输出设备变化并返回切换后的设备信息。应用可以根据切换后的新设备做对应的处理。

### 开发步骤

1. 使用[AudioRenderer.on('outputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)监听音频流输出设备变化及原因。

   ```
   1. // Monitor changes in audio stream output devices.
   2. async watchOutputDeviceChangeWithInfo() {
   3. try {
   4. this.audioRenderer?.on('outputDeviceChangeWithInfo', (deviceChangeInfo: audio.AudioStreamDeviceChangeInfo) => {
   5. hilog.info(DOMAIN, 'testTag', '%{public}s', `outputDeviceChangeWithInfo: ${JSON.stringify(deviceChangeInfo)}.`);
   6. AppStorage.setOrCreate('selectedDeviceType', deviceChangeInfo.devices[0].deviceType);
   7. // ...
   8. } catch (err) {
   9. let error = err as BusinessError;
   10. hilog.error(DOMAIN, 'testTag', '%{public}s',
   11. `Failed to watch outputDeviceChangeWithInfo. error: ${error.code}, ${error.message}`);
   12. }
   13. }
   ```

   [AudioRendering.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AudioRendering.ets#L168-L210)
2. 当监听到AudioStreamDeviceChangeReason.REASON\_OLD\_DEVICE\_UNAVAILABLE时，如果新设备是扬声器，并且在媒体播放场景，应考虑暂停音频播放。

   ```
   1. switch (deviceChangeInfo.changeReason) {
   2. case audio.AudioStreamDeviceChangeReason.REASON_OLD_DEVICE_UNAVAILABLE:
   3. // unavailability event, if the application is in a playback state, it should pause playback.
   4. if (deviceChangeInfo.devices[0].deviceType === audio.DeviceType.SPEAKER &&
   5. this.sceneType === CommonConstants.MEDIA_EQUIPMENT) {
   6. // If the new device is a speaker, pause playback.
   7. this.pauseAudioRenderer();
   8. }
   9. break;
   10. case audio.AudioStreamDeviceChangeReason.REASON_NEW_DEVICE_AVAILABLE:
   11. // The application responds to device availability events based on business conditions.
   12. break;
   13. case audio.AudioStreamDeviceChangeReason.REASON_OVERRODE:
   14. // The application responds to device forced selection events based on business conditions.
   15. break;
   16. case audio.AudioStreamDeviceChangeReason.REASON_UNKNOWN:
   17. // The application responds to events of unknown causes based on business conditions.
   18. break;
   19. }
   ```

   [AudioRendering.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/AudioRendering.ets#L182-L200)

## 使用AudioSession管理音频输出设备

### 场景描述

当应用直接持有AudioRenderer对象时，可以[通过API切换输出设备](bpta-managing-audio-output-devices.md#section914181801319)；当应用不直接持有AudioRenderer对象，但需要通过API接口切换输出设备时，可以使用[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)管理音频输出设备。例如在使用播放器的SDK播放音频流或使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)/[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)播放音频流时。下图中设备列表的“设置”按钮便是基于AudioSessionManager的能力实现输出设备的切换。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/SctiTJKpTGGE55xQmm8WBw/zh-cn_image_0000002548512061.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002047Z&HW-CC-Expire=86400&HW-CC-Sign=C99656528DE7994A66684C5692DFBA82F2A08F2FCF2BA4B184D566B0B68C74AE "点击放大")

### 实现原理

使用[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)的管理应用音频输出设备的相关能力，包括切换输出设备、监听输出设备的变化，实现具体场景下输出设备间的切换。与AudioRenderer相同，仅当音频流类型为语音消息、VoIP语音通话或VoIP视频通话时，支持听筒、扬声器和系统默认设备间的切换。

### 开发步骤

1. 创建AudioSessionManager实例。

   ```
   1. private audioManager = audio.getAudioManager();
   2. private audioSessionManager: audio.AudioSessionManager = this.audioManager.getSessionManager();
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L25-L29)
2. 使用[AudioSessionManager.activateAudioSession()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#activateaudiosession12)激活AudioSession。

   ```
   1. async activeAudioSession() {
   2. let isAudioSessionDeactivated: Boolean | undefined = AppStorage.get('isAudioSessionDeactivated');
   3. if (isAudioSessionDeactivated) {
   4. let strategy: audio.AudioSessionStrategy = {
   5. concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_DEFAULT
   6. }
   7. this.audioSessionManager.activateAudioSession(strategy).then(() => {
   8. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in doing activateAudioSession');
   9. AppStorage.setOrCreate('isAudioSessionDeactivated', false);
   10. }).catch((err: BusinessError) => {
   11. hilog.error(DOMAIN, 'testTag', '%{public}s',
   12. `Failed to activateAudioSession. error: ${err.code}, ${err.message}`);
   13. });
   14. }
   15. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L89-L104)
3. 使用[AudioSessionManager.setDefaultOutputDevice()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)将用户选择的设备设置为输出设备。

   ```
   1. // Set output device.
   2. async setOutputDevice(deviceType: audio.DeviceType) {
   3. // Only the following devices are supported: EARPIECE, SPEAKER, and DEFAULT (system default device).
   4. hilog.info(DOMAIN, 'testTag', '%{public}s', 'setOutputDevice.');
   5. this.audioSessionManager.setDefaultOutputDevice(deviceType).then(() => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in doing setDefaultOutputDevice.');
   7. this.activeAudioSession();
   8. this.getDefaultOutputDevice();
   9. }).catch((err: BusinessError) => {
   10. hilog.error(DOMAIN, 'testTag', '%{public}s',
   11. `Failed to setDefaultOutputDevice. error: ${err.code}, ${err.message}`);
   12. });
   13. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L141-L154)
4. 使用[AudioSessionManager.on('currentOutputDeviceChanged')](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#oncurrentoutputdevicechanged20)监听输出设备变化，当输出设备切换成功后会触发该回调。

   ```
   1. // Monitor current output device change events.
   2. watchCurrentOutputDeviceChanged() {
   3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentOutputDeviceChangedCallback');
   4. let currentOutputDeviceChangedCallback =
   5. (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s',
   7. `reason of currentOutputDeviceChanged: ${currentOutputDeviceChangedEvent.changeReason} `);
   8. };
   9. try {
   10. this.audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
   11. hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentOutputDeviceChanged');
   12. } catch (err) {
   13. let error = err as BusinessError;
   14. hilog.error(DOMAIN, 'testTag', '%{public}s',
   15. `Failed to currentOutputDeviceChangedCallback. error: ${error.code}, ${error.message}`);
   16. }
   17. }
   ```

   [OutputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/manage-audio-output-devices/blob/dev/entry/src/main/ets/common/OutputDevicesOperation.ets#L176-L193)

## 常见问题

### 视频播放时突然自动暂停

**问题描述**

视频在播放过程中突然暂停，但未执行暂停操作，也未切换设备。

**问题根因**

使用了错误的监听音频输出设备变化的接口。AudioRoutingManager.on('deviceChange')可以监听到所有设备的连接状态变化，不建议将其作为应用处理自动暂停的依据。

**解决方案**

使用[AudioRenderer.on('outputDeviceChangeWithInfo')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)监听音频流输出设备的变化，并响应输出设备的变化，合理暂停，可参考[响应输出设备变更时合理暂停](../harmonyos-guides/audio-output-device-change.md)。

## 示例代码

* [实现音频输出设备管理功能](https://gitcode.com/HarmonyOS_Samples/manage-audio-output-devices)
