---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohospixelmapinfos
title: OhosPixelMapInfos
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosPixelMapInfos
category: harmonyos-references
scraped_at: 2026-04-28T08:13:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c6ae3c129fb6b1a4258ef18c152d7003147747f0dc0a57d5efda69e028e12072
---

```
1. typedef struct OhosPixelMapInfos {...} OhosPixelMapInfos
```

## 概述

PhonePC/2in1TabletTVWearable

用于定义PixelMap的相关信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_pixel\_map\_mdk.h](capi-image-pixel-map-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t width | 图片的宽，用pixels表示。 |
| uint32\_t height | 图片的高，用pixels表示。 |
| uint32\_t rowSize | 图片在内存中，每行所占的字节数。  DMA内存为图片的宽 \* 每个像素字节数 + 每行末尾填充字节数；其他内存为图片的宽 \* 每个像素字节数。 |
| int32\_t pixelFormat | Pixel的格式。 |
