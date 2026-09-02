---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-managing-audio-input-devices
title: 管理音频输入设备开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 管理音频输入设备开发实践
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-09-02
content_hash: sha256:f1c1194c66e12c2e3620f8ad771ad9bd68df684b776ac2ce7ddb14fb9accd728
---

## 概述

在录音、语音通话、录制语音消息等场景下，经常需要切换输入设备，例如从手机麦克风切换到蓝牙耳机。因此，开发者需要对系统的音频输入设备进行管理。开发者可使用以下模块实现音频输入设备的管理功能。

| **模块** | **应用场景** |
| --- | --- |
| [Interface (AudioRoutingManager)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md) | 管理全局音频输入设备，提供系统输入设备查询及状态变化的监听接口 |
| [Interface (AudioSessionManager)](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md) | 管理应用音频输入设备，提供切换输入设备的API接口 |
| [Interface (AudioCapturer)](../harmonyos-references/arkts-apis-audio-audiocapturer.md) | 管理音频流输入设备，提供音频流输入设备变化的监听接口 |
| [AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md#avinputcastpicker) | 切换音频输入设备的系统组件，目前仅支持PC/2in1设备 |

本文基于上述模块提供的能力，指导开发者实现获取输入设备信息、切换输入设备、响应设备变更等场景，并提供开发过程中常见问题的解决方案。

## 获取输入设备信息

### 场景描述

在开始录制音频之前，获取系统的输入设备信息并展示；当设备发生变化时，同步更新设备列表。例如，当蓝牙耳机上线时，将蓝牙耳机添加到设备列表中；当蓝牙耳机下线时，将蓝牙耳机从设备列表中移除。如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/ajlewuxPRnK223Z6n3FRPw/zh-cn_image_0000002513603472.gif "点击放大")

### 实现原理

[Interface (AudioRoutingManager)](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)提供管理全局音频输入设备的能力，包括查询设备信息、监听设备连接状态变化等。

### 开发步骤

1. 创建AudioRoutingManager实例。

   ```screen
   private audioManager = audio.getAudioManager();
   // ...
   private audioRoutingManager: audio.AudioRoutingManager = this.audioManager.getRoutingManager();
   ```
