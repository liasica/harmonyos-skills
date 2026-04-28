---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-h
title: avmetadata_extractor.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avmetadata_extractor.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cfb700fcf12336393d359411fd631c129affec3503f0cf2d6c0831acd1fe6b2f
---

## 概述

PhonePC/2in1TabletTVWearable

定义AVMetadataExtractor接口。使用其Native API从媒体资源中获取元数据。

**引用文件：** <multimedia/player\_framework/avmetadata\_extractor.h>

**库：** libavmetadata\_extractor.so

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**相关模块：** [AVMetadataExtractor](capi-avmetadataextractor.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) | OH\_AVMetadataExtractor | 定义OH\_AVMetadataExtractor类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor\_OutputParam\* OH\_AVMetadataExtractor\_OutputParam\_Create()](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_outputparam_create) | 创建OH\_AVMetadataExtractor\_OutputParam实例。 |
| [void OH\_AVMetadataExtractor\_OutputParam\_Destroy(OH\_AVMetadataExtractor\_OutputParam\* outputParam)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_outputparam_destroy) | 释放OH\_AVMetadataExtractor\_OutputParam实例。 |
| [bool OH\_AVMetadataExtractor\_OutputParam\_SetSize(OH\_AVMetadataExtractor\_OutputParam\* outputParam, int32\_t width, int32\_t height)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_outputparam_setsize) | 设置OH\_AVMetadataExtractor\_OutputParam实例的期望输出尺寸。若width或height小于0，则使用原始宽度或高度。若width或height等于0，则保持宽高比按比例缩放。若width和height均大于0，则使用输入的width和height参数缩放图像。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchFrameByTime(OH\_AVMetadataExtractor extractor, int64\_t timeUs, OH\_AVMedia\_SeekMode seekMode, const OH\_AVMetadataExtractor\_OutputParam outputParam, OH\_PixelmapNative\*\* pixelMap)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_fetchframebytime) | 从视频源中提取指定时间点的图像。该函数必须在设置资源之后使用。 |
| [typedef void (\*OH\_AVMetadataExtractor\_OnFrameFetched)(OH\_AVMetadataExtractor extractor, const OH\_AVMetadataExtractor\_FrameInfo frameInfo, OH\_AVErrCode code, void\* userData)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_onframefetched) | 定义用于获取AVMetadataExtractor捕获帧的回调函数。注意：frameInfo会在回调后自动释放，但用户需要使用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)手动释放frameInfo.image，避免内存泄漏。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchFramesByTimes(OH\_AVMetadataExtractor extractor, int64\_t timeUs[], uint16\_t timesUsSize, OH\_AVMedia\_SeekMode seekMode, const OH\_AVMetadataExtractor\_OutputParam outputParam, OH\_AVMetadataExtractor\_OnFrameFetched onFrameInfoCallback, void\* userData)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-h#oh_avmetadataextractor_fetchframesbytimes) | 从视频源中异步提取多个指定时间点的图像。该函数必须在设置资源之后使用。 |
| [void OH\_AVMetadataExtractor\_CancelAllFetchFrames(OH\_AVMetadataExtractor \*extractor)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_cancelallfetchframes) | 取消所有由[OH\_AVMetadataExtractor\_FetchFramesByTimes](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_fetchframesbytimes)发起的批量获取图像操作。在[OH\_AVMetadataExtractor\_OnFrameFetched](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_onframefetched)回调中，挂起的获取操作被取消，并标记结果为已取消。 |
| [OH\_AVFormat \*OH\_AVMetadataExtractor\_GetTrackDescription(OH\_AVMetadataExtractor \*extractor, uint32\_t index)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_gettrackdescription) | 从媒体源中获取指定索引的轨道描述信息。该函数必须在设置资源之后使用。 |
| [OH\_AVFormat \*OH\_AVMetadataExtractor\_GetCustomInfo(OH\_AVMetadataExtractor \*extractor)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_getcustominfo) | 从媒体源中获取自定义元数据信息。该函数必须在设置资源之后使用。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_SetMediaSource(OH\_AVMetadataExtractor \*extractor, OH\_AVMediaSource \*source)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setmediasource) | 为提取器设置媒体源。 |
| [OH\_AVMetadataExtractor\* OH\_AVMetadataExtractor\_Create(void)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_create) | 创建OH\_AVMetadataExtractor实例。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_SetFDSource(OH\_AVMetadataExtractor\* extractor, int32\_t fd, int64\_t offset, int64\_t size)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setfdsource) | 通过媒体文件描述符设置数据源。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchMetadata(OH\_AVMetadataExtractor\* extractor, OH\_AVFormat\* avMetadata)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_fetchmetadata) | 从媒体资源中获取元数据。  此函数必须在[OH\_AVMetadataExtractor\_SetFDSource](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setfdsource)之后调用。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchAlbumCover(OH\_AVMetadataExtractor\* extractor, OH\_PixelmapNative\*\* pixelMap)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_fetchalbumcover) | 获取音频专辑封面。  此函数必须在[OH\_AVMetadataExtractor\_SetFDSource](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setfdsource)之后调用。 |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_Release(OH\_AVMetadataExtractor\* extractor)](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_release) | 释放用于OH\_AVMetadataExtractor的资源并销毁OH\_AVMetadataExtractor实例。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVMetadataExtractor\_OutputParam\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMetadataExtractor_OutputParam* OH_AVMetadataExtractor_OutputParam_Create()
```

**描述**

创建OH\_AVMetadataExtractor\_OutputParam实例。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md) \* | 返回指向OH\_AVMetadataExtractor\_OutputParam实例的指针。 |

### OH\_AVMetadataExtractor\_OutputParam\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_AVMetadataExtractor_OutputParam_Destroy(OH_AVMetadataExtractor_OutputParam* outputParam)
```

