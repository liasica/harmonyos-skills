---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-codecbase
title: CodecBase
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 模块 > CodecBase
category: harmonyos-references
scraped_at: 2026-04-28T08:12:00+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:df8355ef5f8c41ba2319509e57c73cb1a959944c95124a7548132d0e5f43de08
---

## 概述

PhonePC/2in1TabletTVWearable

CodecBase模块提供用于音视频封装、解封装、编解码基础功能的变量、属性以及函数。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [avcodec\_audio\_channel\_layout.h](capi-avcodec-audio-channel-layout-h.md) | 音频编解码声道布局枚举的声明。 |
| [native\_avcodec\_base.h](capi-native-avcodec-base-h.md) | 声明用于音视频封装、解封装、编解码基础功能的Native API。 |

## 媒体编解码格式

PhonePC/2in1TabletTVWearable

用于描述媒体编解码格式的名字如下表。类型是常量字符串。

| 名称 | 描述 |
| --- | --- |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC | AAC音频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC | FLAC音频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS | OPUS音频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU | G711MU音频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A | G711A音频解码器的MIME类型。  从API version 20开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_RAW | RAW音频码流的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS | VORBIS音频解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG | MP3音频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | Audio Vivid音频解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB | AMR\_NB音频解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB | AMR\_WB音频解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE | APE音频解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC | ALAC（Apple Lossless Audio Codec）音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3 | AC3（Dolby Audio Coding 3）音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_EAC3 | EAC3（Enhanced AC-3）音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1 | WMA（Windows Media Audio）V1音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2 | WMA（Windows Media Audio）V2音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO | WMA（Windows Media Audio）Pro音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM | GSM（Global System for Mobile Communications）音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS | GSM MS（Microsoft variant）音频解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_TWINVQ | TWINVQ（Transform-domain Weighted Interleave Vector Quantization）音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_ILBC | ILBC（Internet Low Bitrate Codec） 音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_TRUEHD | TRUEHD（True High Definition）音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_DVAUDIO | DVAUDIO（Digital Video Audio）音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_DTS | DTS（Digital Theater Systems）音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_AUDIO\_COOK | COOK（RealAudio Cook）音频解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC | VVC（H.266）视频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | HEVC（H.265）视频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | AVC（H.264）视频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263 | H.263视频编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VC1 | VC-1视频编解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1 | MSVIDEO1（Microsoft Video 1）视频编解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3 | WMV3视频编解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG | MJPEG（Motion JPEG）视频编解码器的MIME类型。  从API version 22开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4 | MPEG4视频编码的MIME类型，仅用于封装MPEG4视频码流使用。（API11废弃） |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2 | 视频MPEG4 Part2编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2 | 视频MPEG2编解码器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_AV1 | AV1视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP9 | VP9视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP8 | VP8视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV30 | RV30视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV40 | RV40视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_WVC1 | WVC1视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_DVVIDEO | DVVIDEO（Digital Video）视频编解码器的MIME类型。支持DV NTSC、DV PAL与DVCPRO HD。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_RAWVIDEO | RAWVIDEO视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG1 | MPEG1视频编解码器的MIME类型。  从API version 23开始支持。 |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG | JPG图片编码的MIME类型，仅用于封装JPG封面时使用。 |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_PNG | PNG图片编码的MIME类型，仅用于封装PNG封面时使用。 |
| OH\_AVCODEC\_MIMETYPE\_IMAGE\_BMP | BMP图片编码的MIME类型，仅用于封装BMP封面时使用。 |
| OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_WEBVTT | WEBVTT字幕解封装器的MIME类型。 |
| OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_SRT | SRT字幕解封装器的MIME类型。 |

## 媒体数据键值对

PhonePC/2in1TabletTVWearable

用于描述媒体数据的键值对查找表如下。键的类型是常量字符串，值的类型可以是int32\_t/int64\_t/float/double/char \*/uint8\_t \*。

使用以下key的主要接口是[OH\_AVFormat](capi-core-oh-avformat.md)，通过以下key可以进行参数配置或查询。

### 能力查询专有的键值对

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT | 在视频编码中获取长期参考帧（LTR）的最大个数的键，值类型为int32\_t。 |

