---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-base-h
title: native_avcodec_base.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avcodec_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:03+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ce4259d14a393c0c4630889ba383dd75b988b5ae253005888646048732aaca93
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于音视频封装、解封装、编解码基础功能的Native API。

**引用文件：** <multimedia/player\_framework/native\_avcodec\_base.h>

**库：** libnative\_media\_codecbase.so

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

**相关模块：** [CodecBase](capi-codecbase.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVCodecAsyncCallback](capi-codecbase-oh-avcodecasynccallback.md) | OH\_AVCodecAsyncCallback | OH\_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVCodec实例中，并处理回调上报的信息，以保证OH\_AVCodec的正常运行。(API11废弃) |
| [OH\_AVCodecCallback](capi-codecbase-oh-avcodeccallback.md) | OH\_AVCodecCallback | OH\_AVCodec中所有异步回调函数指针的集合。将该结构体的实例注册到OH\_AVCodec实例中，并处理回调上报的信息，以保证OH\_AVCodec的正常运行。 |
| [OH\_AVDataSource](capi-codecbase-oh-avdatasource.md) | OH\_AVDataSource | 用户自定义数据源。 |
| [OH\_AVDataSourceExt](capi-codecbase-oh-avdatasourceext.md) | OH\_AVDataSourceExt | 用户自定义数据源，回调支持通过userData传递用户自定义数据。 |
| [NativeWindow](capi-codecbase-nativewindow.md) | OHNativeWindow | 为图形接口定义native层对象。 |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) | OH\_AVCodec | 为音视频编解码接口定义native层对象。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype) | OH\_MediaType | 媒体类型。 |
| [OH\_AACProfile](capi-native-avcodec-base-h.md#oh_aacprofile) | OH\_AACProfile | AAC档次。 |
| [OH\_AVCProfile](capi-native-avcodec-base-h.md#oh_avcprofile) | OH\_AVCProfile | AVC档次。 |
| [OH\_HEVCProfile](capi-native-avcodec-base-h.md#oh_hevcprofile) | OH\_HEVCProfile | HEVC档次。 |
| [OH\_VVCProfile](capi-native-avcodec-base-h.md#oh_vvcprofile) | OH\_VVCProfile | VVC档次。 |
| [OH\_MPEG2Profile](capi-native-avcodec-base-h.md#oh_mpeg2profile) | OH\_MPEG2Profile | MPEG2档次。 |
| [OH\_MPEG4Profile](capi-native-avcodec-base-h.md#oh_mpeg4profile) | OH\_MPEG4Profile | MPEG4档次。 |
| [OH\_H263Profile](capi-native-avcodec-base-h.md#oh_h263profile) | OH\_H263Profile | H.263档次。 |
| [OH\_VC1Profile](capi-native-avcodec-base-h.md#oh_vc1profile) | OH\_VC1Profile | VC-1档次。 |
| [OH\_AV1Profile](capi-native-avcodec-base-h.md#oh_av1profile) | OH\_AV1Profile | AV1档次。 |
| [OH\_VP9Profile](capi-native-avcodec-base-h.md#oh_vp9profile) | OH\_VP9Profile | VP9档次。 |
| [OH\_WVC1Profile](capi-native-avcodec-base-h.md#oh_wvc1profile) | OH\_WVC1Profile | WVC1档次。 |
| [OH\_WMV3Profile](capi-native-avcodec-base-h.md#oh_wmv3profile) | OH\_WMV3Profile | WMV3档次。 |
| [OH\_AVOutputFormat](capi-native-avcodec-base-h.md#oh_avoutputformat) | OH\_AVOutputFormat | 封装器支持的输出文件格式。 |
| [OH\_AVSeekMode](capi-native-avcodec-base-h.md#oh_avseekmode) | OH\_AVSeekMode | 跳转模式。 |
| [OH\_ScalingMode](capi-native-avcodec-base-h.md#oh_scalingmode) | OH\_ScalingMode | 缩放模式，只在Surface模式下使用。(API14废弃) |
| [OH\_BitsPerSample](capi-native-avcodec-base-h.md#oh_bitspersample) | OH\_BitsPerSample | 每个编码样本的音频位数。 |
| [OH\_ColorPrimary](capi-native-avcodec-base-h.md#oh_colorprimary) | OH\_ColorPrimary | 色域。编解码都支持。 |
| [OH\_TransferCharacteristic](capi-native-avcodec-base-h.md#oh_transfercharacteristic) | OH\_TransferCharacteristic | 转移特性。编解码都支持。 |
| [OH\_MatrixCoefficient](capi-native-avcodec-base-h.md#oh_matrixcoefficient) | OH\_MatrixCoefficient | 矩阵系数。编解码都支持。 |
| [OH\_AVCLevel](capi-native-avcodec-base-h.md#oh_avclevel) | OH\_AVCLevel | AVC级别。 |
| [OH\_HEVCLevel](capi-native-avcodec-base-h.md#oh_hevclevel) | OH\_HEVCLevel | HEVC级别。 |
| [OH\_VVCLevel](capi-native-avcodec-base-h.md#oh_vvclevel) | OH\_VVCLevel | VVC级别。 |
| [OH\_MPEG2Level](capi-native-avcodec-base-h.md#oh_mpeg2level) | OH\_MPEG2Level | MPEG2级别。 |
| [OH\_MPEG4Level](capi-native-avcodec-base-h.md#oh_mpeg4level) | OH\_MPEG4Level | MPEG4级别。 |
| [OH\_H263Level](capi-native-avcodec-base-h.md#oh_h263level) | OH\_H263Level | H.263级别。 |
| [OH\_VC1Level](capi-native-avcodec-base-h.md#oh_vc1level) | OH\_VC1Level | VC-1级别。 |
| [OH\_AV1Level](capi-native-avcodec-base-h.md#oh_av1level) | OH\_AV1Level | AV1级别。 |
| [OH\_VP9Level](capi-native-avcodec-base-h.md#oh_vp9level) | OH\_VP9Level | VP9级别。 |
| [OH\_WVC1Level](capi-native-avcodec-base-h.md#oh_wvc1level) | OH\_WVC1Level | WVC1级别。 |
| [OH\_WMV3Level](capi-native-avcodec-base-h.md#oh_wmv3level) | OH\_WMV3Level | WMV3级别。 |
| [OH\_TemporalGopReferenceMode](capi-native-avcodec-base-h.md#oh_temporalgopreferencemode) | OH\_TemporalGopReferenceMode | 时域图片组参考模式。 |
| [OH\_BitrateMode](capi-native-avcodec-base-h.md#oh_bitratemode) | OH\_BitrateMode | 编码器的比特率模式。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_AVCodecOnError)(OH\_AVCodec \*codec, int32\_t errorCode, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconerror) | OH\_AVCodecOnError | 当OH\_AVCodec实例运行出错时，会调用来上报具体的错误信息的函数指针。 |
| [typedef void (\*OH\_AVCodecOnStreamChanged)(OH\_AVCodec \*codec, OH\_AVFormat \*format, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged) | OH\_AVCodecOnStreamChanged | 当视频解码输入码流分辨率或者视频编码输出码流的分辨率发生变化时，调用此函数指针报告新的流描述信息。  从API version 15开始，支持音频解码时，码流采样率、声道数或者音频采样格式发生变化时，将调用此函数指针报告新的流描述信息，支持检测此变化的解码格式有：Audio Vivid，AAC，FLAC，MP3，VORBIS。  需要注意的是，OH\_AVFormat指针的生命周期只有在函数指针被调用时才有效，调用结束后禁止继续访问。 |
| [typedef void (\*OH\_AVCodecOnNeedInputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata) | OH\_AVCodecOnNeedInputData | 当OH\_AVCodec在运行过程中需要新的输入数据时，将调用此函数指针，并携带可用的缓冲区来填充新的输入数据。(API11废弃) |
| [typedef void (\*OH\_AVCodecOnNewOutputData)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVMemory \*data, OH\_AVCodecBufferAttr \*attr, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputdata) | OH\_AVCodecOnNewOutputData | 当OH\_AVCodec运行过程中生成新的输出数据时，将调用此函数指针，并携带包含新输出数据的缓冲区。需要注意的是，OH\_AVCodecBufferAttr指针的生命周期仅在调用函数指针时有效，这将禁止调用结束后继续访问。(API11废弃) |
| [typedef void (\*OH\_AVCodecOnNeedInputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer) | OH\_AVCodecOnNeedInputBuffer | 当OH\_AVCodec在运行过程中需要新的输入数据时，将调用此函数指针，并携带可用的缓冲区来填充新的输入数据。 |
| [typedef void (\*OH\_AVCodecOnNewOutputBuffer)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVBuffer \*buffer, void \*userData)](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer) | OH\_AVCodecOnNewOutputBuffer | 当OH\_AVCodec运行过程中生成新的输出数据时，将调用此函数指针，并携带包含新输出数据的缓冲区。 |
| [typedef int32\_t (\*OH\_AVDataSourceReadAt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos)](capi-native-avcodec-base-h.md#oh_avdatasourcereadat) | OH\_AVDataSourceReadAt | 函数指针定义，用于提供获取用户自定义媒体数据的能力。 |
| [typedef int32\_t (\*OH\_AVDataSourceReadAtExt)(OH\_AVBuffer \*data, int32\_t length, int64\_t pos, void \*userData)](capi-native-avcodec-base-h.md#oh_avdatasourcereadatext) | OH\_AVDataSourceReadAtExt | 函数指针定义，用于提供获取用户自定义媒体数据的能力。 |

### 变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_AVC | AVC(H.264)视频编解码器的MIME类型。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AAC | AAC音频编解码器的MIME类型。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_FLAC | FLAC音频编解码器的MIME类型。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_VORBIS | VORBIS音频解码器的MIME类型。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_MPEG | MP3音频编解码器的MIME类型。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC | HEVC(H.265)视频编解码器的MIME类型。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4 | MPEG4视频编码的MIME类型，仅用于封装MPEG4视频码流使用。  **起始版本：** 10  **废弃版本：** 11  **替代接口：** OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG4\_PART2 | 视频MPEG4 Part2编解码器的MIME类型。  **起始版本：** 17  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG2 | 视频MPEG2编解码器的MIME类型。  **起始版本：** 17  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_H263 | H.263视频编解码器的MIME类型。  **起始版本：** 17  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VC1 | VC-1视频编解码器的MIME类型。  **起始版本：** 22  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_AV1 | AV1视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP9 | VP9视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VP8 | VP8视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV30 | RV30视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_RV40 | RV40视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_WVC1 | WVC1视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_DVVIDEO | DVVIDEO（Digital Video）视频编解码器的MIME类型。支持DV NTSC、DV PAL与DVCPRO HD。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_RAWVIDEO | RAWVIDEO视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MPEG1 | MPEG1视频编解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MSVIDEO1 | MSVIDEO1（Microsoft Video 1）视频编解码器的MIME类型。  **起始版本：** 22  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_WMV3 | WMV3视频编解码器的MIME类型。  **起始版本：** 22  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_MJPEG | MJPEG（Motion JPEG）视频编解码器的MIME类型。  **起始版本：** 22  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_JPG | JPG图片编码的MIME类型，仅用于封装JPG封面时使用。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_PNG | PNG图片编码的MIME类型，仅用于封装PNG封面时使用。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_IMAGE\_BMP | BMP图片编码的MIME类型，仅用于封装BMP封面时使用。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_VIVID | Audio Vivid音频解码器的MIME类型。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_NB | AMR\_NB音频编解码器的MIME类型。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AMR\_WB | AMR\_WB音频编解码器的MIME类型。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_OPUS | OPUS音频编解码器的MIME类型。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711MU | G711MU音频编解码器的MIME类型。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_ALAC | ALAC（Apple Lossless Audio Codec）音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_AC3 | AC3（Dolby Audio Coding 3）音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_EAC3 | EAC3（Enhanced AC-3）音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1 | WMA（Windows Media Audio）V1音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2 | WMA（Windows Media Audio）V2音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO | WMA（Windows Media Audio）Pro音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_MD\_KEY\_BLOCK\_ALIGN | 划分音频数据块大小的键，单位为字节，值类型为int32\_t。该键仅用于WMA（V1、V2、PRO）解码器。  允许的MIME类型包括OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV1，OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAV2和OH\_AVCODEC\_MIMETYPE\_AUDIO\_WMAPRO。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM | GSM（Global System for Mobile Communications）音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_GSM\_MS | GSM MS（Microsoft variant）音频解码器的MIME类型。  **起始版本：** 22 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_TWINVQ | TWINVQ（Transform-domain Weighted Interleave Vector Quantization）音频解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_ILBC | ILBC（Internet Low Bitrate Codec） 音频解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_TRUEHD | TRUEHD（True High Definition）音频解码器的MIME类型。  **起始版本：** 23 |
| const char \* OH\_AVCODEC\_MIMETYPE\_VIDEO\_VVC | VVC(H.266)视频编解码器的MIME类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_APE | APE音频解码器的MIME类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_SRT | SRT字幕解封装器的MIME类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_SUBTITLE\_WEBVTT | WEBVTT字幕解封装器的MIME类型。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_RAW | RAW音频码流的MIME类型。  **起始版本：** 18  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_G711A | G711A音频解码器的MIME类型。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_COOK | COOK（RealAudio Cook）音频解码器的MIME类型。  **起始版本：** 23  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_DTS | DTS（Digital Theater Systems）音频解码器的MIME类型。  **起始版本：** 23  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_AVCODEC\_MIMETYPE\_AUDIO\_DVAUDIO | DVAUDIO（Digital Video Audio）音频解码器的MIME类型。  **起始版本：** 23  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_ED\_KEY\_TIME\_STAMP | 表示surfacebuffer时间戳的键，值类型为int64\_t。  **起始版本：** 9  **废弃版本：** 14  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_ED\_KEY\_EOS | 表示surfacebuffer流结束符的键，值类型为int32\_t。  **起始版本：** 9  **废弃版本：** 14  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRACK\_TYPE | 轨道媒体类型的键，值类型为int32\_t，请参见[OH\_MediaType](capi-native-avcodec-base-h.md#oh_mediatype)。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_CODEC\_MIME | 编解码器MIME类型的键，值类型为char \*。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_DURATION | 媒体文件持续时间的键，单位为微秒，值类型为int64\_t。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_BITRATE | 比特率的键，值类型为int64\_t。可以通过能力查询接口[OH\_AVCapability\_GetEncoderBitrateRange](capi-native-avcapability-h.md#oh_avcapability_getencoderbitraterange)接口来获取取值范围。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_MAX\_INPUT\_SIZE | 设置解码输入码流大小最大值的键，值类型为int32\_t。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_WIDTH | 视频宽度的键，值类型为int32\_t。  在视频编解码流程中调用Configure接口时，使用此接口来设置视频帧的显示宽度。可以通过能力查询接口[OH\_AVCapability\_GetVideoWidthRange](capi-native-avcapability-h.md#oh_avcapability_getvideowidthrange)来获取取值范围。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_HEIGHT | 视频高度键，值类型为int32\_t。  在视频编解码流程中调用Configure接口时，使用此接口来设置视频帧的显示高度。可以通过能力查询接口[OH\_AVCapability\_GetVideoHeightRange](capi-native-avcapability-h.md#oh_avcapability_getvideoheightrange)来获取取值范围。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_PIXEL\_FORMAT | 视频像素格式的键，值类型为int32\_t，请参见[OH\_AVPixelFormat](capi-native-avformat-h.md#oh_avpixelformat)。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 音频原始格式的键，值类型为int32\_t，请参见[OH\_BitsPerSample](capi-native-avcodec-base-h.md#oh_bitspersample)。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_FRAME\_RATE | 视频帧率的键，值类型为double。该值必须大于 0。可以通过能力查询接口[OH\_AVCapability\_GetVideoFrameRateRange](capi-native-avcapability-h.md#oh_avcapability_getvideoframeraterange)来获取取值范围。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODE\_BITRATE\_MODE | 视频编码码率模式，值类型为int32\_t，请参见[OH\_BitrateMode](capi-native-avcodec-base-h.md#oh_bitratemode)。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_PROFILE | 编码档次，值类型为int32\_t，请参见[OH\_AVCProfile](capi-native-avcodec-base-h.md#oh_avcprofile)、[OH\_HEVCProfile](capi-native-avcodec-base-h.md#oh_hevcprofile)、[OH\_AACProfile](capi-native-avcodec-base-h.md#oh_aacprofile)。可以通过能力查询接口[OH\_AVCapability\_GetSupportedProfiles](capi-native-avcapability-h.md#oh_avcapability_getsupportedprofiles)来获取支持的档次。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 音频通道计数键，值类型为int32\_t。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 音频采样率键，值类型为int32\_t。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_I\_FRAME\_INTERVAL | 关键帧间隔的键，值类型为int32\_t，单位为ms。该键是可选的且只用于视频编码。  负值表示只有第一帧是关键帧，0表示所有帧都是关键帧，正值表示每(frameRate \* 设置值)/1000帧一个关键帧。默认值为1000。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ROTATION | surface旋转角度的键，旋转方向为顺时针。值类型为int32\_t，值为{0, 90, 180, 270}，默认值为0。  该键只在视频解码Surface模式下使用。  设置视频解码surface模式旋转时，推荐使用OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE键。  **起始版本：** 9  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE | 视频翻转角度的键，值类型为int32\_t，请参见[OH\_NativeBuffer\_TransformType](capi-buffer-common-h.md#oh_nativebuffer_transformtype)。  此键用于设置视频解码surface模式的翻转角度。若未指定，默认值为0 ([NATIVEBUFFER\_ROTATE\_NONE](capi-buffer-common-h.md#oh_nativebuffer_transformtype))。  此键与OH\_MD\_KEY\_ROTATION互斥。若两者同时设置，以OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE为准，推荐使用OH\_MD\_KEY\_VIDEO\_TRANSFORM\_TYPE键。  注意：OH\_NativeBuffer\_TransformType中指定的角度表示逆时针旋转，这与OH\_MD\_KEY\_ROTATION定义的旋转方向相反。  对应关系如下:  - [NATIVEBUFFER\_ROTATE\_NONE](capi-buffer-common-h.md#oh_nativebuffer_transformtype)等同于OH\_MD\_KEY\_ROTATION = 0。  - [NATIVEBUFFER\_ROTATE\_90](capi-buffer-common-h.md#oh_nativebuffer_transformtype)等同于OH\_MD\_KEY\_ROTATION = 270。  - [NATIVEBUFFER\_ROTATE\_180](capi-buffer-common-h.md#oh_nativebuffer_transformtype)等同于OH\_MD\_KEY\_ROTATION = 180。  - [NATIVEBUFFER\_ROTATE\_270](capi-buffer-common-h.md#oh_nativebuffer_transformtype)等同于OH\_MD\_KEY\_ROTATION = 90。  **起始版本：** 22 |
| const char \* OH\_MD\_KEY\_RANGE\_FLAG | 视频YUV值域标志的键，值类型为int32\_t，1表示full range，0表示limited range，默认值为0。配置非0值将按照配置1处理，表示full range。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_COLOR\_PRIMARIES | 视频色域的键，值类型为int32\_t，默认值为COLOR\_PRIMARY\_UNSPECIFIED。请参见[OH\_ColorPrimary](capi-native-avcodec-base-h.md#oh_colorprimary)，遵循H.273标准Table2。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 视频传递函数的键，值类型为int32\_t，默认值为TRANSFER\_CHARACTERISTIC\_UNSPECIFIED。请参见[OH\_TransferCharacteristic](capi-native-avcodec-base-h.md#oh_transfercharacteristic)，遵循H.273标准Table3。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 视频矩阵系数的键，值类型为int32\_t，默认值为MATRIX\_COEFFICIENT\_UNSPECIFIED。请参见[OH\_MatrixCoefficient](capi-native-avcodec-base-h.md#oh_matrixcoefficient)，遵循H.273标准Table4。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_REQUEST\_I\_FRAME | 请求立即编码I帧的键。值类型为int32\_t。在调用[OH\_VideoEncoder\_SetParameter](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_setparameter)阶段使用，或随帧立即生效。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_QUALITY | 所需编码质量的键。值类型为int32\_t，默认值为50。在H.264、H.265编码场景值范围可以通过能力查询接口[OH\_AVCapability\_GetEncoderQualityRange](capi-native-avcapability-h.md#oh_avcapability_getencoderqualityrange)来获取取值范围，此键仅适用于配置在恒定质量模式下的编码器。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据的键，视频中表示传递SPS/PPS，音频中表示传递extraData，值类型为uint8\_t\*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TITLE | 媒体文件标题的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ARTIST | 媒体文件艺术家的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ALBUM | 专辑的媒体文件的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ALBUM\_ARTIST | 专辑艺术家的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_DATE | 媒体文件日期的键，值类型为char \*，例如2024年。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_COMMENT | 媒体文件注释的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ENABLE\_MOOV\_FRONT | 媒体文件moov元数据是否前置标志，值类型为int32\_t, 1表示前置， 0表示不前置, 默认为0。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_GENRE | 媒体文件流派的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_COPYRIGHT | 媒体文件版权的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_LANGUAGE | 媒体文件语言的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_DESCRIPTION | 媒体文件描述的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_LYRICS | 媒体文件歌词的键，值类型为char \*。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRACK\_COUNT | 媒体文件轨道数量的键，值类型为int32\_t。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_CHANNEL\_LAYOUT | 所需编码通道布局的键。值类型为int64\_t，此键仅适用于编码器。请参见[OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout)。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | 每个编码样本位数的键，值类型为int32\_t。  API version 20前，FLAC编码必须设置此参数，设置为1即可；未设置此参数配置FLAC编码器时，调用OH\_AudioCodec\_Configure会返回错误码AV\_ERR\_INVALID\_VAL。该值无实际作用，不会影响编码结果。  从API version 20开始，无需设置此参数。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AAC\_IS\_ADTS | aac格式的键，aac格式分为ADTS格式和LATM格式。值类型为int32\_t，0表示LATM格式，1表示ADTS格式。aac解码器支持。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_SBR | aac sbr模式的键，值类型为int32\_t，aac编码器支持。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_COMPLIANCE\_LEVEL | flac兼容性等级的键，值类型为int32\_t，仅在音频编码使用。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_IDENTIFICATION\_HEADER | vorbis标识头的键，值类型为uint8\_t\*，仅vorbis解码器支持。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_SETUP\_HEADER | vorbis设置头的键，值类型为uint8\_t\*，仅vorbis解码器支持。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_SCALING\_MODE | 视频缩放模式，值类型为int32\_t，请参见[OH\_ScalingMode](capi-native-avcodec-base-h.md#oh_scalingmode)。  建议直接调用[OH\_NativeWindow\_NativeWindowSetScalingModeV2](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmodev2)接口进行设置。该键是可选的且只用于视频解码Surface模式。  **起始版本：** 10  **废弃版本：** 14  **替代接口：** [OH\_NativeWindow\_NativeWindowSetScalingModeV2](capi-external-window-h.md#oh_nativewindow_nativewindowsetscalingmodev2)  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_MAX\_INPUT\_BUFFER\_COUNT | 最大输入缓冲区个数的键，值类型为int32\_t。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_MAX\_OUTPUT\_BUFFER\_COUNT | 最大输出缓冲区个数的键，值类型int32\_t。  **起始版本：** 10  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUDIO\_COMPRESSION\_LEVEL | 音频编解码压缩水平的键，只在音频编码使用，值类型为int32\_t。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 媒体文件中的视频轨是否为HDR Vivid的键，支持封装和解封装，值类型为int32\_t。  1表示是HDR Vivid视频轨，0表示不是HDR Vivid视频轨。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUDIO\_OBJECT\_NUMBER | 音频对象数目的键. 值类型为int32\_t，只有Audio Vivid解码使用。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_AUDIO\_VIVID\_METADATA | Audio Vivid元数据的键，值类型为uint8\_t\*，只有Audio Vivid解码使用。  **起始版本：** 11  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_FEATURE\_PROPERTY\_KEY\_VIDEO\_ENCODER\_MAX\_LTR\_FRAME\_COUNT | 在视频编码中获取长期参考帧的最大个数的键，值类型为int32\_t。  可以通过[OH\_AVCapability\_GetFeatureProperties](capi-native-avcapability-h.md#oh_avcapability_getfeatureproperties)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature)中的VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE来查询这个最大值。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY | 使能分层编码的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。  使用前可以通过[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature)中的VIDEO\_ENCODER\_TEMPORAL\_SCALABILITY来查询当前视频编码器是否支持分层编码。  详情请参见：[时域可分层视频编码](../harmonyos-guides/video-encoding-temporal-scalability.md#接口介绍)。  该键是可选的且只用于视频编码，在Configure阶段使用。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_SIZE | 描述图片组基本层图片的间隔大小的键，值类型为int32\_t，只在使能分层编码时生效。  该键是可选的且只用于视频编码，在Configure阶段使用。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_TEMPORAL\_GOP\_REFERENCE\_MODE | 描述图片组内参考模式的键，值类型为int32\_t，请参见[OH\_TemporalGopReferenceMode](capi-native-avcodec-base-h.md#oh_temporalgopreferencemode)，只在使能分层编码时生效。  该键是可选的且只用于视频编码，在Configure阶段使用。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT | 描述长期参考帧个数的键，值类型为int32\_t，必须在支持的值范围内使用。  使用前可以通过[OH\_AVCapability\_GetFeatureProperties](capi-native-avcapability-h.md#oh_avcapability_getfeatureproperties)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature)中的VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE来查询支持的LTR数目。  该键是可选的且只用于视频编码，在Configure阶段使用。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_MARK\_LTR | 标记当前帧为长期参考帧的键，值类型为int32\_t，1表示被标记，0表示未被标记，默认值为0。配置非0值将按照配置1处理，表示被标记。  只在长期参考帧个数被配置后生效。  该键是可选的且只用于视频编码输入轮转中，配置后立即生效。  详情请参见：[时域可分层视频编码](../harmonyos-guides/video-encoding-temporal-scalability.md#接口介绍)。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_PER\_FRAME\_USE\_LTR | 描述当前帧参考的长期参考帧帧的POC号的键，值类型为int32\_t。  该键是可选的且只用于视频编码输入轮转中，配置后立即生效。  详情请参见：[时域可分层视频编码](../harmonyos-guides/video-encoding-temporal-scalability.md#接口介绍)。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_IS\_LTR | 当前OH\_AVBuffer中输出的码流对应的帧是否为长期参考帧的键，值类型为int32\_t，1表示是LTR，0表示不是LTR，默认值为0。配置非0值将按照配置1处理，表示是LTR。  该键是可选的且只用于视频编码输出轮转中。  表示帧的属性。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_PER\_FRAME\_POC | 描述帧的POC的键，值类型为int32\_t。  该键是可选的且只用于视频编码输出轮转中。  表示帧的属性。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_TOP | 描述裁剪矩形顶部坐标(y)值的键，值类型为int32\_t。  包含裁剪框顶部的行，行索引从0开始。  该键只用于视频解码。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_BOTTOM | 描述裁剪矩形底部坐标(y)值的键，值类型为int32\_t。  包含裁剪框底部的行，行索引从0开始。  该键只用于视频解码。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_LEFT | 描述裁剪矩形左坐标(x)值的键，值类型为int32\_t。  包含裁剪框最左边的列，列索引从0开始。  该键只用于视频解码。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_CROP\_RIGHT | 描述裁剪矩形右坐标(x)值的键，值类型为int32\_t。  包含裁剪框最右边的列，列索引从0开始。  该键只用于视频解码。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_STRIDE | 描述视频帧宽跨距的键，值类型为int32\_t。  宽跨距是像素的索引与正下方像素的索引之间的差。  对于YUV420格式，宽跨距对应于Y平面，U和V平面的跨距可以根据颜色格式计算，但通常未定义，并且取决于设备和版本。  使用指导请参见：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-3”。  width、height、wStride、hStride图像排布与使用示例请参考：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-8”或[视频解码Buffer模式](../harmonyos-guides/video-decoding.md#buffer模式)“步骤-11”。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_SLICE\_HEIGHT | 描述视频帧高跨距的键，值类型为int32\_t。  高跨距是指从Y平面顶部到U平面顶部必须偏移的行数。本质上，U平面的偏移量是sliceHeight \* stride。  U/V平面的高度可以根据颜色格式计算，尽管它通常是未定义的，并且取决于设备和版本。  使用指导请参见：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-3”。  width、height、wStride、hStride图像排布与使用示例请参考：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-8”或[视频解码Buffer模式](../harmonyos-guides/video-decoding.md#buffer模式)“步骤-11”。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_PIC\_WIDTH | 描述视频帧真实宽度的键，值类型为int32\_t。  视频解码时调用[OH\_VideoDecoder\_GetOutputDescription](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputdescription)接口，可以从其返回的OH\_AVFormat中解析出宽度值。  当解码输出码流或编码输入图像分辨率变化时，也可从[OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged)返回的OH\_AVFormat实例中解析出宽度值。  从OH\_AVFormat实例中解析出来的是对齐后的宽、高与调用Configure接口设置的OH\_MD\_KEY\_WIDTH、OH\_MD\_KEY\_HEIGHT不一样。  width、height、wStride、hStride图像排布与使用示例请参考：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-8”或[视频解码Buffer模式](../harmonyos-guides/video-decoding.md#buffer模式)“步骤-11”。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_PIC\_HEIGHT | 描述视频帧真实高度的键，值类型为int32\_t。  视频解码时调用[OH\_VideoDecoder\_GetOutputDescription](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputdescription)接口，可以从其返回的OH\_AVFormat中解析出高度值。  当解码输出码流或编码输入图像分辨率变化时，也可从[OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged)返回的OH\_AVFormat实例中解析出高度值。  从OH\_AVFormat实例中解析出来的是对齐后的宽、高与调用Configure接口设置的OH\_MD\_KEY\_WIDTH、OH\_MD\_KEY\_HEIGHT不一样。  width、height、wStride、hStride图像排布与使用示例请参考：[视频编码Buffer模式](../harmonyos-guides/video-encoding.md#buffer模式)的“步骤-8”或[视频解码Buffer模式](../harmonyos-guides/video-decoding.md#buffer模式)“步骤-11”。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENABLE\_LOW\_LATENCY | 使能低时延视频解码的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。  该键是可选的，在Configure阶段使用。  如果使能，则视频解码器持有的输入和输出数据不会超过解码器标准所要求的数量。  可以通过能力查询接口[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)来查询特定解码器是否支持低时延。若解码器支持，使能此接口时，视频解码器将按照解码序输出帧。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MAX | 描述视频编码器允许的最大量化参数的键，值类型为int32\_t。  在Configure/SetParameter阶段使用，或随帧立即生效。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_MIN | 描述视频编码器允许的最小量化参数的键，值类型为int32\_t。  在Configure/SetParameter阶段使用，或随帧立即生效。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_QP\_AVERAGE | 描述视频帧平均量化参数的键，值类型为int32\_t。  表示当前帧编码块的平均qp值，随[OH\_AVBuffer](capi-core-oh-avbuffer.md)输出。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_MSE | 描述视频帧平方误差的键，值类型为double。  表示当前帧编码块的MSE统计值，随[OH\_AVBuffer](capi-core-oh-avbuffer.md)输出。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_DECODING\_TIMESTAMP | AVBuffer中携带的音视频或字幕的sample对应的解码时间戳的键，以微秒为单位，值类型为int64\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_BUFFER\_DURATION | AVBuffer中携带的音视频或字幕的sample对应的持续时间的键，以微秒为单位，值类型为int64\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_SAR | 样本长宽比的键，值类型为double。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_START\_TIME | 媒体文件中第一帧起始位置开始时间的键，以微秒为单位，值类型为int64\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRACK\_START\_TIME | 轨道开始时间的键，以微秒为单位，值类型为int64\_t。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_COLOR\_SPACE | 设置视频解码器输出色彩空间的键，值类型为int32\_t。  支持的值为OH\_COLORSPACE\_BT709\_LIMIT，请参见[OH\_NativeBuffer\_ColorSpace](capi-buffer-common-h.md#oh_nativebuffer_colorspace)。  在视频解码调用[OH\_VideoDecoder\_Configure](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)接口时使用此接口。  在启动OH\_VideoDecoder\_Start接口前，必须要先调用OH\_VideoDecoder\_Prepare接口。  如果支持色彩空间转换功能并配置了此键，则视频解码器会自动将HDR Vivid视频转码为指定的色彩空间。  如果不支持色彩空间转换功能，则接口[OH\_VideoDecoder\_Configure](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_configure)返回错误码[OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode)中的AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION。如果输入视频不是HDR Vivid视频，则会通过回调函数[OH\_AVCodecOnError](capi-native-avcodec-base-h.md#oh_avcodeconerror)报告错误[OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode)中的AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION。  **起始版本：** 12  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_OUTPUT\_ENABLE\_VRR | 解码器是否打开视频可变帧率功能的键，值类型为int32\_t。  1代表使能视频可变帧率功能，0代表不使能。  **起始版本：** 15  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_CREATION\_TIME | 媒体文件创建时间的元数据，值类型为char \*。使用ISO 8601标准的时间格式且为UTC时间，时间格式参考："2024-12-28T00:00:00:000000Z"。  **起始版本：** 14  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER | 如果在上一帧提交给编码器之后没有新的帧可用，则会以毫秒为单位重复提交最后一帧，值类型为int32\_t。  该键只用于视频编码Surface模式，在Configure阶段使用。  配置的值：  - 小于等于0：Configure阶段会被拦截，返回ERROR AV\_ERR\_INVALID\_VAL。  - 大于0：如果在上一帧提交给编码器之后没有新的帧可用，则会以毫秒为单位重复提交最后一帧。  **起始版本：** 18  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_MAX\_COUNT | 描述编码器在没有新的帧可用的情况下，可以对之前的帧进行重复编码的最大次数，值类型为int32\_t。  该键仅在OH\_MD\_KEY\_VIDEO\_ENCODER\_REPEAT\_PREVIOUS\_FRAME\_AFTER可用时生效，在Configure阶段使用。  配置的值：  - 等于0：Configure阶段会被拦截，返回ERROR AV\_ERR\_INVALID\_VAL。  - 小于0：在没有新的帧提交给编码器的这段时间内，编码器会一直重复编上一帧，直到达到系统上限。  - 大于0：在没有新的帧提交给编码器的这段时间内，最多可以重复编码的帧数。  **起始版本：** 18  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_B\_FRAME | 使能B帧编码的键，值类型为int32\_t（0或1）：1表示使能，0表示不使能。该键是可选项，仅用于视频编码器，默认值为0。  如果使能，视频编码器将使用B帧，解码顺序与显示顺序会不同。  对于不支持的平台，配置该键不会生效。  可通过[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME查询平台能力。  该键仅在configure阶段使用。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_MAX\_B\_FRAMES | 描述视频编码器支持的最大连续B帧数的键，值类型为int32\_t。注意：该键目前仅用于查询编码器能力。  使用规范如下：  1. 通过[OH\_AVCapability\_IsFeatureSupported](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME查询特性支持情况。  2. 通过[OH\_AVCapability\_GetFeatureProperties](capi-native-avcapability-h.md#oh_avcapability_getfeatureproperties)接口和枚举值[OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature).VIDEO\_ENCODER\_B\_FRAME获取OH\_AVFormat指针。  3. 通过[OH\_AVFormat\_GetIntValue](capi-native-avformat-h.md#oh_avformat_getintvalue)接口和本键获取最大B帧数。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ROI\_PARAMS | 用于视频编码中，使能ROI编码并下发ROI参数，随帧设置且实时生效。  参数需满足"Top1,Left1-Bottom1,Right1=Offset1;Top2,Left2-Bottom2,Right2=Offset2;"的格式，多个ROI参数之间使用";"连接。  Top、Left、Bottom、Right指定一个ROI区域的上、左、下、右边界，Offset指定deltaQP，“=Offset”可以省略，省略时使用默认值（-3）。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_SQR\_FACTOR | 指定SQR码控模式的质量参数，取值范围为[0, 51]（同编码量化参数QP），值越小，编码输出码率越大，质量越好。  在Configure/SetParameter阶段使用。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_MAX\_BITRATE | 指定SQR码控模式的最大码率，使用[OH\_AVCapability\_GetEncoderBitrateRange](capi-native-avcapability-h.md#oh_avcapability_getencoderbitraterange)方法获取取值范围（同OH\_MD\_KEY\_BITRATE），单位bps，值类型为int64\_t。  在Configure/SetParameter阶段使用。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_PTS\_BASED\_RATECONTROL | 使能基于显示时间戳(PTS)的码控模式的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。  该键值是可选的且只用于视频编码。  如果使能，则必须在每个视频帧中携带PTS信息，并发送到编码器。Surface模式下，通过[OH\_NativeWindow\_NativeWindowHandleOpt](capi-external-window-h.md#oh_nativewindow_nativewindowhandleopt)接口设置PTS，时间单位为纳秒(ns)；Buffer模式下，通过[OH\_AVBuffer\_SetBufferAttr](capi-native-avbuffer-h.md#oh_avbuffer_setbufferattr)接口设置PTS，时间单位为微秒(us)。  在Configure阶段使用。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | 媒体文件轨道间参考、被参考关系，值类型为int32\_t\*。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | 媒体文件辅助轨类型，值类型为char \*。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_TRACK\_DESCRIPTION | 媒体文件辅助轨描述信息，值类型为char \*。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_ENABLE\_SYNC\_MODE | 使能音视频编解码同步模式的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。该键是可选。  如果使能，需要注意：  1. 编解码器不可设置回调函数。  2. 必须使用缓冲区查询接口替代回调。  3. 只能在Configure阶段使用。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_DECODER\_BLANK\_FRAME\_ON\_SHUTDOWN | 用于指定视频解码器关闭时是否输出空白帧的键，值类型为int32\_t，1表示使能，0表示不使能，默认值为0。配置非0值将按照配置1处理，表示使能。该键是可选的且仅用于视频解码Surface模式。  使能后，调用[OH\_VideoDecoder\_Stop](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_stop)接口或者[OH\_VideoDecoder\_Destroy](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_destroy)接口时，视频解码器将输出空白帧（通常为黑色）。该机制可避免因解码器突然终止导致的显示残留。  **起始版本：** 20  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_VIDEO\_NATIVE\_BUFFER\_FORMAT | 用于查询视频编解码中native buffer像素格式的键，值类型为int32\_t。  具体取值请参见[OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format)中定义的像素格式。该键主要用于以下两种场景：  1. 视频解码：调用[OH\_VideoDecoder\_GetOutputDescription](capi-native-avcodec-videodecoder-h.md#oh_videodecoder_getoutputdescription)接口或[OH\_AVCodecOnStreamChanged](capi-native-avcodec-base-h.md#oh_avcodeconstreamchanged)，从返回的OH\_AVFormat对象中获取当前输出格式。  2. 视频编码：调用[OH\_VideoEncoder\_GetInputDescription](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputdescription)接口，从返回的OH\_AVFormat对象中获取当前输入格式。  **起始版本：** 22  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |
| const char \* OH\_MD\_KEY\_BUFFER\_SKIP\_SAMPLES\_INFO | OH\_AVBuffer中携带的键，用于跳过音频解码输出的数据。以采样点为单位，值类型为uint8\_t\*，当使用mp3、vorbis、opus解码器解码时，可设置该键。  仅音频的起始、末尾帧携带该键，该键是可选的。使用方法一：解封装时获取该信息并设置到解码输入的OH\_AVBuffer。  1. 从[OH\_AVCodecCallback](capi-codecbase-oh-avcodeccallback.md)的回调函数[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)里获取解码用的OH\_AVBuffer。  2. 调用[OH\_AVDemuxer\_ReadSampleBuffer](capi-native-avdemuxer-h.md#oh_avdemuxer_readsamplebuffer)接口读取音频数据，该接口会自行设置OH\_MD\_KEY\_BUFFER\_SKIP\_SAMPLES\_INFO。  3. 调用[OH\_AudioCodec\_PushInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_pushinputbuffer)输入OH\_AVBuffer进行解码。  使用方法二：构造该键需要的数据并设置到解码输入的OH\_AVBuffer。  开发者需要先创建一个10字节uint8\_t[]类型的数组，具体结构如下：  1. 数组0~3，这4个字节表示从当前帧第一个采样点开始往后跳过的采样点数，以小端序存储uint32\_t值。  2. 数组4~7，这4个字节表示从当前帧最后一个采样点开始往前跳过的采样点数（不大于1帧采样点数），以小端序存储uint32\_t值。  3. 数组8~9，这2个字节填0即可。  **起始版本：** 23  **系统能力：** SystemCapability.Multimedia.Media.CodecBase |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_MediaType

PhonePC/2in1TabletTVWearable

```
1. enum OH_MediaType
```

**描述**

媒体类型。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| MEDIA\_TYPE\_AUD = 0 | 音频轨。 |
| MEDIA\_TYPE\_VID = 1 | 视频轨。 |
| MEDIA\_TYPE\_SUBTITLE = 2 | 字幕轨。  **起始版本：** 12 |
| MEDIA\_TYPE\_TIMED\_METADATA = 5 | timed metadata轨。  **起始版本：** 20 |
| MEDIA\_TYPE\_AUXILIARY = 6 | 辅助轨。  **起始版本：** 20 |

### OH\_AACProfile

PhonePC/2in1TabletTVWearable

```
1. enum OH_AACProfile
```

**描述**

AAC档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| AAC\_PROFILE\_LC = 0 | AAC编码档次为Low Complexity级别。 |
| AAC\_PROFILE\_HE = 3 | AAC编码档次为High Efficiency级别。包含音频对象类型：AAC LC和SBR。  **起始版本：** 14 |
| AAC\_PROFILE\_HE\_V2 = 4 | AAC编码档次为High Efficiency v2级别。包含音频对象类型：AAC LC、SBR和PS。  **起始版本：** 14 |

### OH\_AVCProfile

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVCProfile
```

**描述**

AVC档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| AVC\_PROFILE\_BASELINE = 0 | AVC编码档次为基本档次。 |
| AVC\_PROFILE\_HIGH = 4 | AVC编码档次为高档次。 |
| AVC\_PROFILE\_MAIN = 8 | AVC编码档次为主档次。 |

### OH\_HEVCProfile

PhonePC/2in1TabletTVWearable

```
1. enum OH_HEVCProfile
```

**描述**

HEVC档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| HEVC\_PROFILE\_MAIN = 0 | HEVC编码档次为主档次。 |
| HEVC\_PROFILE\_MAIN\_10 = 1 | HEVC编码档次为10bit主档次。 |
| HEVC\_PROFILE\_MAIN\_STILL = 2 | HEVC编码档次为静止图像主档次。 |
| HEVC\_PROFILE\_MAIN\_10\_HDR10 = 3 | HEVC编码档次为HDR10主档次。  **废弃版本：** 14 |
| HEVC\_PROFILE\_MAIN\_10\_HDR10\_PLUS = 4 | HEVC编码档次为HDR10+主档次。  **废弃版本：** 14 |

### OH\_VVCProfile

PhonePC/2in1TabletTVWearable

```
1. enum OH_VVCProfile
```

**描述**

VVC档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| VVC\_PROFILE\_MAIN\_10 = 1 | VVC编码档次为10bit主档次。 |
| VVC\_PROFILE\_MAIN\_12 = 2 | VVC编码档次为12bit主档次。 |
| VVC\_PROFILE\_MAIN\_12\_INTRA = 10 | VVC编码档次为12bit帧内主档次。 |
| VVC\_PROFILE\_MULTI\_MAIN\_10 = 17 | VVC编码档次为多层编码10bit主档次。 |
| VVC\_PROFILE\_MAIN\_10\_444 = 33 | VVC编码档次为10bit全采样主档次。 |
| VVC\_PROFILE\_MAIN\_12\_444 = 34 | VVC编码档次为12bit全采样主档次。 |
| VVC\_PROFILE\_MAIN\_16\_444 = 36 | VVC编码档次为16bit全采样主档次。 |
| VVC\_PROFILE\_MAIN\_12\_444\_INTRA = 42 | VVC编码档次为12bit全采样帧内主档次。 |
| VVC\_PROFILE\_MAIN\_16\_444\_INTRA = 44 | VVC编码档次为16bit全采样帧内主档次。 |
| VVC\_PROFILE\_MULTI\_MAIN\_10\_444 = 49 | VVC编码档次为多层编码10bit全采样主档次。 |
| VVC\_PROFILE\_MAIN\_10\_STILL = 65 | VVC编码档次为10bit静止图像主档次。 |
| VVC\_PROFILE\_MAIN\_12\_STILL = 66 | VVC编码档次为12bit静止图像主档次。 |
| VVC\_PROFILE\_MAIN\_10\_444\_STILL = 97 | VVC编码档次为10bit全采样静止图像主档次。 |
| VVC\_PROFILE\_MAIN\_12\_444\_STILL = 98 | VVC编码档次为12bit全采样静止图像主档次。 |
| VVC\_PROFILE\_MAIN\_16\_444\_STILL = 100 | VVC编码档次为16bit全采样静止图像主档次。 |

### OH\_MPEG2Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_MPEG2Profile
```

**描述**

MPEG2档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| MPEG2\_PROFILE\_SIMPLE = 0 | 简单档次。 |
| MPEG2\_PROFILE\_MAIN = 1 | 主档次。 |
| MPEG2\_PROFILE\_SNR\_SCALABLE = 2 | 信噪比可分级档次。 |
| MPEG2\_PROFILE\_SPATIALLY\_SCALABLE = 3 | 空间可分级档次。 |
| MPEG2\_PROFILE\_HIGH = 4 | 高级档次。 |
| MPEG2\_PROFILE\_422 = 5 | 4:2:2档次。 |

### OH\_MPEG4Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_MPEG4Profile
```

**描述**

MPEG4档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| MPEG4\_PROFILE\_SIMPLE = 0 | 简单档次。 |
| MPEG4\_PROFILE\_SIMPLE\_SCALABLE = 1 | 简单可分级档次。 |
| MPEG4\_PROFILE\_CORE = 2 | 核心档次。 |
| MPEG4\_PROFILE\_MAIN = 3 | 主档次。 |
| MPEG4\_PROFILE\_N\_BIT = 4 | N位档次。 |
| MPEG4\_PROFILE\_HYBRID = 5 | 混合档次。 |
| MPEG4\_PROFILE\_BASIC\_ANIMATED\_TEXTURE = 6 | 基本动画纹理档次。 |
| MPEG4\_PROFILE\_SCALABLE\_TEXTURE = 7 | 可分级纹理档次。 |
| MPEG4\_PROFILE\_SIMPLE\_FA = 8 | 简单FA档次。 |
| MPEG4\_PROFILE\_ADVANCED\_REAL\_TIME\_SIMPLE = 9 | 高级实时简单档次。 |
| MPEG4\_PROFILE\_CORE\_SCALABLE = 10 | 核心可分级档次。 |
| MPEG4\_PROFILE\_ADVANCED\_CODING\_EFFICIENCY = 11 | 高级编码效率档次。 |
| MPEG4\_PROFILE\_ADVANCED\_CORE = 12 | 高级核心档次。 |
| MPEG4\_PROFILE\_ADVANCED\_SCALABLE\_TEXTURE = 13 | 高级可分级纹理档次。 |
| MPEG4\_PROFILE\_ADVANCED\_SIMPLE = 17 | 高级简单档次。 |

### OH\_H263Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_H263Profile
```

**描述**

H.263档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| H263\_PROFILE\_BASELINE = 0 | 基线档次。 |
| H263\_PROFILE\_VERSION\_1\_BACKWARD\_COMPATIBILITY = 2 | 版本1向后兼容档次。 |

### OH\_VC1Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_VC1Profile
```

**描述**

VC-1档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| VC1\_PROFILE\_SIMPLE = 0 | 简单档次。 |
| VC1\_PROFILE\_MAIN = 1 | 主档次。 |
| VC1\_PROFILE\_ADVANCED = 2 | 高级档次。 |

### OH\_AV1Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_AV1Profile
```

**描述**

AV1档次。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AV1\_PROFILE\_MAIN = 0 | 主档次。 |
| AV1\_PROFILE\_HIGH = 1 | 高级档次。 |
| AV1\_PROFILE\_PROFESSIONAL = 2 | 专业档次。 |

### OH\_VP9Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_VP9Profile
```

**描述**

VP9档次。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| VP9\_PROFILE\_0 = 0 | 0档次。 |
| VP9\_PROFILE\_1 = 1 | 1档次。 |
| VP9\_PROFILE\_2 = 2 | 2档次。 |
| VP9\_PROFILE\_3 = 3 | 3档次。 |

### OH\_WVC1Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_WVC1Profile
```

**描述**

WVC1档次。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| WVC1\_PROFILE\_ADVANCED = 0 | 高级档次。 |

### OH\_WMV3Profile

PhonePC/2in1TabletTVWearable

```
1. enum OH_WMV3Profile
```

**描述**

WMV3档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| WMV3\_PROFILE\_SIMPLE = 0 | 简单档次。 |
| WMV3\_PROFILE\_MAIN = 1 | 主档次。 |

### OH\_AVOutputFormat

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVOutputFormat
```

**描述**

封装器支持的输出文件格式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| AV\_OUTPUT\_FORMAT\_DEFAULT = 0 | 输出文件格式默认值，默认为MP4格式。 |
| AV\_OUTPUT\_FORMAT\_MPEG\_4 = 2 | 输出文件格式为MP4格式。 |
| AV\_OUTPUT\_FORMAT\_M4A = 6 | 输出文件格式为M4A格式。 |
| AV\_OUTPUT\_FORMAT\_AMR = 8 | 输出文件格式为AMR格式。  **起始版本：** 12 |
| AV\_OUTPUT\_FORMAT\_MP3 = 9 | 输出文件格式为MP3格式。  **起始版本：** 12 |
| AV\_OUTPUT\_FORMAT\_WAV = 10 | 输出文件格式为WAV格式。  **起始版本：** 12 |
| AV\_OUTPUT\_FORMAT\_AAC = 11 | 输出文件格式为AAC格式。  **起始版本：** 18 |
| AV\_OUTPUT\_FORMAT\_FLAC = 12 | 输出文件格式为FLAC格式。  **起始版本：** 20 |
| AV\_OUTPUT\_FORMAT\_OGG = 13 | 输出文件格式为OGG格式。  **起始版本：** 23 |

### OH\_AVSeekMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVSeekMode
```

**描述**

跳转模式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| SEEK\_MODE\_NEXT\_SYNC = 0 | 指定时间位置的下一I帧。若时间点后没有I帧，该模式可能跳转失败。 |
| SEEK\_MODE\_PREVIOUS\_SYNC | 指定时间位置的上一I帧。 |
| SEEK\_MODE\_CLOSEST\_SYNC | 指定时间位置的最近I帧。 |

### OH\_ScalingMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_ScalingMode
```

**描述**

缩放模式，只在Surface模式下使用。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**废弃版本：** 14

**替代接口：** [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2)

| 枚举项 | 描述 |
| --- | --- |
| SCALING\_MODE\_SCALE\_TO\_WINDOW = 1 | 根据窗口尺寸自适应调整图像大小。  **替代接口：** [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2).OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW\_V2 |
| SCALING\_MODE\_SCALE\_CROP = 2 | 根据窗口尺寸裁剪图像大小。  **替代接口：** [OHScalingModeV2](capi-external-window-h.md#ohscalingmodev2).OH\_SCALING\_MODE\_SCALE\_CROP\_V2 |

### OH\_BitsPerSample

PhonePC/2in1TabletTVWearable

```
1. enum OH_BitsPerSample
```

**描述**

每个编码样本的音频位数。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| SAMPLE\_U8 = 0 | 8位无符号整数采样。 |
| SAMPLE\_S16LE = 1 | 16位有符号整数采样。 |
| SAMPLE\_S24LE = 2 | 24位有符号整数采样。 |
| SAMPLE\_S32LE = 3 | 32位有符号整数采样。 |
| SAMPLE\_F32LE = 4 | 32位浮点采样。 |
| SAMPLE\_U8P = 5 | 8位无符号整数平面采样。 |
| SAMPLE\_S16P = 6 | 16位有符号整数平面采样。 |
| SAMPLE\_S24P = 7 | 24位有符号整数平面采样。 |
| SAMPLE\_S32P = 8 | 32位有符号整数平面采样。 |
| SAMPLE\_F32P = 9 | 32位浮点平面采样。 |
| INVALID\_WIDTH = -1 | 无效采样格式。 |

### OH\_ColorPrimary

PhonePC/2in1TabletTVWearable

```
1. enum OH_ColorPrimary
```

**描述**

色域。编解码都支持。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| COLOR\_PRIMARY\_BT709 = 1 | BT709色域。 |
| COLOR\_PRIMARY\_UNSPECIFIED = 2 | 未指定色域。 |
| COLOR\_PRIMARY\_BT470\_M = 4 | BT470\_M色域。 |
| COLOR\_PRIMARY\_BT601\_625 = 5 | BT601\_625色域。 |
| COLOR\_PRIMARY\_BT601\_525 = 6 | BT601\_525色域。 |
| COLOR\_PRIMARY\_SMPTE\_ST240 = 7 | SMPTE\_ST240色域。 |
| COLOR\_PRIMARY\_GENERIC\_FILM = 8 | GENERIC\_FILM色域。 |
| COLOR\_PRIMARY\_BT2020 = 9 | BT2020色域。 |
| COLOR\_PRIMARY\_SMPTE\_ST428 = 10 | SMPTE\_ST428色域。 |
| COLOR\_PRIMARY\_P3DCI = 11 | P3DCI色域。 |
| COLOR\_PRIMARY\_P3D65 = 12 | P3D65色域。 |

### OH\_TransferCharacteristic

PhonePC/2in1TabletTVWearable

```
1. enum OH_TransferCharacteristic
```

**描述**

转移特性。编解码都支持。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| TRANSFER\_CHARACTERISTIC\_BT709 = 1 | BT709传递函数。 |
| TRANSFER\_CHARACTERISTIC\_UNSPECIFIED = 2 | 未指定传递函数。 |
| TRANSFER\_CHARACTERISTIC\_GAMMA\_2\_2 = 4 | GAMMA\_2\_2传递函数。 |
| TRANSFER\_CHARACTERISTIC\_GAMMA\_2\_8 = 5 | GAMMA\_2\_8传递函数。 |
| TRANSFER\_CHARACTERISTIC\_BT601 = 6 | BT601传递函数。 |
| TRANSFER\_CHARACTERISTIC\_SMPTE\_ST240 = 7 | SMPTE\_ST240传递函数。 |
| TRANSFER\_CHARACTERISTIC\_LINEAR = 8 | LINEAR传递函数。 |
| TRANSFER\_CHARACTERISTIC\_LOG = 9 | LOG传递函数。 |
| TRANSFER\_CHARACTERISTIC\_LOG\_SQRT = 10 | LOG\_SQRT传递函数。 |
| TRANSFER\_CHARACTERISTIC\_IEC\_61966\_2\_4 = 11 | IEC\_61966\_2\_4传递函数。 |
| TRANSFER\_CHARACTERISTIC\_BT1361 = 12 | BT1361传递函数。 |
| TRANSFER\_CHARACTERISTIC\_IEC\_61966\_2\_1 = 13 | IEC\_61966\_2\_1传递函数。 |
| TRANSFER\_CHARACTERISTIC\_BT2020\_10BIT = 14 | BT2020\_10BIT传递函数。 |
| TRANSFER\_CHARACTERISTIC\_BT2020\_12BIT = 15 | BT2020\_12BIT传递函数。 |
| TRANSFER\_CHARACTERISTIC\_PQ = 16 | PQ传递函数。 |
| TRANSFER\_CHARACTERISTIC\_SMPTE\_ST428 = 17 | SMPTE\_ST428传递函数。 |
| TRANSFER\_CHARACTERISTIC\_HLG = 18 | HLG传递函数。 |

### OH\_MatrixCoefficient

PhonePC/2in1TabletTVWearable

```
1. enum OH_MatrixCoefficient
```

**描述**

矩阵系数。编解码都支持。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| MATRIX\_COEFFICIENT\_IDENTITY = 0 | 单位矩阵。 |
| MATRIX\_COEFFICIENT\_BT709 = 1 | BT709转换矩阵。 |
| MATRIX\_COEFFICIENT\_UNSPECIFIED = 2 | 未指定转换矩阵。 |
| MATRIX\_COEFFICIENT\_FCC = 4 | FCC转换矩阵。 |
| MATRIX\_COEFFICIENT\_BT601\_625 = 5 | BT601\_625转换矩阵。 |
| MATRIX\_COEFFICIENT\_BT601\_525 = 6 | BT601\_525转换矩阵。 |
| MATRIX\_COEFFICIENT\_SMPTE\_ST240 = 7 | SMPTE\_ST240转换矩阵。 |
| MATRIX\_COEFFICIENT\_YCGCO = 8 | YCGCO转换矩阵。 |
| MATRIX\_COEFFICIENT\_BT2020\_NCL = 9 | BT2020\_NCL转换矩阵。 |
| MATRIX\_COEFFICIENT\_BT2020\_CL = 10 | BT2020\_CL转换矩阵。 |
| MATRIX\_COEFFICIENT\_SMPTE\_ST2085 = 11 | SMPTE\_ST2085转换矩阵。 |
| MATRIX\_COEFFICIENT\_CHROMATICITY\_NCL = 12 | CHROMATICITY\_NCL转换矩阵。 |
| MATRIX\_COEFFICIENT\_CHROMATICITY\_CL = 13 | CHROMATICITY\_CL转换矩阵。 |
| MATRIX\_COEFFICIENT\_ICTCP = 14 | ICTCP转换矩阵。 |

### OH\_AVCLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVCLevel
```

**描述**

AVC级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| AVC\_LEVEL\_1 = 0 | 级别1 |
| AVC\_LEVEL\_1b = 1 | 级别1b |
| AVC\_LEVEL\_11 = 2 | 级别1.1 |
| AVC\_LEVEL\_12 = 3 | 级别1.2 |
| AVC\_LEVEL\_13 = 4 | 级别1.3 |
| AVC\_LEVEL\_2 = 5 | 级别2 |
| AVC\_LEVEL\_21 = 6 | 级别2.1 |
| AVC\_LEVEL\_22 = 7 | 级别2.2 |
| AVC\_LEVEL\_3 = 8 | 级别3 |
| AVC\_LEVEL\_31 = 9 | 级别3.1 |
| AVC\_LEVEL\_32 = 10 | 级别3.2 |
| AVC\_LEVEL\_4 = 11 | 级别4 |
| AVC\_LEVEL\_41 = 12 | 级别4.1 |
| AVC\_LEVEL\_42 = 13 | 级别4.2 |
| AVC\_LEVEL\_5 = 14 | 级别5 |
| AVC\_LEVEL\_51 = 15 | 级别5.1 |
| AVC\_LEVEL\_52 = 16 | 级别5.2 |
| AVC\_LEVEL\_6 = 17 | 级别6 |
| AVC\_LEVEL\_61 = 18 | 级别6.1 |
| AVC\_LEVEL\_62 = 19 | 级别6.2 |

### OH\_HEVCLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_HEVCLevel
```

**描述**

HEVC级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| HEVC\_LEVEL\_1 = 0 | 级别1 |
| HEVC\_LEVEL\_2 = 1 | 级别2 |
| HEVC\_LEVEL\_21 = 2 | 级别2.1 |
| HEVC\_LEVEL\_3 = 3 | 级别3 |
| HEVC\_LEVEL\_31 = 4 | 级别3.1 |
| HEVC\_LEVEL\_4 = 5 | 级别4 |
| HEVC\_LEVEL\_41 = 6 | 级别4.1 |
| HEVC\_LEVEL\_5 = 7 | 级别5 |
| HEVC\_LEVEL\_51 = 8 | 级别5.1 |
| HEVC\_LEVEL\_52 = 9 | 级别5.2 |
| HEVC\_LEVEL\_6 = 10 | 级别6 |
| HEVC\_LEVEL\_61 = 11 | 级别6.1 |
| HEVC\_LEVEL\_62 = 12 | 级别6.2 |

### OH\_VVCLevel

PhonePC/2in1TabletTVWearable

```
1. enum OH_VVCLevel
```

**描述**

VVC级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| VVC\_LEVEL\_1 = 16 | 级别1.0 |
| VVC\_LEVEL\_2 = 32 | 级别2.0 |
| VVC\_LEVEL\_21 = 35 | 级别2.1 |
| VVC\_LEVEL\_3 = 48 | 级别3.0 |
| VVC\_LEVEL\_31 = 51 | 级别3.1 |
| VVC\_LEVEL\_4 = 64 | 级别4.0 |
| VVC\_LEVEL\_41 = 67 | 级别4.1 |
| VVC\_LEVEL\_5 = 80 | 级别5.0 |
| VVC\_LEVEL\_51 = 83 | 级别5.1 |
| VVC\_LEVEL\_52 = 86 | 级别5.2 |
| VVC\_LEVEL\_6 = 96 | 级别6.0 |
| VVC\_LEVEL\_61 = 99 | 级别6.1 |
| VVC\_LEVEL\_62 = 102 | 级别6.2 |
| VVC\_LEVEL\_63 = 105 | 级别6.3 |
| VVC\_LEVEL\_155 = 255 | 级别15.5 |

### OH\_MPEG2Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_MPEG2Level
```

**描述**

MPEG2级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| MPEG2\_LEVEL\_LOW = 0 | 低级别。 |
| MPEG2\_LEVEL\_MAIN = 1 | 主级别。 |
| MPEG2\_LEVEL\_HIGH\_1440 = 2 | 高1440级别。 |
| MPEG2\_LEVEL\_HIGH = 3 | 高级别。 |

### OH\_MPEG4Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_MPEG4Level
```

**描述**

MPEG4级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| MPEG4\_LEVEL\_0 = 0 | 级别0 |
| MPEG4\_LEVEL\_0B = 1 | 级别0B。 |
| MPEG4\_LEVEL\_1 = 2 | 级别1。 |
| MPEG4\_LEVEL\_2 = 3 | 级别2。 |
| MPEG4\_LEVEL\_3 = 4 | 级别3。 |
| MPEG4\_LEVEL\_3B = 5 | 级别3B。 |
| MPEG4\_LEVEL\_4 = 6 | 级别4。 |
| MPEG4\_LEVEL\_4A = 7 | 级别4A。 |
| MPEG4\_LEVEL\_5 = 8 | 级别5。 |
| MPEG4\_LEVEL\_6 = 9 | 级别6。 |

### OH\_H263Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_H263Level
```

**描述**

H.263级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 17

| 枚举项 | 描述 |
| --- | --- |
| H263\_LEVEL\_10 = 0 | 级别10。 |
| H263\_LEVEL\_20 = 1 | 级别20。 |
| H263\_LEVEL\_30 = 2 | 级别30。 |
| H263\_LEVEL\_40 = 3 | 级别40。 |
| H263\_LEVEL\_45 = 4 | 级别45。 |
| H263\_LEVEL\_50 = 5 | 级别50。 |
| H263\_LEVEL\_60 = 6 | 级别60。 |
| H263\_LEVEL\_70 = 7 | 级别70。 |

### OH\_VC1Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_VC1Level
```

**描述**

VC-1级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| VC1\_LEVEL\_L0 = 0 | 级别L0。 |
| VC1\_LEVEL\_L1 = 1 | 级别L1。 |
| VC1\_LEVEL\_L2 = 2 | 级别L2。 |
| VC1\_LEVEL\_L3 = 3 | 级别L3。 |
| VC1\_LEVEL\_L4 = 4 | 级别L4。 |
| VC1\_LEVEL\_LOW = 5 | 低级别。 |
| VC1\_LEVEL\_MEDIUM = 6 | 中级别。 |
| VC1\_LEVEL\_HIGH = 7 | 高级别。 |

### OH\_AV1Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_AV1Level
```

**描述**

AV1级别。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| AV1\_LEVEL\_20 = 0 | 2.0级别。 |
| AV1\_LEVEL\_21 = 1 | 2.1级别。 |
| AV1\_LEVEL\_22 = 2 | 2.2级别。 |
| AV1\_LEVEL\_23 = 3 | 2.3级别。 |
| AV1\_LEVEL\_30 = 4 | 3.0级别。 |
| AV1\_LEVEL\_31 = 5 | 3.1级别。 |
| AV1\_LEVEL\_32 = 6 | 3.2级别。 |
| AV1\_LEVEL\_33 = 7 | 3.3级别。 |
| AV1\_LEVEL\_40 = 8 | 4.0级别。 |
| AV1\_LEVEL\_41 = 9 | 4.1级别。 |
| AV1\_LEVEL\_42 = 10 | 4.2级别。 |
| AV1\_LEVEL\_43 = 11 | 4.3级别。 |
| AV1\_LEVEL\_50 = 12 | 5.0级别。 |
| AV1\_LEVEL\_51 = 13 | 5.1级别。 |
| AV1\_LEVEL\_52 = 14 | 5.2级别。 |
| AV1\_LEVEL\_53 = 15 | 5.3级别。 |
| AV1\_LEVEL\_60 = 16 | 6.0级别。 |
| AV1\_LEVEL\_61 = 17 | 6.1级别。 |
| AV1\_LEVEL\_62 = 18 | 6.2级别。 |
| AV1\_LEVEL\_63 = 19 | 6.3级别。 |
| AV1\_LEVEL\_70 = 20 | 7.0级别。 |
| AV1\_LEVEL\_71 = 21 | 7.1级别。 |
| AV1\_LEVEL\_72 = 22 | 7.2级别。 |
| AV1\_LEVEL\_73 = 23 | 7.3级别。 |

### OH\_VP9Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_VP9Level
```

**描述**

VP9级别。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| VP9\_LEVEL\_1 = 0 | 1级别。 |
| VP9\_LEVEL\_11 = 1 | 1.1级别。 |
| VP9\_LEVEL\_2 = 2 | 2级别。 |
| VP9\_LEVEL\_21 = 3 | 2.1级别。 |
| VP9\_LEVEL\_3 = 4 | 3级别。 |
| VP9\_LEVEL\_31 = 5 | 3.1级别。 |
| VP9\_LEVEL\_4 = 6 | 4级别。 |
| VP9\_LEVEL\_41 = 7 | 4.1级别。 |
| VP9\_LEVEL\_5 = 8 | 5级别。 |
| VP9\_LEVEL\_51 = 9 | 5.1级别。 |
| VP9\_LEVEL\_52 = 10 | 5.2级别。 |
| VP9\_LEVEL\_6 = 11 | 6级别。 |
| VP9\_LEVEL\_61 = 12 | 6.1级别。 |
| VP9\_LEVEL\_62 = 13 | 6.2级别。 |

### OH\_WVC1Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_WVC1Level
```

**描述**

WVC1级别。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| WVC1\_LEVEL\_L0 = 0 | L0级别。 |
| WVC1\_LEVEL\_L1 = 1 | L1级别。 |
| WVC1\_LEVEL\_L2 = 2 | L2级别。 |
| WVC1\_LEVEL\_L3 = 3 | L3级别。 |
| WVC1\_LEVEL\_L4 = 4 | L4级别。 |

### OH\_WMV3Level

PhonePC/2in1TabletTVWearable

```
1. enum OH_WMV3Level
```

**描述**

WMV3级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| WMV3\_LEVEL\_LOW = 0 | 低级别。 |
| WMV3\_LEVEL\_MEDIUM = 1 | 中级别。 |
| WMV3\_LEVEL\_HIGH = 2 | 高级别。 |

### OH\_TemporalGopReferenceMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_TemporalGopReferenceMode
```

**描述**

时域图片组参考模式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| ADJACENT\_REFERENCE = 0 | 参考最近的短期参考帧。 |
| JUMP\_REFERENCE = 1 | 参考最近的长期参考帧。 |
| UNIFORMLY\_SCALED\_REFERENCE = 2 | 均匀分层参考结构，在丢弃最高层级视频帧后，视频帧均匀分布。其中时域图片组个数必须为2的幂。 |

### OH\_BitrateMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_BitrateMode
```

**描述**

编码器的比特率模式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| BITRATE\_MODE\_CBR = 0 | 恒定比特率模式。 |
| BITRATE\_MODE\_VBR = 1 | 可变比特率模式。 |
| BITRATE\_MODE\_CQ = 2 | 恒定质量模式。 |
| BITRATE\_MODE\_SQR = 3 | 质量稳定模式，仅支持H265（HEVC）。  **起始版本：** 20 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVCodecOnError()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnError)(OH_AVCodec *codec, int32_t errorCode, void *userData)
```

**描述**

当OH\_AVCodec实例运行出错时，会调用来上报具体的错误信息的函数指针。

| 使用场景 | 错误码 |
| --- | --- |
| 音频编解码 | AV\_ERR\_DRM\_DECRYPT\_FAILED：DRM解密失败。 |
| 视频编解码 | AV\_ERROR\_NO\_MEMORY：系统资源不足。  AV\_ERROR\_UNKNOWN：未知错误，请通过具体日志分析。  AV\_ERR\_SERVICE\_DIED：服务状态已消亡。 |
| 视频解码 | AV\_ERR\_VIDEO\_UNSUPPORTED\_COLOR\_SPACE\_CONVERSION：当前输入不支持色彩空间转换功能。 |
| 视频编码 | AV\_ERROR\_INPUT\_DATA\_ERROR：  1. 运行过程中surfacebuffer宽、高超出OH\_VideoEncoder\_Configure接口配置的宽、高。  2. 配置信息与输入数据比特不一致，如：编码输入数据为8bit而配置为10bit，或编码输入数据为10bit而配置为8bit。  3. 配置了不支持的pixelformat。 |

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| int32\_t errorCode | 特定错误代码。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVCodecOnStreamChanged()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnStreamChanged)(OH_AVCodec *codec, OH_AVFormat *format, void *userData)
```

**描述**

当视频解码输入码流分辨率或者视频编码输出码流的分辨率发生变化时，调用此函数指针报告新的流描述信息。

从API version 15开始，支持音频解码时，码流采样率、声道数或者音频采样格式发生变化时，将调用此函数指针报告新的流描述信息，支持检测此变化的解码格式有：Audio Vivid，AAC，FLAC，MP3，VORBIS。

需要注意的是，OH\_AVFormat指针的生命周期只有在函数指针被调用时才有效，调用结束后禁止继续访问。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 新输出流描述信息。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVCodecOnNeedInputData()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnNeedInputData)(OH_AVCodec *codec, uint32_t index, OH_AVMemory *data, void *userData)
```

**描述**

当OH\_AVCodec在运行过程中需要新的输入数据时，将调用此函数指针，并携带可用的缓冲区来填充新的输入数据。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| uint32\_t index | 与新可用的输入缓冲区相对应的索引。 |
| [OH\_AVMemory](capi-core-oh-avmemory.md) \*data | 新的可用输入缓冲区。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVCodecOnNewOutputData()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnNewOutputData)(OH_AVCodec *codec, uint32_t index, OH_AVMemory *data, OH_AVCodecBufferAttr *attr, void *userData)
```

**描述**

当OH\_AVCodec运行过程中生成新的输出数据时，将调用此函数指针，并携带包含新输出数据的缓冲区。需要注意的是，OH\_AVCodecBufferAttr指针的生命周期仅在调用函数指针时有效，这将禁止调用结束后继续访问。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AVCodecOnNewOutputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| uint32\_t index | 与新输出缓冲区对应的索引。 |
| [OH\_AVMemory](capi-core-oh-avmemory.md) \*data | 包含新输出数据的缓冲区。 |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) \*attr | 新输出缓冲区的说明。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVCodecOnNeedInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnNeedInputBuffer)(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
```

**描述**

当OH\_AVCodec在运行过程中需要新的输入数据时，将调用此函数指针，并携带可用的缓冲区来填充新的输入数据。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| uint32\_t index | 与新可用的输入缓冲区相对应的索引。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 新的可用输入缓冲区。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVCodecOnNewOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVCodecOnNewOutputBuffer)(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData)
```

**描述**

当OH\_AVCodec运行过程中生成新的输出数据时，将调用此函数指针，并携带包含新输出数据的缓冲区。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | OH\_AVCodec实例。 |
| uint32\_t index | 与新输出缓冲区对应的索引。 |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*buffer | 包含新输出数据的缓冲区。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_AVDataSourceReadAt()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AVDataSourceReadAt)(OH_AVBuffer *data, int32_t length, int64_t pos)
```

**描述**

函数指针定义，用于提供获取用户自定义媒体数据的能力。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*data | 要填充的缓冲区。 |
| int32\_t length | 要读取的数据长度。 |
| int64\_t pos | 从偏移量位置读取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 读取到缓冲区的数据的实际长度。 |

### OH\_AVDataSourceReadAtExt()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AVDataSourceReadAtExt)(OH_AVBuffer *data, int32_t length, int64_t pos, void *userData)
```

**描述**

函数指针定义，用于提供获取用户自定义媒体数据的能力。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \*data | 要填充的缓冲区。 |
| int32\_t length | 要读取的数据长度。 |
| int64\_t pos | 从偏移量位置读取。 |
| void \*userData | 用户自定义数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 读取到缓冲区的数据的实际长度。 |
