---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagerect
title: OhosImageRect
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OhosImageRect
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1509841d816715fba227210f21f2e6269fa9792b0b843612b35c7fdea5e425a9
---

```c
struct OhosImageRect {...}
```

## 概述

定义图像矩形信息。

**起始版本：** 10

**相关模块：** [Image](capi-image.md)

**所在头文件：** [image\_mdk.h](capi-image-mdk-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t x | 矩形x坐标值。 |
| int32\_t y | 矩形y坐标值。 |
| int32\_t width | 矩形宽度值，用pixels表示。 |
| int32\_t height | 矩形高度值，用pixels表示。 |
