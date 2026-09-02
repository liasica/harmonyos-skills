---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesize
title: OhosImageSize
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageSize
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b014d64bda8076db57dbf2a2c425ecfe8a931334ab59770317d0a7aa5d308c6d
---

```c
struct OhosImageSize {...}
```

## 概述

定义图像大小。是[OhosImageDecodingOps](capi-image-ohosimagedecodingops.md)的成员变量。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_mdk\_common.h](capi-image-mdk-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t width | 像素中的图像宽度，用pixels表示。 |
| int32\_t height | 像素中的图像高度，用pixels表示。 |
