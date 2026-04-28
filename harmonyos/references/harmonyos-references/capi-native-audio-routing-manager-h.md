---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-routing-manager-h
title: native_audio_routing_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_routing_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6ee91dccb3b266ce6b9027c2bf20f70e069ce28ae78905d9ff5e563d57e1e1d1
---

## 概述

PhonePC/2in1TabletTVWearable

声明与音频路由管理器相关的接口。

包含用于创建audioRoutingManager，设备连接状态发生变化时的注册和注销功能，以及存储设备信息的指针数组的释放。

**引用文件：** <ohaudio/native\_audio\_routing\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) | OH\_AudioRoutingManager | 声明音频路由管理器。用于管理音频路由相关功能。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef int32\_t (\*OH\_AudioRoutingManager\_OnDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) | OH\_AudioRoutingManager\_OnDeviceChangedCallback | 此函数指针将指向用于返回更改的音频设备描述符的回调函数，可能返回多个音频设备描述符。 |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioRoutingManager(OH\_AudioRoutingManager \*\*audioRoutingManager)](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager) | - | 查询音频路由管理器句柄，该句柄应设置为路由相关函数中的第一个参数。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices) | - | 根据输入的deviceFlag查询可用的设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetAvailableDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getavailabledevices) | - | 获取音频可选设备列表。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredOutputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_Usage streamUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getpreferredoutputdevice) | - | 根据音频输出流的使用场景，获取优先级最高的输出设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_GetPreferredInputDevice(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioStream\_SourceType sourceType, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getpreferredinputdevice) | - | 根据音频输入流的使用场景，获取优先级最高的输入设备。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_RegisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDevice\_Flag deviceFlag, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_registerdevicechangecallback) | - | 注册音频路由管理器的设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceChangedCallback callback)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_unregisterdevicechangecallback) | - | 取消注册音频路由管理器的设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_ReleaseDevices(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices) | - | 释放音频设备描述符数组对象。 |
| [typedef void (\*OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback)(OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray, OH\_AudioDevice\_BlockStatus status, void \*userData)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback) | OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback | 此函数指针将指向用于返回音频设备堵塞状态的回调函数，可能返回多个音频设备描述符。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_IsMicBlockDetectionSupported(OH\_AudioRoutingManager \*audioRoutingManager, bool \*supported)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ismicblockdetectionsupported) | - | 查询当前设备是否支持麦克风堵塞状态检测。 |
| [OH\_AudioCommon\_Result OH\_AudioRoutingManager\_SetMicBlockStatusCallback(OH\_AudioRoutingManager \*audioRoutingManager, OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback callback, void \*userData)](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_setmicblockstatuscallback) | - | 设置麦克风是否堵塞状态回调。  在使用此功能之前，用户应查询当前设备是否支持检测，应用只有在使用麦克风录音时，并且所使用的麦克风的堵塞状态发生改变，才会收到回调，目前此检测功能仅支持麦克风位于本地设备上。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioRoutingManager\_OnDeviceChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AudioRoutingManager_OnDeviceChangedCallback)(OH_AudioDevice_ChangeType type, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray
2. )
```

**描述**

此函数指针将指向用于返回更改的音频设备描述符的回调函数，可能返回多个音频设备描述符。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype) type | 设备连接状态类型。 [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype) 已连接或断开。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组，指向[OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md)设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

### OH\_AudioManager\_GetAudioRoutingManager()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioManager_GetAudioRoutingManager(OH_AudioRoutingManager **audioRoutingManager)
```

**描述**

查询音频路由管理器句柄，该句柄应设置为路由相关函数中的第一个参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*\*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。 |

### OH\_AudioRoutingManager\_GetDevices()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_GetDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Flag deviceFlag, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据输入的deviceFlag查询可用的设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioDevice\_Flag](capi-native-audio-device-base-h.md#oh_audiodevice_flag) deviceFlag | 音频设备标志，用于选择目标设备的滤波器参数。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数deviceFlag无效；  3. 参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetAvailableDevices()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_GetAvailableDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Usage deviceUsage, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

