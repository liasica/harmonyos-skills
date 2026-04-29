---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-managing-audio-input-devices
title: 管理音频输入设备开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 管理音频输入设备开发实践
category: best-practices
scraped_at: 2026-04-29T14:11:49+08:00
doc_updated_at: 2026-04-07
content_hash: sha256:e6dfca5be4c333341013f30973f6ce93237ea6e11f09a7879f700da6143cf1c7
---

## 概述

在录音、语音通话、录制语音消息等场景下，经常需要切换输入设备，例如从手机麦克风切换到蓝牙耳机。因此，开发者需要对系统的音频输入设备进行管理。开发者可使用以下模块实现音频输入设备的管理功能。

| **模块** | **应用场景** |
| --- | --- |
| [AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md) | 管理全局音频输入设备，提供系统输入设备查询及状态变化的监听接口 |
| [AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md) | 管理应用音频输入设备，提供切换输入设备的API接口 |
| [AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md) | 管理音频流输入设备，提供音频流输入设备变化的监听接口 |
| [AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md#avinputcastpicker) | 切换音频输入设备的系统组件，目前仅支持PC/2in1设备 |

本文基于上述模块提供的能力，指导开发者实现获取输入设备信息、切换输入设备、响应设备变更等场景，并提供开发过程中常见问题的解决方案。

## 获取输入设备信息

### 场景描述

在开始录制音频之前，获取系统的输入设备信息并展示；当设备发生变化时，同步更新设备列表。例如，当蓝牙耳机上线时，将蓝牙耳机添加到设备列表中；当蓝牙耳机下线时，将蓝牙耳机从设备列表中移除。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/HU0UjlmSQG6ahgOVx7mF-g/zh-cn_image_0000002513603472.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061139Z&HW-CC-Expire=86400&HW-CC-Sign=6525E6CF64B543909340610FCB70512A998857AFE1BAFDFCEDD6938F6A3D2C38 "点击放大")

### 实现原理

[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)提供管理全局音频输入设备的能力，包括查询设备信息、监听设备连接状态变化等。

### 开发步骤

1. 创建AudioRoutingManager实例。

   ```
   1. private audioManager = audio.getAudioManager();
   2. // ...
   3. private audioRoutingManager: audio.AudioRoutingManager = this.audioManager.getRoutingManager();
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L26-L32)
2. 使用[AudioRoutingManager.getDevices(deviceFlag: DeviceFlag)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9-1)获取所有已连接的输入设备。设置deviceFlag参数为[INPUT\_DEVICES\_FLAG](../harmonyos-references/arkts-apis-audio-e.md#deviceflag)表示获取输入设备。

   ```
   1. // Get all input devices and display them.
   2. async getDevices(inputDeviceType: string) {
   3. this.deviceType = inputDeviceType;
   4. this.audioRoutingManager.getDevices(audio.DeviceFlag.INPUT_DEVICES_FLAG)
   5. .then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s',
   7. `Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
   8. this.getAvailableDevices();
   9. this.watchDeviceChange(); // Get changes in the status of audio devices.
   10. this.watchCurrentInputDeviceChanged(); // Monitor current input device change events.
   11. let deviceUsage = this.deviceType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_INPUT_DEVICES :
   12. audio.DeviceUsage.CALL_INPUT_DEVICES;
   13. this.watchSessionAvailableDeviceChange(deviceUsage); // Available device connection status change events.
   14. this.watchRoutingAvailableDeviceChange(deviceUsage); // Available device connection status change events.
   15. })
   16. .catch((err: BusinessError) => {
   17. hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to get devices. error: ${err.code}, ${err.message}`);
   18. });
   19. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L67-L86)
3. 使用[AudioRoutingManager.on('deviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#ondevicechange9)监听输入设备连接状态的变化。

   ```
   1. // Get changes in the status of audio devices.
   2. watchDeviceChange() {
   3. try {
   4. this.audioRoutingManager.on('deviceChange', audio.DeviceFlag.INPUT_DEVICES_FLAG,
   5. (deviceChanged: audio.DeviceChangeAction) => {
   6. // The device connection status changes, with 0 indicating connection and 1 indicating disconnection.
   7. if (deviceChanged.type === audio.DeviceChangeType.CONNECT) {
   8. hilog.info(DOMAIN, 'testTag', '%{public}s',
   9. 'device connected : ' + deviceChanged.deviceDescriptors[0].displayName);
   10. } else if (deviceChanged.type === audio.DeviceChangeType.DISCONNECT) {
   11. hilog.info(DOMAIN, 'testTag', '%{public}s',
   12. 'device disconnected : ' + deviceChanged.deviceDescriptors[0].displayName);
   13. }
   14. });
   15. } catch (err) {
   16. let error = err as BusinessError;
   17. hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to deviceChange. error: ${error.code}, ${error.message}`);
   18. }
   19. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L203-L222)
