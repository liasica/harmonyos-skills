---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avbuffer-info-h
title: native_avbuffer_info.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avbuffer_info.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:84754f47da887bf20f167565ff35c0ca3ab27bbe72e7788352b6dadc2944df74
---

## 概述

PhonePC/2in1TabletTVWearable

声明了媒体数据结构AVBuffer属性的定义。

**引用文件：** <multimedia/player\_framework/native\_avbuffer\_info.h>

**库：** libnative\_media\_core.so

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

**相关模块：** [Core](capi-core.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) | OH\_AVCodecBufferAttr | 定义OH\_AVCodec的缓冲区描述信息。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AVCodecBufferFlags](capi-native-avbuffer-info-h.md#oh_avcodecbufferflags) | OH\_AVCodecBufferFlags | 枚举OH\_AVCodec缓冲区标记的类别。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_AVCodecBufferFlags

PhonePC/2in1TabletTVWearable

```
1. enum OH_AVCodecBufferFlags
```

**描述**

枚举OH\_AVCodec缓冲区标记的类别。

**系统能力：** SystemCapability.Multimedia.Media.Core

**起始版本：** 9

| 枚举项 | 描述 |
| --- | --- |
| AVCODEC\_BUFFER\_FLAGS\_NONE = 0 | 表示为普通帧。 |
| AVCODEC\_BUFFER\_FLAGS\_EOS = 1 << 0 | 表示缓冲区是流结束帧。 |
| AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME = 1 << 1 | 表示缓冲区包含关键帧。 |
| AVCODEC\_BUFFER\_FLAGS\_INCOMPLETE\_FRAME = 1 << 2 | 表示缓冲区中的数据只是帧的一部分。 |
| AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA = 1 << 3 | 表示缓冲区包含编解码特定数据。 |
| AVCODEC\_BUFFER\_FLAGS\_DISCARD = 1 << 4 | 表示缓冲区被解码依赖，解码之后的数据可丢弃。  **起始版本：** 12 |
| AVCODEC\_BUFFER\_FLAGS\_DISPOSABLE = 1 << 5 | 表示缓冲区不被参考可直接丢弃。  **起始版本：** 12 |
