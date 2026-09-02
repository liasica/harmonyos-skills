---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-input-device-switcher
title: 实现音频输入设备路由切换
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 实现音频输入设备路由切换
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ae41cb293b1969132c26cccd746bdd967b960ab37e397afaba3a3882f6f1af1b
---

从API version 21开始，支持音频输入设备路由切换。

当应用进行音频输入时，系统会根据音频流类型选择对应的输入设备（SOURCE\_TYPE\_MIC：内置MIC录音；SOURCE\_TYPE\_VOICE\_COMMUNICATION：跟随当前输出设备）。若默认输入设备不满足应用需求，应用可通过[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)或[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)实现音频输入设备路由切换。

从API版本26.0.0开始，PC/2in1设备还支持基于[AudioDeviceEnhanceManager](../harmonyos-references/arkts-apis-audio-audiodeviceenhancemanager.md)和[native\_audio\_device\_enhance\_manager.h](../harmonyos-references/capi-native-audio-device-enhance-manager-h.md)的输入设备切换能力，应用可按应用级或音频流级精确指定输入设备，满足多设备场景下对收音来源的控制需求。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRoutingAndVolumeSample)。其中，[PC/2in1设备输入设备切换](audio-input-device-switcher.md#pc2in1设备输入设备切换)的完整示例请参见[ArkTS示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioEnhanceDeviceSampleJS)和[C/C++示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioEnhanceDeviceSampleC)。

## 选择使用蓝牙或者星闪设备进行录音

应用可使用AudioSessionManager的[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置应用程序的输入设备选择偏好，当蓝牙或星闪设备上线时生效。

**说明** 

通话场景下，如果蓝牙或星闪设备在线，系统默认使用蓝牙或星闪设备作为输入设备。

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioManager = audio.getAudioManager();
let audioSessionManager = audioManager.getSessionManager();
// ...

  audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(audio.BluetoothAndNearlinkPreferredRecordCategory.
    PREFERRED_DEFAULT).then(() => {
    console.info('Succeeded in setting bluetooth and nearlink preferred record category.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to set bluetooth and nearlink preferred record category. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

## 选择任意设备进行录音

应用可使用AudioSessionManager的[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)选择输入设备。

**说明** 

通话场景下，输入设备跟随当前输出设备，此时其他与通话并发的录音流也会跟随通话输入设备。

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let audioManager = audio.getAudioManager();
let audioSessionManager = audioManager.getSessionManager();
// ...

  try {
    // 监听当前输入设备变化事件，当选择输入设备成功后会触发该回调。
    audioSessionManager.on('currentInputDeviceChanged', (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
      console.info(`Succeeded in using on function. CurrentInputDeviceChangedEvent: ${JSON.stringify(currentInputDeviceChangedEvent)}`);
      // ...
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  try {
    // 监听音频可选输入设备连接状态变化事件，当有输入设备上下线时会收到回调通知。
    audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, (deviceChanged: audio.DeviceChangeAction) => {
      console.info(`Succeeded in using on function. DeviceChangeAction: ${JSON.stringify(deviceChanged)}`);
      // ...
    });
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  try {
    // 获取当前可选的音频输入设备列表。
    let data = audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_INPUT_DEVICES);
    console.info(`Succeeded in getting available devices. AudioDeviceDescriptors: ${JSON.stringify(data)}`);
    // 当前可选音频输入设备列表不为空时，可进行选择。
    if (data[1] || data[0]) {
      // 选择输入设备。
      audioSessionManager.selectMediaInputDevice(data[1] ? data[1] : data[0]).then(() => {
        console.info('Succeeded in selecting media input device.');
        // ...
      }).catch((err: BusinessError) => {
        console.error(`Failed to select media input device. Code: ${err.code}, message: ${err.message}`);
        // ...
      });
    }
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to getAvailableDevices. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  try {
    // 可通过该接口查询选择输入设备是否成功。
    let device = audioSessionManager.getSelectedMediaInputDevice();
    console.info(`Succeeded in getting selected media input device. Device: ${JSON.stringify(device)}`);
    // ...
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to get selected media input device. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
  // ...

  // 清空通过selectMediaInputDevice选择的输入设备。
  audioSessionManager.clearSelectedMediaInputDevice().then(() => {
    console.info('Succeeded in clearing selected media input device.');
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to clear selected media input device. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

## PC/2in1设备输入设备切换

PC/2in1设备经常存在多路输入设备可用（如内置麦克风、USB/蓝牙耳机麦克风等），系统默认的设备选择策略可能无法满足应用在各种场景下的输入需求。通过本能力，应用可按**应用级**或**音频流级**精确指定输入设备，满足多设备场景下对收音来源的控制需求。

### 查询能力是否支持

使用前需先通过[isEnhancedRoutingSupported](../harmonyos-references/arkts-apis-audio-audiodeviceenhancemanager.md#isenhancedroutingsupported)或[OH\_AudioDeviceEnhanceManager\_IsEnhancedRoutingSupported](../harmonyos-references/capi-native-audio-device-enhance-manager-h.md#oh_audiodeviceenhancemanager_isenhancedroutingsupported)查询系统是否支持该能力，不支持时调用输入设备切换接口不生效，将继续使用当前输入设备。

ArkTS示例：

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...
  let audioManager = audio.getAudioManager();
  let audioDeviceEnhanceManager: audio.AudioDeviceEnhanceManager = audioManager.getDeviceEnhanceManager();
  // 查询系统是否支持当前管理器提供的增强路由能力。
  let isSupported: boolean = audioDeviceEnhanceManager.isEnhancedRoutingSupported();
  console.info(`Succeeded in querying whether enhanced routing is supported. Result: ${isSupported}.`);
```

C/C++示例：

使用前需添加头文件：

```
#include <ohaudio/native_audio_device_enhance_manager.h>
#include <ohaudio/native_audio_routing_manager.h>
#include <ohaudio/native_audio_device_base.h>
#include <ohaudio/native_audiocapturer.h>
#include <ohaudio/native_audiorenderer.h>
#include <ohaudio/native_audiostreambuilder.h>
```

```
napi_value IsEnhancedRoutingSupported(napi_env env, napi_callback_info info)
{
    OH_AudioDeviceEnhanceManager *enhanceManager = nullptr;
    OH_AudioCommon_Result result = OH_AudioManager_GetAudioDeviceEnhanceManager(&enhanceManager);
    bool isSupported = false;
    // 查询系统是否支持当前管理器提供的增强路由能力。
    result = OH_AudioDeviceEnhanceManager_IsEnhancedRoutingSupported(enhanceManager, &isSupported);
    // ...
}
```

### 切换输入设备

输入设备切换支持应用级和音频流级两种粒度，应用级对应用下所有录制流生效，音频流级仅对指定录制流生效，且音频流级的优先级高于应用级。

**说明** 

若某条录制流已通过音频流级接口指定了专属输入设备，则该流使用其专属输入设备，应用内其他录制流仍使用应用级设置的输入设备或系统默认输入设备。

ArkTS示例：

* **应用级：** 通过[selectInputDevice](../harmonyos-references/arkts-apis-audio-audiodeviceenhancemanager.md#selectinputdevice)选择指定的输入设备，设置成功后对应用下创建的所有录制流生效。

  ```typescript
  import { audio } from '@kit.AudioKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...
    let audioManager = audio.getAudioManager();
    let audioDeviceEnhanceManager: audio.AudioDeviceEnhanceManager = audioManager.getDeviceEnhanceManager();
    // 为应用选择输入设备，此处device可通过ArkTS完整示例查看获取方式。
    audioDeviceEnhanceManager.selectInputDevice(device).then(() => {
      console.info('Succeeded in selecting input device.');
      // ...
    }).catch((err: BusinessError) => {
      console.error(`Failed to select input device. Code: ${err.code}, message: ${err.message}`);
      // ...
    });
  ```
* **音频流级：** 通过[selectInputDeviceForAudioCapturer](../harmonyos-references/arkts-apis-audio-audiodeviceenhancemanager.md#selectinputdeviceforaudiocapturer)为指定音频录制流选择输入设备，设置成功后仅对该录制流生效。

  ```typescript
  import { audio } from '@kit.AudioKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...
    let audioManager = audio.getAudioManager();
    let audioDeviceEnhanceManager: audio.AudioDeviceEnhanceManager = audioManager.getDeviceEnhanceManager();
    // 为指定音频录制流设置首选输入设备，此处capturer和inputDevice可通过ArkTS完整示例查看获取方式。
    audioDeviceEnhanceManager.selectInputDeviceForAudioCapturer(capturer, inputDevice).then(() => {
      console.info('Succeeded in selecting input device for audio capturer.');
      // ...
    }).catch((err: BusinessError) => {
      console.error(`Failed to select input device for audio capturer. Code: ${err.code}, message: ${err.message}`);
      // ...
    });
  ```

C/C++示例：

* **应用级：** 通过[OH\_AudioDeviceEnhanceManager\_SelectInputDevice](../harmonyos-references/capi-native-audio-device-enhance-manager-h.md#oh_audiodeviceenhancemanager_selectinputdevice)选择指定的输入设备。

  ```
  // 获取音频设备增强管理器。
  static OH_AudioDeviceEnhanceManager *GetEnhanceManager(std::string &errorMsg)
  {
      OH_AudioDeviceEnhanceManager *manager = nullptr;
      OH_AudioCommon_Result result = OH_AudioManager_GetAudioDeviceEnhanceManager(&manager);
      if (result != AUDIOCOMMON_RESULT_SUCCESS || manager == nullptr) {
          errorMsg = "获取AudioDeviceEnhanceManager失败";
          return nullptr;
      }
      bool isSupported = false;
      OH_AudioDeviceEnhanceManager_IsEnhancedRoutingSupported(manager, &isSupported);
      if (!isSupported) {
          errorMsg = "Enhanced routing不支持，该功能不会生效";
          return nullptr;
      }
      return manager;
  }

  struct DeviceSearchResult {
      OH_AudioRoutingManager *routingManager;
      OH_AudioDeviceDescriptorArray *deviceArray;
      OH_AudioDeviceDescriptor *targetDescriptor;
  };

  // 获取音频可选设备。
  static DeviceSearchResult FindDescriptorById(int32_t deviceId, OH_AudioDevice_Usage usage)
  {
      DeviceSearchResult search = {nullptr, nullptr, nullptr};
      OH_AudioManager_GetAudioRoutingManager(&search.routingManager);
      OH_AudioRoutingManager_GetAvailableDevices(search.routingManager, usage, &search.deviceArray);
      if (search.deviceArray == nullptr) {
          return search;
      }
      for (uint32_t i = 0; i < search.deviceArray->size; i++) {
          uint32_t id = 0;
          OH_AudioDeviceDescriptor_GetDeviceId(search.deviceArray->descriptors[i], &id);
          if (id == static_cast<uint32_t>(deviceId)) {
              search.targetDescriptor = search.deviceArray->descriptors[i];
              break;
          }
      }
      return search;
  }

  static void ReleaseDeviceSearch(DeviceSearchResult &search)
  {
      if (search.routingManager != nullptr && search.deviceArray != nullptr) {
          OH_AudioRoutingManager_ReleaseDevices(search.routingManager, search.deviceArray);
      }
  }
  // ...
  // 为应用选择输入设备。
  napi_value SelectInputDevice(napi_env env, napi_callback_info info)
  {
      int32_t deviceId = 0;
      ParseInt32Arg(env, info, deviceId);
      std::string errorMsg;
      OH_AudioDeviceEnhanceManager *enhanceManager = GetEnhanceManager(errorMsg);
      // ...

      DeviceSearchResult search = FindDescriptorById(deviceId, AUDIO_DEVICE_USAGE_MEDIA_INPUT);
      OH_AudioCommon_Result result = OH_AudioDeviceEnhanceManager_SelectInputDevice(
          enhanceManager, search.targetDescriptor);
      ReleaseDeviceSearch(search);
      // ...
  }
  ```
* **音频流级：** 通过[OH\_AudioDeviceEnhanceManager\_SelectInputDeviceForAudioCapturer](../harmonyos-references/capi-native-audio-device-enhance-manager-h.md#oh_audiodeviceenhancemanager_selectinputdeviceforaudiocapturer)为指定音频录制流选择输入设备。

  ```
  // 获取音频设备增强管理器。
  static OH_AudioDeviceEnhanceManager *GetEnhanceManager(std::string &errorMsg)
  {
      OH_AudioDeviceEnhanceManager *manager = nullptr;
      OH_AudioCommon_Result result = OH_AudioManager_GetAudioDeviceEnhanceManager(&manager);
      if (result != AUDIOCOMMON_RESULT_SUCCESS || manager == nullptr) {
          errorMsg = "获取AudioDeviceEnhanceManager失败";
          return nullptr;
      }
      bool isSupported = false;
      OH_AudioDeviceEnhanceManager_IsEnhancedRoutingSupported(manager, &isSupported);
      if (!isSupported) {
          errorMsg = "Enhanced routing不支持，该功能不会生效";
          return nullptr;
      }
      return manager;
  }

  struct DeviceSearchResult {
      OH_AudioRoutingManager *routingManager;
      OH_AudioDeviceDescriptorArray *deviceArray;
      OH_AudioDeviceDescriptor *targetDescriptor;
  };

  // 获取音频可选设备。
  static DeviceSearchResult FindDescriptorById(int32_t deviceId, OH_AudioDevice_Usage usage)
  {
      DeviceSearchResult search = {nullptr, nullptr, nullptr};
      OH_AudioManager_GetAudioRoutingManager(&search.routingManager);
      OH_AudioRoutingManager_GetAvailableDevices(search.routingManager, usage, &search.deviceArray);
      if (search.deviceArray == nullptr) {
          return search;
      }
      for (uint32_t i = 0; i < search.deviceArray->size; i++) {
          uint32_t id = 0;
          OH_AudioDeviceDescriptor_GetDeviceId(search.deviceArray->descriptors[i], &id);
          if (id == static_cast<uint32_t>(deviceId)) {
              search.targetDescriptor = search.deviceArray->descriptors[i];
              break;
          }
      }
      return search;
  }

  static void ReleaseDeviceSearch(DeviceSearchResult &search)
  {
      if (search.routingManager != nullptr && search.deviceArray != nullptr) {
          OH_AudioRoutingManager_ReleaseDevices(search.routingManager, search.deviceArray);
      }
  }
  // ...
  // 创建音频采集器。
  static OH_AudioCapturer *CreateAudioCapturer()
  {
      OH_AudioStreamBuilder *builder = nullptr;
      if (OH_AudioStreamBuilder_Create(&builder, AUDIOSTREAM_TYPE_CAPTURER) != AUDIOSTREAM_SUCCESS) {
          return nullptr;
      }
      OH_AudioStreamBuilder_SetSamplingRate(builder, SAMPLE_RATE_48K);
      OH_AudioStreamBuilder_SetChannelCount(builder, CHANNEL_COUNT_STEREO);
      OH_AudioStreamBuilder_SetSampleFormat(builder, AUDIOSTREAM_SAMPLE_S16LE);
      OH_AudioStreamBuilder_SetEncodingType(builder, AUDIOSTREAM_ENCODING_TYPE_RAW);
      OH_AudioStreamBuilder_SetCapturerInfo(builder, AUDIOSTREAM_SOURCE_TYPE_VOICE_COMMUNICATION);
      OH_AudioCapturer *capturer = nullptr;
      OH_AudioStreamBuilder_GenerateCapturer(builder, &capturer);
      OH_AudioStreamBuilder_Destroy(builder);
      return capturer;
  }

  // ...
  // 为指定音频播放流设置首选输入设备。
  napi_value SelectInputDeviceForAudioCapturer(napi_env env, napi_callback_info info)
  {
      int32_t deviceId = 0;
      ParseInt32Arg(env, info, deviceId);
      std::string errorMsg;
      OH_AudioDeviceEnhanceManager *enhanceManager = GetEnhanceManager(errorMsg);
      // ...
      OH_AudioCapturer *capturer = CreateAudioCapturer();
      // ...

      DeviceSearchResult search = FindDescriptorById(deviceId, AUDIO_DEVICE_USAGE_MEDIA_INPUT);
      OH_AudioCommon_Result result = OH_AudioDeviceEnhanceManager_SelectInputDeviceForAudioCapturer(
          enhanceManager, capturer, search.targetDescriptor);
      ReleaseDeviceSearch(search);
      // ...
  }
  ```