2. 使用[getDevices()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9-1)获取所有已连接的输入设备。通过[DeviceFlag](../harmonyos-references/arkts-apis-audio-e.md#deviceflag)设置设备类型，INPUT\_DEVICES\_FLAG表示获取输入设备。

   ```screen
   // Get all input devices and display them.
   async getDevices(inputDeviceType: string) {
     this.deviceType = inputDeviceType;
     this.audioRoutingManager.getDevices(audio.DeviceFlag.INPUT_DEVICES_FLAG)
       .then((audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
         hilog.info(DOMAIN, 'testTag', '%{public}s',
           `Succeeded in getting devices, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
         this.getAvailableDevices();
         this.watchDeviceChange(); // Get changes in the status of audio devices.
         this.watchCurrentInputDeviceChanged(); // Monitor current input device change events.
         let deviceUsage = this.deviceType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_INPUT_DEVICES :
           audio.DeviceUsage.CALL_INPUT_DEVICES;
         this.watchSessionAvailableDeviceChange(deviceUsage); // Available device connection status change events.
         this.watchRoutingAvailableDeviceChange(deviceUsage); // Available device connection status change events.
       })
       .catch((err: BusinessError) => {
         hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to get devices. error: ${err.code}, ${err.message}`);
       });
   }
   ```
3. 使用[on('deviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#ondevicechange9)监听输入设备连接状态的变化。

   ```screen
   // Get changes in the status of audio devices.
   watchDeviceChange() {
     try {
       this.audioRoutingManager.on('deviceChange', audio.DeviceFlag.INPUT_DEVICES_FLAG,
         (deviceChanged: audio.DeviceChangeAction) => {
           // The device connection status changes, with 0 indicating connection and 1 indicating disconnection.
           if (deviceChanged.type === audio.DeviceChangeType.CONNECT) {
             hilog.info(DOMAIN, 'testTag', '%{public}s',
               'device connected : ' + deviceChanged.deviceDescriptors[0].displayName);
           } else if (deviceChanged.type === audio.DeviceChangeType.DISCONNECT) {
             hilog.info(DOMAIN, 'testTag', '%{public}s',
               'device disconnected : ' + deviceChanged.deviceDescriptors[0].displayName);
           }
         });
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s', `Failed to deviceChange. error: ${error.code}, ${error.message}`);
     }
   }
   ```
4. 使用[getAvailableDevices()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getavailabledevices12)获取可用输入设备。通过[DeviceUsage](../harmonyos-references/arkts-apis-audio-e.md#deviceusage12)区分不同的使用场景，MEDIA\_INPUT\_DEVICES表示媒体输入设备，CALL\_INPUT\_DEVICES表示通话输入设备。

   ```screen
   // Get the current list of available audio input devices.
   getAvailableDevices() {
     let data: audio.AudioDeviceDescriptors = [];
     // Distinguish between media and calling devices.
     let deviceUsage = this.deviceType === CommonConstants.MEDIA_EQUIPMENT ? audio.DeviceUsage.MEDIA_INPUT_DEVICES :
       audio.DeviceUsage.CALL_INPUT_DEVICES;
     try {
       data = this.audioRoutingManager.getAvailableDevices(deviceUsage);
       hilog.info(DOMAIN, 'testTag', '%{public}s',
         `Succeeded in getting availableDevices: ${JSON.stringify(data)}.`);
       AppStorage.setOrCreate(CommonConstants.AVAILABLE_DEVICES, data);
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to getAvailableDevices. error: ${error.code}, ${error.message}`);
     }
   }
   ```
5. 使用[on('availableDeviceChange')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onavailabledevicechange12)监听可用输入设备的变化，并在设备变化时更新设备列表。

   ```screen
   // Available device connection status change events.
   watchRoutingAvailableDeviceChange(deviceUsage: audio.DeviceUsage) {
     let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
       let data: audio.AudioDeviceDescriptors = deviceChanged.deviceDescriptors;
       hilog.info(DOMAIN, 'testTag', '%{public}s',
         `Get available device audioRoutingManager ChangeCallback, AudioDeviceDescriptors: ${data}.` +
         JSON.stringify(data));
       this.getAvailableDevices(); // Update available devices.
     };
     try {
       this.audioRoutingManager.on('availableDeviceChange', deviceUsage, availableDeviceChangeCallback);
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to availableDeviceChange. error: ${error.code}, ${error.message}`);
     }
   }
   ```
6. 使用[getPreferredInputDeviceForCapturerInfo()](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferredinputdeviceforcapturerinfo10-1)获取录制使用的设备。通过[AudioCapturerInfo](../harmonyos-references/arkts-apis-audio-i.md#audiocapturerinfo8).source参数区分不同的使用场景，例如SOURCE\_TYPE\_MIC表示普通录音，SOURCE\_TYPE\_VOICE\_COMMUNICATION表示语音通话。

   ```screen
   // Get default or preferred input device.
   getPreferredInputDevice() {
     this.audioRoutingManager.getPreferredInputDeviceForCapturerInfo(this.audioCapturerInfo,
       (err: BusinessError, audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
         if (err) {
           hilog.error(DOMAIN, 'testTag', '%{public}s',
             `Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
         } else {
           hilog.info(DOMAIN, 'testTag', '%{public}s',
             `Succeeded in getting preferred input device for capturer info, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
           if (audioDeviceDescriptors.length > 0) {
             AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, audioDeviceDescriptors[0].id);
           }
         }
       });
   }
   ```
7. 使用[on('preferredInputDeviceChangeForCapturerInfo')](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#onpreferredinputdevicechangeforcapturerinfo10)监听录制设备的变化，并在变化时弹框提示用户。

   ```screen
   // Monitor the status changes of preferred input device.
   watchPreferredInputDeviceChange() {
     try {
       this.audioRoutingManager.on('preferredInputDeviceChangeForCapturerInfo', this.audioCapturerInfo,
         (audioDeviceDescriptors: audio.AudioDeviceDescriptors) => {
           hilog.info(DOMAIN, 'testTag', '%{public}s',
             `Succeeded in using on function, AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}.`);
           if (audioDeviceDescriptors.length > 0) {
             AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, audioDeviceDescriptors[0].id);
           }
         });
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to preferredInputDeviceChangeForCapturerInfo. error: ${error.code}, ${error.message}`);
     }
   }
   ```

## 通过API切换输入设备

### 场景描述

音频流类型对输入设备的选择具有决定性影响，对于不同类型的音频流，系统会自动选择相应的输入设备。例如音频流类型是SOURCE\_TYPE\_MIC时，系统使用内置麦克风作为音频输入设备。如果默认的输入设备不符合使用需求，应用可以调用相关接口进行修改。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/YwkBTzbBR-KAoNygdcK38g/zh-cn_image_0000002545043447.gif "点击放大")

### 实现原理

使用[Interface (AudioSessionManager)](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)管理音频输入设备。通过该组件，可默认将蓝牙设备设为音频输入源，同时支持动态切换不同的媒体输入设备。

整体流程如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/8kateh0mSEurp-w2Ex3L9g/zh-cn_image_0000002545123443.png)

**说明** 

在语音通话场景下，由于输入设备跟随当前输出设备，因此使用AudioSessionManager的API无法切换输入设备。

### 开发步骤

1. 创建AudioSessionManager实例。

   ```screen
   private audioManager = audio.getAudioManager();
   private audioSessionManager: audio.AudioSessionManager = this.audioManager.getSessionManager();
   ```
2. 使用[setBluetoothAndNearlinkPreferredRecordCategory()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置优先选择蓝牙设备作为输入设备，当蓝牙设备上线后，会自动切换到蓝牙设备进行录制。通过[BluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-e.md#bluetoothandnearlinkpreferredrecordcategory21)设置蓝牙设备使用模式，当设置PREFERRED\_NONE时，取消优先选择蓝牙设备。

   ```screen
   // Set priority to select Bluetooth devices as input devices.
   async setBluetooth(category: number) {
     await this.audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(category)
       .then(() => {
         hilog.info(DOMAIN, 'testTag', '%{public}s',
           'Succeeded in doing setBluetoothAndNearlinkPreferredRecordCategory.' + category);
         AppStorage.setOrCreate(CommonConstants.BLUETOOTH_AND_NEARLINK_PREFERRED, category);
       })
       .catch((err: BusinessError) => {
         hilog.error(DOMAIN, 'testTag', '%{public}s',
           `Failed to setBluetoothAndNearlinkPreferredRecordCategory. error: ${err.code}, ${err.message}`);
       });
   }
   ```
3. 使用[selectMediaInputDevice()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)将用户选择的设备设置为输入设备。

   ```screen
   // Set input device.
   async setInputDevice(data: audio.AudioDeviceDescriptor) {
     this.audioSessionManager.selectMediaInputDevice(data).then(() => {
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'Succeeded in doing selectMediaInputDevice.');
       this.getSelectedMediaInputDevice();
     }).catch((err: BusinessError) => {
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to selectMediaInputDevice. error: ${err.code}, ${err.message}`);
     });
   }
   ```
4. 使用[on('currentInputDeviceChanged')](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#oncurrentinputdevicechanged21)监听输入设备变化，当输入设备切换成功后会触发该回调。

   ```screen
   // Monitor current input device change events.
   watchCurrentInputDeviceChanged() {
     hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentInputDeviceChangedCallback');
     let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
       hilog.info(DOMAIN, 'testTag', '%{public}s',
         `reason of currentInputDeviceChanged: ${currentInputDeviceChangedEvent.changeReason} `);
     };
     try {
       this.audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);
       hilog.info(DOMAIN, 'testTag', '%{public}s', 'currentInputDeviceChanged');
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to currentInputDeviceChangedCallback. error: ${error.code}, ${error.message}`);
     }
   }
   ```
5. 使用[getSelectedMediaInputDevice()](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#getselectedmediainputdevice21)获取当前设置的输入设备。

   ```screen
   // Get the currently selected input device.
   getSelectedMediaInputDevice() {
     try {
       let device: audio.AudioDeviceDescriptor = this.audioSessionManager.getSelectedMediaInputDevice();
       hilog.info(DOMAIN, 'testTag', '%{public}s',
         'Succeeded in doing getSelectedMediaInputDevice.' + JSON.stringify(device) + ',' + device?.id);
       AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, device.id);
     } catch (err) {
       let error = err as BusinessError;
       hilog.error(DOMAIN, 'testTag', '%{public}s',
         `Failed to getSelectedMediaInputDevice. error: ${error.code}, ${error.message}`);
     }
   }
   ```

## 通过系统组件切换输入设备

### 场景描述

在PC设备上，通过系统提供的录音设备选择组件[AVInputCastPicker](../harmonyos-references/ohos-multimedia-avinputcastpicker.md#avinputcastpicker)切换音频输入设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/WYRg668vTniorfQ8tGhfiQ/zh-cn_image_0000002513443564.gif "点击放大")

### 实现原理

系统提供录音设备选择组件AVInputCastPicker，作为音频输入设备发现与连接的统一入口。点击组件图标将弹出可选设备列表，从列表中选择设备后，即可切换至相应设备。

### 开发步骤

1. 在需要切换设备的界面创建AVInputCastPicker组件。

   ```screen
   @Builder
   customPickerBuilder() {
     Image($r('app.media.devices'))
       .width('100%')
       .height('100%')
   }
   ```

   ```screen
   AVInputCastPicker({
     customPicker: () => this.customPickerBuilder(),
     onStateChange: this.onStateChange
   })
   ```
2. 手动点击AVInputCastPicker组件，并在弹框中选择目标设备，即可切换输入设备。

## 响应音频流输入设备变更

### 场景描述

当系统因音频输入设备上下线、用户主动切换设备、设备抢占或设备选择策略变更等导致音频流输入设备变更时，应用可以根据需要做出对应的处理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/XxGFR_GkRYSwc1_-wpOBKg/zh-cn_image_0000002513603474.gif "点击放大")

### 实现原理

AudioCapturer的[on('inputDeviceChange')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#oninputdevicechange11)可以监听音频流输入设备变化并返回切换后的设备信息。应用可以根据切换后的新设备做对应的处理。

### 开发步骤

使用[on('inputDeviceChange')](../harmonyos-references/arkts-apis-audio-audiocapturer.md#oninputdevicechange11)监听到音频流输入设备变化时，显示新设备信息。

```screen
// Monitor the status changes of input device.
watchInputDeviceChange() {
  try {
    // Use the inputDeviceChange method of audioCapturer to listen for changes in input devices.
    this.audioCapturer?.on('inputDeviceChange', (deviceChangeInfo: audio.AudioDeviceDescriptors) => {
      hilog.info(DOMAIN, 'testTag', '%{public}s', `inputDevice id: ${deviceChangeInfo[0].id}`);
      if (deviceChangeInfo.length > 0) {
        AppStorage.setOrCreate(CommonConstants.SELECTED_DEVICE_ID, deviceChangeInfo[0].id);
      }
    });
  } catch (err) {
    // ...
  }
}
```

## 常见问题

### 确定麦克风是否能够进行录制，判断麦克风是否处于被占用的状态

**解决方案**

API20提供了[isRecordingAvailable()](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)接口，通过设置输入参数AudioCapturerInfo.source为Audio.SourceType.SOURCE\_TYPE\_MIC，然后根据返回值判断麦克风状态。如果返回true，表明可以使用麦克风进行录制；如果返回false，表明麦克风可能已被占用。

API20之前，可以初始化一个AudioCapturer对象并开始录音，如果成功，说明可以使用麦克风进行录制；如果失败，表明麦克风可能已被占用。

## 示例代码

* [实现音频输入设备管理功能](https://gitcode.com/HarmonyOS_Samples/managing-audio-input-devices)