**描述**

释放OH\_AVMetadataExtractor\_OutputParam实例。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)\* outputParam | 指向OH\_AVMetadataExtractor\_OutputParam实例的指针。 |

### OH\_AVMetadataExtractor\_OutputParam\_SetSize()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AVMetadataExtractor_OutputParam_SetSize(OH_AVMetadataExtractor_OutputParam* outputParam, int32_t width, int32_t height)
```

**描述**

设置OH\_AVMetadataExtractor\_OutputParam实例的期望输出尺寸。若width或height小于0，则使用原始宽度或高度。若width或height等于0，则保持宽高比按比例缩放。若width和height均大于0，则使用输入的width和height参数缩放图像。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)\* outputParam | 指向OH\_AVMetadataExtractor\_OutputParam实例的指针。 |
| int32\_t width | 输出图像的期望宽度，如有必要可进行缩放。 |
| int32\_t height | 输出图像的期望高度，如有必要可进行缩放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 成功返回true，失败返回false。  可能失败的原因：outputParam为空指针。 |

### OH\_AVMetadataExtractor\_FetchFrameByTime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_FetchFrameByTime(OH_AVMetadataExtractor *extractor, int64_t timeUs, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam* outputParam, OH_PixelmapNative** pixelMap)
```

**描述**

从视频源中提取指定时间点的图像。该函数必须在设置资源之后使用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| int64\_t timeUs | 要从视频资源中提取图像的时间位置（单位：微秒）。 |
| [OH\_AVMedia\_SeekMode](capi-avmedia-base-h.md#oh_avmedia_seekmode) seekMode | 定义指定时间与关键帧之间关系的跳转模式。详见[OH\_AVMedia\_SeekMode](capi-avmedia-base-h.md#oh_avmedia_seekmode)。 |
| [const OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)\* outputParam | 图像的输出参数，例如图像的高度或者宽度。详见[OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)。若为空指针，使用视频的原始尺寸。注意：用户需要使用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)在使用pixelMap后将其释放。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelMap | 用于接收从视频源提取的图像，详见[OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不允许。  AV\_ERR\_UNSUPPORTED\_FORMAT：格式不支持。  AV\_ERR\_SERVICE\_DIED：服务已终止。  AV\_ERR\_IO\_CLEARTEXT\_NOT\_PERMITTED：不允许HTTP明文流量。 |

### OH\_AVMetadataExtractor\_OnFrameFetched()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AVMetadataExtractor_OnFrameFetched)(OH_AVMetadataExtractor *extractor, const OH_AVMetadataExtractor_FrameInfo* frameInfo, OH_AVErrCode code, void* userData)
```

**描述**

定义用于获取AVMetadataExtractor捕获帧的回调函数。注意：frameInfo会在回调后自动释放，但用户需要使用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)手动释放frameInfo.image，避免内存泄漏。

**起始版本：** 23

### OH\_AVMetadataExtractor\_FetchFramesByTimes()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_FetchFramesByTimes(OH_AVMetadataExtractor *extractor, int64_t timeUs[], uint16_t timesUsSize, OH_AVMedia_SeekMode seekMode, const OH_AVMetadataExtractor_OutputParam* outputParam, OH_AVMetadataExtractor_OnFrameFetched onFrameInfoCallback, void* userData)
```

**描述**

从视频源中异步提取多个指定时间点的图像。该函数必须在设置资源之后使用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| int64\_t timeUs[] | 从视频源提取图像时的时间点数组（单位：微秒）。 |
| uint16\_t timesUsSize | 输入时间点数组的长度。 |
| [OH\_AVMedia\_SeekMode](capi-avmedia-base-h.md#oh_avmedia_seekmode) seekMode | 定义每个给定时间与关键帧之间关系的跳转选项，详见[OH\_AVMedia\_SeekMode](capi-avmedia-base-h.md#oh_avmedia_seekmode)。 |
| [const OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)\* outputParam | 图像的输出参数，例如图像的高度或者宽度。详见[OH\_AVMetadataExtractor\_OutputParam](tadataextractor-oh-avmetadataextractor-outputparam.md)。若该参数为空指针，则获取的帧使用视频原始尺寸。 |
| [OH\_AVMetadataExtractor\_OnFrameFetched](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_onframefetched) onFrameInfoCallback | 每帧提取完成或提取失败后调用的回调函数。 |
| void\* userData | 传递给回调函数的用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数无效。  AV\_ERR\_SERVICE\_DIED：服务已终止。  AV\_ERR\_IO\_CLEARTEXT\_NOT\_PERMITTED：不允许HTTP明文流量。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作不允许。由onFrameInfoCallback返回。  AV\_ERR\_UNSUPPORTED\_FORMAT：格式不支持。由onFrameInfoCallback返回。  AV\_ERR\_TIMEOUT：执行超时。由onFrameInfoCallback返回。 |

### OH\_AVMetadataExtractor\_CancelAllFetchFrames()

PhonePC/2in1TabletTVWearable

```
1. void OH_AVMetadataExtractor_CancelAllFetchFrames(OH_AVMetadataExtractor *extractor)
```

**描述**

取消所有由[OH\_AVMetadataExtractor\_FetchFramesByTimes](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_fetchframesbytimes)发起的批量获取图像操作。在[OH\_AVMetadataExtractor\_OnFrameFetched](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_onframefetched)回调中，挂起的获取操作被取消，并标记结果为已取消。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |

### OH\_AVMetadataExtractor\_GetTrackDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVMetadataExtractor_GetTrackDescription(OH_AVMetadataExtractor *extractor, uint32_t index)
```

**描述**

从媒体源中获取指定索引的轨道描述信息。该函数必须在设置资源之后使用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| uint32\_t index | 要获取的轨道描述的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 成功时返回包含轨道描述信息的OH\_AVFormat实例指针，失败时返回空指针。  可能失败的原因：  1. extractor为空指针。  2. 未设置媒体源。  3. 格式不支持。  注意：用户需要使用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)在使用OH\_AVFormat后将其释放。 |

### OH\_AVMetadataExtractor\_GetCustomInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AVMetadataExtractor_GetCustomInfo(OH_AVMetadataExtractor *extractor)
```

**描述**

从媒体源中获取自定义元数据信息。该函数必须在设置资源之后使用。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat \*](capi-core-oh-avformat.md) | 成功时返回包含自定义元数据的OH\_AVFormat实例指针，失败时返回空指针。  可能失败的原因：  1. extractor为空指针。  2. 未设置媒体源。  3. 未找到自定义信息。  注意：用户需要使用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)在使用OH\_AVFormat后将其释放。 |

