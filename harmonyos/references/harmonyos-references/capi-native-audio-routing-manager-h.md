---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-routing-manager-h
title: native_audio_routing_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_routing_manager.h
category: harmonyos-references
scraped_at: 2026-09-05T06:19:50+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:0b37e375de24fc0654343e86a9125f2f54f9c95738b00200ec1e00dbc7519425
---

## 概述

声明与音频路由管理器相关的接口。

包含获取音频路由管理器、设备连接状态发生变化时的注册和注销功能以及释放存储设备信息的指针数组。

**引用文件：** <ohaudio/native\_audio\_routing\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) | OH\_AudioRoutingManager | 声明音频路由管理器。用于管理音频路由相关功能。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef int32\_t (\*OH\_AudioRoutingManager\_OnDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) | OH\_AudioRoutingManager\_OnDeviceChangedCallback | 此函数指针将指向用于返回更改的音频设备描述符的回调函数，可能返回多个音频设备描述符。 |
| [typedef int32\_t (\*OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredoutputdevicechangedcallback) | OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback | 此函数指针指向用于返回优先级最高的输出设备描述符的回调函数，该回调函数会返回一个或多个音频设备描述符。 |
| [typedef int32\_t (\*OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredinputdevicechangedcallback) | OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback | 此函数指针指向用于返回优先级最高的输入设备描述符的回调函数，该回调函数会返回一个或多个音频设备描述符。 |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioRoutingManager(OH\_AudioRoutingManager \*\*audioRoutingManager)](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager) | - | 获取音频路由管理器实例。  使用音频路由管理器相关功能，首先需要获取音频路由管理器实例。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) | - | 根据输入的deviceFlag查询可用的设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetAvailableDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getavailabledevices) | - | 获取音频可选设备列表。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredOutputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_Usage streamUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getpreferredoutputdevice) | - | 根据音频输出流的使用场景，获取优先级最高的输出设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredInputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_SourceType sourceType, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getpreferredinputdevice) | - | 根据音频输入流的使用场景，获取优先级最高的输入设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerdevicechangecallback) | - | 注册音频路由管理器的设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterdevicechangecallback) | - | 取消注册音频路由管理器的设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterPreferredOutputDevicesChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_Usage streamUsage, OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredoutputdeviceschangecallback) | - | 注册音频路由管理器的最高优先级输出设备变更回调。当指定播放流类型的最高优先级输出设备发生变化时，已注册的客户端将收到回调。  为避免资源浪费或其他异常情况，当应用程序不再需要此回调时，必须通过调用[OH\_AudioRoutingManager\_UnregisterPreferredOutputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredoutputdeviceschangecallback)来释放回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterPreferredOutputDevicesChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredoutputdeviceschangecallback) | - | 取消通过[OH\_AudioRoutingManager\_RegisterPreferredOutputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredoutputdeviceschangecallback)注册的音频路由管理器最高优先级输出设备变更回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterPreferredInputDevicesChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_SourceType sourceType, OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredinputdeviceschangecallback) | - | 注册音频路由管理器的最高优先级输入设备变更回调。当指定播放流类型的最高优先级输入设备发生变化时，已注册的客户端将收到回调。  为避免资源浪费或其他异常情况，当应用程序不再需要此回调时，必须通过调用[OH\_AudioRoutingManager\_UnregisterPreferredInputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredinputdeviceschangecallback)来释放回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterPreferredInputDevicesChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredinputdeviceschangecallback) | - | 取消通过[OH\_AudioRoutingManager\_RegisterPreferredInputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredinputdeviceschangecallback)注册的音频路由管理器最高优先级输入设备变更回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_ReleaseDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices) | - | 释放音频设备描述符数组对象。 |
| [typedef void (\*OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray, OH\_AudioDevice\_BlockStatus status, void \*userData)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback) | OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback | 此函数指针将指向用于返回音频设备堵塞状态的回调函数，可能返回多个音频设备描述符。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_IsMicBlockDetectionSupported(OH\_AudioRoutingManager \*audioRoutingManager, bool \*supported)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ismicblockdetectionsupported) | - | 查询当前设备是否支持麦克风堵塞状态检测。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_SetMicBlockStatusCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback callback, void \*userData)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_setmicblockstatuscallback) | - | 设置麦克风是否堵塞状态回调。  在使用此功能之前，应查询当前设备是否支持检测。仅当应用正在使用麦克风录音且麦克风堵塞状态发生改变时，才会收到回调。目前此检测功能仅支持位于本地设备上的麦克风。 |

## 函数说明

