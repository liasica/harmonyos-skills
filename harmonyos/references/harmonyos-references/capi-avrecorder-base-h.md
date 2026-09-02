---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-base-h
title: avrecorder_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avrecorder_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:19c2c82fd57ebbb7ac26ef050461eceba5c7884068233a043adef57ffcdd8666
---

## 概述

定义了媒体AVRecorder的结构体、枚举和回调函数。

**引用文件：** <multimedia/player\_framework/avrecorder\_base.h>

**库：** libavrecorder.so

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVRecorder\_Profile](capi-avrecorder-oh-avrecorder-profile.md) | OH\_AVRecorder\_Profile | 定义音视频录制的详细参数。通过配置音频/视频编码格式、比特率、采样率、帧率、分辨率、容器格式、HDR录制、是否启用时域可分层视频编码功能等参数，可以灵活控制录制质量和录制文件大小，适用于需要自定义录制质量、选择录制内容类型（仅音频/仅视频/音视频同时录制）、启用HDR录制或时域可分层视频编码功能的场景。  通过参数设置可以选择仅录制音频或视频，或者同时录制音视频：  1. 当 audioBitrate 或 audioChannels 为 0 时，不录制音频。  2. 当 videoFrameWidth 或 videoFrameHeight 为 0 时，不录制视频。  各参数的范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)。 |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) | OH\_AVRecorder | 音视频录制的结构体类型，用于表示AVRecorder实例，支持音视频数据的采集与录制，提供录制流程控制及回调事件监听等能力。适用于需要将音视频内容录制保存为文件的场景，如视频会议录制、屏幕录制应用、安防监控录像等。 |
| [OH\_AVRecorder\_Location](capi-avrecorder-oh-avrecorder-location.md) | OH\_AVRecorder\_Location | 提供媒体资源的地理位置信息，支持在音视频录制过程中标注纬度和经度。该结构体通过AVRecorder的[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口将经纬度信息写入录制文件的元数据中，开发者需在录制前设置该结构体的latitude和longitude参数，录制过程中地理位置信息将自动嵌入到生成的媒体文件中。适用于需要在录制结果中嵌入地理位置的场景，如在视频拍摄时标记拍摄地点、运动记录应用中标记轨迹位置、旅行日记应用中记录行程坐标等，便于后续按位置检索和分类管理媒体资源。 |
| [OH\_AVRecorder\_MetadataTemplate](capi-avrecorder-oh-avrecorder-metadatatemplate.md) | OH\_AVRecorder\_MetadataTemplate | 定义音视频录制过程中元数据的基本模板，通过键值对（key-value）形式组织元数据，适用于需要在录制输出中附加自定义元数据（如标题、作者、描述等）的场景，便于对录制文件进行分类、检索和管理。开发者可通过AVRecorder的[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口将该结构体中的元数据设置到录制输出文件中。 |
| [OH\_AVRecorder\_Metadata](capi-avrecorder-oh-avrecorder-metadata.md) | OH\_AVRecorder\_Metadata | 定义录制的元数据结构，用于描述媒体资源的体裁分类、视频旋转角度、地理位置及自定义参数等元数据信息，适用于录制过程中需要携带或读取媒体元数据的场景。 |
| [OH\_AVRecorder\_Config](capi-avrecorder-oh-avrecorder-config.md) | OH\_AVRecorder\_Config | 提供媒体AVRecorder的配置定义，用于设置音视频录制时的音频源类型、视频源类型、编码配置、输出文件URL、文件生成模式、元数据及最大录制时长参数，适用于需要自定义录制配置的场景。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) | OH\_AVRecorder\_Range | 表示AVRecorder相关参数（如比特率、帧率等）的取值范围，用于限定录制参数的可配置范围。开发者可通过[OH\_AVRecorder\_GetAvailableEncoder](capi-avrecorder-h.md#oh_avrecorder_getavailableencoder)接口获取编码器相关参数取值范围，并在min和max所界定的范围内设置参数值，以确保配置有效。 |
| [OH\_AVRecorder\_EncoderInfo](capi-avrecorder-oh-avrecorder-encoderinfo.md) | OH\_AVRecorder\_EncoderInfo | 提供AVRecorder编码器能力信息，包括编码器的MIME类型、比特率范围、帧率范围等参数，适用于在录制前查询和选择合适的音频或视频编码器配置的场景，帮助开发者根据编码器能力参数选择最优编码配置。开发者可通过[OH\_AVRecorder\_GetAvailableEncoder](capi-avrecorder-h.md#oh_avrecorder_getavailableencoder)接口获取该结构体对象。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVRecorder\_AudioSourceType](capi-avrecorder-base-h.md#oh_avrecorder_audiosourcetype) | OH\_AVRecorder\_AudioSourceType | AVRecorder的音频源类型。 |
| [OH\_AVRecorder\_VideoSourceType](capi-avrecorder-base-h.md#oh_avrecorder_videosourcetype) | OH\_AVRecorder\_VideoSourceType | AVRecorder的视频源类型。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) | OH\_AVRecorder\_CodecMimeType | 编码器MIME类型，用于指定录制时音视频数据的编码格式。编码器类型需与容器格式类型匹配使用，不匹配时将导致录制失败，具体匹配关系请参见对应编码器类型的枚举项说明。 |
| [OH\_AVRecorder\_ContainerFormatType](capi-avrecorder-base-h.md#oh_avrecorder_containerformattype) | OH\_AVRecorder\_ContainerFormatType | 容器格式类型（CFT），用于指定录制文件的封装格式。容器格式需与编码器MIME类型兼容，不兼容时将导致录制失败，各容器格式支持的编码器类型请参见对应容器格式类型的枚举项说明。 |
| [OH\_AVRecorder\_State](capi-avrecorder-base-h.md#oh_avrecorder_state) | OH\_AVRecorder\_State | AVRecorder状态，用于表示录制器在生命周期中的不同阶段，不同状态下可执行的操作不同。 |
| [OH\_AVRecorder\_StateChangeReason](capi-avrecorder-base-h.md#oh_avrecorder_statechangereason) | OH\_AVRecorder\_StateChangeReason | AVRecorder状态变化的原因，用于区分状态变化是由用户操作还是后台事件触发，便于应用根据不同原因执行相应的处理逻辑。 |
| [OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode) | OH\_AVRecorder\_FileGenerationMode | 录制文件的生成模式，用于指定媒体文件的创建方式，适用于需要选择由应用自行管理文件还是由系统自动管理文件的录制场景。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVRecorder\_OnStateChange)(OH\_AVRecorder \*recorder, OH\_AVRecorder\_State state, OH\_AVRecorder\_StateChangeReason reason, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onstatechange) | OH\_AVRecorder\_OnStateChange | 当录制状态发生变化时调用。 |
| [typedef void (\*OH\_AVRecorder\_OnError)(OH\_AVRecorder \*recorder, int32\_t errorCode, const char \*errorMsg, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onerror) | OH\_AVRecorder\_OnError | 当录制过程中发生错误时调用。 |
| [typedef void (\*OH\_AVRecorder\_OnUri)(OH\_AVRecorder \*recorder, OH\_MediaAsset \*asset, void \*userData)](capi-avrecorder-base-h.md#oh_avrecorder_onuri) | OH\_AVRecorder\_OnUri | 当录制文件的生成模式为[OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE时调用，用于通知应用获取录制生成的媒体资源。 |

## 枚举类型说明

### OH\_AVRecorder\_AudioSourceType

```c
enum OH_AVRecorder_AudioSourceType
```

**描述**

AVRecorder的音频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_DEFAULT = 0 | 默认音频源类型。适用于无需指定特定音频源类型的通用录制场景。 |
| AVRECORDER\_MIC = 1 | 麦克风音频源类型。 |
| AVRECORDER\_VOICE\_RECOGNITION = 2 | 语音识别场景的音频源。 |
| AVRECORDER\_VOICE\_COMMUNICATION = 7 | 语音通话场景的音频源。 |
| AVRECORDER\_VOICE\_MESSAGE = 10 | 语音消息的音频源。 |
| AVRECORDER\_CAMCORDER = 13 | 相机录像的音频源。 |

### OH\_AVRecorder\_VideoSourceType

```c
enum OH_AVRecorder_VideoSourceType
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

```c
enum OH_AVRecorder_CodecMimeType
```

**描述**

编码器MIME类型，用于指定录制时音视频数据的编码格式。编码器类型需与容器格式类型匹配使用，不匹配时将导致录制失败，具体匹配关系请参见对应编码器类型的枚举项说明。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_VIDEO\_AVC = 2 | H.264视频编码器MIME类型。需与mp4容器格式匹配使用。 |
| AVRECORDER\_AUDIO\_AAC = 3 | AAC音频编码器MIME类型。需与aac、mp4或m4a容器格式匹配使用。 |
| AVRECORDER\_AUDIO\_MP3 = 4 | MP3音频编码器MIME类型。需与mp3容器格式匹配使用。 |
| AVRECORDER\_AUDIO\_G711MU = 5 | G711-mulaw音频编码器MIME类型。需与wav容器格式匹配使用。 |
| AVRECORDER\_VIDEO\_MPEG4 = 6 | MPEG4视频编码器MIME类型。需与mp4容器格式匹配使用。 |
| AVRECORDER\_VIDEO\_HEVC = 8 | H.265视频编码器MIME类型。需与mp4容器格式匹配使用。 |
| AVRECORDER\_AUDIO\_AMR\_NB = 9 | AMR\_NB音频编码器MIME类型。需与amr容器格式匹配使用。 |
| AVRECORDER\_AUDIO\_AMR\_WB = 10 | AMR\_WB音频编码器MIME类型。需与amr容器格式匹配使用。 |

### OH\_AVRecorder\_ContainerFormatType

```c
enum OH_AVRecorder_ContainerFormatType
```

**描述**

容器格式类型（CFT），用于指定录制文件的封装格式。容器格式需与编码器MIME类型兼容，不兼容时将导致录制失败，各容器格式支持的编码器类型请参见对应容器格式类型的枚举项说明。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_CFT\_MPEG\_4 = 2 | 视频容器格式类型mp4。支持AAC音频编码器及MPEG4、H.264或H.265视频编码器。 |
| AVRECORDER\_CFT\_MPEG\_4A = 6 | 音频容器格式类型m4a。支持AAC音频编码器。 |
| AVRECORDER\_CFT\_AMR = 8 | 音频容器格式类型amr。支持AMR\_NB、AMR\_WB音频编码器。 |
| AVRECORDER\_CFT\_MP3 = 9 | 音频容器格式类型mp3。支持MP3音频编码器。 |
| AVRECORDER\_CFT\_WAV = 10 | 音频容器格式类型wav。支持G711-mulaw音频编码器。 |
| AVRECORDER\_CFT\_AAC = 11 | 音频容器格式类型aac（带ADTS头）。支持AAC音频编码器。  **起始版本：** 20 |

### OH\_AVRecorder\_State

```c
enum OH_AVRecorder_State
```

**描述**

AVRecorder状态，用于表示录制器在生命周期中的不同阶段，不同状态下可执行的操作不同。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_IDLE = 0 | 空闲状态，为AVRecorder实例创建后的默认初始状态。此时可以调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口设置录制参数，进入AVRECORDER\_PREPARED状态。 |
| AVRECORDER\_PREPARED = 1 | 准备状态。参数设置完成，此时可以调用[OH\_AVRecorder\_Start](capi-avrecorder-h.md#oh_avrecorder_start)接口开始录制，进入AVRECORDER\_STARTED状态。 |
| AVRECORDER\_STARTED = 2 | 启动状态。正在录制，此时可以调用[OH\_AVRecorder\_Pause](capi-avrecorder-h.md#oh_avrecorder_pause)接口暂停录制，进入AVRECORDER\_PAUSED状态。  也可以调用[OH\_AVRecorder\_Stop](capi-avrecorder-h.md#oh_avrecorder_stop)接口结束录制，进入AVRECORDER\_STOPPED状态。 |
| AVRECORDER\_PAUSED = 3 | 暂停状态。此时可以调用[OH\_AVRecorder\_Resume](capi-avrecorder-h.md#oh_avrecorder_resume)接口继续录制，进入AVRECORDER\_STARTED状态。  也可以调用[OH\_AVRecorder\_Stop](capi-avrecorder-h.md#oh_avrecorder_stop)接口结束录制，进入AVRECORDER\_STOPPED状态。 |
| AVRECORDER\_STOPPED = 4 | 停止状态。此时可以调用[OH\_AVRecorder\_Prepare](capi-avrecorder-h.md#oh_avrecorder_prepare)接口设置录制参数，重新进入AVRECORDER\_PREPARED状态。 |
| AVRECORDER\_RELEASED = 5 | 释放状态。录制资源释放，此时不能再进行任何操作。在任何其他状态下，均可以通过调用[OH\_AVRecorder\_Release](capi-avrecorder-h.md#oh_avrecorder_release)接口进入AVRECORDER\_RELEASED状态。 |
| AVRECORDER\_ERROR = 6 | 错误状态。当AVRecorder实例发生不可逆错误，会转换至该状态。  在AVRECORDER\_ERROR状态时，不能再进行录制相关操作，用户需要调用[OH\_AVRecorder\_Reset](capi-avrecorder-h.md#oh_avrecorder_reset)接口重置AVRecorder实例，或者调用[OH\_AVRecorder\_Release](capi-avrecorder-h.md#oh_avrecorder_release)接口释放资源。 |

### OH\_AVRecorder\_StateChangeReason

```c
enum OH_AVRecorder_StateChangeReason
```

**描述**

AVRecorder状态变化的原因，用于区分状态变化是由用户操作还是后台事件触发，便于应用根据不同原因执行相应的处理逻辑。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_USER = 0 | 用户操作导致的状态变化。 |
| AVRECORDER\_BACKGROUND = 1 | 后台操作导致的状态变化。 |

### OH\_AVRecorder\_FileGenerationMode

```c
enum OH_AVRecorder_FileGenerationMode
```

**描述**

录制文件的生成模式，用于指定媒体文件的创建方式，适用于需要选择由应用自行管理文件还是由系统自动管理文件的录制场景。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

| 枚举项 | 描述 |
| --- | --- |
| AVRECORDER\_APP\_CREATE = 0 | 由应用自行在沙箱中创建媒体文件，此模式下不会触发[OH\_AVRecorder\_OnUri](capi-avrecorder-base-h.md#oh_avrecorder_onuri)回调。 |
| AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE = 1 | 由系统创建媒体文件，此模式下会触发[OH\_AVRecorder\_OnUri](capi-avrecorder-base-h.md#oh_avrecorder_onuri)回调，应用可通过回调获取录制生成的媒体资源对象。 |

## 函数说明

### OH\_AVRecorder\_OnStateChange()

```c
typedef void (*OH_AVRecorder_OnStateChange)(OH_AVRecorder *recorder, OH_AVRecorder_State state, OH_AVRecorder_StateChangeReason reason, void *userData)
```

**描述**

当录制状态发生变化时调用。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | OH\_AVRecorder实例的指针。 |
| [OH\_AVRecorder\_State](capi-avrecorder-base-h.md#oh_avrecorder_state) state | 表示录制状态。 |
| [OH\_AVRecorder\_StateChangeReason](capi-avrecorder-base-h.md#oh_avrecorder_statechangereason) reason | 录制状态变化的原因。 |
| void \*userData | 用户注册回调时传入的自定义数据指针，在回调触发时由系统回传给调用方。 |

### OH\_AVRecorder\_OnError()

```c
typedef void (*OH_AVRecorder_OnError)(OH_AVRecorder *recorder, int32_t errorCode, const char *errorMsg, void *userData)
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
| const char \*errorMsg | 描述错误详情的字符串。 |
| void \*userData | 用户注册回调时传入的自定义数据指针，在回调触发时由系统回传给调用方。 |

### OH\_AVRecorder\_OnUri()

```c
typedef void (*OH_AVRecorder_OnUri)(OH_AVRecorder *recorder, OH_MediaAsset *asset, void *userData)
```

**描述**

当录制文件的生成模式为[OH\_AVRecorder\_FileGenerationMode](capi-avrecorder-base-h.md#oh_avrecorder_filegenerationmode).AVRECORDER\_AUTO\_CREATE\_CAMERA\_SCENE时调用，用于通知应用获取录制生成的媒体资源。

**系统能力：** SystemCapability.Multimedia.Media.AVRecorder

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVRecorder](capi-avrecorder-oh-avrecorder.md) \*recorder | OH\_AVRecorder实例的指针。 |
| [OH\_MediaAsset](capi-mediaassetmanager-oh-mediaasset.md) \*asset | OH\_MediaAsset实例的指针，用于返回系统自动创建的媒体资源对象，应用可通过该对象访问录制生成的媒体文件。 |
| void \*userData | 用户注册回调时传入的自定义数据指针，在回调触发时由系统回传给调用方。 |