获取音频可选设备列表。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage) deviceUsage | 指向[OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage)用于设置要获取的设备种类。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioRoutingManager为nullptr；  2.参数deviceUsage无效;  3.参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetPreferredOutputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_GetPreferredOutputDevice(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_Usage streamUsage, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据音频输出流的使用场景，获取优先级最高的输出设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) streamUsage | 指向[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)用于设置音频输出流的使用场景。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioRoutingManager为nullptr;  2.参数streamUsage无效;  3.参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_GetPreferredInputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_GetPreferredInputDevice(OH_AudioRoutingManager *audioRoutingManager, OH_AudioStream_SourceType sourceType, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

根据音频输入流的使用场景，获取优先级最高的输入设备。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype) sourceType | 指向[OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)用于设置音频输入流的使用场景。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioRoutingManager为nullptr;  2.参数sourceType无效;  3.参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AudioRoutingManager\_RegisterDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_RegisterDeviceChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDevice_Flag deviceFlag, OH_AudioRoutingManager_OnDeviceChangedCallback callback)
```

**描述**

注册音频路由管理器的设备更改回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioDevice\_Flag](capi-native-audio-device-base-h.md#oh_audiodevice_flag) deviceFlag | 音频设备标志，用来注册回调。 |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) callback | 函数指针将指向用于返回更改的音频设备描述符的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数deviceFlag无效；  3. 参数callback为nullptr。 |

### OH\_AudioRoutingManager\_UnregisterDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_UnregisterDeviceChangeCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnDeviceChangedCallback callback)
```

**描述**

取消注册音频路由管理器的设备更改回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioRoutingManager\_OnDeviceChangedCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondevicechangedcallback) callback | 函数指针将指向用于返回更改的音频设备描述符的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数callback为nullptr。 |

### OH\_AudioRoutingManager\_ReleaseDevices()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_ReleaseDevices(OH_AudioRoutingManager *audioRoutingManager, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

释放音频设备描述符数组对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组应当被释放，获取请调用[OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices)接口。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioRoutingManager为nullptr；  2. 参数audioDeviceDescriptorArray为nullptr。 |

### OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRoutingManager_OnDeviceBlockStatusCallback)(OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray, OH_AudioDevice_BlockStatus status, void *userData)
```

**描述**

此函数指针将指向用于返回音频设备堵塞状态的回调函数，可能返回多个音频设备描述符。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组应当被释放，获取请调用[OH\_AudioRoutingManager\_GetDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_getdevices)接口。设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioRoutingManager\_ReleaseDevices](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_releasedevices)来释放DeviceDescriptor数组。 |
| [OH\_AudioDevice\_BlockStatus](capi-native-audio-device-base-h.md#oh_audiodevice_blockstatus) status | 音频设备的堵塞状态。 |
| void \*userData | 用户自定义数据指针。 |

### OH\_AudioRoutingManager\_IsMicBlockDetectionSupported()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_IsMicBlockDetectionSupported(OH_AudioRoutingManager *audioRoutingManager, bool *supported)
```

**描述**

查询当前设备是否支持麦克风堵塞状态检测。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| bool \*supported | 查询当前设备是否支持麦克风堵塞状态检测的结果。true表示支持，false表示不支持。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioRoutingManager为nullptr；  2.参数supported为nullptr。 |

### OH\_AudioRoutingManager\_SetMicBlockStatusCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioRoutingManager_SetMicBlockStatusCallback(OH_AudioRoutingManager *audioRoutingManager, OH_AudioRoutingManager_OnDeviceBlockStatusCallback callback, void *userData)
```

**描述**

设置麦克风是否堵塞状态回调。

在使用此功能之前，用户应查询当前设备是否支持检测，应用只有在使用麦克风录音时，并且所使用的麦克风的堵塞状态发生改变，才会收到回调，目前此检测功能仅支持麦克风位于本地设备上。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRoutingManager](capi-ohaudio-oh-audioroutingmanager.md) \*audioRoutingManager | 音频路由管理器句柄。通过[OH\_AudioManager\_GetAudioRoutingManager](capi-native-audio-routing-manager-h.md#oh_audiomanager_getaudioroutingmanager)获取句柄。 |
| [OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback) callback | 函数指针将指向用于返回接受设备麦克风堵塞状态[OH\_AudioRoutingManager\_OnDeviceBlockStatusCallback](capi-native-audio-routing-manager-h.md#oh_audioroutingmanager_ondeviceblockstatuscallback)。 |
| void \*userData | 用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioRoutingManager为nullptr；  2.参数callback为nullptr。 |
