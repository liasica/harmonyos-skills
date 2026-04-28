---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostream-base-h
title: native_audiostream_base.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audiostream_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0dfa50ead602de69de1885a424da4346a7dfb6df2e38b2a9feec6a158acbfe0e
---

## 概述

PhonePC/2in1TabletTVWearable

声明OHAudio基础的数据结构。

**引用文件：** <ohaudio/native\_audiostream\_base.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 10

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioStreamInfo](capi-ohaudio-oh-audiostreaminfo.md) | OH\_AudioStreamInfo | 定义音频流信息，用于描述基本音频格式。 |
| [OH\_AudioRenderer\_Callbacks\_Struct](capi-ohaudio-oh-audiorenderer-callbacks-struct.md) | OH\_AudioRenderer\_Callbacks | 声明输出音频流的回调函数指针。(API20废弃) |
| [OH\_AudioCapturer\_Callbacks\_Struct](capi-ohaudio-oh-audiocapturer-callbacks-struct.md) | OH\_AudioCapturer\_Callbacks | 声明输入音频流的回调函数指针。  为了避免不可预期的行为，在设置音频回调函数时，请确保该结构体的每一个成员变量都被自定义的回调方法或空指针初始化。(API20废弃) |
| [OH\_AudioStreamBuilderStruct](capi-ohaudio-oh-audiostreambuilderstruct.md) | OH\_AudioStreamBuilder | 声明音频流的构造器。构造器实例通常被用来设置音频流属性和创建音频流。 |
| [OH\_AudioRendererStruct](capi-ohaudio-oh-audiorendererstruct.md) | OH\_AudioRenderer | 声明输出音频流。输出音频流的实例被用来播放音频数据。 |
| [OH\_AudioCapturerStruct](capi-ohaudio-oh-audiocapturerstruct.md) | OH\_AudioCapturer | 声明输入音频流。输入音频流的实例被用来获取音频数据。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | OH\_AudioStream\_Result | 音频错误码。 |
| [OH\_AudioStream\_Type](capi-native-audiostream-base-h.md#oh_audiostream_type) | OH\_AudioStream\_Type | 音频流类型。 |
| [OH\_AudioStream\_SampleFormat](capi-native-audiostream-base-h.md#oh_audiostream_sampleformat) | OH\_AudioStream\_SampleFormat | 定义音频流采样格式。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype) | OH\_AudioStream\_EncodingType | 定义音频流编码类型。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) | OH\_AudioStream\_Usage | 定义音频流使用场景。  通常用来描述音频输出流的使用场景。 |
| [OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode) | OH\_AudioStream\_LatencyMode | 定义音频时延模式。 |
| [OH\_AudioStream\_DirectPlaybackMode](capi-native-audiostream-base-h.md#oh_audiostream_directplaybackmode) | OH\_AudioStream\_DirectPlaybackMode | 定义音频流direct通路播放模式。 |
| [OH\_AudioStream\_VolumeMode](capi-native-audiostream-base-h.md#oh_audiostream_volumemode) | OH\_AudioStream\_VolumeMode | 定义音频流音量模式。 |
| [OH\_AudioStream\_State](capi-native-audiostream-base-h.md#oh_audiostream_state) | OH\_AudioStream\_State | 定义音频流的状态。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype) | OH\_AudioStream\_SourceType | 定义音频流使用场景。  通常用来描述音频输入流的使用场景。 |
| [OH\_AudioStream\_Event](capi-native-audiostream-base-h.md#oh_audiostream_event) | OH\_AudioStream\_Event | 定义音频事件。(API20废弃) |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) | OH\_AudioInterrupt\_ForceType | 定义音频中断类型。  当用户监听到音频中断时，将获取此信息。  此类型表示本次音频打断的操作是否已由系统强制执行，具体操作信息（如音频暂停、停止等）可通过[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint)获取。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) | OH\_AudioInterrupt\_Hint | 定义音频中断提示类型。  当用户监听到音频中断时，将获取此信息。  此类型表示根据焦点策略，当前需要对音频流的具体操作（如暂停、调整音量等）。  可以结合[OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype)信息，判断该操作是否已由系统强制执行。 |
| [OH\_AudioInterrupt\_Mode](capi-native-audiostream-base-h.md#oh_audiointerrupt_mode) | OH\_AudioInterrupt\_Mode | 定义音频中断模式。 |
| [OH\_AudioStream\_AudioEffectMode](capi-native-audiostream-base-h.md#oh_audiostream_audioeffectmode) | OH\_AudioStream\_AudioEffectMode | 定义音效模式。 |
| [OH\_AudioStream\_FastStatus](capi-native-audiostream-base-h.md#oh_audiostream_faststatus) | OH\_AudioStream\_FastStatus | 定义低时延状态。 |
| [OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason) | OH\_AudioStream\_DeviceChangeReason | 流设备变更原因。 |
| [OH\_AudioStream\_PrivacyType](capi-native-audiostream-base-h.md#oh_audiostream_privacytype) | OH\_AudioStream\_PrivacyType | 用于标识对应播放音频流是否支持被其他应用录制。 |
| [OH\_AudioData\_Callback\_Result](capi-native-audiostream-base-h.md#oh_audiodata_callback_result) | OH\_AudioData\_Callback\_Result | 定义音频数据回调结果。 |
| [OH\_AudioStream\_LatencyType](capi-native-audiostream-base-h.md#oh_audiostream_latencytype) | OH\_AudioStream\_LatencyType | 定义音频时延类型。 |
| [OH\_AudioStream\_PlaybackCaptureMode](capi-native-audiostream-base-h.md#oh_audiostream_playbackcapturemode) | OH\_AudioStream\_PlaybackCaptureMode | 表示内录（录制设备内部应用的声音）的过滤类型，每种过滤类型可录制不同的播放流类型。该API暂不对外支持。 |
| [OH\_AudioStream\_PlaybackCaptureStartState](capi-native-audiostream-base-h.md#oh_audiostream_playbackcapturestartstate) | OH\_AudioStream\_PlaybackCaptureStartState | 定义内录的启动状态，该状态在调用[OH\_AudioCapturer\_RequestPlaybackCaptureStart](capi-native-audiocapturer-h.md#oh_audiocapturer_requestplaybackcapturestart)函数后异步返回。该API暂不对外支持。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AudioRenderer\_OutputDeviceChangeCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_DeviceChangeReason reason)](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback) | OH\_AudioRenderer\_OutputDeviceChangeCallback | 输出音频流设备变更的回调函数。 |
| [typedef void (\*OH\_AudioRenderer\_OnMarkReachedCallback)(OH\_AudioRenderer\* renderer, uint32\_t samplePos, void\* userData)](capi-native-audiostream-base-h.md#oh_audiorenderer_onmarkreachedcallback) | OH\_AudioRenderer\_OnMarkReachedCallback | 到达标记位置时回调。 |
| [typedef int32\_t (\*OH\_AudioRenderer\_WriteDataWithMetadataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize, void\* metadata, int32\_t metadataSize)](capi-native-audiostream-base-h.md#oh_audiorenderer_writedatawithmetadatacallback) | OH\_AudioRenderer\_WriteDataWithMetadataCallback | 该函数指针将指向用于同时写入音频数据和元数据的回调函数。 |
| [typedef OH\_AudioData\_Callback\_Result (\*OH\_AudioRenderer\_OnWriteDataCallback)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)](capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback) | OH\_AudioRenderer\_OnWriteDataCallback | 该函数指针将指向用于写入音频数据的回调函数。  回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。  该函数的返回结果表示填充到缓冲区的数据是否有效。如果结果无效，用户填写的数据将不被播放。  回调函数结束后，音频服务会把audioData指针数据放入队列里等待播放，因此请勿在回调外再次更改audioData指向的数据，且务必保证往audioData填满audioDataSize长度的待播放数据, 否则会导致音频服务播放杂音。  参数audioDataSize可以通过[OH\_AudioStreamBuilder\_SetFrameSizeInCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback)设置。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AudioStream\_Result

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_Result
```

**描述**

音频错误码。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_SUCCESS = 0 | 操作成功 |
| AUDIOSTREAM\_ERROR\_INVALID\_PARAM = 1 | 入参错误。 |
| AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE = 2 | 非法状态。 |
| AUDIOSTREAM\_ERROR\_SYSTEM = 3 | 系统通用错误。 |
| AUDIOSTREAM\_ERROR\_UNSUPPORTED\_FORMAT = 4 | 不支持的音频格式，如不支持的编码类型、采样格式等。  **起始版本：** 19 |

### OH\_AudioStream\_Type

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_Type
```

**描述**

音频流类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_TYPE\_RENDERER = 1 | 该类型代表音频流是输出流。 |
| AUDIOSTREAM\_TYPE\_CAPTURER = 2 | 该类型代表音频流是输入流。 |

### OH\_AudioStream\_SampleFormat

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_SampleFormat
```

**描述**

定义音频流采样格式。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_SAMPLE\_U8 = 0 | Unsigned 8位。 |
| AUDIOSTREAM\_SAMPLE\_S16LE = 1 | Short 16位小端。 |
| AUDIOSTREAM\_SAMPLE\_S24LE = 2 | Short 24位小端。 |
| AUDIOSTREAM\_SAMPLE\_S32LE = 3 | Short 32位小端。 |
| AUDIOSTREAM\_SAMPLE\_F32LE = 4 | Float 32位小端。  **起始版本：** 17 |

### OH\_AudioStream\_EncodingType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_EncodingType
```

**描述**

定义音频流编码类型。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_ENCODING\_TYPE\_RAW = 0 | PCM编码。 |
| AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID = 1 | Audio Vivid编码。  **起始版本：** 12 |
| AUDIOSTREAM\_ENCODING\_TYPE\_E\_AC3 = 2 | E\_AC3编码。  **起始版本：** 19 |

### OH\_AudioStream\_Usage

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_Usage
```

**描述**

定义音频流使用场景。

通常用来描述音频输出流的使用场景。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_USAGE\_UNKNOWN = 0 | 未知类型。 |
| AUDIOSTREAM\_USAGE\_MUSIC = 1 | 音乐。 |
| AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION = 2 | VoIP语音通话。 |
| AUDIOSTREAM\_USAGE\_VOICE\_ASSISTANT = 3 | 语音播报。 |
| AUDIOSTREAM\_USAGE\_ALARM = 4 | 闹钟。 |
| AUDIOSTREAM\_USAGE\_VOICE\_MESSAGE = 5 | 语音消息。 |
| AUDIOSTREAM\_USAGE\_RINGTONE = 6 | 铃声。 |
| AUDIOSTREAM\_USAGE\_NOTIFICATION = 7 | 通知。 |
| AUDIOSTREAM\_USAGE\_ACCESSIBILITY = 8 | 无障碍。 |
| AUDIOSTREAM\_USAGE\_MOVIE = 10 | 电影或视频。 |
| AUDIOSTREAM\_USAGE\_GAME = 11 | 游戏。 |
| AUDIOSTREAM\_USAGE\_AUDIOBOOK = 12 | 有声读物（包括听书、相声、评书）、听新闻、播客等。 |
| AUDIOSTREAM\_USAGE\_NAVIGATION = 13 | 导航。 |
| AUDIOSTREAM\_USAGE\_VIDEO\_COMMUNICATION = 17 | VoIP视频通话。  **起始版本：** 12 |

### OH\_AudioStream\_LatencyMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_LatencyMode
```

**描述**

定义音频时延模式。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_LATENCY\_MODE\_NORMAL = 0 | 该模式代表一个普通时延的音频流。 |
| AUDIOSTREAM\_LATENCY\_MODE\_FAST = 1 | 该模式代表一个低时延的音频流。 |

### OH\_AudioStream\_DirectPlaybackMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_DirectPlaybackMode
```

**描述**

定义音频流direct通路播放模式。

**起始版本：** 19

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_NOT\_SUPPORTED = 0 | 该模式代表不支持direct通路播放。 |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_BITSTREAM\_SUPPORTED = 1 | 该模式代表支持不解码的direct通路播放。 |
| AUDIOSTREAM\_DIRECT\_PLAYBACK\_PCM\_SUPPORTED = 2 | 该模式代表支持pcm编码的direct通路播放。 |

### OH\_AudioStream\_VolumeMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_VolumeMode
```

**描述**

定义音频流音量模式。

**起始版本：** 19

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_VOLUMEMODE\_SYSTEM\_GLOBAL = 0 | 系统级音量（默认模式）。 |
| AUDIOSTREAM\_VOLUMEMODE\_APP\_INDIVIDUAL = 1 | 应用级音量。  设置为该模式后可以通过提供的接口设置、查询应用音量。 |

### OH\_AudioStream\_State

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_State
```

**描述**

定义音频流的状态。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_STATE\_INVALID = -1 | 不合法的状态。 |
| AUDIOSTREAM\_STATE\_NEW = 0 | 新创建时的状态。 |
| AUDIOSTREAM\_STATE\_PREPARED = 1 | 准备状态。 |
| AUDIOSTREAM\_STATE\_RUNNING = 2 | 工作状态。 |
| AUDIOSTREAM\_STATE\_STOPPED = 3 | 停止状态。 |
| AUDIOSTREAM\_STATE\_RELEASED = 4 | 释放状态。 |
| AUDIOSTREAM\_STATE\_PAUSED = 5 | 暂停状态。 |

### OH\_AudioStream\_SourceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_SourceType
```

**描述**

定义音频流使用场景。

通常用来描述音频输入流的使用场景。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_SOURCE\_TYPE\_INVALID = -1 | 不合法状态。 |
| AUDIOSTREAM\_SOURCE\_TYPE\_MIC = 0 | 录音。 |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_RECOGNITION = 1 | 语音识别。 |
| AUDIOSTREAM\_SOURCE\_TYPE\_PLAYBACK\_CAPTURE = 2 | 播放录音。  **废弃版本：** 12  **替代接口：** [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION = 7 | 通话。 |
| AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_MESSAGE = 10 | 语音消息。  **起始版本：** 12 |
| AUDIOSTREAM\_SOURCE\_TYPE\_CAMCORDER = 13 | 录像。  **起始版本：** 13 |
| AUDIOSTREAM\_SOURCE\_TYPE\_UNPROCESSED = 14 | 麦克风纯净录音（系统不做任何算法处理）。  **起始版本：** 14 |
| AUDIOSTREAM\_SOURCE\_TYPE\_LIVE = 17 | 直播。  **起始版本：** 20 |

### OH\_AudioStream\_Event

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_Event
```

**描述**

定义音频事件。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioRenderer\_OutputDeviceChangeCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback)

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_EVENT\_ROUTING\_CHANGED = 0 | 音频的路由已更改。 |

### OH\_AudioInterrupt\_ForceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioInterrupt_ForceType
```

**描述**

定义音频中断类型。

当用户监听到音频中断时，将获取此信息。

此类型表示本次音频打断的操作是否已由系统强制执行，具体操作信息（如音频暂停、停止等）可通过[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint)获取。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_INTERRUPT\_FORCE = 0 | 强制打断类型，即具体操作已由系统强制执行。 |
| AUDIOSTREAM\_INTERRUPT\_SHARE = 1 | 共享打断类型，即系统不执行具体操作，通过[OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint)提示并建议应用操作，应用可自行决策下一步处理方式。 |

### OH\_AudioInterrupt\_Hint

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioInterrupt_Hint
```

**描述**

定义音频中断提示类型。

当用户监听到音频中断时，将获取此信息。

此类型表示根据焦点策略，当前需要对音频流的具体操作（如暂停、调整音量等）。

可以结合[OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype)信息，判断该操作是否已由系统强制执行。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_INTERRUPT\_HINT\_NONE = 0 | 不提示。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_RESUME = 1 | 提示音频恢复，应用可主动触发开始渲染或开始采集的相关操作。  此操作无法由系统强制执行，其对应的[OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype)一定为AUDIOSTREAM\_INTERRUPT\_SHARE类型。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_PAUSE = 2 | 提示音频暂停，暂时失去音频焦点。  后续待焦点可用时，会出现AUDIOSTREAM\_INTERRUPT\_HINT\_RESUME事件。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_STOP = 3 | 提示音频停止，彻底失去音频焦点。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_DUCK = 4 | 提示音频躲避开始，音频降低音量播放，而不会停止。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_UNDUCK = 5 | 提示音量躲避结束，音频恢复正常音量。 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_MUTE = 6 | 提示音频静音。  **起始版本：** 20 |
| AUDIOSTREAM\_INTERRUPT\_HINT\_UNMUTE = 7 | 提示音频解除静音。  **起始版本：** 20 |

### OH\_AudioInterrupt\_Mode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioInterrupt_Mode
```

**描述**

定义音频中断模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_INTERRUPT\_MODE\_SHARE = 0 | 共享模式。 |
| AUDIOSTREAM\_INTERRUPT\_MODE\_INDEPENDENT = 1 | 独立模式。 |

### OH\_AudioStream\_AudioEffectMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_AudioEffectMode
```

**描述**

定义音效模式。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| EFFECT\_NONE = 0 | 无音效模式。 |
| EFFECT\_DEFAULT = 1 | 默认音效模式。 |

### OH\_AudioStream\_FastStatus

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_FastStatus
```

**描述**

定义低时延状态。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_FASTSTATUS\_NORMAL = 0 | 普通音频流状态。 |
| AUDIOSTREAM\_FASTSTATUS\_FAST = 1 | 低时延音频流状态。 |

### OH\_AudioStream\_DeviceChangeReason

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_DeviceChangeReason
```

**描述**

流设备变更原因。

**起始版本：** 11

| 枚举项 | 描述 |
| --- | --- |
| REASON\_UNKNOWN = 0 | 未知原因。 |
| REASON\_NEW\_DEVICE\_AVAILABLE = 1 | 新设备可用。 |
| REASON\_OLD\_DEVICE\_UNAVAILABLE = 2 | 旧设备不可用。当报告此原因时，应用程序应考虑暂停音频播放。 |
| REASON\_OVERRODE = 3 | 用户或系统强制选择切换。 |
| REASON\_SESSION\_ACTIVATED = 4 | 音频会话激活触发的设备切换。  **起始版本：** 20 |
| REASON\_STREAM\_PRIORITY\_CHANGED = 5 | 更高优先级的音频流出现导致的系统设备切换。  **起始版本：** 20 |

### OH\_AudioStream\_PrivacyType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_PrivacyType
```

**描述**

用于标识对应播放音频流是否支持被其他应用录制。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_PUBLIC = 0 | 表示音频流可以被其他应用录制或屏幕投射，不包含隐私类型的流。 |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_PRIVATE = 1 | 表示音频流不可以被其他应用录制或屏幕投射。 |
| AUDIO\_STREAM\_PRIVACY\_TYPE\_SHARED = 2 | 表示音频流可以被其他应用录制或屏幕投射，包含隐私类型的流。  例如，在PRIVACY\_TYPE\_PUBLIC策略下，[AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION](capi-native-audiostream-base-h.md#oh_audiostream_usage)类型音频流不会被其他应用录制或屏幕投射。然而，在PRIVACY\_TYPE\_SHARED策略下，这些音频流将会允许被其他应用录制或屏幕投射。  **起始版本：** 21 |

### OH\_AudioData\_Callback\_Result

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioData_Callback_Result
```

**描述**

定义音频数据回调结果。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID = -1 | 表示音频数据回调结果无效，音频数据不播放。 |
| AUDIO\_DATA\_CALLBACK\_RESULT\_VALID = 0 | 表示音频数据回调结果有效，音频数据将被播放。 |

### OH\_AudioStream\_LatencyType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_LatencyType
```

**描述**

定义音频时延类型。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_LATENCY\_TYPE\_ALL = 0 | 获取包含软件与硬件在内的整体音频处理时延。 |
| AUDIOSTREAM\_LATENCY\_TYPE\_SOFTWARE = 1 | 获取软件部分的时延，包括软件侧音效处理。 |
| AUDIOSTREAM\_LATENCY\_TYPE\_HARDWARE = 2 | 获取硬件部分的时延，包括硬件抽象层（HAL） 、驱动与硬件侧音效处理。 |

### OH\_AudioStream\_PlaybackCaptureMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_PlaybackCaptureMode
```

**描述**

表示内录（录制设备内部应用的声音）的过滤类型，每种过滤类型可录制不同的播放流类型。该API暂不对外支持。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_MODE\_DEFAULT = 0x0 | 默认模式。录制大部分音频流，但不包括提示音流和隐私流。  **起始版本：** 23 |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_MODE\_MEDIA = 0x1 | 媒体模式。获取媒体、语音消息和未知流等。  **起始版本：** 23 |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_MODE\_EXCLUDING\_SELF = 0x8000 | 排除自身模式。获取除应用自身播放的音频以外的流。  **起始版本：** 23 |

### OH\_AudioStream\_PlaybackCaptureStartState

PhonePC/2in1TabletTVWearable

```
1. enum OH_AudioStream_PlaybackCaptureStartState
```

**描述**

定义内录的启动状态，该状态在调用[OH\_AudioCapturer\_RequestPlaybackCaptureStart](capi-native-audiocapturer-h.md#oh_audiocapturer_requestplaybackcapturestart)函数后异步返回。该API暂不对外支持。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_START\_STATE\_SUCCESS = 0 | 启动内录成功。  **起始版本：** 23 |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_START\_STATE\_FAILED = 1 | 启动内录失败。原因是请求焦点（根据流类型做优先级的选择）过程中被打断，或发生系统内部错误。  **起始版本：** 23 |
| AUDIOSTREAM\_PLAYBACKCAPTURE\_START\_STATE\_NOT\_AUTHORIZED = 2 | 用户未授权，启动内录失败。  **起始版本：** 23 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioRenderer\_OutputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRenderer_OutputDeviceChangeCallback)(OH_AudioRenderer* renderer, void* userData, OH_AudioStream_DeviceChangeReason reason)
```

**描述**

输出音频流设备变更的回调函数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |
| [OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason) reason | 流设备变更原因。 |

### OH\_AudioRenderer\_OnMarkReachedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRenderer_OnMarkReachedCallback)(OH_AudioRenderer* renderer, uint32_t samplePos, void* userData)
```

**描述**

到达标记位置时回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| uint32\_t samplePos | 设置目标标记位置。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

### OH\_AudioRenderer\_WriteDataWithMetadataCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AudioRenderer_WriteDataWithMetadataCallback)(OH_AudioRenderer* renderer, void* userData, void* audioData, int32_t audioDataSize, void* metadata, int32_t metadataSize)
```

**描述**

该函数指针将指向用于同时写入音频数据和元数据的回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |
| void\* audioData | 指向用户写入的音频数据的指针。 |
| int32\_t audioDataSize | 用户写入的音频数据的数据长度，以字节为单位。 |
| void\* metadata | 指向用户写入的元数据的指针。 |
| int32\_t metadataSize | 用户写入的元数据的数据长度，以字节为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 用户返回的回调函数的错误码。 |

### OH\_AudioRenderer\_OnWriteDataCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef OH_AudioData_Callback_Result (*OH_AudioRenderer_OnWriteDataCallback)(OH_AudioRenderer* renderer, void* userData, void* audioData, int32_t audioDataSize)
```

**描述**

该函数指针将指向用于写入音频数据的回调函数。

回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。

该函数的返回结果表示填充到缓冲区的数据是否有效。如果结果无效，用户填写的数据将不被播放。

回调函数结束后，音频服务会把audioData指针数据放入队列里等待播放，因此请勿在回调外再次更改audioData指向的数据，且务必保证往audioData填满audioDataSize长度的待播放数据, 否则会导致音频服务播放杂音。

参数audioDataSize可以通过[OH\_AudioStreamBuilder\_SetFrameSizeInCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback)设置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |
| void\* audioData | 指向用户写入的音频数据的指针。 |
| int32\_t audioDataSize | 用户写入的音频数据的数据长度，以字节为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioData\_Callback\_Result](capi-native-audiostream-base-h.md#oh_audiodata_callback_result) | AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID：音频数据回调结果无效，音频数据不播放。  AUDIO\_DATA\_CALLBACK\_RESULT\_VALID：音频数据回调结果有效，音频数据将被播放。 |
