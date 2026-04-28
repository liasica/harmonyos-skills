---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avdemuxer-h
title: native_avdemuxer.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avdemuxer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:05+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:aaaa9aba62aae0fcc26b42b2b5ad3766726c40900a489a6829b9e36065b52caa
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于音视频媒体数据解析的接口。

**引用文件：** <multimedia/player\_framework/native\_avdemuxer.h>

**库：** libnative\_media\_avdemuxer.so

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**相关模块：** [AVDemuxer](capi-avdemuxer.md)

**相关示例：**[AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) | OH\_AVDemuxer | 为OH\_AVDemuxer接口定义native层对象。 |
| [DRM\_MediaKeySystemInfo](capi-avdemuxer-drm-mediakeysysteminfo.md) | DRM\_MediaKeySystemInfo | 为DRM\_MediaKeySystemInfo接口定义native层对象。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo\* mediaKeySystemInfo)](capi-native-avdemuxer-h.md#drm_mediakeysysteminfocallback) | DRM\_MediaKeySystemInfoCallback | DRM\_MediaKeySystemInfo回调函数指针类型，不返回解封装器实例，适用于单个解封装器实例场景。  需要使用[OH\_AVDemuxer\_SetMediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#oh_avdemuxer_setmediakeysysteminfocallback)接口将其设置为回调。 |
| [typedef void (\*Demuxer\_MediaKeySystemInfoCallback)(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback) | Demuxer\_MediaKeySystemInfoCallback | DRM\_MediaKeySystemInfo回调函数指针类型，返回解封装器实例，适用于多个解封装器实例场景。  需要使用[OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#oh_avdemuxer_setdemuxermediakeysysteminfocallback)接口将其设置为回调，推荐使用。 |
| [OH\_AVDemuxer \*OH\_AVDemuxer\_CreateWithSource(OH\_AVSource \*source)](capi-native-avdemuxer-h.md#oh_avdemuxer_createwithsource) | - | 通过source实例创建OH\_AVDemuxer实例。  source的创建、销毁及使用，详情请参考[OH\_AVSource](capi-avsource.md)。 |
| [OH\_AVErrCode OH\_AVDemuxer\_Destroy(OH\_AVDemuxer \*demuxer)](capi-native-avdemuxer-h.md#oh_avdemuxer_destroy) | - | 销毁OH\_AVDemuxer实例并清理内部资源。同一实例只能被销毁一次。  注意，销毁的实例在被重新创建之前不能再被使用。建议实例销毁成功后将指针置为NULL。 |
| [OH\_AVErrCode OH\_AVDemuxer\_SelectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)](capi-native-avdemuxer-h.md#oh_avdemuxer_selecttrackbyid) | - | 指定读取sample的轨道，解封装器将会从该轨道中读取数据，未指定的轨道不会读取。  注意，通过多次调用接口并传入不同轨道的索引来选中多个轨道。  调用[OH\_AVDemuxer\_ReadSample](capi-native-avdemuxer-h.md#oh_avdemuxer_readsample)时只会读取被选中的轨道中数据，同一轨道被选择多次时，接口会返回AV\_ERR\_OK，并且只会生效一次。 |
| [OH\_AVErrCode OH\_AVDemuxer\_UnselectTrackByID(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex)](capi-native-avdemuxer-h.md#oh_avdemuxer_unselecttrackbyid) | - | 移除读取sample的轨道，未选中的轨道的数据不会被解封装器读取。  注意，通过多次调用接口并传入不同轨道的索引来取消对多个轨道的选择。  同一轨道被多次取消选择时，接口会返回AV\_ERR\_OK，并且只会生效一次。 |
| [OH\_AVErrCode OH\_AVDemuxer\_ReadSample(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVMemory \*sample, OH\_AVCodecBufferAttr \*info)](capi-native-avdemuxer-h.md#oh_avdemuxer_readsample) | - | 获取指定轨道的sample及相关信息。  注意，读取轨道sample前，轨道必须被选中。调用接口后解封装器将自动前进到下一帧。 |
| [OH\_AVErrCode OH\_AVDemuxer\_ReadSampleBuffer(OH\_AVDemuxer \*demuxer, uint32\_t trackIndex, OH\_AVBuffer \*sample)](capi-native-avdemuxer-h.md#oh_avdemuxer_readsamplebuffer) | - | 获取指定轨道的sample及相关信息。  注意，读取轨道sample前，轨道必须被选中。调用接口后解封装器将自动前进到下一帧。 |
| [OH\_AVErrCode OH\_AVDemuxer\_SeekToTime(OH\_AVDemuxer \*demuxer, int64\_t millisecond, OH\_AVSeekMode mode)](capi-native-avdemuxer-h.md#oh_avdemuxer_seektotime) | - | 根据设定的跳转模式，将所有选中的轨道到指定时间附近。 |
| [OH\_AVErrCode OH\_AVDemuxer\_SetMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfoCallback callback)](capi-native-avdemuxer-h.md#oh_avdemuxer_setmediakeysysteminfocallback) | - | 设置DRM信息回调函数。 |
| [OH\_AVErrCode OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback(OH\_AVDemuxer \*demuxer, Demuxer\_MediaKeySystemInfoCallback callback)](capi-native-avdemuxer-h.md#oh_avdemuxer_setdemuxermediakeysysteminfocallback) | - | 设置DRM信息回调函数。 |
| [OH\_AVErrCode OH\_AVDemuxer\_GetMediaKeySystemInfo(OH\_AVDemuxer \*demuxer, DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](capi-native-avdemuxer-h.md#oh_avdemuxer_getmediakeysysteminfo) | - | 获取DRM信息。在[Demuxer\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback)或[DRM\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#drm_mediakeysysteminfocallback)接口成功回调以后，调用此接口才能获取到DRM信息。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### DRM\_MediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*DRM_MediaKeySystemInfoCallback)(DRM_MediaKeySystemInfo* mediaKeySystemInfo)
```

**描述**

DRM\_MediaKeySystemInfo回调函数指针类型，不返回解封装器实例，适用于单个解封装器实例场景。

需要使用[OH\_AVDemuxer\_SetMediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#oh_avdemuxer_setmediakeysysteminfocallback)接口将其设置为回调。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 11

**废弃版本：** 14

**替代接口：** [Demuxer\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback)

### Demuxer\_MediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Demuxer_MediaKeySystemInfoCallback)(OH_AVDemuxer *demuxer, DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

DRM\_MediaKeySystemInfo回调函数指针类型，返回解封装器实例，适用于多个解封装器实例场景。

需要使用[OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#oh_avdemuxer_setdemuxermediakeysysteminfocallback)接口将其设置为回调，推荐使用。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

### OH\_AVDemuxer\_CreateWithSource()

PhonePC/2in1TabletTVWearable

```
1. OH_AVDemuxer *OH_AVDemuxer_CreateWithSource(OH_AVSource *source)
```

**描述**

通过source实例创建OH\_AVDemuxer实例。

source的创建、销毁及使用，详情请参考[OH\_AVSource](capi-avsource.md)。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSource](capi-avsource-oh-avsource.md) \*source | 指向OH\_AVSource实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \* | 返回一个指向OH\_AVDemuxer实例的指针。  如果执行成功，则返回指向OH\_AVDemuxer实例的指针，否则返回NULL。  可能的失败原因：  1. source无效，即空指针或非OH\_AVSource实例。  2. 非OH\_AVSource实例。 |

### OH\_AVDemuxer\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_Destroy(OH_AVDemuxer *demuxer)
```

**描述**

销毁OH\_AVDemuxer实例并清理内部资源。同一实例只能被销毁一次。

注意，销毁的实例在被重新创建之前不能再被使用。建议实例销毁成功后将指针置为NULL。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：当输入的demuxer指针为空或非解封装器实例。 |

### OH\_AVDemuxer\_SelectTrackByID()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_SelectTrackByID(OH_AVDemuxer *demuxer, uint32_t trackIndex)
```

**描述**

指定读取sample的轨道，解封装器将会从该轨道中读取数据，未指定的轨道不会读取。

注意，通过多次调用接口并传入不同轨道的索引来选中多个轨道。

调用[OH\_AVDemuxer\_ReadSample](capi-native-avdemuxer-h.md#oh_avdemuxer_readsample)时只会读取被选中的轨道中数据，同一轨道被选择多次时，接口会返回AV\_ERR\_OK，并且只会生效一次。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| uint32\_t trackIndex | 需选择的轨道的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：  1. 输入的demuxer指针为空或为非解封装器实例。  2. 轨道的索引超出范围。  3. 不支持读取轨道。  AV\_ERR\_OPERATE\_NOT\_PERMIT：demuxer没有正确的初始化。 |

### OH\_AVDemuxer\_UnselectTrackByID()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_UnselectTrackByID(OH_AVDemuxer *demuxer, uint32_t trackIndex)
```

**描述**

移除读取sample的轨道，未选中的轨道的数据不会被解封装器读取。

注意，通过多次调用接口并传入不同轨道的索引来取消对多个轨道的选择。

同一轨道被多次取消选择时，接口会返回AV\_ERR\_OK，并且只会生效一次。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| uint32\_t trackIndex | 需取消选择的轨道的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的demuxer指针为空或为非解封装器实例。  AV\_ERR\_OPERATE\_NOT\_PERMIT：demuxer没有正确的初始化。 |

### OH\_AVDemuxer\_ReadSample()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_ReadSample(OH_AVDemuxer *demuxer, uint32_t trackIndex, OH_AVMemory *sample, OH_AVCodecBufferAttr *info)
```

**描述**

获取指定轨道的sample及相关信息。

注意，读取轨道sample前，轨道必须被选中。调用接口后解封装器将自动前进到下一帧。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AVDemuxer\_ReadSampleBuffer](capi-native-avdemuxer-h.md#oh_avdemuxer_readsamplebuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| uint32\_t trackIndex | 本次读取压缩帧的轨道的索引。 |
| [OH\_AVMemory](capi-core-oh-avmemory.md) \*sample | 指向OH\_AVMemory实例的指针，用于储存压缩帧数据。 |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) \*info | 指向OH\_AVCodecBufferAttr实例的指针，用于储存压缩帧的相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：  1. 输入的demuxer指针为空或为非解封装器实例。  2. 轨道的索引超出范围。  3. 不支持读取轨道。  4. 输入sample为空。  5. 输入info为空。  AV\_ERR\_OPERATE\_NOT\_PERMIT：  1. 轨道的索引没有被选中。  2. demuxer没有正确的初始化。  AV\_ERR\_NO\_MEMORY：sample容量不足以存储所有帧数据。  AV\_ERR\_UNKNOWN：无法从文件中读取或解析帧。 |

### OH\_AVDemuxer\_ReadSampleBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_ReadSampleBuffer(OH_AVDemuxer *demuxer, uint32_t trackIndex, OH_AVBuffer *sample)
```

**描述**

获取指定轨道的sample及相关信息。

注意，读取轨道sample前，轨道必须被选中，可使用[OH\_AVDemuxer\_SelectTrackByID](capi-native-avdemuxer-h.md#oh_avdemuxer_selecttrackbyid)。调用接口后解封装器将自动前进到下一帧。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| uint32\_t trackIndex | 本次读取压缩帧的轨道的索引。 |
| OH\_AVBuffer \*sample | 指向OH\_AVBuffer实例的指针，用于储存压缩帧数据以及相关信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：  1. 输入的demuxer指针为空或为非解封装器实例。  2. sample为空指针。  3. 轨道的索引超出范围。  4. 输入sample为空。  AV\_ERR\_OPERATE\_NOT\_PERMIT：  1. 轨道的索引没有被选中。  2. demuxer没有正确的初始化。  AV\_ERR\_NO\_MEMORY：sample容量不足以存储所有帧数据。  AV\_ERR\_UNKNOWN：无法从文件中读取或解析帧。 |

### OH\_AVDemuxer\_SeekToTime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_SeekToTime(OH_AVDemuxer *demuxer, int64_t millisecond, OH_AVSeekMode mode)
```

**描述**

根据设定的跳转模式，将所有选中的轨道到指定时间附近。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| int64\_t millisecond | 期望跳转位置对应的时间，单位为ms，该时间戳是相对文件开始的位置。 |
| [OH\_AVSeekMode](capi-native-avcodec-base-h.md#oh_avseekmode) mode | 跳转的模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：  1. 输入的demuxer指针为空或为非解封装器实例。  2. 毫秒值超出范围。  AV\_ERR\_OPERATE\_NOT\_PERMIT：  1. 轨道的索引没有被选中。  2. demuxer没有正确的初始化。  3. 资源无法seek。  AV\_ERR\_UNKNOWN：  1. seek失败。  2. OH\_AVSeekMode选择SEEK\_MODE\_NEXT\_SYNC，并且时间点后无I帧，可能会跳转失败。 |

### OH\_AVDemuxer\_SetMediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_SetMediaKeySystemInfoCallback(OH_AVDemuxer *demuxer, DRM_MediaKeySystemInfoCallback callback)
```

**描述**

设置DRM信息回调函数。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 11

**废弃版本：** 14

**替代接口：** [OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#oh_avdemuxer_setdemuxermediakeysysteminfocallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| [DRM\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#drm_mediakeysysteminfocallback) callback | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_OPERATE\_NOT\_PERMIT：demuxer没有正确的初始化。  AV\_ERR\_INVALID\_VAL：输入的demuxer指针为空或为非解封装器实例。 |

### OH\_AVDemuxer\_SetDemuxerMediaKeySystemInfoCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_SetDemuxerMediaKeySystemInfoCallback(OH_AVDemuxer *demuxer, Demuxer_MediaKeySystemInfoCallback callback)
```

**描述**

设置DRM信息回调函数。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| [Demuxer\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback) callback | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_OPERATE\_NOT\_PERMIT：demuxer没有正确的初始化。  AV\_ERR\_INVALID\_VAL：输入的demuxer指针为空或为非解封装器实例。 |

### OH\_AVDemuxer\_GetMediaKeySystemInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AVDemuxer_GetMediaKeySystemInfo(OH_AVDemuxer *demuxer, DRM_MediaKeySystemInfo *mediaKeySystemInfo)
```

**描述**

获取DRM信息。在[Demuxer\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback)或[DRM\_MediaKeySystemInfoCallback](capi-native-avdemuxer-h.md#drm_mediakeysysteminfocallback)接口成功回调以后，调用此接口才能获取到DRM信息。

**系统能力：** SystemCapability.Multimedia.Media.Spliter

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVDemuxer](capi-avdemuxer-oh-avdemuxer.md) \*demuxer | 指向OH\_AVDemuxer实例的指针。 |
| [DRM\_MediaKeySystemInfo](capi-avdemuxer-drm-mediakeysysteminfo.md) \*mediaKeySystemInfo | 指向DRM信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：操作成功。  AV\_ERR\_OPERATE\_NOT\_PERMIT：解封装引擎未初始化或初始化失败。  AV\_ERR\_INVALID\_VAL：  1. 输入的demuxer指针为空或为非解封装器实例。  2. mediaKeySystemInfo为nullptr。 |
