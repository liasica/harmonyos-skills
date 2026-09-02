---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-image-info
title: OH_Drawing_Image_Info
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 结构体 > OH_Drawing_Image_Info
category: harmonyos-references
scraped_at: 2026-09-02T15:02:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:010fe556e1ba789be17c0e5ac43b849c5a299af4b62f9ee16f5fe96d604e560e
---

```c
typedef struct {...} OH_Drawing_Image_Info
```

## 概述

定义图片信息结构体。

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

**所在头文件：** [drawing\_types.h](capi-drawing-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t width | 宽度，单位为像素。 |
| int32\_t height | 高度，单位为像素。 |
| [OH\_Drawing\_ColorFormat](capi-drawing-types-h.md#oh_drawing_colorformat) colorType | 颜色类型[OH\_Drawing\_ColorFormat](capi-drawing-types-h.md#oh_drawing_colorformat)。 |
| [OH\_Drawing\_AlphaFormat](capi-drawing-types-h.md#oh_drawing_alphaformat) alphaType | 透明度类型[OH\_Drawing\_AlphaFormat](capi-drawing-types-h.md#oh_drawing_alphaformat)。 |
