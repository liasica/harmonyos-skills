---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceinfo
title: OhosImageSourceInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e967b1b27c0bef9118f0af9794c94322b90181a0e86388329c9d91a258d263f6
---

```c
struct OhosImageSourceInfo {...}
```

## 概述

定义图像源信息，由[OH\_ImageSource\_GetImageInfo](capi-image-source-mdk-h.md#oh_imagesource_getimageinfo)获取。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t pixelFormat | 图像源像素格式，由[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)设置。 |
| int32\_t colorSpace | 图像源色彩空间。 |
| int32\_t alphaType | 图像源透明度类型。 |
| int32\_t density | 图像源密度，由[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)设置。 |
| struct [OhosImageSize](capi-image-ohosimagesize.md) size | 图像源像素宽高的大小。 |
