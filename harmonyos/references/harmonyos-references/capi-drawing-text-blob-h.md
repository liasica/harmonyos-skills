---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-text-blob-h
title: drawing_text_blob.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_text_blob.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:080d8285d2ccc05c3539a8739acdeb25f931b7be93da5674331bbc9a69cd4a58
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与文字相关的功能函数。

**引用文件：** <native\_drawing/drawing\_text\_blob.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_RunBuffer](capi-drawing-oh-drawing-runbuffer.md) | OH\_Drawing\_RunBuffer | 结构体用于描述一块内存，描述文字和位置信息。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlobBuilder\* OH\_Drawing\_TextBlobBuilderCreate(void)](capi-drawing-text-blob-h.md#oh_drawing_textblobbuildercreate) | 用于创建一个文本构造器对象。 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromText(const void\* text, size\_t byteLength,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefromtext) | 使用文本创建一个文本对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  text、font任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromPosText(const void\* text, size\_t byteLength,OH\_Drawing\_Point2D\* point2D, const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefrompostext) | 使用文本创建文本对象，文本对象中每个字符的坐标由OH\_Drawing\_Point2D数组中对应的坐标信息决定。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  text、point2D、font任意一个为NULL或byteLength等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobCreateFromString(const char\* str,const OH\_Drawing\_Font\* font, OH\_Drawing\_TextEncoding textEncoding)](capi-drawing-text-blob-h.md#oh_drawing_textblobcreatefromstring) | 使用字符串创建文本对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  str、font任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；  textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。 |
| [void OH\_Drawing\_TextBlobGetBounds(OH\_Drawing\_TextBlob\* textBlob, OH\_Drawing\_Rect\* rect)](capi-drawing-text-blob-h.md#oh_drawing_textblobgetbounds) | 获取文本对象的边界范围。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  textBlob、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_TextBlobUniqueID(const OH\_Drawing\_TextBlob\* textBlob)](capi-drawing-text-blob-h.md#oh_drawing_textblobuniqueid) | 获取文本的标识符，该标识符是唯一的非零值。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  textBlob为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [const OH\_Drawing\_RunBuffer\* OH\_Drawing\_TextBlobBuilderAllocRunPos(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder,const OH\_Drawing\_Font\* font, int32\_t count, const OH\_Drawing\_Rect\* rect)](capi-drawing-text-blob-h.md#oh_drawing_textblobbuilderallocrunpos) | 申请一块内存，用于存储文字和位置信息。返回的指针无需调用者管理，当调用[OH\_Drawing\_TextBlobBuilderMake](capi-drawing-text-blob-h.md#oh_drawing_textblobbuildermake)后禁止使用。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  textBlobBuilder、font任意一个为NULL或者count小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_TextBlob\* OH\_Drawing\_TextBlobBuilderMake(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)](capi-drawing-text-blob-h.md#oh_drawing_textblobbuildermake) | 用于从文本构造器中创建文本对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  textBlobBuilder为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_TextBlobDestroy(OH\_Drawing\_TextBlob\* textBlob)](capi-drawing-text-blob-h.md#oh_drawing_textblobdestroy) | 用于销毁文本对象并回收该对象占有的内存。 |
| [void OH\_Drawing\_TextBlobBuilderDestroy(OH\_Drawing\_TextBlobBuilder\* textBlobBuilder)](capi-drawing-text-blob-h.md#oh_drawing_textblobbuilderdestroy) | 用于销毁文本构造器对象并回收该对象占有的内存。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_TextBlobBuilderCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextBlobBuilder* OH_Drawing_TextBlobBuilderCreate(void)
```

**描述**

用于创建一个文本构造器对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBlobBuilder](capi-drawing-oh-drawing-textblobbuilder.md)\* | 函数会返回一个指针，指针指向创建的文本构造器对象。 |

### OH\_Drawing\_TextBlobCreateFromText()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromText(const void* text, size_t byteLength,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用文本创建一个文本对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

text、font任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void\* text | 指向文本的指针。 |
| size\_t byteLength | 文本的字节长度。 |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字体对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncoding | 文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* | 函数返回一个指针，指针指向创建的文本对象[OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)。 |

### OH\_Drawing\_TextBlobCreateFromPosText()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromPosText(const void* text, size_t byteLength,OH_Drawing_Point2D* point2D, const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用文本创建文本对象，文本对象中每个字符的坐标由OH\_Drawing\_Point2D数组中对应的坐标信息决定。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

text、point2D、font任意一个为NULL或byteLength等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const void\* text | 指向文本的指针。 |
| size\_t byteLength | 文本的字节长度。 |
| [OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)\* point2D | 二维点[OH\_Drawing\_Point2D](capi-drawing-oh-drawing-point2d.md)数组首地址，数组个数由[OH\_Drawing\_FontCountText](capi-drawing-font-h.md#oh_drawing_fontcounttext)计算结果决定。 |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字体对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncoding | 文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* | 函数返回一个指针，指针指向创建的文本对象[OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)。 |

### OH\_Drawing\_TextBlobCreateFromString()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextBlob* OH_Drawing_TextBlobCreateFromString(const char* str,const OH_Drawing_Font* font, OH_Drawing_TextEncoding textEncoding)
```

**描述**

使用字符串创建文本对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

str、font任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER；

textEncoding不在枚举范围内返回OH\_DRAWING\_ERROR\_PARAMETER\_OUT\_OF\_RANGE。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* str | 指向字符串的指针。 |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字体对象[OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)的指针。 |
| [OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding) textEncoding | 文本编码类型[OH\_Drawing\_TextEncoding](capi-drawing-types-h.md#oh_drawing_textencoding)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* | 函数返回一个指针，指针指向创建的文本对象[OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)。 |

### OH\_Drawing\_TextBlobGetBounds()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_TextBlobGetBounds(OH_Drawing_TextBlob* textBlob, OH_Drawing_Rect* rect)
```

**描述**

获取文本对象的边界范围。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

textBlob、rect任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* textBlob | 指向文本对象[OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)的指针。 |
| [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 指向矩形对象[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)的指针，开发者可调用[OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)接口创建。 |

### OH\_Drawing\_TextBlobUniqueID()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_TextBlobUniqueID(const OH_Drawing_TextBlob* textBlob)
```

**描述**

获取文本的标识符，该标识符是唯一的非零值。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

textBlob为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* textBlob | 指向文本对象[OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 返回文本对象的标识符。 |

### OH\_Drawing\_TextBlobBuilderAllocRunPos()

PhonePC/2in1TabletTVWearable

```
1. const OH_Drawing_RunBuffer* OH_Drawing_TextBlobBuilderAllocRunPos(OH_Drawing_TextBlobBuilder* textBlobBuilder,const OH_Drawing_Font* font, int32_t count, const OH_Drawing_Rect* rect)
```

**描述**

申请一块内存，用于存储文字和位置信息。返回的指针无需调用者管理，当调用[OH\_Drawing\_TextBlobBuilderMake](capi-drawing-text-blob-h.md#oh_drawing_textblobbuildermake)后禁止使用。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder、font任意一个为NULL或者count小于等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlobBuilder](capi-drawing-oh-drawing-textblobbuilder.md)\* textBlobBuilder | 指向文本构造器对象的指针。 |
| const [OH\_Drawing\_Font](capi-drawing-oh-drawing-font.md)\* font | 指向字体对象的指针。 |
| int32\_t count | 文字的数量。 |
| const [OH\_Drawing\_Rect](capi-drawing-oh-drawing-rect.md)\* rect | 文本的边界框，为NULL表示不设置边界框。 |

### OH\_Drawing\_TextBlobBuilderMake()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_TextBlob* OH_Drawing_TextBlobBuilderMake(OH_Drawing_TextBlobBuilder* textBlobBuilder)
```

**描述**

用于从文本构造器中创建文本对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

textBlobBuilder为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlobBuilder](capi-drawing-oh-drawing-textblobbuilder.md)\* textBlobBuilder | 指向文本构造器对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* | 返回一个指针，指针指向创建的文本对象。 |

### OH\_Drawing\_TextBlobDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_TextBlobDestroy(OH_Drawing_TextBlob* textBlob)
```

**描述**

用于销毁文本对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlob](capi-drawing-oh-drawing-textblob.md)\* textBlob | 指向文本对象的指针。 |

### OH\_Drawing\_TextBlobBuilderDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_TextBlobBuilderDestroy(OH_Drawing_TextBlobBuilder* textBlobBuilder)
```

**描述**

用于销毁文本构造器对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_TextBlobBuilder](capi-drawing-oh-drawing-textblobbuilder.md)\* textBlobBuilder | 指向文本构造器对象的指针。 |
