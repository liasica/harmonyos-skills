---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-core-oh-avcodecbufferattr
title: OH_AVCodecBufferAttr
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 结构体 > OH_AVCodecBufferAttr
category: harmonyos-references
scraped_at: 2026-09-02T15:02:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8cfbe8900a5296bc9d893f4f3d39a88c3b27f9a4d934ec3671924f3f8612813a
---

```c
typedef struct OH_AVCodecBufferAttr {...} OH_AVCodecBufferAttr
```

## 概述

定义OH\_AVCodec的缓冲区描述信息。

**起始版本：** 9

**相关模块：** [Core](capi-core.md)

**所在头文件：** [native\_avbuffer\_info.h](capi-native-avbuffer-info-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t pts | 此缓冲区的显示时间戳（以微秒为单位）。 |
| int32\_t size | 缓冲区中包含的数据的大小（以字节为单位）。 |
| int32\_t offset | 此缓冲区中有效数据的起始偏移量（以字节为单位）。 |
| uint32\_t flags | 此缓冲区具有的标志，请参阅[OH\_AVCodecBufferFlags](capi-native-avbuffer-info-h.md#oh_avcodecbufferflags)。 |
