---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-manager-h
title: native_audio_session_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_session_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b981608699825353521bada6a25488e2e5905dcd7382977361dce635ff66d800
---

## 概述

PhonePC/2in1TabletTVWearable

声明音频会话管理相关的接口。

包含创建音频会话管理器、激活/停用音频会话、检查音频会话是否已激活，以及监听音频会话停用事件。

**引用文件：** <ohaudio/native\_audio\_session\_manager.h>

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
| [OH\_AudioSession\_Strategy](capi-ohaudio-oh-audiosession-strategy.md) | OH\_AudioSession\_Strategy | 音频会话策略。 |
| [OH\_AudioSession\_DeactivatedEvent](capi-ohaudio-oh-audiosession-deactivatedevent.md) | OH\_AudioSession\_DeactivatedEvent | 音频会话已停用事件。 |
| [OH\_AudioSession\_StateChangedEvent](capi-ohaudio-oh-audiosession-statechangedevent.md) | OH\_AudioSession\_StateChangedEvent | 音频会话状态变更事件。 |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) | OH\_AudioSessionManager | 声明音频会话管理器。用于管理音频会话相关功能。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioSession\_ConcurrencyMode](capi-native-audio-session-manager-h.md#oh_audiosession_concurrencymode) | OH\_AudioSession\_ConcurrencyMode | 音频并发模式。 |
| [OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene) | OH\_AudioSession\_Scene | 音频会话场景。 |
| [OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint) | OH\_AudioSession\_StateChangeHint | 音频会话状态变更的提示信息。 |
| [OH\_AudioSession\_OutputDeviceChangeRecommendedAction](capi-native-audio-session-manager-h.md#oh_audiosession_outputdevicechangerecommendedaction) | OH\_AudioSession\_OutputDeviceChangeRecommendedAction | 输出设备变更后推荐的操作。 |
| [OH\_AudioSession\_DeactivatedReason](capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedreason) | OH\_AudioSession\_DeactivatedReason | 音频会话停用原因。 |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](capi-native-audio-session-manager-h.md#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) | OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AudioSession\_StateChangedCallback)(OH\_AudioSession\_StateChangedEvent event)](capi-native-audio-session-manager-h.md#oh_audiosession_statechangedcallback) | OH\_AudioSession\_StateChangedCallback | 这个函数指针将指向用于监听音频会话状态变更事件的回调函数。 |
| [typedef void (\*OH\_AudioSession\_AvailableDeviceChangedCallback)(OH\_AudioDevice\_ChangeType type, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-session-manager-h.md#oh_audiosession_availabledevicechangedcallback) | OH\_AudioSession\_AvailableDeviceChangedCallback | 此函数指针将指向用于返回变化的音频设备描述符的回调函数，可能会返回多个音频设备描述符。 |
| [typedef void (\*OH\_AudioSession\_CurrentInputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason)](capi-native-audio-session-manager-h.md#oh_audiosession_currentinputdevicechangedcallback) | OH\_AudioSession\_CurrentInputDeviceChangedCallback | 这个函数指针将指向用于监听当前输入设备变化事件的回调函数。 |
| [typedef void (\*OH\_AudioSession\_CurrentOutputDeviceChangedCallback)(OH\_AudioDeviceDescriptorArray \*devices, OH\_AudioStream\_DeviceChangeReason changeReason, OH\_AudioSession\_OutputDeviceChangeRecommendedAction recommendedAction)](capi-native-audio-session-manager-h.md#oh_audiosession_currentoutputdevicechangedcallback) | OH\_AudioSession\_CurrentOutputDeviceChangedCallback | 这个函数指针将指向用于监听当前输出设备变化事件的回调函数。 |
| [typedef int32\_t (\*OH\_AudioSession\_DeactivatedCallback)(OH\_AudioSession\_DeactivatedEvent event)](capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedcallback) | OH\_AudioSession\_DeactivatedCallback | 这个函数指针将指向用于监听音频会话停用事件的回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioSessionManager(OH\_AudioSessionManager \*\*audioSessionManager)](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager) | - | 获取音频会话管理器。使用音频会话管理器相关功能，首先需要获取音频会话管理器实例。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ActivateAudioSession(OH\_AudioSessionManager \*audioSessionManager, const OH\_AudioSession\_Strategy \*strategy)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_activateaudiosession) | - | 激活音频会话。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_DeactivateAudioSession(OH\_AudioSessionManager \*audioSessionManager)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_deactivateaudiosession) | - | 停用音频会话。 |
| [bool OH\_AudioSessionManager\_IsAudioSessionActivated(OH\_AudioSessionManager \*audioSessionManager)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_isaudiosessionactivated) | - | 检查音频会话是否已激活。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registersessiondeactivatedcallback) | - | 注册音频会话停用事件回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_DeactivatedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregistersessiondeactivatedcallback) | - | 取消注册音频会话停用事件回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetScene(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_Scene scene)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene) | - | 设置音频会话场景参数。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registerstatechangecallback) | - | 注册音频会话状态变更事件回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterStateChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_StateChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregisterstatechangecallback) | - | 取消音频会话状态变更事件回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type deviceType)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setdefaultoutputdevice) | - | 设置默认本机内置发声设备。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetDefaultOutputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Type \*deviceType)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_getdefaultoutputdevice) | - | 获取通过[OH\_AudioSessionManager\_SetDefaultOutputDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setdefaultoutputdevice)设置的默认发声设备。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptorArray \*audioDeviceDescriptorArray)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevices) | - | 释放音频设备描述符数组对象。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentoutputdevicechangecallback) | - | 注册当前输出设备变化回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentOutputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentOutputDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregistercurrentoutputdevicechangecallback) | - | 取消注册当前输出设备变化回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetAvailableDevices(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioDeviceDescriptorArray \*\*audioDeviceDescriptorArray)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_getavailabledevices) | - | 获取音频可选设备列表。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDevice\_Usage deviceUsage, OH\_AudioSession\_AvailableDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registeravailabledeviceschangecallback) | - | 注册可用设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterAvailableDevicesChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_AvailableDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregisteravailabledeviceschangecallback) | - | 取消注册可用设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SelectMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*deviceDescriptor)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_selectmediainputdevice) | - | 设置媒体输入设备。此功能不适用于呼叫录音，即[SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)为SOURCE\_TYPE\_VOICE\_COMMUNICATION的场景不适用。  在存在更高优先级的并发录音流的场景中，应用程序实际使用的输入设备可能与所选设备不同。  应用程序可以使用[OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentinputdevicechangecallback)注册一个回调来监听实际的输入设备。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetSelectedMediaInputDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*\*audioDeviceDescriptor)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_getselectedmediainputdevice) | - | 获得通过[OH\_AudioSessionManager\_SelectMediaInputDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_selectmediainputdevice)设置的媒体输入设备。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_SetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory category)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setbluetoothandnearlinkpreferredrecordcategory) | - | 设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。  在更高优先级的并发录音流的场景中，应用程序实际使用的输入设备可能与当前设置的偏好设备不同。  应用程序可以使用[OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentinputdevicechangecallback)注册一个回调来监听实际的输入设备。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_GetBluetoothAndNearlinkPreferredRecordCategory(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory \*category)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_getbluetoothandnearlinkpreferredrecordcategory) | - | 获取应用程序设置的在使用蓝牙或星闪进行录音时的设备偏好分类。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentinputdevicechangecallback) | - | 注册音频会话管理器的输入设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_UnregisterCurrentInputDeviceChangeCallback(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioSession\_CurrentInputDeviceChangedCallback callback)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_unregistercurrentinputdevicechangecallback) | - | 取消注册音频会话管理器的输入设备更改回调。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_ReleaseDevice(OH\_AudioSessionManager \*audioSessionManager, OH\_AudioDeviceDescriptor \*audioDeviceDescriptor)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevice) | - | 释放音频设备描述符对象。 |
| [OH\_AudioCommon\_Result OH\_AudioSessionManager\_EnableMuteSuggestionWhenMixWithOthers(OH\_AudioSessionManager \*audioSessionManager, bool enable)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_enablemutesuggestionwhenmixwithothers) | - | 启用混音播放下接收静音播放建议通知功能。 |
| [bool OH\_AudioSessionManager\_IsOtherMediaPlaying(OH\_AudioSessionManager \*audioSessionManager)](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_isothermediaplaying) | - | 检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AudioSession\_ConcurrencyMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_ConcurrencyMode
```

**描述**

音频并发模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CONCURRENCY\_DEFAULT = 0 | 默认使用系统策略。 |
| CONCURRENCY\_MIX\_WITH\_OTHERS = 1 | 和其它正在播放应用进行混音。 |
| CONCURRENCY\_DUCK\_OTHERS = 2 | 后来播放应用压低正在播放应用的音量。 |
| CONCURRENCY\_PAUSE\_OTHERS = 3 | 后来播放应用暂停正在播放应用。 |

### OH\_AudioSession\_Scene

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_Scene
```