4. 使用[AudioRoutingManager.getAvailableDevices(deviceUsage: DeviceUsage)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getavailabledevices12)获取可用输入设备。通过[DeviceUsage](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)参数区分不同的使用场景，[MEDIA\_INPUT\_DEVICES](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)表示媒体输入设备，[CALL\_INPUT\_DEVICES](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)表示通话输入设备。

   ```
   1. // Get the current list of available audio input devices.
   2. getAvailableDevices() {
   3. let data: audio.AudioDeviceDescriptors = [];
   4. // Distinguish between media and calling devices.
   5. let deviceUsage = this.deviceType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_INPUT_DEVICES :
   6. audio.DeviceUsage.CALL_INPUT_DEVICES;
   7. try {
   8. data = this.audioRoutingManager.getAvailableDevices(deviceUsage);
   9. hilog.info(DOMAIN, 'testTag', '%{public}s',
   10. `Succeeded in getting availableDevices: ${JSON.stringify(data)}.`);
   11. AppStorage.setOrCreate(CommonConstants.AVAILABLE_DEVICES, data);
   12. } catch (err) {
   13. let error = err as BusinessError;
   14. hilog.error(DOMAIN, 'testTag', '%{public}s',
   15. `Failed to getAvailableDevices. error: ${error.code}, ${error.message}`);
   16. }
   17. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L90-L107)
5. 使用[AudioRoutingManager.on('availableDeviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onavailabledevicechange12)监听可用输入设备的变化，并在设备变化时更新设备列表。

   ```
   1. // Available device connection status change events.
   2. watchRoutingAvailableDeviceChange(deviceUsage: audio.DeviceUsage) {
   3. let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
   4. let data: audio.AudioDeviceDescriptors = deviceChanged.deviceDescriptors;
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. `Get available device audioRoutingManager ChangeCallback, AudioDeviceDescriptors: ${data}.` +
   7. JSON.stringify(data));
   8. this.getAvailableDevices(); // Update available devices.
   9. };
   10. try {
   11. this.audioRoutingManager.on('availableDeviceChange', deviceUsage, availableDeviceChangeCallback);
   12. } catch (err) {
   13. let error = err as BusinessError;
   14. hilog.error(DOMAIN, 'testTag', '%{public}s',
   15. `Failed to availableDeviceChange. error: ${error.code}, ${error.message}`);
   16. }
   17. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L182-L199)
