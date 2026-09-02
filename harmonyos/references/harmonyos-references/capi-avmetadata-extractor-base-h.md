---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadata-extractor-base-h
title: avmetadata_extractor_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > avmetadata_extractor_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a3932efd95fddb2474329c0514b4f3e5c2b1db9b861e7da6161081e59b1ebc74
---

## 概述

定义AVMetadataExtractor常量。

**引用文件：** <multimedia/player\_framework/avmetadata\_extractor\_base.h>

**库：** libavmetadata\_extractor.so

**系统能力：** SystemCapability.Multimedia.Media.AVMetadataExtractor

**起始版本：** 18

**相关模块：** [AVMetadataExtractor](capi-avmetadataextractor.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVMetadataExtractor\_FrameInfo](capi-avmetadataextractor-oh-avmetadataextractor-frameinfo.md) | OH\_AVMetadataExtractor\_FrameInfo | 定义从视频中提取出的帧的信息。 |
| [OH\_AVMetadataExtractor\_OutputParam](capi-avmetadataextractor-oh-avmetadataextractor-outputparam.md) | OH\_AVMetadataExtractor\_OutputParam | 定义由AVMetadataExtractor提取的帧的输出参数。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVMetadataExtractor\_FetchState](capi-avmetadata-extractor-base-h.md#oh_avmetadataextractor_fetchstate) | OH\_AVMetadataExtractor\_FetchState | 枚举帧提取操作的结果状态。 |

### 变量

| 名称 | 描述 |
| --- | --- |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_ALBUM = "album" | 获取专辑标题的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_ALBUM\_ARTIST = "albumArtist" | 获取专辑艺术家的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_ARTIST = "artist" | 获取媒体资源艺术家的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_AUTHOR = "author" | 获取媒体资源作者的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_DATE\_TIME = "dateTime" | 获取媒体资源创建时间的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_DATE\_TIME\_FORMAT = "dateTimeFormat" | 获取媒体资源创建时间的关键字，对应值类型为const char\*，按YYYY-MM-DD HH:mm:ss格式输出。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_COMPOSER = "composer" | 获取媒体资源作曲家的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_DURATION = "duration" | 获取媒体资源时长的关键字，对应值类型为int64\_t，单位为毫秒（ms）。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_GENRE = "genre" | 获取媒体资源类型或体裁的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_HAS\_AUDIO = "hasAudio" | 获取媒体资源是否包含音频的关键字，对应值类型为int32\_t。  取值原则：0表示不包含音频，1表示包含音频。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_HAS\_VIDEO = "hasVideo" | 获取媒体资源是否包含视频的关键字，对应值类型为int32\_t。  取值原则：0表示不包含视频，1表示包含视频。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_MIME\_TYPE = "mimeType" | 获取媒体资源mime类型的关键字，对应值类型为const char\*，例如：“video/mp4”、“audio/mp4”和“audio/amr-wb”。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_TRACK\_COUNT = "trackCount" | 获取媒体资源轨道数量的关键字，对应值类型为int32\_t。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_SAMPLE\_RATE = "sampleRate" | 获取音频采样率的关键字，对应值类型为int32\_t，单位为赫兹（Hz）。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_TITLE = "title" | 获取媒体资源标题的关键字，对应值类型为const char\*。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_HEIGHT = "videoHeight" | 获取视频高度的关键字，对应值类型为int32\_t，单位为像素。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_WIDTH = "videoWidth" | 获取视频宽度的关键字，对应值类型为int32\_t，单位为像素。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_ORIENTATION = "videoOrientation" | 获取视频旋转方向的关键字，对应值类型为int32\_t，单位为度（°）。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_VIDEO\_IS\_HDR\_VIVID = "hdrType" | 获取是否是HDR Vivid视频的关键字，对应值类型为int32\_t。  详情请参阅media\_types.h中的[OH\_Core\_HdrType](capi-media-types-h.md#oh_core_hdrtype)。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_LOCATION\_LATITUDE = "latitude" | 获取地理位置中的纬度值的关键字，对应值类型为float。  **起始版本：** 18 |
| static const char \* OH\_AVMETADATA\_EXTRACTOR\_LOCATION\_LONGITUDE = "longitude" | 获取地理位置中的经度值的关键字，对应值类型为float。  **起始版本：** 18 |

## 枚举类型说明

### OH\_AVMetadataExtractor\_FetchState

```c
enum OH_AVMetadataExtractor_FetchState
```

**描述**

枚举帧提取操作的结果状态。

**起始版本：** 23

| 枚举项 | 描述 |
| --- | --- |
| OH\_AVMETADATA\_EXTRACTOR\_FETCH\_FAILED = 0 | 帧提取操作失败。 |
| OH\_AVMETADATA\_EXTRACTOR\_FETCH\_SUCCEEDED = 1 | 帧提取操作成功。 |
| OH\_AVMETADATA\_EXTRACTOR\_FETCH\_CANCELED = 2 | 帧提取操作被用户取消。 |
