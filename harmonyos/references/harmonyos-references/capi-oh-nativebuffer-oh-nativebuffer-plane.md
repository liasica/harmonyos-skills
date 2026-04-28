---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-plane
title: OH_NativeBuffer_Plane
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Plane
category: harmonyos-references
scraped_at: 2026-04-28T08:15:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:38120268f5c463b7bb023f05a89c5d04266974e456989b9953e7f2d15b543ee3
---

```
1. typedef struct {...} OH_NativeBuffer_Plane
```

## 概述

PhonePC/2in1TabletTVWearable

单个图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [native\_buffer.h](capi-native-buffer-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint64\_t offset | 图像平面的偏移量，单位为Byte。 |
| uint32\_t rowStride | 从图像一行的第一个值到下一行的第一个值的距离，单位为Byte。 |
| uint32\_t columnStride | 从图像一列的第一个值到下一列的第一个值的距离，单位为Byte。 |