**描述**

音频会话场景。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_SESSION\_SCENE\_MEDIA = 0 | 媒体音频会话场景。 |
| AUDIO\_SESSION\_SCENE\_GAME = 1 | 游戏音频会话场景。 |
| AUDIO\_SESSION\_SCENE\_VOICE\_COMMUNICATION = 2 | VoIP语音通话音频会话场景。 |

### OH\_AudioSession\_StateChangeHint

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_StateChangeHint
```

**描述**

音频会话状态变更的提示信息。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME = 0 | 提示音频会话恢复，应用可主动触发开始渲染等相关操作。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE = 1 | 提示音频会话暂停，暂时失去音频焦点。当焦点再次可用时，会收到AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME事件。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_STOP = 2 | 提示音频会话在焦点被抢占后停止，彻底失去音频焦点。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_TIME\_OUT\_STOP = 3 | 提示长时间没有音频业务，音频会话将被系统停止，彻底失去音频焦点。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_DUCK = 4 | 提示音频会话躲避开始，降低音量播放。如果已启用[OH\_AudioSessionManager\_EnableMuteSuggestionWhenMixWithOthers](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_enablemutesuggestionwhenmixwithothers)，此时可以选择执行静音操作。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNDUCK = 5 | 提示音频会话躲避结束，恢复音量播放。如果已启用[OH\_AudioSessionManager\_EnableMuteSuggestionWhenMixWithOthers](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_enablemutesuggestionwhenmixwithothers)，此时可取消静音。 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE\_SUGGESTION = 6 | 静音播放建议。当其他应用程序开始播放不可混音的音频时，应用程序可以自行决定是否静音。  **起始版本：** 23 |
| AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE\_SUGGESTION = 7 | 取消静音播放建议。当其他应用程序不可混音的音频已结束，该应用程序可自行决定是否取消静音。  **起始版本：** 23 |

### OH\_AudioSession\_OutputDeviceChangeRecommendedAction

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_OutputDeviceChangeRecommendedAction
```

