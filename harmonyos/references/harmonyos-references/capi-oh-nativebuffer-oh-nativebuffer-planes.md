---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-planes
title: OH_NativeBuffer_Planes
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Planes
category: harmonyos-references
scraped_at: 2026-04-28T08:15:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eae4936b244b2ae127ef25ae94ff64b168248b0db2eb7b63f8fd4e7ad59d2db6
---

```
1. typedef struct OH_NativeBuffer_Planes {...} OH_NativeBuffer_Planes
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [native\_buffer.h](capi-native-buffer-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t planeCount | 不同平面的数量。 |
| [OH\_NativeBuffer\_Plane](capi-oh-nativebuffer-oh-nativebuffer-plane.md) planes[4] | 图像平面格式信息数组。 |