### OH\_AudioRoutingManager\_OnDeviceChangedCallback()

```c
typedef int32_t (*OH_AudioRoutingManager_OnDeviceChangedCallback)(OH_AudioDevice_ChangeType type, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray
)
```

**描述**

此函数指针将指向用于返回更改的音频设备描述符的回调函数，可能返回多个音频设备描述符。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype) type | 设备连接状态类型。 [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype)已连接或断开。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组，指向[OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md)设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices) 来释放DeviceDescriptor数组。 |

### OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback()

```c
typedef int32_t (*OH_AudioRoutingManager_OnPreferredOutputDeviceChangedCallback)(OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

此函数指针指向用于返回优先级最高的输出设备描述符的回调函数，该回调函数会返回一个或多个音频设备描述符。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组。  设置音频设备描述符值的指针变量，不能单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

### OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback()

```c
typedef int32_t (*OH_AudioRoutingManager_OnPreferredInputDeviceChangedCallback)(OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

此函数指针指向用于返回优先级最高的输入设备描述符的回调函数，该回调函数会返回一个或多个音频设备描述符。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组。  设置音频设备描述符值的指针变量，不能单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices) 来释放DeviceDescriptor数组。 |

### OH\_AudioManager\_GetAudioRoutingManager()

```c
OH_AudioCommon_Result OH_AudioManager_GetAudioRoutingManager(OH_AudioRoutingManager **audioRoutingManager)
```

**描述**

获取音频路由管理器实例。

使用音频路由管理器相关功能，首先需要获取音频路由管理器实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*\*audioRoutingManager | 指向OH\_AudioRoutingManager指针的地址，用于接收获取的音频路由管理器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。 |

### OH\_AudioRoutingManager\_GetDevices()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_GetDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Flag deviceFlag, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据输入的deviceFlag查询可用的设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioDevice\_Flag](capi-native-audio-device-base-h.md#oh_audiodevice_flag) deviceFlag | 音频设备标志，用于选择目标设备的滤波器参数。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数deviceFlag无效；  3. 参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetAvailableDevices()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_GetAvailableDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Usage deviceUsage, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

获取音频可选设备列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage) deviceUsage | 指向[OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage)用于设置要获取的设备种类。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数deviceUsage无效；  3. 参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetPreferredOutputDevice()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_GetPreferredOutputDevice(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_Usage streamUsage, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据音频输出流的使用场景，获取优先级最高的输出设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) streamUsage | 指向[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)用于设置音频输出流的使用场景。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数streamUsage无效；  3. 参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetPreferredInputDevice()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_GetPreferredInputDevice(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_SourceType sourceType, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据音频输入流的使用场景，获取优先级最高的输入设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype) sourceType | 指向[OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)用于设置音频输入流的使用场景。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数sourceType无效；  3. 参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_RegisterDeviceChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_RegisterDeviceChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Flag deviceFlag, OH_AudioRoutingManager_OnDeviceChangedCallback callback)
```

**描述**

注册音频路由管理器的设备更改回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioDevice\_Flag](capi-native-audio-device-base-h.md#oh_audiodevice_flag) deviceFlag | 音频设备标志，用来注册回调。 |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) callback | 函数指针将指向用于返回更改的音频设备描述符的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数deviceFlag无效；  3. 参数callback为nullptr。 |

### OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_UnregisterDeviceChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnDeviceChangedCallback callback)
```

**描述**

取消注册音频路由管理器的设备更改回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) callback | 函数指针将指向用于返回更改的音频设备描述符的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数callback为nullptr。 |

### OH\_AudioRoutingManager\_RegisterPreferredOutputDevicesChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_RegisterPreferredOutputDevicesChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_Usage streamUsage, OH_AudioRoutingManager_OnPreferredOutputDeviceChangedCallback callback)
```

**描述**

注册音频路由管理器的最高优先级输出设备变更回调。当指定播放流类型的最高优先级输出设备发生变化时，已注册的客户端将收到回调。

为避免资源浪费或其他异常情况，当应用程序不再需要此回调时，必须通过调用[OH\_AudioRoutingManager\_UnregisterPreferredOutputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredoutputdeviceschangecallback) 来释放回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) streamUsage | 指向OH\_AudioStream\_Usage，用于注册最高优先级输出设备变化事件的过滤参数设置。 |
| [OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredoutputdevicechangedcallback) callback | 指向OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback，用于接收最高优先级输出设备变化事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数校验失败。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频客户端在调用音频服务的过程中遇到系统错误，导致调用失败。 |

### OH\_AudioRoutingManager\_UnregisterPreferredOutputDevicesChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_UnregisterPreferredOutputDevicesChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnPreferredOutputDeviceChangedCallback callback)
```