**描述**

输出设备变更后推荐的操作。

常见场景示例：耳机设备和外放设备之间进行切换。当佩戴耳机时，从外放设备切换到耳机设备，系统会推荐继续播放，提示应用无需停止当前播放。当摘下耳机设备切换到外放设备时，系统会推荐停止播放。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_CONTINUE = 0 | 推荐继续播放（该事件作为播放维持提示，作用是告知应用本次设备变动音频无需停止播放，但‌不可将其作为启动音频播放的判断依据）。 |
| DEVICE\_CHANGE\_RECOMMEND\_TO\_STOP = 1 | 推荐停止播放。 |

### OH\_AudioSession\_DeactivatedReason

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_DeactivatedReason
```

**描述**

音频会话停用原因。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| DEACTIVATED\_LOWER\_PRIORITY = 0 | 应用焦点被抢占。 |
| DEACTIVATED\_TIMEOUT = 1 | 应用停流后超时。 |

### OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioSession_BluetoothAndNearlinkPreferredRecordCategory
```

**描述**

在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| PREFERRED\_NONE = 0 | 无指定设备偏好。 |
| PREFERRED\_DEFAULT = 1 | 更偏好使用蓝牙或星闪录音。是否使用低延迟或高质量录音取决于系统。 |
| PREFERRED\_LOW\_LATENCY = 2 | 更偏好使用蓝牙或星闪低延迟模式进行录音。 |
| PREFERRED\_HIGH\_QUALITY = 3 | 更偏好使用蓝牙或星闪高质量模式进行录音。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioSession\_StateChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioSession_StateChangedCallback)(OH_AudioSession_StateChangedEvent event)
```

**描述**

这个函数指针将指向用于监听音频会话状态变更事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSession\_StateChangedEvent](capi-ohaudio-oh-audiosession-statechangedevent.md) event | 音频会话状态变更事件。 |

### OH\_AudioSession\_AvailableDeviceChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioSession_AvailableDeviceChangedCallback)(OH_AudioDevice_ChangeType type, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

此函数指针将指向用于返回变化的音频设备描述符的回调函数，可能会返回多个音频设备描述符。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDevice\_ChangeType](capi-native-audio-device-base-h.md#oh_audiodevice_changetype) type | 设备连接状态类型，已连接或断开。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 音频设备描述符数组。  不再继续使用audioDeviceDescriptorArray指针时，请使用[OH\_AudioSessionManager\_ReleaseDevices](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevices)进行释放。 |

### OH\_AudioSession\_CurrentInputDeviceChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioSession_CurrentInputDeviceChangedCallback)(OH_AudioDeviceDescriptorArray *devices, OH_AudioStream_DeviceChangeReason changeReason)
```

