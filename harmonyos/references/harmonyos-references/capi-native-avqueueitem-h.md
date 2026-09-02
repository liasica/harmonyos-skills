---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avqueueitem-h
title: native_avqueueitem.h
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > C API > 头文件 > native_avqueueitem.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a46a3a3a629f233f4701334866cfceace86c7f8eb98938ebd0557856e9bb062e
---

## 概述

提供音视频队列元素的定义。

**引用文件：** <multimedia/av\_session/native\_avqueueitem.h>

**库：** libohavsession.so

**系统能力：** SystemCapability.Multimedia.AVSession.Core

**起始版本：** 23

**相关模块：** [OHAVSession](capi-ohavsession.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVSession\_AVQueueItem](capi-ohavsession-oh-avsession-avqueueitem.md) | OH\_AVSession\_AVQueueItem | 音视频队列元素的定义。 |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md) | OH\_AVSession\_AVMediaDescription | AVMediaDescription的声明。应用为当前资源设置的音视频媒体描述实例。 |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md) | OH\_AVSession\_AVMediaDescriptionBuilder | 音视频媒体描述构建器的声明。构建器的实例用于创建媒体描述信息。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_Create(OH\_AVSession\_AVMediaDescriptionBuilder\*\* builder)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_create) | 创建OH\_AVSession\_AVMediaDescriptionBuilder实例。当该实例不再被使用时，调用[OH\_AVSession\_AVMediaDescriptionBuilder\_Destroy](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_destroy)来释放构建器对象。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_Destroy(OH\_AVSession\_AVMediaDescriptionBuilder\* builder)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_destroy) | 销毁构建器。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetAssetId(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* assetId)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setassetid) | 设置媒体资源的当前资产ID。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetTitle(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* title)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_settitle) | 设置媒体资源的标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetSubTitle(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* subtitle)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setsubtitle) | 设置媒体资源的副标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetArtist(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* artist)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setartist) | 设置媒体资源的艺术家信息。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetAlbumCoverUri(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* albumCoverUri)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setalbumcoveruri) | 设置媒体资源的媒体图像URL。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaType(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* mediaType)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setmediatype) | 设置媒体资源的媒体类型。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetLyricContent(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* lyricContent)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setlyriccontent) | 设置媒体资源的歌词内容。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetDuration(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const int32\_t duration)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setduration) | 设置媒体资源的持续时间。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaUri(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* mediaUri)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setmediauri) | 设置媒体资源的媒体URI。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetStartPosition(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const int32\_t startPosition)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setstartposition) | 设置媒体资源的起始位置。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaSize(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const int32\_t mediaSize)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setmediasize) | 设置媒体资源的大小。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetAlbumTitle(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* albumTitle)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setalbumtitle) | 设置媒体资源的专辑标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_SetAppName(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, const char\* appName)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_setappname) | 设置媒体资源来源的应用名称。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetAssetId(OH\_AVSession\_AVMediaDescription\* description, char\*\* assetId)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getassetid) | 获取媒体资源的当前资产ID。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetTitle(OH\_AVSession\_AVMediaDescription\* description, char\*\* title)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_gettitle) | 获取媒体资源的标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetSubtitle(OH\_AVSession\_AVMediaDescription\* description, char\*\* subtitle)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getsubtitle) | 获取媒体资源的副标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetArtist(OH\_AVSession\_AVMediaDescription\* description, char\*\* artist)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getartist) | 获取媒体资源的艺术家信息。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetAlbumCoverUri(OH\_AVSession\_AVMediaDescription\* description, char\*\* albumCoverUri)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getalbumcoveruri) | 获取媒体资源的媒体图像URL。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetMediaType(OH\_AVSession\_AVMediaDescription\* description, char\*\* mediaType)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getmediatype) | 获取媒体类型信息。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetLyricContent(OH\_AVSession\_AVMediaDescription\* description, char\*\* lyricContent)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getlyriccontent) | 获取资源的歌词内容。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetDuration(OH\_AVSession\_AVMediaDescription\* description, int32\_t\* duration)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getduration) | 获取媒体资源的持续时间。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetMediaUri(OH\_AVSession\_AVMediaDescription\* description, char\*\* mediaUri)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getmediauri) | 获取媒体资源的媒体URI。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetStartPosition(OH\_AVSession\_AVMediaDescription\* description, int32\_t\* startPosition)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getstartposition) | 获取媒体资源的起始位置。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetMediaSize(OH\_AVSession\_AVMediaDescription\* description, int32\_t\* mediaSize)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getmediasize) | 获取资源的媒体大小。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetAlbumTitle(OH\_AVSession\_AVMediaDescription\* description, char\*\* albumTitle)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getalbumtitle) | 获取媒体资源的专辑标题。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_GetAppName(OH\_AVSession\_AVMediaDescription\* description, char\*\* appName)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_getappname) | 获取媒体资源的应用名。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescriptionBuilder\_GenerateAVMediaDescription(OH\_AVSession\_AVMediaDescriptionBuilder\* builder, OH\_AVSession\_AVMediaDescription\*\* avMediaDescription)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_generateavmediadescription) | 创建avMediaDescription对象。当该对象不再使用时，调用[OH\_AVSession\_AVMediaDescription\_Destroy](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_destroy)释放avMediaDescription对象。 |
| [AVQueueItem\_Result OH\_AVSession\_AVMediaDescription\_Destroy(OH\_AVSession\_AVMediaDescription\* avMediaDescription)](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_destroy) | 释放avMediaDescription对象。 |

