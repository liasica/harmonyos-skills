---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-bitmapformat
title: OH_Drawing_BitmapFormat
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_BitmapFormat
category: harmonyos-references
scraped_at: 2026-04-28T08:15:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5166d1de63f3b49a3403b29ee6c3b8a7705fa7c0913b8dcebaeeace242779c47
---

```
1. typedef struct {...} OH_Drawing_BitmapFormat
```

## 概述

PhonePC/2in1TabletTVWearable

结构体用于描述位图像素的格式，包括颜色类型和透明度类型。

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_bitmap.h](capi-drawing-bitmap-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| OH\_Drawing\_ColorFormat colorFormat | 描述位图像素的存储格式。 |
| OH\_Drawing\_AlphaFormat alphaFormat | 描述位图像素的透明度分量。 |
