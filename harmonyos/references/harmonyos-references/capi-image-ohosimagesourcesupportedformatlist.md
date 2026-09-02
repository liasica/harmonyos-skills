---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist
title: OhosImageSourceSupportedFormatList
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSourceSupportedFormatList
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a9d1531f05b5dec4727bf4c1ce814a8c70a3e7a3d10ed0f7fae9abd27e760b82
---

```c
struct OhosImageSourceSupportedFormatList {...}
```

## 概述

定义图像源支持的格式字符串列表。由[OH\_ImageSource\_GetSupportedFormats](capi-image-source-mdk-h.md#oh_imagesource_getsupportedformats)获取。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_source\_mdk.h](capi-image-source-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| struct [OhosImageSourceSupportedFormat](capi-image-ohosimagesourcesupportedformat.md)\*\* supportedFormatList = nullptr | 图像源支持的格式字符串列表头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串列表大小。 |
