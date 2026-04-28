---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-volume-manager-h
title: native_audio_volume_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_volume_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a4863d71cf72fd954183027106b1c24ac694ab289d6e567e88343dad485eaf5e
---

## 概述

PhonePC/2in1TabletTVWearable

声明音频音量管理器接口。

该文件接口用于创建AudioVolumeManager。

**引用文件：** <ohaudio/native\_audio\_volume\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 20

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) | OH\_AudioVolumeManager | 声明音频音量管理器。音频音量管理器提供多种函数，供开发人员获取系统音量信息。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback)(void \*userData, OH\_AudioStream\_Usage usage, int32\_t volumeLevel, bool updateUi)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onstreamvolumechangecallback) | OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback | 音量变化回调函数的原型定义，用于传递给[OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerstreamvolumechangecallback)。 |
| [typedef void (\*OH\_AudioVolumeManager\_OnRingerModeChangeCallback)(void \*userData, OH\_AudioRingerMode ringerMode)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onringermodechangecallback) | OH\_AudioVolumeManager\_OnRingerModeChangeCallback | 铃声模式变化回调函数的原型定义，用于传递给[OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerringermodechangecallback)。 |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioVolumeManager(OH\_AudioVolumeManager \*\*volumeManager)](capi-native-audio-volume-manager-h.md#oh_audiomanager_getaudiovolumemanager) | - | 使用音量管理器相关功能，首先需要获取音量管理器实例。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMaxVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*maxVolumeLevel)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_getmaxvolumebyusage) | - | 获取指定用途类型音频流的最大音量等级。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetMinVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*minVolumeLevel)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_getminvolumebyusage) | - | 获取指定用途类型音频流的最小音量等级。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetVolumeByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, int32\_t \*volumeLevel)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_getvolumebyusage) | - | 获取指定用途类型音频流的系统音量等级。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_IsMuteByUsage(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, bool \*muted)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_ismutebyusage) | - | 检查指定用途类型的音频流是否处于静音状态。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioStream\_Usage usage, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback, void \*userData)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerstreamvolumechangecallback) | - | 注册音频流音量修改回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterStreamVolumeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback callback)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_unregisterstreamvolumechangecallback) | - | 取消注册音频流音量修改回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_GetRingerMode(OH\_AudioVolumeManager \*volumeManager, OH\_AudioRingerMode \*ringerMode)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_getringermode) | - | 获取当前铃声模式。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback, void \*userData)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerringermodechangecallback) | - | 注册铃声模式切换回调函数。 |
| [OH\_AudioCommon\_Result OH\_AudioVolumeManager\_UnregisterRingerModeChangeCallback(OH\_AudioVolumeManager \*volumeManager, OH\_AudioVolumeManager\_OnRingerModeChangeCallback callback)](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_unregisterringermodechangecallback) | - | 取消注册铃声模式切换回调函数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioVolumeManager_OnStreamVolumeChangeCallback)(void *userData, OH_AudioStream_Usage usage, int32_t volumeLevel, bool updateUi)
```

**描述**

音量变化回调函数的原型定义，用于传递给[OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerstreamvolumechangecallback)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*userData | 用户自定义数据指针。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 对应音量被调整的流的用途类型。 |
| int32\_t volumeLevel | 修改后的音量。 |
| bool updateUi | 是否在UI界面显示音量变化。true表示显示，false表示不显示。 |

### OH\_AudioVolumeManager\_OnRingerModeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioVolumeManager_OnRingerModeChangeCallback)(void *userData, OH_AudioRingerMode ringerMode)
```

**描述**

