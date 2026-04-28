---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-fontadjustinfo
title: OH_Drawing_FontAdjustInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_FontAdjustInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a80fd4481546c20e7367079eaf987189a68a1dcb847b1631aa0caba206a64e3
---

```
1. typedef struct OH_Drawing_FontAdjustInfo {...} OH_Drawing_FontAdjustInfo
```

## 概述

PhonePC/2in1TabletTVWearable

字重映射信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_text\_typography.h](capi-drawing-text-typography-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int weight | 字体原本的字重值。 |
| int to | 字体在应用中显示的字重值。 |