### OH\_AVMetadataExtractor\_SetMediaSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_SetMediaSource(OH_AVMetadataExtractor *extractor, OH_AVMediaSource *source)
```

**描述**

为提取器设置媒体源。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md) \*extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| [OH\_AVMediaSource](capi-avmedia-source-oh-avmediasource.md) \*source | 要设置的媒体源。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 函数执行结果。  AV\_ERR\_OK：表示执行成功。  AV\_ERR\_INVALID\_VAL：输入的extractor为空指针或输入的source无效。 |

### OH\_AVMetadataExtractor\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AVMetadataExtractor* OH_AVMetadataExtractor_Create(void)
```

**描述**

创建OH\_AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md)\* | 创建成功时返回指向OH\_AVMetadataExtractor实例的指针，否则返回空指针。  可能的失败原因：HstEngineFactory::CreateAVMetadataHelperEngine执行失败。 |

### OH\_AVMetadataExtractor\_SetFDSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_SetFDSource(OH_AVMetadataExtractor* extractor, int32_t fd, int64_t offset, int64_t size)
```

**描述**

通过媒体文件描述符设置数据源。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md)\* extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| int32\_t fd | 媒体源的文件描述符。 |
| int64\_t offset | 媒体源在文件描述符中的偏移量。 |
| int64\_t size | 媒体源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL： 输入的extractor为空指针或参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作被禁止。  AV\_ERR\_NO\_MEMORY：内部内存分配失败。 |

### OH\_AVMetadataExtractor\_FetchMetadata()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_FetchMetadata(OH_AVMetadataExtractor* extractor, OH_AVFormat* avMetadata)
```

