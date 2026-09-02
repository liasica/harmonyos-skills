---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceops
title: OhosImageSourceOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceOps
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50dc209882182f259c2f4312018842d65d2132ae51469de770b24592d50d3ec0
---

```c
struct OhosImageSourceOps {...}
```

## 概述

定义图像源选项信息。此选项给[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)、[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)和[OH\_ImageSource\_CreateIncremental](capi-image-source-mdk-h.md#oh_imagesource_createincremental)接口使用。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t density | 图像源像素密度。 |
| int32\_t pixelFormat | 图像源像素格式，通常用于描述YUV缓冲区。 |
| struct [OhosImageSize](capi-image-ohosimagesize.md) size | 图像源像素宽高的大小。 |