### 音视频公共的键值对

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据的键，视频中表示传递SPS/PPS，音频中表示传递extraData，值类型为uint8\_t\*。该键是可选的。 |
| OH\_MD\_MAX\_INPUT\_BUFFER\_COUNT | 最大输入缓冲区个数的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_MAX\_OUTPUT\_BUFFER\_COUNT | 最大输出缓冲区个数的键，值类型int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_BITRATE | 比特率的键，值类型为int64\_t。该键用于音视频编码场景。在视频编码场景下该键是可选的。 |
| OH\_MD\_KEY\_PROFILE | 编码档次，值类型为int32\_t，请参见[OH\_AVCProfile](capi-native-avcodec-base-h.md#oh_avcprofile)，[OH\_HEVCProfile](capi-native-avcodec-base-h.md#oh_hevcprofile)，[OH\_AACProfile](capi-native-avcodec-base-h.md#oh_aacprofile)。该键是可选的。 |
| OH\_MD\_KEY\_MAX\_INPUT\_SIZE | 设置解码输入码流大小最大值的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_ENABLE\_SYNC\_MODE | 使能音视频编解码同步模式的键，值类型为int32\_t，1表示使能，0表示不使能。该键是可选的配置项，默认不配置则表示不使能同步模式，在Configure阶段使用。 |

### 视频专有的键值对

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_ED\_KEY\_TIME\_STAMP | 表示surfacebuffer时间戳的键，值类型为int64\_t。该键是可选的。（API14废弃） |
| OH\_ED\_KEY\_EOS | 表示surfacebuffer流结束符的键，值类型为int32\_t。该键是可选的。（API14废弃） |
| OH\_MD\_KEY\_WIDTH | 视频宽度的键，值类型为int32\_t。 |
| OH\_MD\_KEY\_HEIGHT | 视频高度键，值类型为int32\_t。 |
| OH\_MD\_KEY\_PIXEL\_FORMAT | 视频像素格式的键，值类型为int32\_t，请参见[OH\_AVPixelFormat](capi-native-avformat-h.md#oh_avpixelformat)。 |
| OH\_MD\_KEY\_FRAME\_RATE | 视频帧率的键，值类型为double。该键是可选的。 |
| OH\_MD\_KEY\_RANGE\_FLAG | 视频YUV值域标志的键，值类型为int32\_t，1表示full range，0表示limited range。该键是可选的。 |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | 视频色域的键，值类型为int32\_t，请参见[OH\_ColorPrimary](capi-native-avcodec-base-h.md#oh_colorprimary)，遵循H.273标准Table2。该键是可选的。 |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 视频传递函数的键，值类型为int32\_t，请参见[OH\_TransferCharacteristic](capi-native-avcodec-base-h.md#oh_transfercharacteristic)，遵循H.273标准Table3。该键是可选的。 |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 视频矩阵系数的键，值类型为int32\_t，请参见[OH\_MatrixCoefficient](capi-native-avcodec-base-h.md#oh_matrixcoefficient)，遵循H.273标准Table4。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_STRIDE | 描述视频帧宽跨距的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT | 描述视频帧高跨距的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH | 描述视频帧真实宽度的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT | 描述视频帧真实高度的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY | 使能低时延视频编解码的键，值类型为int32\_t，1表示使能，0表示不使能。该键是可选的配置项，默认不配置则表示不使能，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE | 视频编码码率模式，值类型为int32\_t，请参见[OH\_BitrateMode](capi-native-avcodec-base-h.md#oh_bitratemode)。该键是可选的。 |
| OH\_MD\_KEY\_QUALITY | 所需编码质量的键。值类型为int32\_t，此键仅适用于配置在恒定质量模式下的编码器。该键是可选的。 |
| OH\_MD\_KEY\_REQUEST\_I\_FRAME | 请求立即编码I帧的键。值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_I\_FRAME\_INTERVAL | 关键帧间隔的键，值类型为int32\_t，单位为ms。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | 使能分层编码的键，值类型为int32\_t，1表示使能，0表示不使能。该键是可选的且只用于视频编码，默认不配置则表示不使能，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | 描述图片组基本层图片的间隔大小的键，值类型为int32\_t，只在使能分层编码时生效。该键是可选的且只用于视频编码，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | 描述图片组内参考模式的键，值类型为int32\_t，请参见[OH\_TemporalGopReferenceMode](capi-native-avcodec-base-h.md#oh_temporalgopreferencemode)，只在使能分层编码时生效。该键是可选的且只用于视频编码，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | 描述长期参考帧（LTR）个数的键，值类型为int32\_t，必须在支持的值范围内使用。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | 标记当前帧为长期参考帧（LTR）的键，值类型为int32\_t，1表示被标记为长期参考帧（LTR），0表示未被标记为长期参考帧（LTR）。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | 描述当前帧参考的长期参考帧（LTR）的POC号的键，值类型为int32\_t。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_IS\_LTR | 当前[OH\_AVBuffer](capi-core-oh-avbuffer.md)中输出的码流对应的帧是否为长期参考帧（LTR）的键，值类型为int32\_t，1表示是长期参考帧（LTR），0表示不是长期参考帧（LTR）。该键是可选的且只用于视频编码，默认值为0。 |
| OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_POC | 描述帧的POC号的键，值类型为int32\_t。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX | 描述视频编码器允许的最大量化参数的键，值类型为int32\_t。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN | 描述视频编码器允许的最小量化参数的键，值类型为int32\_t。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE | 描述视频帧平均量化参数的键，值类型为int32\_t。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE | 描述视频帧平方误差的键，值类型为double。该键是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER | 如果在上一帧提交给编码器之后没有新的帧可用，则会以毫秒为单位重复提交最后一帧，值类型为int32\_t。该键只用于视频编码Surface模式，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_MAX\_COUNT | 描述编码器在没有新的帧可用的情况下，可以对之前的帧进行重复编码的最大次数，值类型为int32\_t。该键仅在OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER可用时生效，在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE | 设置视频解码器输出色彩空间的键，值类型为int32\_t。 支持的值为OH\_COLORSPACE\_BT709\_LIMIT。 |
| OH\_MD\_KEY\_ROTATION | surface旋转角度的键，旋转方向为顺时针。值类型为int32\_t，值为{0, 90, 180, 270}，默认值为0。该键只在视频解码Surface模式下使用。该键是可选的。 |
| OH\_MD\_KEY\_SCALING\_MODE | 视频缩放模式，值类型为int32\_t，请参见[OH\_ScalingMode](capi-native-avcodec-base-h.md#oh_scalingmode)。该键是可选的且只用于视频解码Surface模式。建议直接调用[OH\_NativeWindow\_NativeWindowSetScalingModeV2](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmodev2)接口进行设置。（API14废弃） |
| OH\_MD\_KEY\_VIDEO\_CROP\_TOP | 描述裁剪矩形顶部坐标（y）值的键，值类型为int32\_t。该键是可选的且只用于视频解码。 |
| OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM | 描述裁剪矩形底部坐标（y）值的键，值类型为int32\_t。该键是可选的且只用于视频解码。 |
| OH\_MD\_KEY\_VIDEO\_CROP\_LEFT | 描述裁剪矩形左坐标（x）值的键，值类型为int32\_t。该键是可选的且只用于视频解码。 |
| OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT | 描述裁剪矩形右坐标（x）值的键，值类型为int32\_t。该键是可选的且只用于视频解码。 |
| OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR | 解码器是否打开视频可变帧率功能的键，值类型为int32\_t。该键是可选的且只用于视频解码。 |
| OH\_MD\_KEY\_SQR\_FACTOR | 描述SQR码控模式的质量参数，取值范围为[0, 51]（同编码量化参数QP），值越小，编码输出码率越大，质量越好，值类型为int32\_t。该键值是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_MAX\_BITRATE | 描述SQR码控模式的最大码率，使用[OH\_AVCapability\_GetEncoderBitrateRange](capi-native-avcapability-h.md#oh_avcapability_getencoderbitraterange)方法获取取值范围（同OH\_MD\_KEY\_BITRATE），单位bps，值类型为int64\_t。该键值是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS | 描述ROI编码参数，包括ROI区域和deltaQp，值类型为char \*。该键值是可选的且只用于视频编码。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_PTS\_BASED\_RATECONTROL | 使能基于显示时间戳（PTS）的码控模式的键，值类型为int32\_t，1表示使能，0表示不使能。该键值是可选的且只用于视频编码，默认值为0。如果使能，则必须在每个视频帧中携带PTS信息，并发送到编码器。在Configure阶段使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME | 使能双向预测帧（B帧）编码的键，值类型为int32\_t：1表示使能，0表示不使能。该键是可选项，仅用于视频编码器，默认值为0。  如果使能，视频编码器将会使用B帧编码，编码后的视频在解码时解码顺序与显示顺序会不同。  对于不支持的设备，配置该键不会生效。  可通过[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME查询设备能力。  该键仅通过调用[OH\_VideoEncoder\_Configure](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)使用。 |
| OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES | 描述视频编码器支持的最大连续B帧数的键，值类型为int32\_t。注意：该键目前仅用于查询编码器能力。  使用规范如下：  1. 通过[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME查询特性支持情况。  2. 通过[OH\_AVCapability\_GetFeatureProperties](capi-native-avcapability-h.md#oh_avcapability_getfeatureproperties)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME获取OH\_AVFormat指针。  3. 通过[OH\_AVFormat\_GetIntValue](capi-native-avformat-h.md#oh_avformat_getintvalue)接口和本键获取最大B帧数。 |
| OH\_MD\_KEY\_VIDEO\_DECODER\_BLANK\_FRAME\_ON\_SHUTDOWN | 用于指定视频解码器关闭时是否输出空白帧的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。该键是可选的且仅用于视频解码Surface模式。  使能后，调用[OH\_VideoDecoder\_Stop](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_stop)接口或者[OH\_VideoDecoder\_Destroy](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_destroy)接口时，视频解码器将输出空白帧（通常为黑色）。该机制可避免因解码器突然终止导致的显示残留。 |
| OH\_MD\_KEY\_VIDEO\_NATIVE\_BUFFER\_FORMAT | 用于查询视频编解码中native buffer像素格式的键，值类型为int32\_t。  具体取值请参见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)中定义的像素格式。该键主要用于以下两种场景：  1. 视频解码：调用[OH\_VideoDecoder\_GetOutputDescription](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputdescription)接口或[OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged)，从返回的OH\_AVFormat对象中获取当前输出格式。  2. 视频编码：调用[OH\_VideoEncoder\_GetInputDescription](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputdescription)接口，从返回的OH\_AVFormat对象中获取当前输入格式。 |

### 音频专有的键值对

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 音频原始格式的键，值类型为int32\_t。请参见[OH\_BitsPerSample](capi-native-avcodec-base-h.md#oh_bitspersample)。 |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 音频通道计数键，值类型为int32\_t。 |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 音频采样率键，值类型为int32\_t。 |
| OH\_MD\_KEY\_AUDIO\_COMPRESSION\_LEVEL | 音频编解码压缩水平的键，只在音频编码使用，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 所需编码通道布局的键。值类型为int64\_t，此键仅适用于编码器。请参见[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout)。 |
| OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | 每个编码样本位数的键，值类型为int32\_t。该键是可选的。  API version 20前，FLAC编码必须设置此参数，设置为1即可；未设置此参数配置FLAC编码器时，调用OH\_AudioCodec\_Configure会返回错误码AV\_ERR\_INVALID\_VAL。该值无实际作用，不会影响编码结果。从API version 20开始，无需设置此参数。 |
| OH\_MD\_KEY\_SBR | aac sbr模式的键，值类型为int32\_t，aac编码器支持。该键是可选的。 |
| OH\_MD\_KEY\_COMPLIANCE\_LEVEL | flac兼容性等级的键，值类型为int32\_t，仅在音频编码使用。该键是可选的。 |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | aac格式的键，aac格式分为ADTS格式和LATM格式。值类型为int32\_t，aac解码器支持。该键是可选的。 |
| OH\_MD\_KEY\_IDENTIFICATION\_HEADER | vorbis标识头的键，值类型为uint8\_t\*，仅vorbis解码器支持。该键是可选的。 |
| OH\_MD\_KEY\_SETUP\_HEADER | vorbis设置头的键，值类型为uint8\_t\*，仅vorbis解码器支持。该键是可选的。 |
| OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER | 音频对象数目的键，值类型为int32\_t，只有Audio Vivid解码使用。该键是可选的。 |
| OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA | Audio Vivid元数据的键，值类型为uint8\_t\*，只有Audio Vivid解码使用。该键是可选的。 |
| OH\_MD\_KEY\_BLOCK\_ALIGN | 划分音频数据块大小的键，单位为字节，值类型为int32\_t。该键从API version 22开始支持，仅WMAV1、WMAV2、WMA PRO解码时必须配置。 |

### 封装/解封装专有的键值对

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 媒体文件中的视频轨是否为HDR Vivid的键，支持封装和解封装，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_START\_TIME | 媒体文件中第一帧起始位置开始时间的键，以微秒为单位，值类型为int64\_t。该键是可选的。 |
| OH\_MD\_KEY\_TRACK\_START\_TIME | 轨道开始时间的键，以微秒为单位，值类型为int64\_t。该键是可选的。 |
| OH\_MD\_KEY\_TRACK\_TYPE | 轨道媒体类型的键，值类型为int32\_t，请参见[OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype)。该键是可选的。 |
| OH\_MD\_KEY\_DURATION | 媒体文件持续时间的键，值类型为int64\_t。该键是可选的。 |
| OH\_MD\_KEY\_TITLE | 媒体文件标题的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_ARTIST | 艺术家的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_ALBUM | 专辑的媒体文件的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_ALBUM\_ARTIST | 专辑艺术家的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_DATE | 媒体文件日期的键，值类型为char \*，例如2024年。该键是可选的。 |
| OH\_MD\_KEY\_COMMENT | 媒体文件注释的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_GENRE | 媒体文件流派的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_COPYRIGHT | 媒体文件版权的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_LANGUAGE | 媒体文件语言的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_DESCRIPTION | 媒体文件描述的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_LYRICS | 媒体文件歌词的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_TRACK\_COUNT | 媒体文件轨道数量的键，值类型为int32\_t。该键是可选的。 |
| OH\_MD\_KEY\_BUFFER\_DURATION | AVBuffer中携带的音视频或字幕的sample对应的持续时间的键，以微秒为单位，值类型为int64\_t。该键是可选的。 |
| OH\_MD\_KEY\_DECODING\_TIMESTAMP | AVBuffer中携带的音视频或字幕的sample对应的解码时间戳的键，以微秒为单位，值类型为int64\_t。该键是可选的。 |
| OH\_MD\_KEY\_CODEC\_MIME | 编解码器[MIME](capi-codecbase.md#媒体编解码格式)类型的键，值类型为char \*。该键是可选的。 |
| OH\_MD\_KEY\_VIDEO\_SAR | 样本长宽比的键，值类型为double。 |
| OH\_MD\_KEY\_CREATION\_TIME | 媒体文件创建时间的元数据，值类型为char \*。 |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | 媒体文件轨道间参考、被参考关系，值类型为int32\_t\*。 |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | 媒体文件辅助轨类型，值类型为char \*。 |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | 媒体文件辅助轨描述信息，值类型为char \*。 |
| OH\_MD\_KEY\_BUFFER\_SKIP\_SAMPLES\_INFO | OH\_AVBuffer中携带的键，仅解封装支持。在解封装输出音频的起始、末尾帧可能携带此键。  此键对应一个10字节的uint8\_t[]类型的数组，记录的是音频文件元数据中解码后需跳过的音频采样点数。  具体结构如下：  1. 数组0~3，这4个字节表示从当前帧第一个采样点开始往后跳过的采样点数，以小端序存储uint32\_t值。  2. 数组4~7，这4个字节表示从当前帧最后一个采样点开始往前跳过的采样点数（不大于1帧采样点数），以小端序存储uint32\_t值。  3. 数组8~9，这2个字节表示保留位，默认输出为0。  该键从API version 23开始支持。 |