6. 使用[AudioRoutingManager.getPreferredInputDeviceForCapturerInfo()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferredinputdeviceforcapturerinfo10-1)获取录制使用的设备。通过[AudioCapturerInfo.source](../harmonyos-references/arkts-apis-audio-i.md#audiocapturerinfo8)参数区分不同的使用场景，例如SOURCE\_TYPE\_MIC表示普通录音，SOURCE\_TYPE\_VOICE\_COMMUNICATION表示语音通话。

   ```
   1. // Get default or preferred input device.
   2. getPreferredInputDevice() {
   3. this.audioRoutingManager.getPreferredInputDeviceForCapturerInfo(this.audioCapturerInfo,
   4. (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
   5. if (err) {
   6. hilog.error(DOMAIN, 'testTag', '%{public}s',
   7. `Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
   8. } else {
   9. hilog.info(DOMAIN, 'testTag', '%{public}s',
   10. `Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
   11. if (audioDeviceDescriptors.length > 0) {
   12. AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, audioDeviceDescriptors[0].id);
   13. }
   14. }
   15. });
   16. }
   ```

   [AudioRecording.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/AudioRecording.ets#L191-L207)
7. 使用[AudioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onpreferredinputdevicechangeforcapturerinfo10)监听录制设备的变化，并在变化时弹框提示用户。

   ```
   1. // Monitor the status changes of preferred input device.
   2. watchPreferredInputDeviceChange() {
   3. try {
   4. this.audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', this.audioCapturerInfo,
   5. (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
   6. hilog.info(DOMAIN, 'testTag', '%{public}s',
   7. `Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
   8. if (audioDeviceDescriptors.length > 0) {
   9. AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, audioDeviceDescriptors[0].id);
   10. }
   11. });
   12. } catch (err) {
   13. let error = err as BusinessError;
   14. hilog.error(DOMAIN, 'testTag', '%{public}s',
   15. `Failed to preferredInputDeviceChangeForCapturerInfo. error: ${error.code}, ${error.message}`);
   16. }
   17. }
   ```

   [AudioRecording.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/AudioRecording.ets#L241-L258)

## 通过API切换输入设备

### 场景描述

音频流类型对输入设备的选择具有决定性影响，对于不同类型的音频流，系统会自动选择相应的输入设备。例如音频流类型是SOURCE\_TYPE\_MIC时，系统使用内置麦克风作为音频输入设备。如果默认的输入设备不符合使用需求，应用可以调用相关接口进行修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/lKkX1lUbSRmso4L1T8cfig/zh-cn_image_0000002545043447.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061139Z&HW-CC-Expire=86400&HW-CC-Sign=A240EE12E88CB22A87575EF1C85F7C797B13EB1D9CD27EDA2CA888065D36D175 "点击放大")

### 实现原理

使用[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)管理音频输入设备。通过该组件，可默认将蓝牙设备设为音频输入源，同时支持动态切换不同的媒体输入设备。

整体流程如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/qmAfXF1xTwuqInARfRXJWg/zh-cn_image_0000002545123443.png?HW-CC-KV=V1&HW-CC-Date=20260429T061139Z&HW-CC-Expire=86400&HW-CC-Sign=0B5AC730197176D921F64D0A4A2D0C548AEDCC351720BB8C0B9726C7F7FAF82C)

说明

在语音通话场景下，由于输入设备跟随当前输出设备，因此使用AudioSessionManager的API无法切换输入设备。

### 开发步骤

1. 创建AudioSessionManager实例。

   ```
   1. private audioManager = audio.getAudioManager();
   2. private audioSessionManager: audio.AudioSessionManager = this.audioManager.getSessionManager();
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L25-L29)
2. 使用[AudioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category)](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置优先选择蓝牙设备作为输入设备，当蓝牙设备上线后，会自动切换到蓝牙设备进行录制。通过[category](../harmonyos-references/arkts-apis-audio-e.md#bluetoothandnearlinkpreferredrecordcategory21)参数设置蓝牙设备使用模式，当设置[PREFERRED\_NONE](../harmonyos-references/arkts-apis-audio-e.md#bluetoothandnearlinkpreferredrecordcategory21)时，取消优先选择蓝牙设备。

   ```
   1. // Set priority to select Bluetooth devices as input devices.
   2. async setBluetooth(category: number) {
   3. await this.audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category)
   4. .then(() => {
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. 'Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.' + category);
   7. AppStorage.setOrCreate(CommonConstants.BLUETOOTH_AND_NEARLINK_PREFERRED, category);
   8. })
   9. .catch((err: BusinessError) => {
   10. hilog.error(DOMAIN, 'testTag', '%{public}s',
   11. `Failed to setBluetoothAndNearlinkPreferredRecordCategory. error: ${err.code}, ${err.message}`);
   12. });
   13. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L36-L49)
3. 使用[AudioSessionManager.selectMediaInputDevice()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)将用户选择的设备设置为输入设备。

   ```
   1. // Set input device.
   2. async setInputDevice(data: audio.AudioDeviceDescriptor) {
   3. this.audioSessionManager.selectMediaInputDevice(data).then(() => {
   4. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in doing selectMediaInputDevice.');
   5. this.getSelectedMediaInputDevice();
   6. }).catch((err: BusinessError) => {
   7. hilog.error(DOMAIN, 'testTag', '%{public}s',
   8. `Failed to selectMediaInputDevice. error: ${err.code}, ${err.message}`);
   9. });
   10. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L111-L121)
4. 使用[AudioSessionManager.on('currentInputDeviceChanged')](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#oncurrentinputdevicechanged21)监听输入设备变化，当输入设备切换成功后会触发该回调。

   ```
   1. // Monitor current input device change events.
   2. watchCurrentInputDeviceChanged() {
   3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentInputDeviceChangedCallback');
   4. let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. `reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
   7. };
   8. try {
   9. this.audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);
   10. hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentInputDeviceChanged');
   11. } catch (err) {
   12. let error = err as BusinessError;
   13. hilog.error(DOMAIN, 'testTag', '%{public}s',
   14. `Failed to currentInputDeviceChangedCallback. error: ${error.code}, ${error.message}`);
   15. }
   16. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L142-L158)
