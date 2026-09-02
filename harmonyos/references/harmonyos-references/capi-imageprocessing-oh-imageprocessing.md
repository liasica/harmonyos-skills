---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing-oh-imageprocessing
title: OH_ImageProcessing
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageProcessing
category: harmonyos-references
scraped_at: 2026-09-02T14:52:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ba931bf4f88a90c40ad8189c1244456a1e44b2a5479b30e1b75a664987e5cd7
---

```c
typedef struct OH_ImageProcessing OH_ImageProcessing
```

## 概述

提供OH\_ImageProcessing结构体声明。

定义一个初始化为空的OH\_ImageProcessing指针，并调用[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)来创建图片处理实例。调用该接口前，应确保传入的指针为空。用户可根据不同的图片处理类型，分别创建多个图片处理实例。

**起始版本：** 13

**相关模块：** [ImageProcessing](capi-imageprocessing.md)

**所在头文件：** [image\_processing\_types.h](capi-image-processing-types-h.md)