## 函数说明

### OH\_AVSession\_AVMediaDescriptionBuilder\_Create()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Create(OH_AVSession_AVMediaDescriptionBuilder** builder)
```

**描述**

创建OH\_AVSession\_AVMediaDescriptionBuilder实例。当该实例不再被使用时，调用[OH\_AVSession\_AVMediaDescriptionBuilder\_Destroy](capi-native-avqueueitem-h.md#oh_avsession_avmediadescriptionbuilder_destroy)来释放构建器对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\*\* builder | 用于接收创建结果的构建器对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。  AVQUEUEITEM\_ERROR\_NO\_MEMORY：内存不足。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_Destroy()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_Destroy(OH_AVSession_AVMediaDescriptionBuilder* builder)
```

**描述**

销毁构建器。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetAssetId()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAssetId(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* assetId)
```

**描述**

设置媒体资源的当前资产ID。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* assetId | 媒体资源的当前资产ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数assetId为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetTitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* title)
```

**描述**

设置媒体资源的标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* title | 媒体资源的标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数title为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetSubTitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetSubTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* subtitle)
```

**描述**

设置媒体资源的副标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* subtitle | 媒体资源的副标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数subtitle为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetArtist()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetArtist(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* artist)
```

**描述**

设置媒体资源的艺术家信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* artist | 媒体资源的艺术家。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数artist为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetAlbumCoverUri()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumCoverUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumCoverUri)
```

**描述**

设置媒体资源的媒体图像URL。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* albumCoverUri | 在媒体中心显示的资源的图像URL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数albumCoverUri为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaType()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaType(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaType)
```

**描述**

设置媒体资源的媒体类型。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* mediaType | 媒体资源的媒体类型。如VIDEO或AUDIO。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数mediaType为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetLyricContent()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetLyricContent(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* lyricContent)
```

**描述**

设置媒体资源的歌词内容。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* lyricContent | 媒体资源的歌词内容，为LRC（Lyric Reduced Codec）格式，需符合标准LRC歌词格式规范。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数lyricContent为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetDuration()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetDuration(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t duration)
```

**描述**

设置媒体资源的持续时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32\_t duration | 媒体资源的持续时间。单位为毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数duration为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaUri()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaUri(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* mediaUri)
```

**描述**

设置媒体资源的媒体URI。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* mediaUri | 媒体资源的URI。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数mediaUri为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetStartPosition()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetStartPosition(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t startPosition)
```

**描述**

设置媒体资源的起始位置。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32\_t startPosition | 媒体资源的起始位置。单位为毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数startPosition是无效的。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetMediaSize()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetMediaSize(OH_AVSession_AVMediaDescriptionBuilder* builder, const int32_t mediaSize)
```

**描述**

设置媒体资源的大小。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const int32\_t mediaSize | 媒体资源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数mediaSize是无效的。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetAlbumTitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAlbumTitle(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* albumTitle)
```

**描述**

设置媒体资源的专辑标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* albumTitle | 媒体资源的专辑标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数albumTitle为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_SetAppName()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_SetAppName(OH_AVSession_AVMediaDescriptionBuilder* builder, const char* appName)
```

**描述**

设置媒体资源来源的应用名称。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| const char\* appName | 媒体资源来源的应用名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数appName为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetAssetId()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAssetId(OH_AVSession_AVMediaDescription* description, char** assetId)
```

**描述**

获取媒体资源的当前资产ID。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* assetId | 指针变量，用于接收媒体资源的当前资产ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数assetId为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetTitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetTitle(OH_AVSession_AVMediaDescription* description, char** title)
```

**描述**

获取媒体资源的标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* title | 指针变量将返回当前媒体资源的标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数title为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetSubtitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetSubtitle(OH_AVSession_AVMediaDescription* description, char** subtitle)
```

