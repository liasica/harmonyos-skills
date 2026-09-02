---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avmetadataextractor-oh-avmetadataextractor-frameinfo
title: OH_AVMetadataExtractor_FrameInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVMetadataExtractor_FrameInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:49bb2c72185c4c3009585e48ef31aeedc269da3d5ee16e45249e0d7e97b3390a
---

```c
typedef struct {...} OH_AVMetadataExtractor_FrameInfo
```

## 概述

定义从视频中提取出的帧的信息。

**起始版本：** 23

**相关模块：** [AVMetadataExtractor](capi-avmetadataextractor.md)

**所在头文件：** [avmetadata\_extractor\_base.h](capi-avmetadata-extractor-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t requestTimeUs | 用户传入的请求时间。 |
| int64\_t actualTimeUs | 实际提取到的帧的时间；若提取失败，则为-1。 |
| [OH\_PixelmapNative\*](capi-image-nativemodule-oh-pixelmapnative.md) image | 从视频中提取出的帧图像；若提取失败，则为空指针。 |
| [OH\_AVMetadataExtractor\_FetchState](capi-avmetadata-extractor-base-h.md#oh_avmetadataextractor_fetchstate) result | 本次帧提取操作的结果状态。 |
