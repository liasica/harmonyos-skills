---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcapability-h
title: native_avcapability.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avcapability.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9e0ad0a12c4dea84ab4b5d62f0e3b0be8d757eaf9d115696970516e0cf6b1c09
---

## 概述

声明用于编解码能力查询到的Native API。

**引用文件：** <multimedia/player\_framework/native\_avcapability.h>

**库：** libnative\_media\_codecbase.so

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**相关模块：** [AVCapability](capi-avcapability.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) | OH\_AVRange | 范围包含最小值和最大值。 |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) | OH\_AVCapability | 为OH\_AVCapability接口定义native层对象。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVCodecCategory](capi-native-avcapability-h.md#oh_avcodeccategory) | OH\_AVCodecCategory | 编解码器类别。 |
| [OH\_AVCodecType](capi-native-avcapability-h.md#oh_avcodectype) | OH\_AVCodecType | 编解码器类型。 |
| [OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature) | OH\_AVCapabilityFeature | 可以在特定编解码器场景中使用的可选特性。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCapability \*OH\_AVCodec\_GetCapability(const char \*mime, bool isEncoder)](capi-native-avcapability-h.md#oh_avcodec_getcapability) | 获取系统推荐的编解码器能力。 |
| [OH\_AVCapability \*OH\_AVCodec\_GetCapabilityByCategory(const char \*mime, bool isEncoder, OH\_AVCodecCategory category)](capi-native-avcapability-h.md#oh_avcodec_getcapabilitybycategory) | 获取指定类别中的编解码器能力。通过指定类别，匹配的编解码器仅限于硬件编解码器或软件编解码器。 |
| [OH\_AVCapability \*\*OH\_AVCodec\_GetCapabilityList(OH\_AVCodecType codecType, uint32\_t \*count)](capi-native-avcapability-h.md#oh_avcodec_getcapabilitylist) | 获取指定编解码器类型的能力列表。此功能会根据提供的编解码器类型检索出系统支持的所有匹配的编解码器能力。 |
| [bool OH\_AVCapability\_IsHardware(OH\_AVCapability \*capability)](capi-native-avcapability-h.md#oh_avcapability_ishardware) | 检查能力实例是否描述了硬件编解码器。 |
| [bool OH\_AVCapability\_IsSecure(OH\_AVCapability \*capability)](capi-native-avcapability-h.md#oh_avcapability_issecure) | 检查能力实例是否描述了一个DRM解码器。 |
| [const char \*OH\_AVCapability\_GetName(OH\_AVCapability \*capability)](capi-native-avcapability-h.md#oh_avcapability_getname) | 获取对应的编解码器名称。 |
| [const char \*OH\_AVCapability\_GetMimeType(OH\_AVCapability \*capability)](capi-native-avcapability-h.md#oh_avcapability_getmimetype) | 获取编解码器的MIME类型。 |
| [bool OH\_AVCapability\_CheckMimeType(OH\_AVCapability \*capability, const char \*mimeType)](capi-native-avcapability-h.md#oh_avcapability_checkmimetype) | 检查编解码器的MIME类型是否与指定的MIME类型匹配。 |
| [int32\_t OH\_AVCapability\_GetMaxSupportedInstances(OH\_AVCapability \*capability)](capi-native-avcapability-h.md#oh_avcapability_getmaxsupportedinstances) | 获取编解码器支持的最大实例数。 |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderBitrateRange(OH\_AVCapability \*capability, OH\_AVRange \*bitrateRange)](capi-native-avcapability-h.md#oh_avcapability_getencoderbitraterange) | 获取编码器支持的比特率范围。 |
| [bool OH\_AVCapability\_IsEncoderBitrateModeSupported(OH\_AVCapability \*capability, OH\_BitrateMode bitrateMode)](capi-native-avcapability-h.md#oh_avcapability_isencoderbitratemodesupported) | 检查编码器是否支持特定的比特率模式。 |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderQualityRange(OH\_AVCapability \*capability, OH\_AVRange \*qualityRange)](capi-native-avcapability-h.md#oh_avcapability_getencoderqualityrange) | 获取编码器支持的质量范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetEncoderComplexityRange(OH\_AVCapability \*capability, OH\_AVRange \*complexityRange)](capi-native-avcapability-h.md#oh_avcapability_getencodercomplexityrange) | 获取编码器支持的编码器复杂性范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRates(OH\_AVCapability \*capability, const int32\_t \*\*sampleRates, uint32\_t \*sampleRateNum)](capi-native-avcapability-h.md#oh_avcapability_getaudiosupportedsamplerates) | 获取音频编解码器支持的采样率。 |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioSupportedSampleRateRanges(OH\_AVCapability \*capability, OH\_AVRange \*\*sampleRateRanges, uint32\_t \*rangesNum)](capi-native-avcapability-h.md#oh_avcapability_getaudiosupportedsamplerateranges) | 获取音频编解码器支持的采样率范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetAudioChannelCountRange(OH\_AVCapability \*capability, OH\_AVRange \*channelCountRange)](capi-native-avcapability-h.md#oh_avcapability_getaudiochannelcountrange) | 获取音频编解码器支持的音频通道计数范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthAlignment(OH\_AVCapability \*capability, int32\_t \*widthAlignment)](capi-native-avcapability-h.md#oh_avcapability_getvideowidthalignment) | 获取视频编解码器支持的视频宽度对齐。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightAlignment(OH\_AVCapability \*capability, int32\_t \*heightAlignment)](capi-native-avcapability-h.md#oh_avcapability_getvideoheightalignment) | 获取视频编解码器支持的视频高度对齐。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRangeForHeight(OH\_AVCapability \*capability, int32\_t height, OH\_AVRange \*widthRange)](capi-native-avcapability-h.md#oh_avcapability_getvideowidthrangeforheight) | 获取指定高度情况下视频编解码器支持的视频宽度范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRangeForWidth(OH\_AVCapability \*capability, int32\_t width, OH\_AVRange \*heightRange)](capi-native-avcapability-h.md#oh_avcapability_getvideoheightrangeforwidth) | 获取指定宽度情况下视频编解码器支持的视频高度范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoWidthRange(OH\_AVCapability \*capability, OH\_AVRange \*widthRange)](capi-native-avcapability-h.md#oh_avcapability_getvideowidthrange) | 获取视频编解码器支持的视频宽度范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoHeightRange(OH\_AVCapability \*capability, OH\_AVRange \*heightRange)](capi-native-avcapability-h.md#oh_avcapability_getvideoheightrange) | 获取视频编解码器支持的视频高度范围。 |
| [bool OH\_AVCapability\_IsVideoSizeSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height)](capi-native-avcapability-h.md#oh_avcapability_isvideosizesupported) | 检查视频编解码器是否支持特定的视频大小。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRange(OH\_AVCapability \*capability, OH\_AVRange \*frameRateRange)](capi-native-avcapability-h.md#oh_avcapability_getvideoframeraterange) | 获取视频编解码器支持的视频帧率范围。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoFrameRateRangeForSize(OH\_AVCapability \*capability, int32\_t width, int32\_t height, OH\_AVRange \*frameRateRange)](capi-native-avcapability-h.md#oh_avcapability_getvideoframeraterangeforsize) | 获取指定视频大小的视频编解码器支持的视频帧率范围。 |
| [bool OH\_AVCapability\_AreVideoSizeAndFrameRateSupported(OH\_AVCapability \*capability, int32\_t width, int32\_t height, int32\_t frameRate)](capi-native-avcapability-h.md#oh_avcapability_arevideosizeandframeratesupported) | 检查视频编解码器是否支持视频大小和帧率的特定组合。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedPixelFormats(OH\_AVCapability \*capability, const int32\_t \*\*pixelFormats, uint32\_t \*pixelFormatNum)](capi-native-avcapability-h.md#oh_avcapability_getvideosupportedpixelformats) | 获取视频编解码器支持的视频像素格式。 |
| [OH\_AVErrCode OH\_AVCapability\_GetVideoSupportedNativeBufferFormats(OH\_AVCapability \*capability, const OH\_NativeBuffer\_Format \*\*nativeBufferFormats, uint32\_t \*nativeBufferFormatNum)](capi-native-avcapability-h.md#oh_avcapability_getvideosupportednativebufferformats) | 获取视频编解码器支持的OH\_NativeBuffer格式。该函数提供了视频编解码器能够处理的OH\_NativeBuffer格式信息，具体取值可见OH\_NativeBuffer\_Format。 |
| [OH\_AVErrCode OH\_AVCapability\_GetSupportedProfiles(OH\_AVCapability \*capability, const int32\_t \*\*profiles, uint32\_t \*profileNum)](capi-native-avcapability-h.md#oh_avcapability_getsupportedprofiles) | 获取编解码器支持的档次。 |
| [OH\_AVErrCode OH\_AVCapability\_GetSupportedLevelsForProfile(OH\_AVCapability \*capability, int32\_t profile, const int32\_t \*\*levels, uint32\_t \*levelNum)](capi-native-avcapability-h.md#oh_avcapability_getsupportedlevelsforprofile) | 获取特定档次支持的编解码器级别。 |
| [bool OH\_AVCapability\_AreProfileAndLevelSupported(OH\_AVCapability \*capability, int32\_t profile, int32\_t level)](capi-native-avcapability-h.md#oh_avcapability_areprofileandlevelsupported) | 检查编解码器是否支持档次和级别的特定组合。 |
| [bool OH\_AVCapability\_IsFeatureSupported(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)](capi-native-avcapability-h.md#oh_avcapability_isfeaturesupported) | 检查编解码器是否支持指定特性。 |
| [OH\_AVFormat \*OH\_AVCapability\_GetFeatureProperties(OH\_AVCapability \*capability, OH\_AVCapabilityFeature feature)](capi-native-avcapability-h.md#oh_avcapability_getfeatureproperties) | 获取指定特性的属性。需要注意的是，返回值指向的OH\_AVFormat实例的生命周期需要调用者手动释放。 |

## 枚举类型说明

### OH\_AVCodecCategory

```c
enum OH_AVCodecCategory
```

**描述**

编解码器类别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| HARDWARE = 0 | 硬件编解码。 |
| SOFTWARE | 软件编解码。 |

### OH\_AVCodecType

```c
enum OH_AVCodecType
```

**描述**

编解码器类型。

**起始版本：** 24

| 枚举项 | 描述 |
| --- | --- |
| OH\_AVCODEC\_TYPE\_VIDEO\_ENCODER = 0 | 表示视频编码器。  **起始版本：** 24 |
| OH\_AVCODEC\_TYPE\_VIDEO\_DECODER = 1 | 表示视频解码器。  **起始版本：** 24 |
| OH\_AVCODEC\_TYPE\_AUDIO\_ENCODER = 2 | 表示音频编码器。  **起始版本：** 24 |
| OH\_AVCODEC\_TYPE\_AUDIO\_DECODER = 3 | 表示音频解码器。  **起始版本：** 24 |

### OH\_AVCapabilityFeature

```c
enum OH_AVCapabilityFeature
```

**描述**

可以在特定编解码器场景中使用的可选特性。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_ENCODER\_TEMPORAL\_SCALABILITY = 0 | 编解码器支持时域可分层特性，只用于视频编码场景。 |
| VIDEO\_ENCODER\_LONG\_TERM\_REFERENCE = 1 | 编解码器支持长期参考帧特性，只用于视频编码场景。 |
| VIDEO\_LOW\_LATENCY = 2 | 编解码器支持低时延特性，只用于视频解码场景。 |
| VIDEO\_ENCODER\_B\_FRAME = 7 | 编解码器支持B帧特性，只用于视频编码场景。  **起始版本：** 20 |
| VIDEO\_DECODER\_OUTPUT\_IN\_DECODING\_ORDER = 8 | 解码器支持按解码顺序输出帧特性，只用于视频解码场景。  **起始版本：** 26.0.0 |
| VIDEO\_ENCODER\_PREPROC\_DOWNSAMPLING = 9 | 编码器支持视频编码前处理降采样特性，该能力仅适用于视频编码器。  仅当编码器通过[OH\_VideoEncoder\_CreatePrimaryWithPreproc](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createprimarywithpreproc)或[OH\_VideoEncoder\_CreateSecondaryFromPrimary](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createsecondaryfromprimary)接口创建时，方可启用该能力。  **起始版本：** 26.0.0 |
| VIDEO\_ENCODER\_PREPROC\_CROP = 10 | 编码器支持视频编码前处理裁剪特性，该特性仅适用于视频编码器。  仅当编码器通过[OH\_VideoEncoder\_CreatePrimaryWithPreproc](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createprimarywithpreproc)或[OH\_VideoEncoder\_CreateSecondaryFromPrimary](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createsecondaryfromprimary)接口创建时，方可启用该能力。  **起始版本：** 26.0.0 |

## 函数说明

### OH\_AVCodec\_GetCapability()

```c
OH_AVCapability *OH_AVCodec_GetCapability(const char *mime, bool isEncoder)
```

**描述**

获取系统推荐的编解码器能力。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mime | MIME类型描述字符串，请参阅AVCODEC\_MIME\_TYPE类型[变量](capi-native-avcodec-base-h.md#变量)。 |
| bool isEncoder | 编码器为true，解码器为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \* | 如果现有编解码器匹配，则返回能力实例，如果指定的MIME类型与任何现有编解码器不匹配，则返回NULL。 |

### OH\_AVCodec\_GetCapabilityByCategory()

```c
OH_AVCapability *OH_AVCodec_GetCapabilityByCategory(const char *mime, bool isEncoder, OH_AVCodecCategory category)
```

**描述**

获取指定类别中的编解码器能力。通过指定类别，匹配的编解码器仅限于硬件编解码器或软件编解码器。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mime | MIME类型描述字符串，请参阅AVCODEC\_MIME\_TYPE类型[变量](capi-native-avcodec-base-h.md#变量)。 |
| bool isEncoder | 编码器为true，解码器为false。 |
| [OH\_AVCodecCategory](capi-native-avcapability-h.md#oh_avcodeccategory) category | 编解码器类别。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \* | 如果现有编解码器匹配，则返回能力实例，如果指定的MIME类型与任何现有编解码器不匹配，则返回NULL。 |

### OH\_AVCodec\_GetCapabilityList()

```c
OH_AVCapability **OH_AVCodec_GetCapabilityList(OH_AVCodecType codecType, uint32_t *count)
```

**描述**

获取指定编解码器类型的能力列表。此功能会根据提供的编解码器类型检索出系统支持的所有匹配的编解码器能力。

**说明** 

编解码器能力列表的内存由系统底层全局维护，调用者无需管理其生命周期，不得手动分配或释放此内存。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodecType](capi-native-avcapability-h.md#oh_avcodectype) codecType | 指定要查询的编解码器类型。 |
| uint32\_t \*count | 输出参数。指向一个uint32\_t变量的指针，用于存储匹配到的编解码器能力数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCapability \*\*](capi-avcapability-oh-avcapability.md) | 如果找到匹配项，则返回指向OH\_AVCapability实例数组的指针。  如果未找到匹配的编解码器或发生错误，则返回NULL。 |

### OH\_AVCapability\_IsHardware()

```c
bool OH_AVCapability_IsHardware(OH_AVCapability *capability)
```

**描述**

检查能力实例是否描述了硬件编解码器。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果能力实例描述的是硬件编解码器，则返回true，如果功能实例描述的是软件编解码器，则为false。 |

### OH\_AVCapability\_IsSecure()

```c
bool OH_AVCapability_IsSecure(OH_AVCapability *capability)
```

**描述**

检查能力实例是否描述了一个DRM解码器。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果能力实例描述的是DRM解码器，则返回true。  如果能力实例描述的是非DRM解码器，则为false。 |

### OH\_AVCapability\_GetName()

```c
const char *OH_AVCapability_GetName(OH_AVCapability *capability)
```

**描述**

获取对应的编解码器名称。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回编解码器名称字符串。 |

### OH\_AVCapability\_GetMimeType()

```c
const char *OH_AVCapability_GetMimeType(OH_AVCapability *capability)
```

**描述**

获取编解码器的MIME类型。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char \* | 返回编解码器的MIME类型字符串。 |

### OH\_AVCapability\_CheckMimeType()

```c
bool OH_AVCapability_CheckMimeType(OH_AVCapability *capability, const char *mimeType)
```

**描述**

检查编解码器的MIME类型是否与指定的MIME类型匹配。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| const char \*mimeType | 要检查的目标MIME类型字符串。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果MIME类型匹配则返回true，否则返回false。 |

### OH\_AVCapability\_GetMaxSupportedInstances()

```c
int32_t OH_AVCapability_GetMaxSupportedInstances(OH_AVCapability *capability)
```

**描述**

获取编解码器支持的最大实例数。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回支持的最大编解码器实例数。 |

### OH\_AVCapability\_GetEncoderBitrateRange()

```c
OH_AVErrCode OH_AVCapability_GetEncoderBitrateRange(OH_AVCapability *capability, OH_AVRange *bitrateRange)
```

**描述**

获取编码器支持的比特率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*bitrateRange | 输出参数。编码器码率范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向编码器码率范围的指针为空指针。 |

### OH\_AVCapability\_IsEncoderBitrateModeSupported()

```c
bool OH_AVCapability_IsEncoderBitrateModeSupported(OH_AVCapability *capability, OH_BitrateMode bitrateMode)
```

**描述**

检查编码器是否支持特定的比特率模式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。 |
| [OH\_BitrateMode](capi-native-avcodec-base-h.md#oh_bitratemode) bitrateMode | 比特率模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持该比特率模式，则返回true；如果不支持该比特率模式，则返回false。 |

### OH\_AVCapability\_GetEncoderQualityRange()

```c
OH_AVErrCode OH_AVCapability_GetEncoderQualityRange(OH_AVCapability *capability, OH_AVRange *qualityRange)
```

**描述**

获取编码器支持的质量范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*qualityRange | 输出参数。编码器质量范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向编码器质量范围的指针为空指针。 |

### OH\_AVCapability\_GetEncoderComplexityRange()

```c
OH_AVErrCode OH_AVCapability_GetEncoderComplexityRange(OH_AVCapability *capability, OH_AVRange *complexityRange)
```

**描述**

获取编码器支持的编码器复杂性范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编码器能力指针。如果给的是解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*complexityRange | 输出参数。编码器复杂度范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向编码器复杂度范围的指针为空指针。 |

### OH\_AVCapability\_GetAudioSupportedSampleRates()

```c
OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRates(OH_AVCapability *capability, const int32_t **sampleRates, uint32_t *sampleRateNum)
```

**描述**

获取音频编解码器支持的采样率。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。 |
| const int32\_t \*\*sampleRates | 输出参数。指向采样率数组的指针。 |
| uint32\_t \*sampleRateNum | 输出参数。采样率数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向采样率数组的指针为空指针，或者指向采样率数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_GetAudioSupportedSampleRateRanges()

```c
OH_AVErrCode OH_AVCapability_GetAudioSupportedSampleRateRanges(OH_AVCapability *capability, OH_AVRange **sampleRateRanges, uint32_t *rangesNum)
```

**描述**

获取音频编解码器支持的采样率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*\*sampleRateRanges | 输出参数。指向采样率范围数组的指针。 |
| uint32\_t \*rangesNum | 输出参数。采样率范围数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向采样率范围数组的指针为空指针，或者指向采样率范围数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_GetAudioChannelCountRange()

```c
OH_AVErrCode OH_AVCapability_GetAudioChannelCountRange(OH_AVCapability *capability, OH_AVRange *channelCountRange)
```

**描述**

获取音频编解码器支持的音频通道计数范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 音频编解码能力指针。如果给的是视频编解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*channelCountRange | 输出参数。音频通道计数范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向音频通道计数范围的指针为空指针。 |

### OH\_AVCapability\_GetVideoWidthAlignment()

```c
OH_AVErrCode OH_AVCapability_GetVideoWidthAlignment(OH_AVCapability *capability, int32_t *widthAlignment)
```

**描述**

获取视频编解码器支持的视频宽度对齐。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t \*widthAlignment | 输出参数。视频宽度对齐。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频宽度对齐的指针为空指针。 |

### OH\_AVCapability\_GetVideoHeightAlignment()

```c
OH_AVErrCode OH_AVCapability_GetVideoHeightAlignment(OH_AVCapability *capability, int32_t *heightAlignment)
```

**描述**

获取视频编解码器支持的视频高度对齐。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t \*heightAlignment | 输出参数。视频高度对齐。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频高度对齐的指针为空指针。 |

### OH\_AVCapability\_GetVideoWidthRangeForHeight()

```c
OH_AVErrCode OH_AVCapability_GetVideoWidthRangeForHeight(OH_AVCapability *capability, int32_t height, OH_AVRange *widthRange)
```

**描述**

获取指定高度情况下视频编解码器支持的视频宽度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t height | 视频垂直像素数。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*widthRange | 输出参数。视频宽度范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者高度不在通过[OH\_AVCapability\_GetVideoHeightRange](capi-native-avcapability-h.md#oh_avcapability_getvideoheightrange)获取支持的高度范围中，或者指向宽度范围的指针为空指针。 |

### OH\_AVCapability\_GetVideoHeightRangeForWidth()

```c
OH_AVErrCode OH_AVCapability_GetVideoHeightRangeForWidth(OH_AVCapability *capability, int32_t width, OH_AVRange *heightRange)
```

**描述**

获取指定宽度情况下视频编解码器支持的视频高度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t width | 视频水平像素数。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*heightRange | 输出参数。视频高度范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者宽度不在通过[OH\_AVCapability\_GetVideoWidthRange](capi-native-avcapability-h.md#oh_avcapability_getvideowidthrange)获取支持的宽度范围中，或者指向高度范围的指针为空指针。 |

### OH\_AVCapability\_GetVideoWidthRange()

```c
OH_AVErrCode OH_AVCapability_GetVideoWidthRange(OH_AVCapability *capability, OH_AVRange *widthRange)
```

**描述**

获取视频编解码器支持的视频宽度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*widthRange | 输出参数。视频宽度范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频宽度范围的指针为空指针。 |

### OH\_AVCapability\_GetVideoHeightRange()

```c
OH_AVErrCode OH_AVCapability_GetVideoHeightRange(OH_AVCapability *capability, OH_AVRange *heightRange)
```

**描述**

获取视频编解码器支持的视频高度范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*heightRange | 输出参数。视频高度范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频高度范围的指针为空指针。 |

### OH\_AVCapability\_IsVideoSizeSupported()

```c
bool OH_AVCapability_IsVideoSizeSupported(OH_AVCapability *capability, int32_t width, int32_t height)
```

**描述**

检查视频编解码器是否支持特定的视频大小。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t width | 视频水平像素数。 |
| int32\_t height | 视频垂直像素数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持该视频大小，则返回true，如果不支持该视频大小，则返回false。 |

### OH\_AVCapability\_GetVideoFrameRateRange()

```c
OH_AVErrCode OH_AVCapability_GetVideoFrameRateRange(OH_AVCapability *capability, OH_AVRange *frameRateRange)
```

**描述**

获取视频编解码器支持的视频帧率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*frameRateRange | 输出参数。视频帧率范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频帧率范围的指针为空指针。 |

### OH\_AVCapability\_GetVideoFrameRateRangeForSize()

```c
OH_AVErrCode OH_AVCapability_GetVideoFrameRateRangeForSize(OH_AVCapability *capability, int32_t width, int32_t height, OH_AVRange *frameRateRange)
```

**描述**

获取指定视频大小的视频编解码器支持的视频帧率范围。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t width | 视频水平像素数。 |
| int32\_t height | 视频垂直像素数。 |
| [OH\_AVRange](capi-avcapability-oh-avrange.md) \*frameRateRange | 输出参数。视频帧率范围。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者宽度和高度组合不支持，或者指向帧率范围的指针为空指针。 |

### OH\_AVCapability\_AreVideoSizeAndFrameRateSupported()

```c
bool OH_AVCapability_AreVideoSizeAndFrameRateSupported(OH_AVCapability *capability, int32_t width, int32_t height, int32_t frameRate)
```

**描述**

检查视频编解码器是否支持视频大小和帧率的特定组合。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| int32\_t width | 视频水平像素数。 |
| int32\_t height | 视频垂直像素数。 |
| int32\_t frameRate | 每秒帧数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持视频大小和帧率的组合，则返回true。如果不支持，则为false。 |

### OH\_AVCapability\_GetVideoSupportedPixelFormats()

```c
OH_AVErrCode OH_AVCapability_GetVideoSupportedPixelFormats(OH_AVCapability *capability, const int32_t **pixelFormats, uint32_t *pixelFormatNum)
```

**描述**

获取视频编解码器支持的视频像素格式。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。如果给的是音频编解码器能力指针，会导致未定义行为。 |
| const int32\_t \*\*pixelFormats | 输出参数。指向视频像素格式数组的指针。参考[OH\_AVPixelFormat](capi-native-avformat-h.md#oh_avpixelformat)。 |
| uint32\_t \*pixelFormatNum | 输出参数。像素格式数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向视频像素格式数组的指针为空指针，或者指向像素格式数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_GetVideoSupportedNativeBufferFormats()

```c
OH_AVErrCode OH_AVCapability_GetVideoSupportedNativeBufferFormats(OH_AVCapability *capability, const OH_NativeBuffer_Format **nativeBufferFormats, uint32_t *nativeBufferFormatNum)
```

**描述**

获取视频编解码器支持的OH\_NativeBuffer格式。该函数提供了视频编解码器能够处理的OH\_NativeBuffer格式信息，具体取值可见OH\_NativeBuffer\_Format。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 视频编解码能力指针。 |
| const [OH\_NativeBuffer\_Format](capi-buffer-common-h.md#oh_nativebuffer_format) \*\*nativeBufferFormats | 输出参数。指向OH\_NativeBuffer\_Format数组的指针。 |
| uint32\_t \*nativeBufferFormatNum | 输出参数。OH\_NativeBuffer\_Format数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效、能力实例是音频编解码器能力、指向NativeBuffer格式数组的指针为空指针、  或指向NativeBuffer格式数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_GetSupportedProfiles()

```c
OH_AVErrCode OH_AVCapability_GetSupportedProfiles(OH_AVCapability *capability, const int32_t **profiles, uint32_t *profileNum)
```

**描述**

获取编解码器支持的档次。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| const int32\_t \*\*profiles | 输出参数。指向档次数组的指针。例如，H.264档次参考[OH\_AVCProfile](capi-native-avcodec-base-h.md#oh_avcprofile)。 |
| uint32\_t \*profileNum | 输出参数。档次数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者指向档次数组的指针为空指针，或者指向档次数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_GetSupportedLevelsForProfile()

```c
OH_AVErrCode OH_AVCapability_GetSupportedLevelsForProfile(OH_AVCapability *capability, int32_t profile, const int32_t **levels, uint32_t *levelNum)
```

**描述**

获取特定档次支持的编解码器级别。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| int32\_t profile | 编解码器档次。 |
| const int32\_t \*\*levels | 输出参数。指向级别数组的指针。例如，H.264级别参考[OH\_AVCLevel](capi-native-avcodec-base-h.md#oh_avclevel)。 |
| uint32\_t \*levelNum | 输出参数。级别数组的元素数目。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：能力实例无效，或者档次不在通过[OH\_AVCapability\_GetSupportedProfiles](capi-native-avcapability-h.md#oh_avcapability_getsupportedprofiles)获取支持的档次数组中，或者指向级别数组的指针为空指针，或者指向级别数组的元素数目的指针为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_NO\_MEMORY：内部使用内存分配失败。 |

### OH\_AVCapability\_AreProfileAndLevelSupported()

```c
bool OH_AVCapability_AreProfileAndLevelSupported(OH_AVCapability *capability, int32_t profile, int32_t level)
```

**描述**

检查编解码器是否支持档次和级别的特定组合。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| int32\_t profile | 编解码器档次。 |
| int32\_t level | 编解码器级别。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持档次和级别的组合，则返回true。如果不支持，则为false。 |

### OH\_AVCapability\_IsFeatureSupported()

```c
bool OH_AVCapability_IsFeatureSupported(OH_AVCapability *capability, OH_AVCapabilityFeature feature)
```

**描述**

检查编解码器是否支持指定特性。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| [OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature) feature | 编解码特性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持该特性，则返回true。如果不支持，则为false。 |

### OH\_AVCapability\_GetFeatureProperties()

```c
OH_AVFormat *OH_AVCapability_GetFeatureProperties(OH_AVCapability *capability, OH_AVCapabilityFeature feature)
```

**描述**

获取指定特性的属性。需要注意的是，返回值指向的OH\_AVFormat实例的生命周期需要调用者手动释放。

**系统能力：** SystemCapability.Multimedia.Media.CodecBase

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCapability](capi-avcapability-oh-avcapability.md) \*capability | 编解码能力指针。 |
| [OH\_AVCapabilityFeature](capi-native-avcapability-h.md#oh_avcapabilityfeature) feature | 编解码特性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \* | 返回指向OH\_AVFormat实例的指针。 |