**描述**

取消通过[OH\_AudioRoutingManager\_RegisterPreferredOutputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredoutputdeviceschangecallback) 注册的音频路由管理器最高优先级输出设备变更回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取。 |
| [OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredoutputdevicechangedcallback) callback | 指向OH\_AudioRoutingManager\_OnPreferredOutputDeviceChangedCallback，用于接收最高优先级输出设备变化事件。传入nullptr时，系统将取消所有已注册的最高优先级输出设备变化回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数校验失败。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频客户端在调用音频服务的过程中遇到系统错误，导致调用失败。 |

### OH\_AudioRoutingManager\_RegisterPreferredInputDevicesChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_RegisterPreferredInputDevicesChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_SourceType sourceType, OH_AudioRoutingManager_OnPreferredInputDeviceChangedCallback callback)
```

**描述**

注册音频路由管理器的最高优先级输入设备变更回调。当指定播放流类型的最高优先级输入设备发生变化时，已注册的客户端将收到回调。

为避免资源浪费或其他异常情况，当应用程序不再需要此回调时，必须通过调用[OH\_AudioRoutingManager\_UnregisterPreferredInputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterpreferredinputdeviceschangecallback) 来释放回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype) sourceType | 指向OH\_AudioStream\_SourceType，用于注册最高优先级输入设备变化事件的过滤参数设置。 |
| [OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredinputdevicechangedcallback) callback | 指向OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback，用于接收最高优先级输入设备变化事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数校验失败。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频客户端在调用音频服务的过程中遇到系统错误，导致调用失败。 |

### OH\_AudioRoutingManager\_UnregisterPreferredInputDevicesChangeCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_UnregisterPreferredInputDevicesChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnPreferredInputDeviceChangedCallback callback)
```

**描述**

取消通过[OH\_AudioRoutingManager\_RegisterPreferredInputDevicesChangeCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerpreferredinputdeviceschangecallback) 注册的音频路由管理器最高优先级输入设备变更回调。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取。 |
| [OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_onpreferredinputdevicechangedcallback) callback | 指向OH\_AudioRoutingManager\_OnPreferredInputDeviceChangedCallback，用于接收最高优先级输入设备变化事件。传入nullptr时，系统将取消所有已注册的最高优先级输入设备变化回调。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数校验失败。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：音频客户端在调用音频服务的过程中遇到系统错误，导致调用失败。 |

### OH\_AudioRoutingManager\_ReleaseDevices()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_ReleaseDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

释放音频设备描述符数组对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组应当被释放，获取请调用[OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices)接口。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数audioDeviceDescriptorArray为nullptr。 |

### OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback()

```c
typedef void (*OH_AudioRoutingManager_OnDeviceBlockStatusCallback)(OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray, OH_AudioDevice_BlockStatus status, void *userData)
```

**描述**

此函数指针将指向用于返回音频设备堵塞状态的回调函数，可能返回多个音频设备描述符。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组。由系统回调传入，调用者需调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)进行释放。 |
| [OH\_AudioDevice\_BlockStatus](capi-native-audio-device-base-h.md#oh_audiodevice_blockstatus) status | 音频设备的堵塞状态。 |
| void \*userData | 用户自定义数据指针。 |

### OH\_AudioRoutingManager\_IsMicBlockDetectionSupported()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_IsMicBlockDetectionSupported(OH_AudioRoutingManager *audioRoutingManager, bool *supported)
```

**描述**

查询当前设备是否支持麦克风堵塞状态检测。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| bool \*supported | 查询当前设备是否支持麦克风堵塞状态检测的结果。true表示支持，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数supported为nullptr。 |

### OH\_AudioRoutingManager\_SetMicBlockStatusCallback()

```c
OH_AudioCommon_Result OH_AudioRoutingManager_SetMicBlockStatusCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnDeviceBlockStatusCallback callback, void *userData)
```

**描述**

设置麦克风是否堵塞状态回调。

在使用此功能之前，应查询当前设备是否支持检测。仅当应用正在使用麦克风录音且麦克风堵塞状态发生改变时，才会收到回调。目前此检测功能仅支持位于本地设备上的麦克风。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 指向通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取的音频路由管理器实例。 |
| [OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback) callback | 函数指针将指向用于返回接收设备麦克风堵塞状态[OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback)。 |
| void \*userData | 用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数callback为nullptr。 |
