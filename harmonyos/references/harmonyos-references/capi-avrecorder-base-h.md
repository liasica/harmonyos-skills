---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h
title: avrecorder_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avrecorder_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:54+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:2f964e3791b538918c59fc87975c4382f7dae21be70db4e03d8206c5c50d6a20
---

## 概述

PhonePC/2in1TabletTVWearable

定义了媒体AVRecorder的结构体和枚举。

**引用文件：** <multimedia/player\_framework/avrecorder\_base.h>

**库：** libavrecorder.so

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVRecorder\_Profile](capi-avrecorder-oh-avrecorder-profile.md) | OH\_AVRecorder\_Profile | 定义音视频录制的详细参数。 |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) | OH\_AVRecorder | 初始化AVRecorder。 |
| [OH\_AVRecorder\_Location](capi-avrecorder-oh-avrecorder-location.md) | OH\_AVRecorder\_Location | 提供媒体资源的地理位置信息。 |
| [OH\_AVRecorder\_MetadataTemplate](capi-avrecorder-oh-avrecorder-metadatatemplate.md) | OH\_AVRecorder\_MetadataTemplate | 定义元数据的基本模板。 |
| [OH\_AVRecorder\_Metadata](capi-avrecorder-oh-avrecorder-metadata.md) | OH\_AVRecorder\_Metadata | 元数据信息数据结构。 |
| [OH\_AVRecorder\_Config](capi-avrecorder-oh-avrecorder-config.md) | OH\_AVRecorder\_Config | 提供媒体AVRecorder的配置定义。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) | OH\_AVRecorder\_Range | 表示类型的范围。 |
| [OH\_AVRecorder\_EncoderInfo](capi-avrecorder-oh-avrecorder-encoderinfo.md) | OH\_AVRecorder\_EncoderInfo | 提供编码器信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVRecorder\_AudioSourceType](capi-avrecorder-base-h.md#oh_avrecorder_audiosourcetype) | OH\_AVRecorder\_AudioSourceType | AVRecorder的音频源类型。 |
| [OH\_AVRecorder\_VideoSourceType](capi-avrecorder-base-h.md#oh_avrecorder_videosourcetype) | OH\_AVRecorder\_VideoSourceType | AVRecorder的视频源类型。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) | OH\_AVRecorder\_CodecMimeType | 编码器MIME类型。 |
| [OH\_AVRecorder\_ContainerFormatType](capi-avrecorder-base-h.md#oh_avrecorder_containerformattype) | OH\_AVRecorder\_ContainerFormatType | 容器格式类型（容器格式类型的缩写是 CFT）。 |
| [OH\_AVRecorder\_State](capi-avrecorder-base-h.md#oh_avrecorder_state) | OH\_AVRecorder\_State | AVRecorder状态。 |
| [OH\_AVRecorder\_StateChangeReason](capi-avrecorder-base-h.md#oh_avrecorder_statechangereason) | OH\_AVRecorder\_StateChangeReason | AVRecorder状态变化的原因。 |
| [OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode) | OH\_AVRecorder\_FileGenerationMode | 创建录制文件的模式。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVRecorder\_OnStateChange)(OH\_AVRecorder \*recorder, OH\_AVRecorder\_State state, OH\_AVRecorder\_StateChangeReason reason, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onstatechange) | OH\_AVRecorder\_OnStateChange | 当录制状态发生变化时调用。 |
| [typedef void (\*OH\_AVRecorder\_OnError)(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onerror) | OH\_AVRecorder\_OnError | 当录制过程中发生错误时调用。 |
| [typedef void (\*OH\_AVRecorder\_OnUri)(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onuri) | OH\_AVRecorder\_OnUri | 当录制在[OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE模式时调用。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVRecorder\_AudioSourceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_AudioSourceType
```

**描述**

AVRecorder的音频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_DEFAULT = 0 | 默认音频源类型。 |
| AVRECORDER\_MIC = 1 | 麦克风音频源类型。 |
| AVRECORDER\_VOICE\_RECOGNITION = 2 | 语音识别场景的音频源。 |
| AVRECORDER\_VOICE\_COMMUNICATION = 7 | 语音通话场景的音频源。 |
| AVRECORDER\_VOICE\_MESSAGE = 10 | 短语音消息的音频源。 |
| AVRECORDER\_CAMCORDER = 13 | 相机录像的音频源。 |

### OH\_AVRecorder\_VideoSourceType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_VideoSourceType
```

**描述**

AVRecorder的视频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_SURFACE\_YUV = 0 | 原始数据Surface。 |
| AVRECORDER\_SURFACE\_ES = 1 | ES数据Surface。 |

### OH\_AVRecorder\_CodecMimeType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_CodecMimeType
```

**描述**

编码器MIME类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_VIDEO\_AVC = 2 | H.264 编码器MIME类型。 |
| AVRECORDER\_AUDIO\_AAC = 3 | AAC 编码器MIME类型。 |
| AVRECORDER\_AUDIO\_MP3 = 4 | mp3 编码器MIME类型。 |
| AVRECORDER\_AUDIO\_G711MU = 5 | G711-mulaw 编码器MIME类型。 |
| AVRECORDER\_VIDEO\_MPEG4 = 6 | MPEG4 编码器MIME类型。 |
| AVRECORDER\_VIDEO\_HEVC = 8 | H.265 编码器MIME类型。 |
| AVRECORDER\_AUDIO\_AMR\_NB = 9 | AMR\_NB 编解码器MIME类型。 |
| AVRECORDER\_AUDIO\_AMR\_WB = 10 | AMR\_WB 编解码器MIME类型。 |

### OH\_AVRecorder\_ContainerFormatType

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_ContainerFormatType
```

**描述**

容器格式类型（容器格式类型的缩写是 CFT）。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_CFT\_MPEG\_4 = 2 | 视频容器格式类型mp4。 |
| AVRECORDER\_CFT\_MPEG\_4A = 6 | 音频容器格式类型m4a。 |
| AVRECORDER\_CFT\_AMR = 8 | 音频容器格式类型amr。 |
| AVRECORDER\_CFT\_MP3 = 9 | 音频容器格式类型mp3。 |
| AVRECORDER\_CFT\_WAV = 10 | 音频容器格式类型wav。 |
| AVRECORDER\_CFT\_AAC = 11 | 音频容器格式类型aac（带ADTS头）。  **起始版本：** 20 |

### OH\_AVRecorder\_State

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_State
```

**描述**

AVRecorder状态。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_IDLE = 0 | 空闲状态。此时可以调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)方法设置录制参数，进入AVRECORDER\_PREPARED状态。 |
| AVRECORDER\_PREPARED = 1 | 准备状态。参数设置完成，此时可以调用[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)方法开始录制，进入AVRECORDER\_STARTED状态。 |
| AVRECORDER\_STARTED = 2 | 启动状态。正在录制，此时可以调用[OH\_AVRecorder\_Pause](capi-avrecorder-h.md#oh_avrecorder_pause)方法暂停录制，进入AVRECORDER\_PAUSED状态。  也可以调用[OH\_AVRecorder\_Stop](capi-avrecorder-h.md#oh_avrecorder_stop)方法结束录制，进入AVRECORDER\_STOPPED状态。 |
| AVRECORDER\_PAUSED = 3 | 暂停状态。此时可以调用[OH\_AVRecorder\_Resume](capi-avrecorder-h.md#oh_avrecorder_resume)方法继续录制，进入AVRECORDER\_STARTED状态。  也可以调用[OH\_AVRecorder\_Stop](capi-avrecorder-h.md#oh_avrecorder_stop)方法结束录制，进入AVRECORDER\_STOPPED状态。 |
| AVRECORDER\_STOPPED = 4 | 停止状态。此时可以调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)方法设置录制参数，重新进入AVRECORDER\_PREPARED状态。 |
| AVRECORDER\_RELEASED = 5 | 释放状态。录制资源释放，此时不能再进行任何操作。在任何其他状态下，均可以通过调用[OH\_AVRecorder\_Release](capi-avrecorder-h.md#oh_avrecorder_release)方法进入AVRECORDER\_RELEASED状态。 |
| AVRECORDER\_ERROR = 6 | 错误状态。当AVRecorder实例发生不可逆错误，会转换至当前状态。  切换至AVRECORDER\_ERROR状态时会伴随[OH\_AVRecorder\_OnError](capi-avrecorder-base-h.md#oh_avrecorder_onerror)事件，该事件会上报详细错误原因。  在AVRECORDER\_ERROR状态时，用户需要调用[OH\_AVRecorder\_Reset](capi-avrecorder-h.md#oh_avrecorder_reset)方法重置AVRecorder实例，或者调用[OH\_AVRecorder\_Release](capi-avrecorder-h.md#oh_avrecorder_release)方法释放资源。 |

### OH\_AVRecorder\_StateChangeReason

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_StateChangeReason
```

**描述**

AVRecorder状态变化的原因。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_USER = 0 | 用户操作导致的状态变化。 |
| AVRECORDER\_BACKGROUND = 1 | 后台操作导致的状态变化。 |

### OH\_AVRecorder\_FileGenerationMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVRecorder_FileGenerationMode
```

**描述**

创建录制文件的模式。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_APP\_CREATE = 0 | 由应用自行在沙箱中创建媒体文件。 |
| AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE = 1 | 由系统创建媒体文件，当前仅在相机录制场景下生效。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVRecorder\_OnStateChange()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder,OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData)
```

**描述**

当录制状态发生变化时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_State](capi-avrecorder-base-h.md#oh_avrecorder_state) state | 表示录制器状态。 |
| [OH\_AVRecorder\_StateChangeReason](capi-avrecorder-base-h.md#oh_avrecorder_statechangereason) reason | 录制器状态变化的原因。 |
| void \*userData | 用户特定数据的指针。 |

### OH\_AVRecorder\_OnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg,void *userData)
```

**描述**

当录制过程中发生错误时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | OH\_AVRecorder实例的指针。 |
| int32\_t errorCode | 错误码，详细说明请参见[OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode)。 |
| const char \*errorMsg | 错误信息。 |
| void \*userData | 用户特定数据的指针。 |

### OH\_AVRecorder\_OnUri()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
```

**描述**

当录制在[OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE模式下时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | OH\_AVRecorder实例的指针。 |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md) \*asset | OH\_MediaAsset实例的指针。 |
| void \*userData | 用户特定数据的指针。 |
