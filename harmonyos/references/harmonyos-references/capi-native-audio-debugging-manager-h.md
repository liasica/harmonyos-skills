---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-debugging-manager-h
title: native_audio_debugging_manager.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_debugging_manager.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f774026681980654dd520cc8ed7d342470a745413c4190ea0ff05f40e89ee306
---

## 概述

声明音频调试管理器相关的接口。本文件中的接口用于获取音频调试管理器实例，提供音频运行时调试功能，包括快照信息获取等。

**引用文件：** <ohaudio/native\_audio\_debugging\_manager.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) | OH\_AudioDebuggingManager | 声明音频调试管理器。用于音频运行时调试，包括获取快照信息等功能。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioCommon\_Result OH\_AudioManager\_GetAudioDebuggingManager(OH\_AudioDebuggingManager \*\*manager)](capi-native-audio-debugging-manager-h.md#oh_audiomanager_getaudiodebuggingmanager) | 获取音频调试管理器实例（单例）。 |
| [OH\_AudioCommon\_Result OH\_AudioDebuggingManager\_PrintAppInfo(OH\_AudioDebuggingManager \*manager, int32\_t fd)](capi-native-audio-debugging-manager-h.md#oh_audiodebuggingmanager_printappinfo) | 打印当前进程中所有音频模块的快照信息。 |
| [OH\_AudioCommon\_Result OH\_AudioDebuggingManager\_PrintRendererInfo(OH\_AudioDebuggingManager \*manager, OH\_AudioRenderer \*renderer, int32\_t fd)](capi-native-audio-debugging-manager-h.md#oh_audiodebuggingmanager_printrendererinfo) | 打印指定音频播放实例的快照信息。 |
| [OH\_AudioCommon\_Result OH\_AudioDebuggingManager\_PrintCapturerInfo(OH\_AudioDebuggingManager \*manager, OH\_AudioCapturer \*capturer, int32\_t fd)](capi-native-audio-debugging-manager-h.md#oh_audiodebuggingmanager_printcapturerinfo) | 打印指定录音实例的快照信息。 |
| [OH\_AudioCommon\_Result OH\_AudioDebuggingManager\_PrintSessionInfo(OH\_AudioDebuggingManager \*manager, OH\_AudioSessionManager \*session, int32\_t fd)](capi-native-audio-debugging-manager-h.md#oh_audiodebuggingmanager_printsessioninfo) | 打印指定会话管理器实例的快照信息。 |

## 函数说明

### OH\_AudioManager\_GetAudioDebuggingManager()

```c
OH_AudioCommon_Result OH_AudioManager_GetAudioDebuggingManager(OH_AudioDebuggingManager **manager)
```

**描述**

获取音频调试管理器实例（单例）。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) \*\*manager | 输出参数，用于接收OH\_AudioDebuggingManager实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AudioCommon\_Result | * AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  * AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数manager为nullptr。 |

### OH\_AudioDebuggingManager\_PrintAppInfo()

```c
OH_AudioCommon_Result OH_AudioDebuggingManager_PrintAppInfo(OH_AudioDebuggingManager *manager, int32_t fd)
```

**描述**

打印当前进程中所有音频模块的快照信息。

**说明** 

快照信息的内容和格式随版本迭代发生变化，仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) \*manager | 通过[OH\_AudioManager\_GetAudioDebuggingManager](capi-native-audio-debugging-manager-h.md#oh_audiomanager_getaudiodebuggingmanager)获取的音频调试管理器实例。 |
| int32\_t fd | 文件描述符。当fd小于0或不可写时，快照信息将输出到运行日志，否则输出到fd指向的文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AudioCommon\_Result | * AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  * AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数manager为nullptr。 |

### OH\_AudioDebuggingManager\_PrintRendererInfo()

```c
OH_AudioCommon_Result OH_AudioDebuggingManager_PrintRendererInfo(OH_AudioDebuggingManager *manager, OH_AudioRenderer *renderer, int32_t fd)
```

**描述**

打印指定音频播放实例的快照信息。

**说明** 

快照信息的内容和格式随版本迭代发生变化，仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) \*manager | 通过[OH\_AudioManager\_GetAudioDebuggingManager](capi-native-audio-debugging-manager-h.md#oh_audiomanager_getaudiodebuggingmanager)获取的音频调试管理器实例。 |
| OH\_AudioRenderer \*renderer | 指向目标音频播放实例的指针，用于打印快照信息。 |
| int32\_t fd | 文件描述符。当fd小于0或不可写时，快照信息将输出到运行日志，否则输出到fd指向的文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AudioCommon\_Result | * AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  * AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数manager或renderer为nullptr。 |

### OH\_AudioDebuggingManager\_PrintCapturerInfo()

```c
OH_AudioCommon_Result OH_AudioDebuggingManager_PrintCapturerInfo(OH_AudioDebuggingManager *manager, OH_AudioCapturer *capturer, int32_t fd)
```

**描述**

打印指定录音实例的快照信息。

**说明** 

快照信息的内容和格式随版本迭代发生变化，仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) \*manager | 通过[OH\_AudioManager\_GetAudioDebuggingManager](capi-native-audio-debugging-manager-h.md#oh_audiomanager_getaudiodebuggingmanager)获取的音频调试管理器实例。 |
| OH\_AudioCapturer \*capturer | 指向目标录音实例的指针，用于打印快照信息。 |
| int32\_t fd | 文件描述符。当fd小于0或不可写时，快照信息将输出到运行日志，否则输出到fd指向的文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AudioCommon\_Result | * AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  * AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数manager或capturer为nullptr。 |

### OH\_AudioDebuggingManager\_PrintSessionInfo()

```c
OH_AudioCommon_Result OH_AudioDebuggingManager_PrintSessionInfo(OH_AudioDebuggingManager *manager, OH_AudioSessionManager *session, int32_t fd)
```

**描述**

打印指定会话管理器实例的快照信息。

**说明** 

快照信息的内容和格式随版本迭代发生变化，仅供人工调试参考，不建议开发者依据快照信息开发功能逻辑。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioDebuggingManager](capi-ohaudio-oh-audiodebuggingmanager.md) \*manager | 通过[OH\_AudioManager\_GetAudioDebuggingManager](capi-native-audio-debugging-manager-h.md#oh_audiomanager_getaudiodebuggingmanager)获取的音频调试管理器实例。 |
| [OH\_AudioSessionManager](capi-ohaudio-oh-audiosessionmanager.md) \*session | 指向目标会话管理器实例的指针，用于打印快照信息。 |
| int32\_t fd | 文件描述符。当fd小于0或不可写时，快照信息将输出到运行日志，否则输出到fd指向的文件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AudioCommon\_Result | * AUDIOCOMMON\_RESULT\_SUCCESS：函数执行成功。  * AUDIOCOMMON\_RESULT\_ERROR\_INVALID\_PARAM：参数manager或session为nullptr。 |
