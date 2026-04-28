---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h
title: native_avscreen_capture_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > native_avscreen_capture_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:352cdb643e5302619c109e15fa8b59d59d5094267a7c39b0b884b50cd6b2bcad
---

## 概述

PhonePC/2in1TabletTV

声明用于运行屏幕录制通用的结构体、字符常量、枚举。

**引用文件：** <multimedia/player\_framework/native\_avscreen\_capture\_base.h>

**库：** libnative\_avscreen\_capture.so

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) | OH\_AudioCaptureInfo | 音频采样信息。  当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。 |
| [OH\_AudioEncInfo](capi-avscreencapture-oh-audioencinfo.md) | OH\_AudioEncInfo | 音频编码信息。 |
| [OH\_AudioInfo](capi-avscreencapture-oh-audioinfo.md) | OH\_AudioInfo | 音频信息。  同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。 |
| [OH\_VideoCaptureInfo](capi-avscreencapture-oh-videocaptureinfo.md) | OH\_VideoCaptureInfo | 视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。 |
| [OH\_VideoEncInfo](capi-avscreencapture-oh-videoencinfo.md) | OH\_VideoEncInfo | 视频编码参数。 |
| [OH\_VideoInfo](capi-avscreencapture-oh-videoinfo.md) | OH\_VideoInfo | 视频信息。 |
| [OH\_RecorderInfo](capi-avscreencapture-oh-recorderinfo.md) | OH\_RecorderInfo | 录制文件信息。 |
| [OH\_AVScreenCaptureConfig](capi-avscreencapture-oh-avscreencaptureconfig.md) | OH\_AVScreenCaptureConfig | 屏幕录制配置参数。 |
| [OH\_AVScreenCaptureCallback](capi-avscreencapture-oh-avscreencapturecallback.md) | OH\_AVScreenCaptureCallback | OH\_AVScreenCapture中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVScreenCapture实例中，并处理回调上报的信息，以保证OH\_AVScreenCapture的正常运行。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)、[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_Rect](capi-avscreencapture-oh-rect.md) | OH\_Rect | 定义录屏界面的宽高以及画面信息。 |
| [OH\_AudioBuffer](capi-avscreencapture-oh-audiobuffer.md) | OH\_AudioBuffer | 定义了音频数据的大小、类型、时间戳等配置信息。 |
| [OH\_AVScreenCaptureHighlightConfig](-avscreencapture-oh-avscreencapturehighlightconfig.md) | OH\_AVScreenCaptureHighlightConfig | 表示高亮边框的样式，包括高亮边框的模式、边框宽度和边框颜色。 |
| [OH\_NativeBuffer](pi-avscreencapture-avscreencapture-oh-nativebuffer.md) | OH\_NativeBuffer | 提供录屏的视频原始码流类。 |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) | OH\_AVScreenCapture | 通过OH\_AVScreenCapture可以获取视频与音频的原始码流。 |
| [OH\_AVScreenCapture\_ContentFilter](i-avscreencapture-oh-avscreencapture-contentfilter.md) | OH\_AVScreenCapture\_ContentFilter | 通过OH\_AVScreenCapture\_ContentFilter过滤音视频内容。 |
| [OH\_AVScreenCapture\_CaptureStrategy](avscreencapture-oh-avscreencapture-capturestrategy.md) | OH\_AVScreenCapture\_CaptureStrategy | 通过OH\_AVScreenCapture\_CaptureStrategy设置录屏策略。 |
| [OH\_AVScreenCapture\_UserSelectionInfo](screencapture-oh-avscreencapture-userselectioninfo.md) | OH\_AVScreenCapture\_UserSelectionInfo | 通过OH\_AVScreenCapture\_UserSelectionInfo获取用户在授权界面（选择界面）选择的参数。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CaptureMode](capi-native-avscreen-capture-base-h.md#oh_capturemode) | OH\_CaptureMode | 枚举，表示屏幕录制的不同模式。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) | OH\_AudioCaptureSourceType | 枚举，表示屏幕录制时的音频源类型。 |
| [OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat) | OH\_AudioCodecFormat | 枚举，表示音频编码格式。 |
| [OH\_VideoCodecFormat](capi-native-avscreen-capture-base-h.md#oh_videocodecformat) | OH\_VideoCodecFormat | 枚举，表示视频编码格式。 |
| [OH\_DataType](capi-native-avscreen-capture-base-h.md#oh_datatype) | OH\_DataType | 枚举，表示屏幕录制流的数据格式。 |
| [OH\_VideoSourceType](capi-native-avscreen-capture-base-h.md#oh_videosourcetype) | OH\_VideoSourceType | 枚举，表示视频源格式。当前仅支持RGBA格式。 |
| [OH\_ContainerFormatType](capi-native-avscreen-capture-base-h.md#oh_containerformattype) | OH\_ContainerFormatType | 枚举，表示屏幕录制生成的文件类型。 |
| [OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode) | OH\_AVScreenCaptureStateCode | 枚举，表示状态码。 |
| [OH\_AVScreenCaptureBufferType](capi-native-avscreen-capture-base-h.md#oh_avscreencapturebuffertype) | OH\_AVScreenCaptureBufferType | 枚举，表示buffer类型。 |
| [OH\_AVScreenCaptureFilterableAudioContent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturefilterableaudiocontent) | OH\_AVScreenCaptureFilterableAudioContent | 枚举，表示可过滤的音频类型。 |
| [OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent) | OH\_AVScreenCaptureContentChangedEvent | 枚举，表示录屏内容变更事件。 |
| [OH\_AVScreenCapture\_FillMode](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_fillmode) | OH\_AVScreenCapture\_FillMode | 图像填充模式。 |
| [OH\_ScreenCaptureHighlightMode](capi-native-avscreen-capture-base-h.md#oh_screencapturehighlightmode) | OH\_ScreenCaptureHighlightMode | 枚举，表示屏幕录制高亮边框的模式。 |
| [OH\_CapturePickerMode](capi-native-avscreen-capture-base-h.md#oh_capturepickermode) | OH\_CapturePickerMode | 枚举，表示Picker显示模式。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVScreenCaptureOnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonerror) | OH\_AVScreenCaptureOnError | 当OH\_AVScreenCapture实例运行出错时，将调用函数指针。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)替代。 |
| [typedef void (\*OH\_AVScreenCaptureOnAudioBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady, OH\_AudioCaptureSourceType type)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonaudiobufferavailable) | OH\_AVScreenCaptureOnAudioBufferAvailable | 当OH\_AVScreenCapture实例操作期间音频缓存区可用时，将调用函数指针。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [typedef void (\*OH\_AVScreenCaptureOnVideoBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonvideobufferavailable) | OH\_AVScreenCaptureOnVideoBufferAvailable | 当OH\_AVScreenCapture实例操作期间视频缓存区可用时，将调用函数指针。  从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [typedef void (\*OH\_AVScreenCapture\_OnStateChange)(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureStateCode stateCode, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange) | OH\_AVScreenCapture\_OnStateChange | 当OH\_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。 |
| [typedef void (\*OH\_AVScreenCapture\_OnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror) | OH\_AVScreenCapture\_OnError | 当OH\_AVScreenCapture实例操作期间发生错误时，将调用函数指针。 |
| [typedef void (\*OH\_AVScreenCapture\_OnBufferAvailable)(OH\_AVScreenCapture \*capture, OH\_AVBuffer \*buffer, OH\_AVScreenCaptureBufferType bufferType, int64\_t timestamp, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable) | OH\_AVScreenCapture\_OnBufferAvailable | 当OH\_AVScreenCapture实例操作期间音频或视频缓存区可用时，将调用该函数指针。 |
| [typedef void (\*OH\_AVScreenCapture\_OnDisplaySelected)(OH\_AVScreenCapture \*capture, uint64\_t displayId, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_ondisplayselected) | OH\_AVScreenCapture\_OnDisplaySelected | 当录屏事件开始时，将调用函数指针。 |
| [typedef void (\*OH\_AVScreenCapture\_OnCaptureContentChanged)(OH\_AVScreenCapture\* capture, OH\_AVScreenCaptureContentChangedEvent event, OH\_Rect\* area, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_oncapturecontentchanged) | OH\_AVScreenCapture\_OnCaptureContentChanged | 当OH\_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。 |
| [typedef void (\*OH\_AVScreenCapture\_OnUserSelected)(OH\_AVScreenCapture\* capture, OH\_AVScreenCapture\_UserSelectionInfo\* selections, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected) | OH\_AVScreenCapture\_OnUserSelected | 当用户在授权界面（选择界面）选择参数时，功能接口将参数返回给应用程序。 |

## 枚举类型说明

PhonePC/2in1TabletTV

### OH\_CaptureMode

PhonePC/2in1TabletTV

```
1. enum OH_CaptureMode
```

**描述**

枚举，表示屏幕录制的不同模式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_CAPTURE\_HOME\_SCREEN = 0 | 录制主屏幕。 |
| OH\_CAPTURE\_SPECIFIED\_SCREEN = 1 | 录制指定屏幕。 |
| OH\_CAPTURE\_SPECIFIED\_WINDOW = 2 | 录制指定窗口。 |
| OH\_CAPTURE\_INVAILD = -1 | 无效模式。 |

### OH\_AudioCaptureSourceType

PhonePC/2in1TabletTV

```
1. enum OH_AudioCaptureSourceType
```

**描述**

枚举，表示屏幕录制时的音频源类型。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_SOURCE\_INVALID = -1 | 无效音频源。 |
| OH\_SOURCE\_DEFAULT = 0 | 默认音频源，默认为麦克风。 |
| OH\_MIC = 1 | 麦克风录制的外部音频流。 |
| OH\_ALL\_PLAYBACK = 2 | 系统播放的所有内部音频流。 |
| OH\_APP\_PLAYBACK = 3 | 指定应用播放的内部音频流。 |

### OH\_AudioCodecFormat

PhonePC/2in1TabletTV

```
1. enum OH_AudioCodecFormat
```

**描述**

枚举，表示音频编码格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_AUDIO\_DEFAULT = 0 | 默认音频编码，默认为AAC\_LC。 |
| OH\_AAC\_LC = 3 | AAC\_LC音频编码。 |
| OH\_AUDIO\_CODEC\_FORMAT\_BUTT | 无效格式。 |

### OH\_VideoCodecFormat

PhonePC/2in1TabletTV

```
1. enum OH_VideoCodecFormat
```

**描述**

枚举，表示视频编码格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_VIDEO\_DEFAULT = 0 | 默认视频编码，默认为H.264。 |
| OH\_H264 = 2 | H.264。 |
| OH\_H265 = 4 | H.265/HEVC。 |
| OH\_MPEG4 = 6 | MPEG4。 |
| OH\_VP8 = 8 | VP8。 |
| OH\_VP9 = 10 | VP9。 |
| OH\_VIDEO\_CODEC\_FORMAT\_BUTT | 无效格式。 |

### OH\_DataType

PhonePC/2in1TabletTV

```
1. enum OH_DataType
```

**描述**

枚举，表示屏幕录制流的数据格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_ORIGINAL\_STREAM = 0 | 原始流格式，如YUV/RGBA/PCM等。 |
| OH\_ENCODED\_STREAM = 1 | 编码格式，如H264/AAC等。当前版本暂不支持。 |
| OH\_CAPTURE\_FILE = 2 | 保存文件格式，支持mp4。 |
| OH\_INVAILD = -1 | 无效格式。 |

### OH\_VideoSourceType

PhonePC/2in1TabletTV

```
1. enum OH_VideoSourceType
```

**描述**

枚举，表示视频源格式。当前仅支持RGBA格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_VIDEO\_SOURCE\_SURFACE\_YUV = 0 | YUV格式。当前版本暂不支持。 |
| OH\_VIDEO\_SOURCE\_SURFACE\_ES | raw格式。当前版本暂不支持。 |
| OH\_VIDEO\_SOURCE\_SURFACE\_RGBA | RGBA格式。 |
| OH\_VIDEO\_SOURCE\_BUTT | 无效格式。 |

### OH\_ContainerFormatType

PhonePC/2in1TabletTV

```
1. enum OH_ContainerFormatType
```

**描述**

枚举，表示屏幕录制生成的文件类型。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| CFT\_MPEG\_4A = 0 | 音频格式 m4a。 |
| CFT\_MPEG\_4 = 1 | 视频格式 mp4。 |

### OH\_AVScreenCaptureStateCode

PhonePC/2in1TabletTV

```
1. enum OH_AVScreenCaptureStateCode
```

**描述**

枚举，表示状态码。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREEN\_CAPTURE\_STATE\_STARTED = 0 | 已开始录屏。 |
| OH\_SCREEN\_CAPTURE\_STATE\_CANCELED = 1 | 已取消录屏。 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER = 2 | 已停止录屏。 |
| OH\_SCREEN\_CAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER = 3 | 录屏被其他录屏中断。 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL = 4 | 录屏被通话中断。 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNAVAILABLE = 5 | 麦克风不可用。 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_MUTED\_BY\_USER = 6 | 麦克风被静音。 |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER = 7 | 麦克风被取消静音。 |
| OH\_SCREEN\_CAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE = 8 | 进入隐私界面。 |
| OH\_SCREEN\_CAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE = 9 | 隐私界面退出。 |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES = 10 | 系统用户切换，录屏中断。 |

### OH\_AVScreenCaptureBufferType

PhonePC/2in1TabletTV

```
1. enum OH_AVScreenCaptureBufferType
```

**描述**

枚举，表示buffer类型。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_VIDEO = 0 | 视频数据。 |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_INNER = 1 | 内录音频数据。 |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_MIC = 2 | 麦克风音频数据。 |

### OH\_AVScreenCaptureFilterableAudioContent

PhonePC/2in1TabletTV

```
1. enum OH_AVScreenCaptureFilterableAudioContent
```

**描述**

枚举，表示可过滤的音频类型。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREEN\_CAPTURE\_NOTIFICATION\_AUDIO = 0 | 通知音。 |
| OH\_SCREEN\_CAPTURE\_CURRENT\_APP\_AUDIO = 1 | 应用自身声音。 |

### OH\_AVScreenCaptureContentChangedEvent

PhonePC/2in1TabletTV

```
1. enum OH_AVScreenCaptureContentChangedEvent
```

**描述**

枚举，表示录屏内容变更事件。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREEN\_CAPTURE\_CONTENT\_HIDE = 0 | 录屏内容变为隐藏。 |
| OH\_SCREEN\_CAPTURE\_CONTENT\_VISIBLE = 1 | 录屏内容变为可见。 |
| OH\_SCREEN\_CAPTURE\_CONTENT\_UNAVAILABLE = 2 | 录屏内容状态变化为不可用，如录屏窗口关闭。 |

### OH\_AVScreenCapture\_FillMode

PhonePC/2in1TabletTV

```
1. enum OH_AVScreenCapture_FillMode
```

**描述**

图像填充模式。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREENCAPTURE\_FILLMODE\_ASPECT\_SCALE\_FIT = 0 | 保持图像原始宽高比匹配目标图像大小，若比例不一致可能存在黑边。 |
| OH\_SCREENCAPTURE\_FILLMODE\_SCALE\_TO\_FILL = 1 | 图像拉伸匹配目标图像大小，若比例不一致图像变形。 |

### OH\_ScreenCaptureHighlightMode

PhonePC/2in1TabletTV

```
1. enum OH_ScreenCaptureHighlightMode
```

**描述**

枚举，表示屏幕录制高亮边框的模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_HIGHLIGHT\_MODE\_CLOSED = 0 | 默认模式，用方形全包边框高亮显示录制区域。 |
| OH\_HIGHLIGHT\_MODE\_CORNER\_WRAP = 1 | 用四角包裹边框高亮显示录制区域。 |

### OH\_CapturePickerMode

PhonePC/2in1TabletTV

```
1. enum OH_CapturePickerMode
```

**描述**

枚举，表示Picker显示模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_CAPTURE\_PICKER\_MODE\_WINDOW\_ONLY = 0 | 仅显示窗口模式。 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_ONLY = 1 | 仅显示屏幕模式。 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_AND\_WINDOW = 2 | 显示屏幕和窗口模式（默认模式）。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_AVScreenCaptureOnError()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCaptureOnError)(OH_AVScreenCapture *capture, int32_t errorCode)
```

**描述**

当OH\_AVScreenCapture实例运行出错时，将调用函数指针。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t errorCode | 指定错误码。 |

### OH\_AVScreenCaptureOnAudioBufferAvailable()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCaptureOnAudioBufferAvailable)(OH_AVScreenCapture *capture, bool isReady, OH_AudioCaptureSourceType type)
```

**描述**

当OH\_AVScreenCapture实例操作期间音频缓存区可用时，将调用函数指针。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool isReady | 音频缓存区是否可用。true表示音频缓存区可用，false表示音频缓存区不可用。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频源类型。 |

### OH\_AVScreenCaptureOnVideoBufferAvailable()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCaptureOnVideoBufferAvailable)(OH_AVScreenCapture *capture, bool isReady)
```

**描述**

当OH\_AVScreenCapture实例操作期间视频缓存区可用时，将调用函数指针。

从API version 12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool isReady | 视频缓存区是否可用。true表示视频缓存区可用，false表示视频缓存区不可用。 |

### OH\_AVScreenCapture\_OnStateChange()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnStateChange)(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode) stateCode | 指定状态码。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnError()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnError)(OH_AVScreenCapture *capture, int32_t errorCode, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间发生错误时，将调用函数指针。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t errorCode | 指定错误码。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnBufferAvailable()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnBufferAvailable)(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间音频或视频缓存区可用时，将调用该函数指针。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer缓存区实例的指针，该回调方法执行结束返回后，数据缓存区不再有效。 |
| [OH\_AVScreenCaptureBufferType](capi-native-avscreen-capture-base-h.md#oh_avscreencapturebuffertype) bufferType | 可用缓存区的数据类型。 |
| int64\_t timestamp | 时间戳，单位纳秒。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnDisplaySelected()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnDisplaySelected)(OH_AVScreenCapture *capture, uint64_t displayId, void *userData)
```

**描述**

当录屏事件开始时，将调用函数指针。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| uint64\_t displayId | 录屏屏幕的Id。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnCaptureContentChanged()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnCaptureContentChanged)(OH_AVScreenCapture* capture, OH_AVScreenCaptureContentChangedEvent event, OH_Rect* area, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)\* capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent) event | 录屏内容变更事件。 |
| [OH\_Rect](capi-avscreencapture-oh-rect.md)\* area | 录屏内容可见时，对应位置信息。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnUserSelected()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_AVScreenCapture_OnUserSelected)(OH_AVScreenCapture* capture, OH_AVScreenCapture_UserSelectionInfo* selections, void *userData)
```

**描述**

当用户在授权界面（选择界面）选择参数时，功能接口将参数返回给应用程序。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)\* capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_UserSelectionInfo](screencapture-oh-avscreencapture-userselectioninfo.md)\* selections | 用户在授权界面选择的录制参数信息。 |
| void \*userData | 指向用户数据的指针。 |
