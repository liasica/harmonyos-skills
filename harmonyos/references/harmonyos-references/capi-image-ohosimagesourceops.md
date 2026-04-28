---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceops
title: OhosImageSourceOps
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceOps
category: harmonyos-references
scraped_at: 2026-04-28T08:13:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:50b60bcd76cf5dac3c9c4cea8ea61c6048cc561e260921521efe229a432df80b
---

```
1. struct OhosImageSourceOps {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源选项信息。此选项给[OH\_ImageSource\_CreateFromUri](capi-image-source-mdk-h.md#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](capi-image-source-mdk-h.md#oh_imagesource_createfromfd)、[OH\_ImageSource\_CreateFromData](capi-image-source-mdk-h.md#oh_imagesource_createfromdata)和[OH\_ImageSource\_CreateIncremental](capi-image-source-mdk-h.md#oh_imagesource_createincremental)接口使用。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t density | 图像源像素密度。 |
| int32\_t pixelFormat | 图像源像素格式，通常用于描述YUV缓冲区。 |
| struct [OhosImageSize](capi-image-ohosimagesize.md) size | 图像源像素宽高的大小。 |
