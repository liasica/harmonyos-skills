---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avscreen-capture-base-h
title: native_avscreen_capture_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > native_avscreen_capture_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:29145b5b63b769d0aa4ca18826faaa3155ae2db42a7664d78b7fbbd2d1339e2b
---

## 概述

声明用于运行屏幕录制相关的结构体、字符常量、枚举、变量和函数。屏幕录制通过配置参数设置录制模式与音视频信息，通过回调函数获取录制数据、状态变更和隐私保护事件通知。支持多种录制模式（主屏幕、指定屏幕、指定窗口）、音频源类型（麦克风、内录、指定应用音频）配置及隐私保护、内容过滤等功能，适用于需要捕获屏幕画面和音频数据的应用场景。详细设计逻辑请参见[AVScreenCapture](capi-avscreencapture.md)。

**引用文件：** <multimedia/player\_framework/native\_avscreen\_capture\_base.h>

**库：** libnative\_avscreen\_capture.so

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) | OH\_AudioCaptureInfo | 音频采样信息。  当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。  同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。 |
| [OH\_AudioEncInfo](capi-avscreencapture-oh-audioencinfo.md) | OH\_AudioEncInfo | 音频编码信息。 |
| [OH\_AudioInfo](capi-avscreencapture-oh-audioinfo.md) | OH\_AudioInfo | 音频信息。  同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同，若不相同将导致录制失败。  当某类型音频的audioSampleRate和audioChannels同时为0时，将忽略该类型音频相关参数，不录制该类型音频数据。 |
| [OH\_VideoCaptureInfo](capi-avscreencapture-oh-videocaptureinfo.md) | OH\_VideoCaptureInfo | 视频录制信息。当videoFrameWidth和videoFrameHeight同时为0时，忽略视频相关参数不录制屏幕数据。 |
| [OH\_VideoEncInfo](capi-avscreencapture-oh-videoencinfo.md) | OH\_VideoEncInfo | 视频编码参数。 |
| [OH\_VideoInfo](capi-avscreencapture-oh-videoinfo.md) | OH\_VideoInfo | 视频信息。  当videoFrameWidth和videoFrameHeight同时为0时，将忽略视频相关参数，不录制屏幕数据。 |
| [OH\_RecorderInfo](capi-avscreencapture-oh-recorderinfo.md) | OH\_RecorderInfo | 录制文件信息。 |
| [OH\_AVScreenCaptureConfig](capi-avscreencapture-oh-avscreencaptureconfig.md) | OH\_AVScreenCaptureConfig | 屏幕录制配置参数。  注意：当某类型音频的audioSampleRate和audioChannels同时为0时，将忽略该类型音频参数；同时采集麦克风和内录音频时，两路音频采样参数需相同；当videoFrameWidth和videoFrameHeight同时为0时，将忽略视频参数。 |
| [OH\_PrivacyProtectInfo](capi-avscreencapture-oh-privacyprotectinfo.md) | OH\_PrivacyProtectInfo | 隐私保护信息结构体。 |
| [OH\_AVScreenCaptureCallback](capi-avscreencapture-oh-avscreencapturecallback.md) | OH\_AVScreenCaptureCallback | OH\_AVScreenCapture中所有异步回调函数指针的集合。应用将该结构体的实例注册到OH\_AVScreenCapture实例中，并处理回调上报的信息，以保证OH\_AVScreenCapture的正常运行。  从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)、[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [OH\_Rect](capi-avscreencapture-oh-rect.md) | OH\_Rect | 定义录屏界面的宽高以及画面信息。 |
| [OH\_AudioBuffer](capi-avscreencapture-oh-audiobuffer.md) | OH\_AudioBuffer | 定义了音频缓冲区数据及其大小、类型、时间戳等配置信息。 |
| [OH\_AVScreenCaptureHighlightConfig](capi-avscreencapture-oh-avscreencapturehighlightconfig.md) | OH\_AVScreenCaptureHighlightConfig | 表示高亮边框的样式，包括高亮边框的模式、边框宽度和边框颜色。 |
| [OH\_MultiDisplayCapability](capi-avscreencapture-oh-multidisplaycapability.md) | OH\_MultiDisplayCapability | 多屏幕录制能力信息。多屏场景下，用户选择的多屏幕是否支持联合录制，以及联合录制的屏幕宽度和高度。 |
| [OH\_NativeBuffer](capi-avscreencapture-avscreencapture-oh-nativebuffer.md) | OH\_NativeBuffer | 提供录屏的视频原始码流类。 |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) | OH\_AVScreenCapture | 通过OH\_AVScreenCapture可以获取视频与音频的原始码流。 |
| [OH\_AVScreenCapture\_ContentFilter](capi-avscreencapture-oh-avscreencapture-contentfilter.md) | OH\_AVScreenCapture\_ContentFilter | 通过OH\_AVScreenCapture\_ContentFilter过滤音视频内容。 |
| [OH\_AVScreenCapture\_CaptureStrategy](capi-avscreencapture-oh-avscreencapture-capturestrategy.md) | OH\_AVScreenCapture\_CaptureStrategy | 通过OH\_AVScreenCapture\_CaptureStrategy设置录屏策略。 |
| [OH\_AVScreenCapture\_UserSelectionInfo](capi-avscreencapture-oh-avscreencapture-userselectioninfo.md) | OH\_AVScreenCapture\_UserSelectionInfo | 通过OH\_AVScreenCapture\_UserSelectionInfo获取用户在授权界面（选择界面）选择的参数。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_CaptureMode](capi-native-avscreen-capture-base-h.md#oh_capturemode) | OH\_CaptureMode | 枚举，表示屏幕录制的不同模式。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) | OH\_AudioCaptureSourceType | 枚举，表示屏幕录制时的音频源类型。 |
| [OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat) | OH\_AudioCodecFormat | 枚举，表示音频编码格式。 |
| [OH\_VideoCodecFormat](capi-native-avscreen-capture-base-h.md#oh_videocodecformat) | OH\_VideoCodecFormat | 枚举，表示视频编码格式。 |
| [OH\_DataType](capi-native-avscreen-capture-base-h.md#oh_datatype) | OH\_DataType | 枚举，表示屏幕录制流的数据格式。 |
| [OH\_VideoSourceType](capi-native-avscreen-capture-base-h.md#oh_videosourcetype) | OH\_VideoSourceType | 枚举，表示视频源格式。此枚举类型当前仅支持RGBA格式。 |
| [OH\_ContainerFormatType](capi-native-avscreen-capture-base-h.md#oh_containerformattype) | OH\_ContainerFormatType | 枚举，表示屏幕录制生成的文件类型。 |
| [OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode) | OH\_AVScreenCaptureStateCode | 枚举，表示状态码。 |
| [OH\_AVScreenCaptureBufferType](capi-native-avscreen-capture-base-h.md#oh_avscreencapturebuffertype) | OH\_AVScreenCaptureBufferType | 枚举，表示buffer类型。 |
| [OH\_AVScreenCaptureFilterableAudioContent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturefilterableaudiocontent) | OH\_AVScreenCaptureFilterableAudioContent | 枚举，表示可过滤的音频类型。 |
| [OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent) | OH\_AVScreenCaptureContentChangedEvent | 枚举，表示录屏内容变更事件。 |
| [OH\_AVScreenCapture\_FillMode](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_fillmode) | OH\_AVScreenCapture\_FillMode | 枚举，图像填充模式。 |
| [OH\_ScreenCaptureHighlightMode](capi-native-avscreen-capture-base-h.md#oh_screencapturehighlightmode) | OH\_ScreenCaptureHighlightMode | 枚举，表示屏幕录制高亮边框的模式。 |
| [OH\_CapturePickerMode](capi-native-avscreen-capture-base-h.md#oh_capturepickermode) | OH\_CapturePickerMode | 枚举，表示Picker显示模式。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVScreenCaptureOnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonerror) | OH\_AVScreenCaptureOnError | 当OH\_AVScreenCapture实例运行出错时，系统将调用该函数指针通知应用程序。  从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)替代。 |
| [typedef void (\*OH\_AVScreenCaptureOnAudioBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady, OH\_AudioCaptureSourceType type)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonaudiobufferavailable) | OH\_AVScreenCaptureOnAudioBufferAvailable | 当OH\_AVScreenCapture实例操作期间音频缓冲区可用时，系统将调用该函数指针通知应用程序。  从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。OH\_AVScreenCapture\_OnBufferAvailable将音频和视频缓冲区回调统一为一个接口，通过bufferType参数区分缓冲区数据类型，同时增加了timestamp和userData参数支持，开发者无需分别注册音频和视频回调。 |
| [typedef void (\*OH\_AVScreenCaptureOnVideoBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady)](capi-native-avscreen-capture-base-h.md#oh_avscreencaptureonvideobufferavailable) | OH\_AVScreenCaptureOnVideoBufferAvailable | 当OH\_AVScreenCapture实例操作期间视频缓冲区可用时，系统将调用该函数指针通知应用程序。  从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。 |
| [typedef void (\*OH\_AVScreenCapture\_OnStateChange)(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureStateCode stateCode, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onstatechange) | OH\_AVScreenCapture\_OnStateChange | 当OH\_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。  需通过OH\_AVScreenCapture相关接口设置该回调后方可生效，未设置时回调不会被调用。  此回调通过stateCode参数返回状态码。状态变更包括录屏开始、暂停、恢复、停止、中断及隐私场景切换等，具体状态码见[OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode)。 |
| [typedef void (\*OH\_AVScreenCapture\_OnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror) | OH\_AVScreenCapture\_OnError | 当OH\_AVScreenCapture实例操作期间发生错误时，系统将调用该函数指针通知应用程序。使用前需将该回调注册到OH\_AVScreenCapture实例中。应在录屏开始前注册该错误回调以便及时处理错误。 |
| [typedef void (\*OH\_AVScreenCapture\_OnBufferAvailable)(OH\_AVScreenCapture \*capture, OH\_AVBuffer \*buffer, OH\_AVScreenCaptureBufferType bufferType, int64\_t timestamp, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable) | OH\_AVScreenCapture\_OnBufferAvailable | 当OH\_AVScreenCapture实例操作期间音频或视频缓冲区可用时，系统将调用该函数指针通知应用程序。使用前需将该回调注册到OH\_AVScreenCapture实例中。  该回调方法执行结束返回后，数据缓冲区不再有效，应用需要在回调内及时处理数据。 |
| [typedef void (\*OH\_AVScreenCapture\_OnDisplaySelected)(OH\_AVScreenCapture \*capture, uint64\_t displayId, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_ondisplayselected) | OH\_AVScreenCapture\_OnDisplaySelected | 当录屏事件开始时，将调用函数指针。使用前需将该回调注册到OH\_AVScreenCapture实例中。应在录屏开始前完成注册。 |
| [typedef void (\*OH\_AVScreenCapture\_OnCaptureContentChanged)(OH\_AVScreenCapture\* capture, OH\_AVScreenCaptureContentChangedEvent event, OH\_Rect\* area, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_oncapturecontentchanged) | OH\_AVScreenCapture\_OnCaptureContentChanged | 当OH\_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。使用前需将该回调注册到OH\_AVScreenCapture实例中。  此回调通过event参数返回内容变更事件，具体事件值参见[OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent)枚举。 |
| [typedef void (\*OH\_AVScreenCapture\_OnUserSelected)(OH\_AVScreenCapture\* capture, OH\_AVScreenCapture\_UserSelectionInfo\* selections, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onuserselected) | OH\_AVScreenCapture\_OnUserSelected | 当用户在授权界面（选择界面）选择参数时，系统通过该回调函数将用户选择的参数返回给应用程序。  需要通过相关注册方法设置到OH\_AVScreenCapture实例中。应在启动授权流程前完成注册以便接收用户选择结果。 |
| [typedef void (\*OH\_AVScreenCapture\_OnPrivacyProtect)(OH\_AVScreenCapture\* capture, OH\_PrivacyProtectInfo\* privacyProtect, void \*userData)](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onprivacyprotect) | OH\_AVScreenCapture\_OnPrivacyProtect | 当[OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)实例在运行过程中发生隐私保护事件时，将调用函数指针。 |

### 变量

| 名称 | 描述 |
| --- | --- |
| const char \* OH\_SCREEN\_CAPTURE\_CONTENT\_RECT | 获取录屏图像帧中有效内容区域信息的key。  通过此key获取到的返回值是一个int32\_t数组，单位为像素（px）。数组长度为4。数组元素定义为[top, left, width, height]，其中top表示矩形窗口左上角纵坐标，left表示矩形窗口左上角横坐标，width表示矩形窗口的宽度，height表示矩形窗口的高度。数组元素可以从[OH\_AVFormat\_GetIntBuffer](capi-native-avformat-h.md#oh_avformat_getintbuffer)中获取。  **起始版本：** 26.0.0 |

## 枚举类型说明

### OH\_CaptureMode

```c
enum OH_CaptureMode
```

**描述**

枚举，表示屏幕录制的不同模式。

根据录制需求选择合适的模式：录制主屏幕适用于全屏录制场景；录制指定屏幕适用于多屏环境下选择特定屏幕的场景；录制指定窗口适用于仅录制单个应用窗口的场景。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_CAPTURE\_HOME\_SCREEN = 0 | 录制主屏幕。 |
| OH\_CAPTURE\_SPECIFIED\_SCREEN = 1 | 录制指定屏幕。使用此模式需在OH\_AVScreenCaptureConfig中指定displayId。 |
| OH\_CAPTURE\_SPECIFIED\_WINDOW = 2 | 录制指定窗口。使用此模式需在OH\_AVScreenCaptureConfig中指定windowId。 |
| OH\_CAPTURE\_INVAILD = -1 | 无效模式。 |

### OH\_AudioCaptureSourceType

```c
enum OH_AudioCaptureSourceType
```

**描述**

枚举，表示屏幕录制时的音频源类型。

适用于不同的音频录制需求：OH\_MIC适用于需要录制外部声音（如解说、旁白）的场景；OH\_ALL\_PLAYBACK适用于需要录制系统播放的所有内部音频流（如系统音效、应用音频）的场景；OH\_APP\_PLAYBACK适用于需要仅录制指定应用播放音频的场景。

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

```c
enum OH_AudioCodecFormat
```

**描述**

枚举，表示音频编码格式。

OH\_AUDIO\_DEFAULT为默认编码，适用于大多数音视频录制场景；OH\_AAC\_LC为AAC\_LC编码，适用于需要较好音质和较小文件大小的通用音视频应用场景。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_AUDIO\_DEFAULT = 0 | 默认音频编码，默认为AAC\_LC。 |
| OH\_AAC\_LC = 3 | AAC\_LC音频编码。 |
| OH\_AUDIO\_CODEC\_FORMAT\_BUTT | 无效格式。 |

### OH\_VideoCodecFormat

```c
enum OH_VideoCodecFormat
```

**描述**

枚举，表示视频编码格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_VIDEO\_DEFAULT = 0 | 默认视频编码，默认为H.264。 |
| OH\_H264 = 2 | H.264。适用于大多数录制场景，兼容性最好，是最广泛支持的视频编码格式。 |
| OH\_H265 = 4 | H.265/HEVC。适用于对压缩效率要求高的场景，相同画质下文件更小，但兼容性低于H.264。 |
| OH\_MPEG4 = 6 | MPEG4。适用于对兼容性要求不高的场景，压缩效率低于H.264/H.265。 |
| OH\_VP8 = 8 | VP8。适用于Web场景的开源编码格式，兼容性有限。 |
| OH\_VP9 = 10 | VP9。适用于Web高清场景的开源编码格式，压缩效率优于VP8，兼容性有限。 |
| OH\_VIDEO\_CODEC\_FORMAT\_BUTT | 无效格式。 |

### OH\_DataType

```c
enum OH_DataType
```

**描述**

枚举，表示屏幕录制流的数据格式。

根据使用需求选择合适的数据格式：原始流格式适用于需要实时处理音视频数据的场景（如实时预览、流式传输）；保存文件格式适用于直接录制为文件的场景。

当前仅支持原始流格式和保存文件格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_ORIGINAL\_STREAM = 0 | 原始流格式，如YUV/RGBA/PCM等。 |
| OH\_ENCODED\_STREAM = 1 | 编码流格式，如H.264/AAC等。当前版本暂不支持。 |
| OH\_CAPTURE\_FILE = 2 | 保存文件格式，支持mp4。 |
| OH\_INVAILD = -1 | 无效格式。 |

### OH\_VideoSourceType

```c
enum OH_VideoSourceType
```

**描述**

枚举，表示视频源格式。此枚举类型当前仅支持RGBA格式。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| OH\_VIDEO\_SOURCE\_SURFACE\_YUV = 0 | YUV格式。当前版本暂不支持。 |
| OH\_VIDEO\_SOURCE\_SURFACE\_ES | raw格式。当前版本暂不支持。 |
| OH\_VIDEO\_SOURCE\_SURFACE\_RGBA | RGBA格式。 |
| OH\_VIDEO\_SOURCE\_BUTT | 无效格式。 |

### OH\_ContainerFormatType

```c
enum OH_ContainerFormatType
```

**描述**

枚举，表示屏幕录制生成的文件类型。

适用于不同的文件输出需求：CFT\_MPEG\_4A为音频格式m4a，适用于仅需要录制音频的场景；CFT\_MPEG\_4为视频格式mp4，适用于需要同时录制音视频的场景。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| CFT\_MPEG\_4A = 0 | 音频格式 m4a。 |
| CFT\_MPEG\_4 = 1 | 视频格式 mp4。 |

### OH\_AVScreenCaptureStateCode

```c
enum OH_AVScreenCaptureStateCode
```

**描述**

枚举，表示状态码。

状态码反映了录屏的生命周期变化，包括开始、暂停、恢复、停止、中断及隐私场景切换等状态，状态变更通过OH\_AVScreenCapture\_OnStateChange回调通知应用。

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
| OH\_SCREEN\_CAPTURE\_STATE\_PAUSED\_BY\_USER = 11 | 录屏已由用户暂停。  **起始版本：** 26.0.0 |
| OH\_SCREEN\_CAPTURE\_STATE\_RESUMED\_BY\_USER = 12 | 录屏已由用户恢复。  **起始版本：** 26.0.0 |
| OH\_SCREEN\_CAPTURE\_STATE\_PAUSED\_BY\_APP = 13 | 录屏已由应用程序暂停。  **起始版本：** 26.0.0 |
| OH\_SCREEN\_CAPTURE\_STATE\_RESUMED\_BY\_APP = 14 | 录屏已由应用程序恢复。  **起始版本：** 26.0.0 |

### OH\_AVScreenCaptureBufferType

```c
enum OH_AVScreenCaptureBufferType
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

```c
enum OH_AVScreenCaptureFilterableAudioContent
```

**描述**

枚举，表示可过滤的音频类型。

在录屏场景中，可通过过滤特定音频类型来控制录制内容：过滤通知音适用于避免系统通知声音干扰录屏内容的场景；过滤应用自身声音适用于仅录制应用内音频而排除其他声音的场景。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREEN\_CAPTURE\_NOTIFICATION\_AUDIO = 0 | 通知音。 |
| OH\_SCREEN\_CAPTURE\_CURRENT\_APP\_AUDIO = 1 | 应用自身声音。 |

### OH\_AVScreenCaptureContentChangedEvent

```c
enum OH_AVScreenCaptureContentChangedEvent
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

```c
enum OH_AVScreenCapture_FillMode
```

**描述**

枚举，图像填充模式。

OH\_SCREENCAPTURE\_FILLMODE\_ASPECT\_SCALE\_FIT适用于需要保持图像原始宽高比、避免变形的场景；

OH\_SCREENCAPTURE\_FILLMODE\_SCALE\_TO\_FILL适用于需要完全填充目标区域、可接受图像变形的场景。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| OH\_SCREENCAPTURE\_FILLMODE\_ASPECT\_SCALE\_FIT = 0 | 保持图像原始宽高比匹配目标图像大小，若比例不一致可能存在黑边。 |
| OH\_SCREENCAPTURE\_FILLMODE\_SCALE\_TO\_FILL = 1 | 图像拉伸匹配目标图像大小，若比例不一致可能会导致图像变形。 |

### OH\_ScreenCaptureHighlightMode

```c
enum OH_ScreenCaptureHighlightMode
```

**描述**

枚举，表示屏幕录制高亮边框的模式。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_HIGHLIGHT\_MODE\_CLOSED = 0 | 默认模式，用方形全包边框高亮显示录制区域。 |
| OH\_HIGHLIGHT\_MODE\_CORNER\_WRAP = 1 | 用四角包裹边框高亮显示录制区域。 |

### OH\_CapturePickerMode

```c
enum OH_CapturePickerMode
```

**描述**

枚举，表示Picker显示模式。

根据应用需求选择合适的Picker模式：仅显示窗口模式适用于只允许用户选择窗口进行录制的场景；仅显示屏幕模式适用于只允许用户选择整个屏幕的场景；同时显示屏幕和窗口模式为默认模式，适用于需要灵活选择录制目标的场景；仅显示应用模式适用于只允许录制单个应用的场景。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| OH\_CAPTURE\_PICKER\_MODE\_WINDOW\_ONLY = 0 | 仅显示窗口模式。 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_ONLY = 1 | 仅显示屏幕模式。 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_AND\_WINDOW = 2 | 显示屏幕和窗口模式（默认模式）。 |
| OH\_CAPTURE\_PICKER\_MODE\_APP\_ONLY = 3 | 仅显示应用模式。  **起始版本：** 26.0.0 |
| OH\_CAPTURE\_PICKER\_MODE\_WINDOW\_AND\_APP = 4 | 同时显示窗口和应用模式。  **起始版本：** 26.0.0 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_AND\_APP = 5 | 同时显示屏幕和应用模式。  **起始版本：** 26.0.0 |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_WINDOW\_AND\_APP = 6 | 同时显示屏幕、窗口和应用模式。  **起始版本：** 26.0.0 |

## 函数说明

### OH\_AVScreenCaptureOnError()

```c
typedef void (*OH_AVScreenCaptureOnError)(OH_AVScreenCapture *capture, int32_t errorCode)
```

**描述**

当OH\_AVScreenCapture实例运行出错时，系统将调用该函数指针通知应用程序。

从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnError](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onerror)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t errorCode | 指定错误码，具体错误码值及含义请参考[OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode)说明。 |

### OH\_AVScreenCaptureOnAudioBufferAvailable()

```c
typedef void (*OH_AVScreenCaptureOnAudioBufferAvailable)(OH_AVScreenCapture *capture, bool isReady, OH_AudioCaptureSourceType type)
```

**描述**

当OH\_AVScreenCapture实例操作期间音频缓冲区可用时，系统将调用该函数指针通知应用程序。

从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。OH\_AVScreenCapture\_OnBufferAvailable将音频和视频缓冲区回调统一为一个接口，通过bufferType参数区分缓冲区数据类型，同时增加了timestamp和userData参数支持，开发者无需分别注册音频和视频回调。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool isReady | 音频缓冲区是否可用。true表示音频缓冲区可用，false表示音频缓冲区不可用。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) type | 音频源类型，用于标识音频数据的来源。OH\_MIC表示麦克风音频数据；OH\_ALL\_PLAYBACK表示系统内录音频数据；OH\_APP\_PLAYBACK表示指定应用播放的音频数据。开发者应根据type值对音频数据进行相应处理。 |

### OH\_AVScreenCaptureOnVideoBufferAvailable()

```c
typedef void (*OH_AVScreenCaptureOnVideoBufferAvailable)(OH_AVScreenCapture *capture, bool isReady)
```

**描述**

当OH\_AVScreenCapture实例操作期间视频缓冲区可用时，系统将调用该函数指针通知应用程序。

从API版本12开始，推荐使用接口[OH\_AVScreenCapture\_OnBufferAvailable](capi-native-avscreen-capture-base-h.md#oh_avscreencapture_onbufferavailable)替代。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| bool isReady | 视频缓冲区是否可用。true表示视频缓冲区可用，false表示视频缓冲区不可用。 |

### OH\_AVScreenCapture\_OnStateChange()

```c
typedef void (*OH_AVScreenCapture_OnStateChange)(struct OH_AVScreenCapture *capture, OH_AVScreenCaptureStateCode stateCode, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间发生状态变更时，将调用函数指针。

需通过OH\_AVScreenCapture相关接口设置该回调后方可生效，未设置时回调不会被调用。

此回调通过stateCode参数返回状态码。状态变更包括录屏开始、暂停、恢复、停止、中断及隐私场景切换等，具体状态码见[OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode)。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureStateCode](capi-native-avscreen-capture-base-h.md#oh_avscreencapturestatecode) stateCode | 指定状态码，用于标识录屏状态的变化。常见状态包括：OH\_SCREEN\_CAPTURE\_STATE\_STARTED（录屏已开始）、OH\_SCREEN\_CAPTURE\_STATE\_CANCELED（用户取消录屏）、OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER（用户停止录屏）等。开发者应根据不同状态执行相应操作。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnError()

```c
typedef void (*OH_AVScreenCapture_OnError)(OH_AVScreenCapture *capture, int32_t errorCode, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间发生错误时，系统将调用该函数指针通知应用程序。使用前需将该回调注册到OH\_AVScreenCapture实例中。应在录屏开始前注册该错误回调以便及时处理错误。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| int32\_t errorCode | 指定错误码，具体错误码值及含义请参考[OH\_AVSCREEN\_CAPTURE\_ErrCode](capi-native-avscreen-capture-errors-h.md#oh_avscreen_capture_errcode)说明。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnBufferAvailable()

```c
typedef void (*OH_AVScreenCapture_OnBufferAvailable)(OH_AVScreenCapture *capture, OH_AVBuffer *buffer, OH_AVScreenCaptureBufferType bufferType, int64_t timestamp, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间音频或视频缓冲区可用时，系统将调用该函数指针通知应用程序。使用前需将该回调注册到OH\_AVScreenCapture实例中。

该回调方法执行结束返回后，数据缓冲区不再有效，应用需要在回调内及时处理数据。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 指向OH\_AVBuffer缓冲区实例的指针，该回调方法执行结束返回后，数据缓冲区不再有效。 |
| [OH\_AVScreenCaptureBufferType](capi-native-avscreen-capture-base-h.md#oh_avscreencapturebuffertype) bufferType | 可用缓冲区的数据类型，指示当前可用缓冲区的数据类型。  OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_VIDEO表示视频数据缓冲区可用；OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_INNER表示内录音频缓冲区可用；OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_MIC表示麦克风音频缓冲区可用。  开发者应根据bufferType类型对buffer数据进行相应处理。 |
| int64\_t timestamp | 时间戳，单位：纳秒（ns）。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnDisplaySelected()

```c
typedef void (*OH_AVScreenCapture_OnDisplaySelected)(OH_AVScreenCapture *capture, uint64_t displayId, void *userData)
```

**描述**

当录屏事件开始时，将调用函数指针。使用前需将该回调注册到OH\_AVScreenCapture实例中。应在录屏开始前完成注册。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md) \*capture | 指向OH\_AVScreenCapture实例的指针。 |
| uint64\_t displayId | 录屏屏幕的ID。用于标识用户选择的具体屏幕。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnCaptureContentChanged()

```c
typedef void (*OH_AVScreenCapture_OnCaptureContentChanged)(OH_AVScreenCapture* capture, OH_AVScreenCaptureContentChangedEvent event, OH_Rect* area, void *userData)
```

**描述**

当OH\_AVScreenCapture实例操作期间录屏内容变化时，将调用函数指针。使用前需将该回调注册到OH\_AVScreenCapture实例中。

此回调通过event参数返回内容变更事件，具体事件值参见[OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent)枚举。

**系统能力：** SystemCapability.Multimedia.Media.AVScreenCapture

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)\* capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCaptureContentChangedEvent](capi-native-avscreen-capture-base-h.md#oh_avscreencapturecontentchangedevent) event | 录屏内容变更事件，指示录屏内容的状态变化。  OH\_SCREEN\_CAPTURE\_CONTENT\_HIDE表示录屏内容变为隐藏（如进入隐私界面）；OH\_SCREEN\_CAPTURE\_CONTENT\_VISIBLE表示录屏内容从隐藏变为可见；OH\_SCREEN\_CAPTURE\_CONTENT\_UNAVAILABLE表示录屏内容不可用（如窗口关闭）。  开发者应根据不同事件类型调整录屏状态。 |
| [OH\_Rect](capi-avscreencapture-oh-rect.md)\* area | 录屏内容可见时，对应位置信息；录屏内容隐藏或不可见时，该参数无效。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnUserSelected()

```c
typedef void (*OH_AVScreenCapture_OnUserSelected)(OH_AVScreenCapture* capture, OH_AVScreenCapture_UserSelectionInfo* selections, void *userData)
```

**描述**

当用户在授权界面（选择界面）选择参数时，系统通过该回调函数将用户选择的参数返回给应用程序。

需要通过相关注册方法设置到OH\_AVScreenCapture实例中。应在启动授权流程前完成注册以便接收用户选择结果。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)\* capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_AVScreenCapture\_UserSelectionInfo](capi-avscreencapture-oh-avscreencapture-userselectioninfo.md)\* selections | 用户在授权界面选择的录制参数信息。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |

### OH\_AVScreenCapture\_OnPrivacyProtect()

```c
typedef void (*OH_AVScreenCapture_OnPrivacyProtect)(OH_AVScreenCapture* capture, OH_PrivacyProtectInfo* privacyProtect, void *userData)
```

**描述**

当[OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)实例在运行过程中发生隐私保护事件时，函数指针将调用。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVScreenCapture](capi-avscreencapture-oh-avscreencapture.md)\* capture | 指向OH\_AVScreenCapture实例的指针。 |
| [OH\_PrivacyProtectInfo](capi-avscreencapture-oh-privacyprotectinfo.md)\* privacyProtect | 隐私保护信息指针。指向包含隐私保护事件详细信息的结构体，用于处理录屏过程中的隐私保护回调事件。 |
| void \*userData | 指向应用设置该回调处理方法时提供的自定义数据的指针。 |