铃声模式变化回调函数的原型定义，用于传递给[OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerringermodechangecallback)。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| void \*userData | 用户自定义数据指针。 |
| [OH\_AudioRingerMode](capi-native-audio-common-h.md#oh_audioringermode) ringerMode | 切换后的铃声模式。 |

### OH\_AudioManager\_GetAudioVolumeManager()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioManager_GetAudioVolumeManager(OH_AudioVolumeManager **volumeManager)
```

**描述**

使用音量管理器相关功能，首先需要获取音量管理器实例。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*\*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager为nullptr。 |

### OH\_AudioVolumeManager\_GetMaxVolumeByUsage()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_GetMaxVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *maxVolumeLevel)
```

**描述**

获取指定用途类型音频流的最大音量等级。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 用于映射特定音量类型的音频流用途类型。 |
| int32\_t \*maxVolumeLevel | 用于接收返回的最大音量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或maxVolumeLevel为nullptr，或usage是无效值。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_GetMinVolumeByUsage()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_GetMinVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *minVolumeLevel)
```

**描述**

获取指定用途类型音频流的最小音量等级。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 用于映射特定音量类型的音频流用途类型。 |
| int32\_t \*minVolumeLevel | 用于接收返回的最小音量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或minVolumeLevel为nullptr，或usage是无效值。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_GetVolumeByUsage()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_GetVolumeByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, int32_t *volumeLevel)
```

**描述**

获取指定用途类型音频流的系统音量等级。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 用于映射特定音量类型的音频流用途类型。 |
| int32\_t \*volumeLevel | 用于接收返回的系统音量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或volumeLevel为nullptr，或usage是无效值。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_IsMuteByUsage()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_IsMuteByUsage(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, bool *muted)
```

**描述**

检查指定用途类型的音频流是否处于静音状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 用于映射特定音量类型的音频流用途类型。 |
| bool \*muted | 用于接收返回的音频流是否静音。true表示静音，false表示未静音。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或muted为nullptr，或usage是无效值。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_RegisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioStream_Usage usage, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback, void *userData)
```

**描述**

注册音频流音量修改回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 监听用于映射特定音量类型的音频流用途类型。 |
| [OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onstreamvolumechangecallback) callback | 监听的音频流音量发生时，将调用此回调函数[OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onstreamvolumechangecallback)。 |
| void \*userData | 用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager、usage或callback为nullptr，或usage是无效值。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_UnregisterStreamVolumeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterStreamVolumeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnStreamVolumeChangeCallback callback)
```

**描述**

取消注册音频流音量修改回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioVolumeManager\_OnStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onstreamvolumechangecallback) callback | 指向[OH\_AudioVolumeManager\_RegisterStreamVolumeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerstreamvolumechangecallback)传入的回调函数，用于取消注册。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_GetRingerMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_GetRingerMode(OH_AudioVolumeManager *volumeManager, OH_AudioRingerMode *ringerMode)
```

**描述**

获取当前铃声模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioRingerMode](capi-native-audio-common-h.md#oh_audioringermode) \*ringerMode | 用于接收返回的铃声模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或ringerMode为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_RegisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback, void *userData)
```

**描述**

注册铃声模式切换回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioVolumeManager\_OnRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onringermodechangecallback) callback | 监听的铃声模式发生切换时，将调用此回调函数[OH\_AudioVolumeManager\_OnRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onringermodechangecallback)。 |
| void \*userData | 用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |

### OH\_AudioVolumeManager\_UnregisterRingerModeChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioCommon_Result OH_AudioVolumeManager_UnregisterRingerModeChangeCallback(OH_AudioVolumeManager *volumeManager, OH_AudioVolumeManager_OnRingerModeChangeCallback callback)
```

**描述**

取消注册铃声模式切换回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioVolumeManager](capi-ohaudio-oh-audiovolumemanager.md) \*volumeManager | 指向OH\_AudioVolumeManager用于接收创建的音量管理器实例。 |
| [OH\_AudioVolumeManager\_OnRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_onringermodechangecallback) callback | 指向[OH\_AudioVolumeManager\_RegisterRingerModeChangeCallback](capi-native-audio-volume-manager-h.md#oh_audiovolumemanager_registerringermodechangecallback)传入的回调函数，用于取消注册。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioCommon\_Result](capi-native-audio-common-h.md#oh_audiocommon_result) | AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数volumeManager或callback为nullptr。  AUDIOCOMMON\_RESULT\_ERROR\_SYSTEM：系统处理错误。 |
