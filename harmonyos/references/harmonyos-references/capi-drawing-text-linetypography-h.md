---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-linetypography-h
title: drawing_text_lineTypography.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_text_lineTypography.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1606feaa5f1190a64f4d9ec6f22c298b9d98df6e52f54b549323786a002a3c9d
---

## 概述

PhonePC/2in1TabletTVWearable

提供排版行相关的接口，比如获取指定位置处开始可以排版的字符个数等函数。

**引用文件：** <native\_drawing/drawing\_text\_lineTypography.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineTypography\* OH\_Drawing\_CreateLineTypography(OH\_Drawing\_TypographyCreate\* handler)](capi-drawing-text-linetypography-h.md#oh_drawing_createlinetypography) | 创建一个排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针，排版行对象保存着文本内容以及样式的载体，可以用于计算单行排版信息。 |
| [void OH\_Drawing\_DestroyLineTypography(OH\_Drawing\_LineTypography\* lineTypography)](capi-drawing-text-linetypography-h.md#oh_drawing_destroylinetypography) | 释放排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)占用的内存。 |
| [size\_t OH\_Drawing\_LineTypographyGetLineBreak(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, double width)](capi-drawing-text-linetypography-h.md#oh_drawing_linetypographygetlinebreak) | 计算在限定排版宽度的情况下，从指定位置处开始可以排版的字符个数。 |
| [OH\_Drawing\_TextLine\* OH\_Drawing\_LineTypographyCreateLine(OH\_Drawing\_LineTypography\* lineTypography,size\_t startIndex, size\_t count)](capi-drawing-text-linetypography-h.md#oh_drawing_linetypographycreateline) | 根据指定区间文本内容创建一个指向文本行对象[OH\_Drawing\_TextLine](capi-drawing-oh-drawing-textline.md)的指针。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_CreateLineTypography()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_LineTypography* OH_Drawing_CreateLineTypography(OH_Drawing_TypographyCreate* handler)
```

**描述**

创建一个排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针，排版行对象保存着文本内容以及样式的载体，可以用于计算单行排版信息。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)\* handler | 指向[OH\_Drawing\_TypographyCreate](capi-drawing-oh-drawing-typographycreate.md)对象的指针，由[OH\_Drawing\_CreateTypographyHandler](capi-drawing-text-typography-h.md#oh_drawing_createtypographyhandler)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)\* | 返回一个指向排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针。 |

### OH\_Drawing\_DestroyLineTypography()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_DestroyLineTypography(OH_Drawing_LineTypography* lineTypography)
```

**描述**

释放排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)\* lineTypography | 指向排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针，由[OH\_Drawing\_CreateLineTypography](capi-drawing-text-linetypography-h.md#oh_drawing_createlinetypography)获取。 |

### OH\_Drawing\_LineTypographyGetLineBreak()

PhonePC/2in1TabletTVWearable

```
1. size_t OH_Drawing_LineTypographyGetLineBreak(OH_Drawing_LineTypography* lineTypography,size_t startIndex, double width)
```

**描述**

计算在限定排版宽度的情况下，从指定位置处开始可以排版的字符个数。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)\* lineTypography | 指向排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针，由[OH\_Drawing\_CreateLineTypography](capi-drawing-text-linetypography-h.md#oh_drawing_createlinetypography)获取。 |
| size\_t startIndex | 开始计算排版的起始位置（包括起始位置）。取值范围需要为[0,文本字符总数）的整数。 |
| double width | 换行宽度，大于0的浮点数，单位为物理像素px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| size\_t | 返回在限定排版宽度的情况下，从指定位置处开始可以排版的字符总数，取值为整数。 |

### OH\_Drawing\_LineTypographyCreateLine()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextLine* OH_Drawing_LineTypographyCreateLine(OH_Drawing_LineTypography* lineTypography,size_t startIndex, size_t count)
```

**描述**

根据指定区间文本内容创建一个指向文本行对象[OH\_Drawing\_TextLine](capi-drawing-oh-drawing-textline.md)的指针。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)\* lineTypography | 指向排版行对象[OH\_Drawing\_LineTypography](capi-drawing-oh-drawing-linetypography.md)的指针，由[OH\_Drawing\_CreateLineTypography](capi-drawing-text-linetypography-h.md#oh_drawing_createlinetypography)获取。 |
| size\_t startIndex | 表示计算排版的起始位置，整数，取值范围为[0, 文本字符总数)。 |
| size\_t count | 表示从指定排版起始位置开始进行排版的字符个数，取值为[0,文本字符总数)的整数，startIndex和count之和不能大于文本字符总数。  可以先使用[OH\_Drawing\_LineTypographyGetLineBreak](capi-drawing-text-linetypography-h.md#oh_drawing_linetypographygetlinebreak)获得合理的可用于进行排版的字符总数。如果该值设置为0，则返回nullptr。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextLine](capi-drawing-oh-drawing-textline.md)\* | 返回一个指向文本行对象[OH\_Drawing\_TextLine](capi-drawing-oh-drawing-textline.md)的指针。 |