5. 使用[AudioSessionManager.getSelectedMediaInputDevice()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#getselectedmediainputdevice21)获取当前设置的输入设备。

   ```
   1. // Get the currently selected input device.
   2. getSelectedMediaInputDevice() {
   3. try {
   4. let device: audio.AudioDeviceDescriptor = this.audioSessionManager.getSelectedMediaInputDevice();
   5. hilog.info(DOMAIN, 'testTag', '%{public}s',
   6. 'Succeeded in doing getSelectedMediaInputDevice.' + JSON.stringify(device) + ',' + device?.id);
   7. AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, device.id);
   8. } catch (err) {
   9. let error = err as BusinessError;
   10. hilog.error(DOMAIN, 'testTag', '%{public}s',
   11. `Failed to getSelectedMediaInputDevice. error: ${error.code}, ${error.message}`);
   12. }
   13. }
   ```

   [InputDevicesOperation.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/InputDevicesOperation.ets#L125-L138)

## 通过系统组件切换输入设备

### 场景描述

在PC设备上，通过系统提供的录音设备选择组件[AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md)切换音频输入设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/0-ugQ78BRXWJnBGFfbm-2w/zh-cn_image_0000002513443564.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061139Z&HW-CC-Expire=86400&HW-CC-Sign=DCCA4C893CC06E51DA1F449033F2D5A03B1B6150001B8B8C99ED4CA6E0F32F88 "点击放大")

### 实现原理

系统提供录音设备选择组件[AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md)，作为音频输入设备发现与连接的统一入口。点击组件图标将弹出可选设备列表，从列表中选择设备后，即可切换至相应设备。

### 开发步骤

1. 在需要切换设备的界面创建AVInputCastPicker组件。

   ```
   1. @Builder
   2. customPickerBuilder() {
   3. Image($r('app.media.devices'))
   4. .width('100%')
   5. .height('100%')
   6. }
   ```

   [RecordAndPlay.ets](https://gitcode.com/HarmonyOS_Samples/managing-audio-input-devices/blob/master/entry/src/main/ets/view/RecordAndPlay.ets#L97-L103)

   ```
   1. AVInputCastPicker({
   2. customPicker: () => this.customPickerBuilder(),
   3. onStateChange: this.onStateChange
   4. })
   ```

   [RecordAndPlay.ets](https://gitcode.com/HarmonyOS_Samples/managing-audio-input-devices/blob/master/entry/src/main/ets/view/RecordAndPlay.ets#L76-L79)
2. 手动点击AVInputCastPicker组件，并在弹框中选择目标设备，即可切换输入设备。

## 响应音频流输入设备变更

### 场景描述

当系统因音频输入设备上下线、用户主动切换设备、设备抢占或设备选择策略变更等导致音频流输入设备变更时，应用可以根据需要做出对应的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/NedaJZfaS3eP7bOc02QVPw/zh-cn_image_0000002513603474.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061139Z&HW-CC-Expire=86400&HW-CC-Sign=676F0F3FAE0A859A1E9B65C31704FBAB37108ADD421EFC519B9FCE93632BE621 "点击放大")

### 实现原理

[AudioCapturer.on('inputDeviceChange')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#oninputdevicechange11)可以监听音频流输入设备变化并返回切换后的设备信息。应用可以根据切换后的新设备做对应的处理。

### 开发步骤

使用[AudioCapturer.on('inputDeviceChange')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#oninputdevicechange11)监听到音频流输入设备变化时，显示新设备信息。

```
1. // Monitor the status changes of input device.
2. watchInputDeviceChange() {
3. try {
4. // Use the inputDeviceChange method of audioCapturer to listen for changes in input devices.
5. this.audioCapturer?.on('inputDeviceChange', (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
6. hilog.info(DOMAIN, 'testTag', '%{public}s', `inputDevice id: ${deviceChangeInfo[0].id}`);
7. if (deviceChangeInfo.length > 0) {
8. AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, deviceChangeInfo[0].id);
9. }
10. });
11. } catch (err) {
12. // ...
13. }
14. }
```

[AudioRecording.ets](https://gitcode.com/harmonyos_samples/managing-audio-input-devices/blob/dev/entry/src/main/ets/common/AudioRecording.ets#L219-L237)

## 常见问题

### 确定麦克风是否能够进行录制，判断麦克风是否处于被占用的状态

**解决方案**

API20提供了[AudioStreamManager.isRecordingAvailable(capturerInfo: AudioCapturerInfo)](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)接口，设置AudioCapturerInfo.source为Audio.SourceType.SOURCE\_TYPE\_MIC，然后根据返回值判断麦克风状态。如果返回true，表明可以使用麦克风进行录制；如果返回false，表明麦克风可能已被占用。

API20之前，可以初始化一个AudioCapturer对象并开始录音，如果成功，说明可以使用麦克风进行录制；如果失败，表明麦克风可能已被占用。

## 示例代码

* [实现音频输入设备管理功能](https://gitcode.com/HarmonyOS_Samples/managing-audio-input-devices)