**描述**

这个函数指针将指向用于监听当前输入设备变化事件的回调函数。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*devices | 音频设备描述符数组。  不再继续使用devices指针时，请使用[OH\_AudioSessionManager\_ReleaseDevices](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevices)进行释放。 |
| [OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason) changeReason | 设备变更原因。 |

### OH\_AudioSession\_CurrentOutputDeviceChangedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioSession_CurrentOutputDeviceChangedCallback)(OH_AudioDeviceDescriptorArray *devices, OH_AudioStream_DeviceChangeReason changeReason, OH_AudioSession_OutputDeviceChangeRecommendedAction recommendedAction)
```

**描述**

这个函数指针将指向用于监听当前输出设备变化事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*devices | 音频设备描述符数组，指向OH\_AudioDeviceDescriptorArray设置音频设备描述符值的指针变量，不要单独释放audioDeviceDescriptorArray指针，而是调用[OH\_AudioSessionManager\_ReleaseDevices](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevices)来释放DeviceDescriptor数组。 |
| [OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason) changeReason | 指向[OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason)，用于接收设备变更原因。 |
| [OH\_AudioSession\_OutputDeviceChangeRecommendedAction](capi-native-audio-session-manager-h.md#oh_audiosession_outputdevicechangerecommendedaction) recommendedAction | 指向[OH\_AudioSession\_OutputDeviceChangeRecommendedAction](capi-native-audio-session-manager-h.md#oh_audiosession_outputdevicechangerecommendedaction)，用于接收设备变更后推荐的操作。 |

### OH\_AudioSession\_DeactivatedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AudioSession_DeactivatedCallback)(OH_AudioSession_DeactivatedEvent event)
```

**描述**

这个函数指针将指向用于监听音频会话停用事件的回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSession\_DeactivatedEvent](capi-ohaudio-oh-audiosession-deactivatedevent.md) event | 音频会话已停用事件。 |

### OH\_AudioManager\_GetAudioSessionManager()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioManager_GetAudioSessionManager(OH_AudioSessionManager **audioSessionManager)
```

**描述**

获取音频会话管理器。使用音频会话管理器相关功能，首先需要获取音频会话管理器实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*\*audioSessionManager | 音频会话管理器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统错误。 |

### OH\_AudioSessionManager\_ActivateAudioSession()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_ActivateAudioSession(OH_AudioSessionManager *audioSessionManager, const OH_AudioSession_Strategy *strategy)
```

**描述**

激活音频会话。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [const OH\_AudioSession\_Strategy](capi-ohaudio-oh-audiosession-strategy.md) \*strategy | 指向[OH\_AudioSession\_Strategy](capi-ohaudio-oh-audiosession-strategy.md)，用于设置音频会话策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | 函数返回值：  AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数strategy无效。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：非法状态。 |

### OH\_AudioSessionManager\_DeactivateAudioSession()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_DeactivateAudioSession(OH_AudioSessionManager *audioSessionManager)
```

**描述**

停用音频会话。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数audioSessionManager为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：非法状态。 |

### OH\_AudioSessionManager\_IsAudioSessionActivated()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AudioSessionManager_IsAudioSessionActivated(OH_AudioSessionManager *audioSessionManager)
```