**描述**

从媒体资源中获取元数据。

此函数必须在[OH\_AVMetadataExtractor\_SetFDSource](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md)\* extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md)\* avMetadata | 指向OH\_AVFormat实例的指针，其内容包含获取的元数据信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL： 输入的extractor为空指针或参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作被禁止。  AV\_ERR\_UNSUPPORTED\_FORMAT：格式不支持。  AV\_ERR\_NO\_MEMORY：内部内存分配失败。  AV\_ERR\_IO\_CLEARTEXT\_NOT\_PERMITTED：（API version 23新增）不允许HTTP明文流量。 |

### OH\_AVMetadataExtractor\_FetchAlbumCover()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_FetchAlbumCover(OH_AVMetadataExtractor* extractor, OH_PixelmapNative** pixelMap)
```

**描述**

获取音频专辑封面。

此函数必须在[OH\_AVMetadataExtractor\_SetFDSource](capi-avmetadata-extractor-h.md#oh_avmetadataextractor_setfdsource)之后调用。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md)\* extractor | 指向OH\_AVMetadataExtractor实例的指针。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelMap | 从音频源获取的专辑封面。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL： 输入的extractor为空指针或参数无效。  AV\_ERR\_OPERATE\_NOT\_PERMIT：操作被禁止。  AV\_ERR\_UNSUPPORTED\_FORMAT：格式不支持。  AV\_ERR\_NO\_MEMORY：内部内存分配失败。 |

### OH\_AVMetadataExtractor\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVMetadataExtractor_Release(OH_AVMetadataExtractor* extractor)
```

**描述**

释放用于OH\_AVMetadataExtractor的资源并销毁OH\_AVMetadataExtractor实例。

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataExtractor](capi-avmetadataextractor-oh-avmetadataextractor.md)\* extractor | 指向OH\_AVMetadataExtractor实例指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL： 输入的extractor为空指针或参数无效。 |
