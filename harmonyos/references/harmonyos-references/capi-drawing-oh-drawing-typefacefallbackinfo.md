---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-typefacefallbackinfo
title: OH_Drawing_TypefaceFallbackInfo
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_TypefaceFallbackInfo
category: harmonyos-references
scraped_at: 2026-11-12T09:57:05+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bb84e252add34169b185a01a81f2bf9e3d60f567c0cadc42e09a93cb606a86d3
---

```c
typedef struct {...} OH_Drawing_TypefaceFallbackInfo
```

## 概述

定义字体回退信息的结构体，包含一组使用相同回退字体的字形数组。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 26.0.1

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_font.h](capi-drawing-font-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md) \*typeface | 指向匹配到的字体对象的指针。  **起始版本：** 26.0.1 |
| uint16\_t \*glyphIds | 指向字形ID数组的指针。  **起始版本：** 26.0.1 |
| uint32\_t glyphCount | 字形ID数组glyphIds的大小。  **起始版本：** 26.0.1 |
