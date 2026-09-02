---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-planes
title: OH_NativeBuffer_Planes
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_NativeBuffer_Planes
category: harmonyos-references
scraped_at: 2026-09-02T15:02:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a20ff64e3b67cf7874629638ea18a66942e62611c1c07509b0fafcf123dc3c2b
---

```c
typedef struct {...} OH_NativeBuffer_Planes
```

## 概述

OH\_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](capi-oh-nativebuffer.md)

**所在头文件：** [native\_buffer.h](capi-native-buffer-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t planeCount | 不同平面的数量。 |
| [OH\_NativeBuffer\_Plane](capi-oh-nativebuffer-oh-nativebuffer-plane.md) planes[4] | 图像平面格式信息数组。 |