**描述**

检查音频会话是否已激活。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 用于返回当前应用的音频会话是否已激活，true表示已激活，false表示已停用。 |

### OH\_AudioSessionManager\_RegisterSessionDeactivatedCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_RegisterSessionDeactivatedCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_DeactivatedCallback callback)
```

**描述**

注册音频会话停用事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_DeactivatedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedcallback) callback | 用于接收音频会话已停用事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。 |

### OH\_AudioSessionManager\_UnregisterSessionDeactivatedCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_UnregisterSessionDeactivatedCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_DeactivatedCallback callback)
```

**描述**

取消注册音频会话停用事件回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_DeactivatedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_deactivatedcallback) callback | 用于接收音频会话已停用事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。 |

### OH\_AudioSessionManager\_SetScene()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_SetScene(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_Scene scene)
```

**描述**

设置音频会话场景参数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene) scene | 指向[OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene)要设置的音频会话场景。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数scene为枚举范围外的值。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：系统当前状态下不允许设置，例如audio session未处于ready态。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_RegisterStateChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_RegisterStateChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_StateChangedCallback callback)
```

**描述**

注册音频会话状态变更事件回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_StateChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_statechangedcallback) callback | 用于接收音频会话状态变更事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：系统内存申请异常。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_UnregisterStateChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_UnregisterStateChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_StateChangedCallback callback)
```

**描述**

取消音频会话状态变更事件回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_StateChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_statechangedcallback) callback | 用于接收音频会话状态变更事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_SetDefaultOutputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_SetDefaultOutputDevice(OH_AudioSessionManager *audioSessionManager, OH_AudioDevice_Type deviceType)
```

**描述**

设置默认本机内置发声设备。

说明

* 本接口适用范围如下：当设置的[OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene)为VoIP场景时，激活AudioSession后立即生效；如果[OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene)为非VoIP场景，激活AudioSession时不会生效，直到启动播放的[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)为语音消息、VoIP语音通话或VoIP视频通话时才生效。支持听筒、扬声器和系统默认设备。
* 本接口允许在[OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md)创建后随时调用。系统记录应用设置的默认本机内置发声设备，但只有激活AudioSession后才能生效。应用启动播放时，若外接设备如蓝牙耳机或有线耳机已接入，系统优先从外接设备发声；否则，系统遵循应用设置的默认本机内置发声设备。

**设备行为差异：** 当该接口在无听筒的设备上设置默认发声设备为听筒时，将继续从扬声器发声。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type) deviceType | 指向[OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type)用于设置发声设备类型。可设置的设备类型包括：  AUDIO\_DEVICE\_TYPE\_EARPIECE：听筒。  AUDIO\_DEVICE\_TYPE\_SPEAKER：扬声器。  AUDIO\_DEVICE\_TYPE\_DEFAULT：系统默认设备。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数deviceType超出枚举OH\_AudioDevice\_Type范围。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_GetDefaultOutputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_GetDefaultOutputDevice(OH_AudioSessionManager *audioSessionManager, OH_AudioDevice_Type *deviceType)
```

**描述**

获取通过[OH\_AudioSessionManager\_SetDefaultOutputDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setdefaultoutputdevice)设置的默认发声设备。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type) \*deviceType | 指向[OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type)用于获取发声设备类型参数指针。返回的设备类型包括：  AUDIO\_DEVICE\_TYPE\_EARPIECE：听筒。  AUDIO\_DEVICE\_TYPE\_SPEAKER：扬声器。  AUDIO\_DEVICE\_TYPE\_DEFAULT：系统默认设备。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数deviceType为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：系统当前状态下不允许获取默认设备类型，例如audio session未处于ready态。 |

### OH\_AudioSessionManager\_ReleaseDevices()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_ReleaseDevices(OH_AudioSessionManager *audioSessionManager, OH_AudioDeviceDescriptorArray *audioDeviceDescriptorArray)
```

**描述**

释放音频设备描述符数组对象。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*audioDeviceDescriptorArray | 需要释放的音频设备描述符数组。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数audioDeviceDescriptorArray为nullptr。 |