**描述**

获取媒体资源的副标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* subtitle | 指针变量将返回当前媒体资源的副标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数subtitle为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetArtist()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetArtist(OH_AVSession_AVMediaDescription* description, char** artist)
```

**描述**

获取媒体资源的艺术家信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* artist | 指针变量将返回当前媒体资源的艺术家信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数artist为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetAlbumCoverUri()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumCoverUri(OH_AVSession_AVMediaDescription* description, char** albumCoverUri)
```

**描述**

获取媒体资源的媒体图像URL。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* albumCoverUri | 指针变量将返回资源的媒体图像URL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数albumCoverUri为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetMediaType()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaType(OH_AVSession_AVMediaDescription* description, char** mediaType)
```

**描述**

获取媒体类型信息。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* mediaType | 指针变量将返回当前媒体类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数mediaType为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetLyricContent()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetLyricContent(OH_AVSession_AVMediaDescription* description, char** lyricContent)
```

**描述**

获取资源的歌词内容。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* lyricContent | 指针变量将返回当前媒体歌词内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数lyricContent为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetDuration()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetDuration(OH_AVSession_AVMediaDescription* description, int32_t* duration)
```

**描述**

获取媒体资源的持续时间。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| int32\_t\* duration | 指针变量将返回当前媒体资源的总时长。单位为毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数duration为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetMediaUri()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaUri(OH_AVSession_AVMediaDescription* description, char** mediaUri)
```

**描述**

获取媒体资源的媒体URI。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* mediaUri | 指针变量将返回当前媒体资源标识符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数mediaUri为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetStartPosition()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetStartPosition(OH_AVSession_AVMediaDescription* description, int32_t* startPosition)
```

**描述**

获取媒体资源的起始位置。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| int32\_t\* startPosition | 指针变量将返回当前媒体资源开始的位置。单位为毫秒（ms）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数startPosition为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetMediaSize()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetMediaSize(OH_AVSession_AVMediaDescription* description, int32_t* mediaSize)
```

**描述**

获取资源的媒体大小。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| int32\_t\* mediaSize | 指针变量将返回当前媒体资源的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数mediaSize为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetAlbumTitle()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAlbumTitle(OH_AVSession_AVMediaDescription* description, char** albumTitle)
```

**描述**

获取媒体资源的专辑标题。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* albumTitle | 指针变量将返回当前媒体资源的专辑标题。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数albumTitle为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_GetAppName()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_GetAppName(OH_AVSession_AVMediaDescription* description, char** appName)
```

**描述**

获取媒体资源的应用名。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* description | 表示音视频媒体描述实例指针。 |
| char\*\* appName | 指针变量将返回媒体资源的应用名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数description为nullptr。  2. 参数appName为nullptr。 |

### OH\_AVSession\_AVMediaDescriptionBuilder\_GenerateAVMediaDescription()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescriptionBuilder_GenerateAVMediaDescription(OH_AVSession_AVMediaDescriptionBuilder* builder, OH_AVSession_AVMediaDescription** avMediaDescription)
```

**描述**

创建avMediaDescription对象。当该对象不再使用时，调用[OH\_AVSession\_AVMediaDescription\_Destroy](capi-native-avqueueitem-h.md#oh_avsession_avmediadescription_destroy)释放avMediaDescription对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescriptionBuilder](capi-ohavsession-oh-avsession-avmediadescriptionbuilder.md)\* builder | 表示音视频媒体描述构建器实例指针。 |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\*\* avMediaDescription | 指向用于接收avMediaDescription对象的指针变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_NO\_MEMORY：内存不足。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr。  2. 参数avMediaDescription为nullptr。 |

### OH\_AVSession\_AVMediaDescription\_Destroy()

```c
AVQueueItem_Result OH_AVSession_AVMediaDescription_Destroy(OH_AVSession_AVMediaDescription* avMediaDescription)
```

**描述**

释放avMediaDescription对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVSession\_AVMediaDescription](capi-ohavsession-oh-avsession-avmediadescription.md)\* avMediaDescription | 指向要释放的avMediaDescription对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AVQueueItem\_Result](capi-native-avsession-errors-h.md#avqueueitem_result) | AVQUEUEITEM\_SUCCESS：函数执行成功。  AVQUEUEITEM\_ERROR\_INVALID\_PARAM：参数avMediaDescription为nullptr。 |
