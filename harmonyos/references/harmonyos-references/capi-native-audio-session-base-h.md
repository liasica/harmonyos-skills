---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audio-session-base-h
title: native_audio_session_base.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audio_session_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d046c2237e7a2bebc477494209c56d2729e701624d927d136fb27630d9483156
---

## 概述

声明音频会话基础数据结构。

**引用文件：** <ohaudio/native\_audio\_session\_base.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 24

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioSession\_Strategy](capi-ohaudio-oh-audiosession-strategy.md) | OH\_AudioSession\_Strategy | 音频会话策略。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioSession\_BehaviorFlags](capi-native-audio-session-base-h.md#oh_audiosession_behaviorflags) | OH\_AudioSession\_BehaviorFlags | 音频会话行为标志。 |
| [OH\_AudioSession\_ConcurrencyMode](capi-native-audio-session-base-h.md#oh_audiosession_concurrencymode) | OH\_AudioSession\_ConcurrencyMode | 音频并发模式。 |

## 枚举类型说明

### OH\_AudioSession\_BehaviorFlags

```c
enum OH_AudioSession_BehaviorFlags
```

**描述**

音频会话行为标志。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| DEFAULT\_BEHAVIOR = 0x00000000 | 默认行为，用于清除会话行为标记。  **起始版本：** 24 |
| MUTE\_WHEN\_INTERRUPTED = 0x00000002 | 当系统需要停止或暂停音频流时，执行强制静音替代。  调用[OH\_AudioSessionManager\_SetBehavior](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setbehavior)接口配置该行为时，必须同步调用[OH\_AudioSessionManager\_SetScene](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)接口，否则配置将无法生效。  在音频会话场景下，当音频流静音或恢复时，应用将分别收到[OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint).AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_MUTE与[OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint).AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_UNMUTE的通知。  在OH\_AudioRenderer和OH\_AudioCapturer场景下，当音频流静音或恢复时，应用将分别收到[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint).AUDIOSTREAM\_INTERRUPT\_HINT\_MUTE与[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint).AUDIOSTREAM\_INTERRUPT\_HINT\_UNMUTE的通知。  **注意：** 该标志不能与PAUSE\_WHEN\_INTERRUPTED共存，若同时设置，仅PAUSE\_WHEN\_INTERRUPTED生效。  **起始版本：** 24 |
| PAUSE\_WHEN\_INTERRUPTED = 0x00000004 | 当系统需要停止音频流时，执行暂停替代。  调用[OH\_AudioSessionManager\_SetBehavior](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setbehavior)接口配置该行为时，必须同步调用[OH\_AudioSessionManager\_SetScene](capi-native-audio-session-manager-h.md#oh_audiosessionmanager_setscene)接口，否则配置将无法生效。  在音频会话场景下，当音频流暂停或恢复时，应用将分别收到[OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint).AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_PAUSE与[OH\_AudioSession\_StateChangeHint](capi-native-audio-session-manager-h.md#oh_audiosession_statechangehint).AUDIO\_SESSION\_STATE\_CHANGE\_HINT\_RESUME的通知。  在OH\_AudioRenderer和OH\_AudioCapturer场景下，当音频流暂停或恢复时，应用将分别收到[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint).AUDIOSTREAM\_INTERRUPT\_HINT\_PAUSE与[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint).AUDIOSTREAM\_INTERRUPT\_HINT\_RESUME的通知。  **注意：** 该标志不能与MUTE\_WHEN\_INTERRUPTED共存，若同时设置，仅该标志生效。  **起始版本：** 26.0.0 |

### OH\_AudioSession\_ConcurrencyMode

```c
enum OH_AudioSession_ConcurrencyMode
```

**描述**

音频并发模式。

从API version 24开始，此枚举由native\_audio\_session\_manager.h移动至此头文件。

在API version 24之前，使用该枚举请引用native\_audio\_session\_manager.h头文件；从API version 24开始，引用native\_audio\_session\_manager.h或native\_audio\_session\_base.h均可正常使用该枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| CONCURRENCY\_DEFAULT = 0 | 默认使用系统策略。 |
| CONCURRENCY\_MIX\_WITH\_OTHERS = 1 | 当前应用与其他应用混音播放。 |
| CONCURRENCY\_DUCK\_OTHERS = 2 | 当前应用播放时会压低其他正在播放的应用音量。 |
| CONCURRENCY\_PAUSE\_OTHERS = 3 | 当前应用播放时会暂停其他正在播放的应用。 |
