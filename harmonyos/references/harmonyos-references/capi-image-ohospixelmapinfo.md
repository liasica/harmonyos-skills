---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfo
title: OhosPixelMapInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosPixelMapInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:593dbe276e4cf9894300b34a09796471205498236a545f2b9deab1b6b569f6e8
---

```
1. struct OhosPixelMapInfo {...}
```

## 概述

PhonePC/2in1TabletTVWearable

用于定义PixelMap的相关信息。

**起始版本：** 8

**废弃版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_pixel\_map\_napi.h](capi-image-pixel-map-napi-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t width | 图片的宽，用pixels表示。 |
| uint32\_t height | 图片的高，用pixels表示。 |
| uint32\_t rowSize | 图片在内存中，每行所占的字节数。  DMA内存为图片的宽 \* 每个像素字节数 + 每行末尾填充字节数；其他内存为图片的宽 \* 每个像素字节数。 |
| int32\_t pixelFormat | Pixel的格式，取值范围：  0：未知格式。  2：格式为RGB\_565。  3：格式为RGBA\_8888。  4：格式为BGRA\_8888。  5：格式为RGB\_888。  6：格式为ALPHA\_8。  7：格式为RGBA\_F16。  8：格式为NV21。  9：格式为NV12。 |
