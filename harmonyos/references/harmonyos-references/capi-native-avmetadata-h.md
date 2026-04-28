---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avmetadata-h
title: native_avmetadata.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avmetadata.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7c7393e473ff48dbb1b5bfd7a664c038e3f246f8cdc47f8c8a13ac0a963478d7
---

## 概述

PhonePC/2in1TabletTVWearable

提供播控元数据的定义。

**引用文件：** <multimedia/av\_session/native\_avmetadata.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 13

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVMetadataBuilderStruct](capi-ohavsession-oh-avmetadatabuilderstruct.md) | OH\_AVMetadataBuilder | 会话元数据构造器。构造器用于构造会话元数据。 |
| [OH\_AVMetadataStruct](capi-ohavsession-oh-avmetadatastruct.md) | OH\_AVMetadata | 会话元数据。资源设置的avmetadata的实例。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_Create(OH\_AVMetadataBuilder\*\* builder)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_create) | 创建一个元数据构造器。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_Destroy(OH\_AVMetadataBuilder\* builder)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_destroy) | 销毁元数据构造器。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAssetId(OH\_AVMetadataBuilder\* builder, const char\* assetId)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setassetid) | 设置当前媒体资源id。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetTitle(OH\_AVMetadataBuilder\* builder, const char\* title)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_settitle) | 设置资源标题。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetArtist(OH\_AVMetadataBuilder\* builder, const char\* artist)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setartist) | 设置资源所属的艺术家信息。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAuthor(OH\_AVMetadataBuilder\* builder, const char\* author)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setauthor) | 设置资源的作者。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAlbum(OH\_AVMetadataBuilder\* builder, const char\* album)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setalbum) | 设置资源专辑名称。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetWriter(OH\_AVMetadataBuilder\* builder, const char\* writer)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setwriter) | 设置资源词作者。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetComposer(OH\_AVMetadataBuilder\* builder, const char\* composer)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setcomposer) | 设置资源作曲者。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDuration(OH\_AVMetadataBuilder\* builder, int64\_t duration)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setduration) | 设置资源播放时长。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetMediaImageUri(OH\_AVMetadataBuilder\* builder, const char\* mediaImageUri)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setmediaimageuri) | 设置媒体图片数据。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetSubtitle(OH\_AVMetadataBuilder\* builder, const char\* subtitle)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setsubtitle) | 设置副标题。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDescription(OH\_AVMetadataBuilder\* builder, const char\* description)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setdescription) | 设置媒体描述信息。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetLyric(OH\_AVMetadataBuilder\* builder, const char\* lyric)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setlyric) | 设置歌词。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetSkipIntervals(OH\_AVMetadataBuilder\* builder, AVMetadata\_SkipIntervals intervals)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setskipintervals) | 设置资源的跳转间隔时间。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDisplayTags(OH\_AVMetadataBuilder\* builder, int32\_t tags)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setdisplaytags) | 设置媒体资源的金标类型。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetFilter(OH\_AVMetadataBuilder\* builder, uint32\_t filter)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_setfilter) | 设置支持的协议。 |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_GenerateAVMetadata(OH\_AVMetadataBuilder\* builder, OH\_AVMetadata\*\* avMetadata)](capi-native-avmetadata-h.md#oh_avmetadatabuilder_generateavmetadata) | 生成媒体元数据对象。 |
| [AVMetadata\_Result OH\_AVMetadata\_Destroy(OH\_AVMetadata\* avMetadata)](capi-native-avmetadata-h.md#oh_avmetadata_destroy) | 释放媒体元数据对象。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AVMetadataBuilder\_Create()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_Create(OH_AVMetadataBuilder** builder)
```

**描述**

创建一个元数据构造器。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\*\* builder | 该引用指向创建的构造器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：参数builder为nullptr。  AVMETADATA\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AVMetadataBuilder\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_Destroy(OH_AVMetadataBuilder* builder)
```

**描述**

销毁元数据构造器。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AVMetadataBuilder\_SetAssetId()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetAssetId(OH_AVMetadataBuilder* builder, const char* assetId)
```

**描述**

设置当前媒体资源id。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* assetId | 资源id。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数assetId为nullptr。 |

### OH\_AVMetadataBuilder\_SetTitle()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetTitle(OH_AVMetadataBuilder* builder, const char* title)
```

**描述**

设置资源标题。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* title | 标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数title为nullptr。 |

### OH\_AVMetadataBuilder\_SetArtist()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetArtist(OH_AVMetadataBuilder* builder, const char* artist)
```

**描述**

设置资源所属的艺术家信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* artist | 媒体资源的艺术家。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数artist为nullptr。 |

### OH\_AVMetadataBuilder\_SetAuthor()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetAuthor(OH_AVMetadataBuilder* builder, const char* author)
```

**描述**

设置资源的作者。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* author | 作者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数author为nullptr。 |

### OH\_AVMetadataBuilder\_SetAlbum()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetAlbum(OH_AVMetadataBuilder* builder, const char* album)
```

**描述**

设置资源专辑名称。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* album | 专辑名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数album为nullptr。 |

### OH\_AVMetadataBuilder\_SetWriter()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetWriter(OH_AVMetadataBuilder* builder, const char* writer)
```

**描述**

设置资源词作者。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* writer | 词作者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数writer为nullptr。 |

### OH\_AVMetadataBuilder\_SetComposer()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetComposer(OH_AVMetadataBuilder* builder, const char* composer)
```

**描述**

设置资源作曲者。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* composer | 作曲者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数composer为nullptr。 |

### OH\_AVMetadataBuilder\_SetDuration()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetDuration(OH_AVMetadataBuilder* builder, int64_t duration)
```

**描述**

设置资源播放时长。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| int64\_t duration | 资源播放时长，以ms为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AVMetadataBuilder\_SetMediaImageUri()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetMediaImageUri(OH_AVMetadataBuilder* builder, const char* mediaImageUri)
```

**描述**

设置媒体图片数据。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* mediaImageUri | 网络资源图片数据地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数mediaImageUri为nullptr。 |

### OH\_AVMetadataBuilder\_SetSubtitle()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetSubtitle(OH_AVMetadataBuilder* builder, const char* subtitle)
```

**描述**

设置副标题。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* subtitle | 副标题名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数subtitle为nullptr。 |

### OH\_AVMetadataBuilder\_SetDescription()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetDescription(OH_AVMetadataBuilder* builder, const char* description)
```

**描述**

设置媒体描述信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* description | 媒体描述信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数description为nullptr。 |

### OH\_AVMetadataBuilder\_SetLyric()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetLyric(OH_AVMetadataBuilder* builder, const char* lyric)
```

**描述**

设置歌词。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| const char\* lyric | LRC格式的歌词内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数lyric为nullptr。 |

### OH\_AVMetadataBuilder\_SetSkipIntervals()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetSkipIntervals(OH_AVMetadataBuilder* builder, AVMetadata_SkipIntervals intervals)
```

**描述**

设置资源的跳转间隔时间。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| [AVMetadata\_SkipIntervals](capi-native-avsession-base-h.md#avmetadata_skipintervals) intervals | 跳转的时间间隔。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数intervals为nullptr。 |

### OH\_AVMetadataBuilder\_SetDisplayTags()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetDisplayTags(OH_AVMetadataBuilder* builder, int32_t tags)
```

**描述**

设置媒体资源的金标类型。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| int32\_t tags | 用于显示在播控的媒体资源的金标类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AVMetadataBuilder\_SetFilter()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_SetFilter(OH_AVMetadataBuilder* builder, uint32_t filter)
```

**描述**

设置支持的协议。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| uint32\_t filter | 此会话支持的协议。如果没有设置，默认为[AVSession\_ProtocolType](capi-native-avsession-base-h.md#avsession_protocoltype).TYPE\_CAST\_PLUS\_STREAM。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数filter是无效的。 |

### OH\_AVMetadataBuilder\_GenerateAVMetadata()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadataBuilder_GenerateAVMetadata(OH_AVMetadataBuilder* builder, OH_AVMetadata** avMetadata)
```

**描述**

生成媒体元数据对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadataBuilder](capi-ohavsession-oh-avmetadatabuilderstruct.md)\* builder | 指向元数据构造器的实例。 |
| [OH\_AVMetadata](capi-ohavsession-oh-avmetadatastruct.md)\*\* avMetadata | 指向元数据的指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_NO\_MEMORY：内存不足。  AVMETADATA\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数avMetadata为nullptr。 |

### OH\_AVMetadata\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. AVMetadata_Result OH_AVMetadata_Destroy(OH_AVMetadata* avMetadata)
```

**描述**

释放媒体元数据对象。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVMetadata](capi-ohavsession-oh-avmetadatastruct.md)\* avMetadata | 指向元数据的指针对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVMetadata\_Result](capi-native-avsession-errors-h.md#avmetadata_result) | AVMETADATA\_SUCCESS：函数执行成功。  AVMETADATA\_ERROR\_INVALID\_PARAM：参数avMetadata为nullptr。 |
