---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat
title: OhosImageSourceSupportedFormat
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceSupportedFormat
category: harmonyos-references
scraped_at: 2026-04-28T08:13:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9b3cde320247bdf82a1898152fac7959106ac9ab7ef698ed02a70c0173e4a5d0
---

```
1. struct OhosImageSourceSupportedFormat {...}
```

## 概述

PhonePC/2in1TabletTVWearable

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](capi-image-ohosimagesourcesupportedformatlist.md)和[OH\_ImageSource\_GetSupportedFormats](capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)接口使用。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* format = nullptr | 图像源支持的格式字符串头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串大小。 |