### OH\_AudioSessionManager\_RegisterCurrentOutputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_RegisterCurrentOutputDeviceChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_CurrentOutputDeviceChangedCallback callback)
```

**描述**

注册当前输出设备变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_CurrentOutputDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_currentoutputdevicechangedcallback) callback | 用于返回音频设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：系统内存申请异常。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_UnregisterCurrentOutputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_UnregisterCurrentOutputDeviceChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_CurrentOutputDeviceChangedCallback callback)
```

**描述**

取消注册当前输出设备变化回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_CurrentOutputDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_currentoutputdevicechangedcallback) callback | 用于返回音频设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_GetAvailableDevices()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_GetAvailableDevices(OH_AudioSessionManager *audioSessionManager, OH_AudioDevice_Usage deviceUsage, OH_AudioDeviceDescriptorArray **audioDeviceDescriptorArray)
```

**描述**

获取音频可选设备列表。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage) deviceUsage | 用于设置要获取的设备种类。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md) \*\*audioDeviceDescriptorArray | 音频设备描述符数组。  不再继续使用audioDeviceDescriptorArray指针时，请使用[OH\_AudioSessionManager\_ReleaseDevices](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevices)进行释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1.参数audioSessionManager为nullptr；  2.参数deviceUsage无效;  3.参数audioDeviceDescriptorArray为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_RegisterAvailableDevicesChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_RegisterAvailableDevicesChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioDevice_Usage deviceUsage, OH_AudioSession_AvailableDeviceChangedCallback callback)
```

**描述**

注册可用设备更改回调。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDevice\_Usage](capi-native-audio-device-base-h.md#oh_audiodevice_usage) deviceUsage | 用于设置要获取的设备种类。 |
| [OH\_AudioSession\_AvailableDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_availabledevicechangedcallback) callback | 用于返回可用音频设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数deviceUsage无效；  3. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_UnregisterAvailableDevicesChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_UnregisterAvailableDevicesChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_AvailableDeviceChangedCallback callback)
```

**描述**

取消注册可用设备更改回调。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_AvailableDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_availabledevicechangedcallback) callback | 用于返回可用音频设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_SelectMediaInputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_SelectMediaInputDevice(OH_AudioSessionManager *audioSessionManager, OH_AudioDeviceDescriptor *deviceDescriptor)
```

**描述**

设置媒体输入设备。此功能不适用于呼叫录音，即[SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)为SOURCE\_TYPE\_VOICE\_COMMUNICATION的场景不适用。

在存在更高优先级的并发录音流的场景中，应用程序实际使用的输入设备可能与所选设备不同。

应用程序可以使用[OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentinputdevicechangecallback)注册一个回调来监听实际的输入设备。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*deviceDescriptor | 目标设备。可用设备必须位于由[OH\_AudioSessionManager\_GetAvailableDevices](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_getavailabledevices)返回的数组中。  当传递nullptr时，系统将清除上一次的设置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数audioSessionManager为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_GetSelectedMediaInputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_GetSelectedMediaInputDevice(OH_AudioSessionManager *audioSessionManager, OH_AudioDeviceDescriptor **audioDeviceDescriptor)
```

**描述**

获得通过[OH\_AudioSessionManager\_SelectMediaInputDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_selectmediainputdevice)设置的媒体输入设备。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*\*audioDeviceDescriptor | 通过[OH\_AudioSessionManager\_SelectMediaInputDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_selectmediainputdevice)设置的媒体设备，如果没有设置，返回一个类型为AUDIO\_DEVICE\_TYPE\_INVALID的设备。  不再继续使用audioDeviceDescriptor指针时，请使用[OH\_AudioSessionManager\_ReleaseDevice](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_releasedevice)进行释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数audioDeviceDescriptor为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_SetBluetoothAndNearlinkPreferredRecordCategory()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_SetBluetoothAndNearlinkPreferredRecordCategory(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_BluetoothAndNearlinkPreferredRecordCategory category)
```

**描述**

设置在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。应用程序可以在蓝牙或星闪连接之前设置此分类，系统将在设备连接时优先使用蓝牙或星闪进行录音。

在更高优先级的并发录音流的场景中，应用程序实际使用的输入设备可能与当前设置的偏好设备不同。

