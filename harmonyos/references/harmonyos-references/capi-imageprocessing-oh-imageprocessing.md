---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-imageprocessing-oh-imageprocessing
title: OH_ImageProcessing
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageProcessing
category: harmonyos-references
scraped_at: 2026-04-28T08:13:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df88a1cc01a0d3dbb2c6f4e978cc7799ad38df315140a96c623339656c16bcde
---

```
1. typedef struct OH_ImageProcessing OH_ImageProcessing
```

## 概述

PhonePC/2in1TabletTV

提供OH\_ImageProcessing结构体声明。

定义了OH\_ImageProcessing的空指针并调用[OH\_ImageProcessing\_Create](capi-image-processing-h.md#oh_imageprocessing_create)来创建图片处理实例。在创建实例之前，指针应为空。用户可以为不同的处理类型创建多个图片实例。

**起始版本：** 13

**相关模块：** [ImageProcessing](capi-imageprocessing.md)

**所在头文件：** [image\_processing\_types.h](capi-image-processing-types-h.md)