应用程序可以使用[OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registercurrentinputdevicechangecallback)注册一个回调来监听实际的输入设备。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](capi-native-audio-session-manager-h.md#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) category | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数category错误。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_GetBluetoothAndNearlinkPreferredRecordCategory()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_GetBluetoothAndNearlinkPreferredRecordCategory(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_BluetoothAndNearlinkPreferredRecordCategory *category)
```

**描述**

获取应用程序设置的在使用蓝牙或星闪进行录音时的设备偏好分类。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_BluetoothAndNearlinkPreferredRecordCategory](capi-native-audio-session-manager-h.md#oh_audiosession_bluetoothandnearlinkpreferredrecordcategory) \*category | 在使用蓝牙或星闪进行录音时，应用程序的设备偏好分类。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数category为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_RegisterCurrentInputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_RegisterCurrentInputDeviceChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_CurrentInputDeviceChangedCallback callback)
```

**描述**

注册音频会话管理器的输入设备更改回调。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_CurrentInputDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_currentinputdevicechangedcallback) callback | 用于返回音频输入设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_NO\_MEMORY：内存不足。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_UnregisterCurrentInputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_UnregisterCurrentInputDeviceChangeCallback(OH_AudioSessionManager *audioSessionManager, OH_AudioSession_CurrentInputDeviceChangedCallback callback)
```

**描述**

取消注册音频会话管理器的输入设备更改回调。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioSession\_CurrentInputDeviceChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_currentinputdevicechangedcallback) callback | 用于返回音频输入设备变更信息的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_ReleaseDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_ReleaseDevice(OH_AudioSessionManager *audioSessionManager, OH_AudioDeviceDescriptor *audioDeviceDescriptor)
```

**描述**

释放音频设备描述符对象。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md) \*audioDeviceDescriptor | 需要被释放的音频设备描述符对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：  1. 参数audioSessionManager为nullptr；  2. 参数audioDeviceDescriptor为nullptr。 |

### OH\_AudioSessionManager\_EnableMuteSuggestionWhenMixWithOthers()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioSessionManager_EnableMuteSuggestionWhenMixWithOthers(OH_AudioSessionManager *audioSessionManager, bool enable)
```

**描述**

启用混音播放下接收静音播放建议通知功能。通常，当使用混音模式时，如果有其他应用的音频同时播放，此时两者会混合播放。部分场景下（如游戏或广播），应用可以通过启用静音建议通知，以给用户提供更好的体验。如果启用此功能，当订阅音频会话状态更改事件后静音建议和取消静音建议提示将通过[OH\_AudioSession\_StateChangedCallback](capi-native-audio-session-manager-h.md#oh_audiosession_statechangedcallback)回调发送，该回调由[OH\_AudioSessionManager\_RegisterStateChangeCallback](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_registerstatechangecallback)注册。

收到静音建议表示其他应用程序开始播放音频，且播放的音频和本应用的音频不能混音。此功能仅支持已设置[OH\_AudioSession\_Scene](capi-native-audio-session-manager-h.md#oh_audiosession_scene)并激活模式为[OH\_AudioSession\_ConcurrencyMode](capi-native-audio-session-manager-h.md#oh_audiosession_concurrencymode).CONCURRENCY\_MIX\_WITH\_OTHERS的音频会话使用。

并且仅在激活音频会话期间生效一次，每次激活音频会话前都必须重新启用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |
| bool enable | 表示是否启用静音建议回调功能。true表示启用，false表示不启用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数audioSessionManager为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_ILLEGAL\_STATE：  1. 未设置音频会话场景。  2. 音频会话激活后调用此函数。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统异常，例如系统服务异常退出等。 |

### OH\_AudioSessionManager\_IsOtherMediaPlaying()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AudioSessionManager_IsOtherMediaPlaying(OH_AudioSessionManager *audioSessionManager)
```

**描述**

检查是否有其他应用正在播放MUSIC、MOVIE、AUDIOBOOK、GAME四种媒体类型的音频，已激活媒体类型的音频会话也将会被检查。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*audioSessionManager | 指向[OH\_AudioManager\_GetAudioSessionManager](capi-native-audio-session-manager-h.md#oh_audiomanager_getaudiosessionmanager)创建的音频会话管理实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 是否有其他应用正在播放媒体类型的音频。true表示有，false表示没有。 |
