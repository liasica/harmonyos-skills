---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-typeface-h
title: drawing_typeface.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_typeface.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7d30b9b83b2b4f764e2467d876a6d2253986e13f15b78483820c1d265261dc0
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与字形相关的功能函数。

不同的平台有自己的默认字形，也可以从ttf文件解析出三方指定字形，如宋体、黑体字形等。

**引用文件：** <native\_drawing/drawing\_typeface.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateDefault(void)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatedefault) | 用于创建一个默认的字形对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFile(const char\* path, int index)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfile) | 通过文件创建一个字形对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFileWithArguments(const char\* path,const OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfilewitharguments) | 从指定文件路径创建带有字型参数的字体对象。  如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。  在这种情况下，此函数将提供与[OH\_Drawing\_TypefaceCreateFromFile](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfile)相同的功能。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromCurrent(const OH\_Drawing\_Typeface\* current,const OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromcurrent) | 通过已存在的字体对象创建带有字型参数的字体对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromStream(OH\_Drawing\_MemoryStream\* memoryStream, int32\_t index)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromstream) | 通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  memoryStream为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_TypefaceDestroy(OH\_Drawing\_Typeface\* typeface)](capi-drawing-typeface-h.md#oh_drawing_typefacedestroy) | 用于销毁字形对象并回收该对象占有的内存。 |
| [OH\_Drawing\_FontArguments\* OH\_Drawing\_FontArgumentsCreate(void)](capi-drawing-typeface-h.md#oh_drawing_fontargumentscreate) | 用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsAddVariation(OH\_Drawing\_FontArguments\* fontArguments,const char\* axis, float value)](capi-drawing-typeface-h.md#oh_drawing_fontargumentsaddvariation) | 给字型参数对象添加可变维度。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsDestroy(OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_fontargumentsdestroy) | 用于销毁一个字型参数对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_TypefaceIsBold(const OH\_Drawing\_Typeface\* typeface, bool\* isBold)](capi-drawing-typeface-h.md#oh_drawing_typefaceisbold) | 检查字形是否为粗体。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_TypefaceIsItalic(const OH\_Drawing\_Typeface\* typeface, bool\* isItalic)](capi-drawing-typeface-h.md#oh_drawing_typefaceisitalic) | 检查字形是否为斜体。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_TypefaceCreateDefault()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void)
```

**描述**

用于创建一个默认的字形对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 返回一个指针，指针指向创建的字形对象。 |

### OH\_Drawing\_TypefaceCreateFromFile()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index)
```

**描述**

通过文件创建一个字形对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* path | 指向文件路径的指针。 |
| int index | 文件索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字形对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。 |

### OH\_Drawing\_TypefaceCreateFromFileWithArguments()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path,const OH_Drawing_FontArguments* fontArguments)
```

**描述**

从指定文件路径创建带有字型参数的字体对象。

如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。

在这种情况下，此函数将提供与[OH\_Drawing\_TypefaceCreateFromFile](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfile)相同的功能。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* path | 指向字体对象所在文件路径的指针。 |
| const [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象[OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的路径无效。 |

### OH\_Drawing\_TypefaceCreateFromCurrent()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current,const OH_Drawing_FontArguments* fontArguments)
```

**描述**

通过已存在的字体对象创建带有字型参数的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* current | 指向字体对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)的指针。 |
| const [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象[OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的字体对象不支持字型参数对象中描述的可变维度。 |

### OH\_Drawing\_TypefaceCreateFromStream()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index)
```

**描述**

通过内存流创建一个字形对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

memoryStream为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)\* memoryStream | 指向内存流对象[OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)的指针。 |
| int32\_t index | 内存流索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 返回一个指针，指针指向创建的字形对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)。 |

### OH\_Drawing\_TypefaceDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface)
```

**描述**

用于销毁字形对象并回收该对象占有的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字形对象的指针。 |

### OH\_Drawing\_FontArgumentsCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void)
```

**描述**

用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* | 返回一个指针，指针指向创建的字型参数对象。 |

### OH\_Drawing\_FontArgumentsAddVariation()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments,const char* axis, float value)
```

**描述**

给字型参数对象添加可变维度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象[OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)的指针。 |
| const char\* axis | 字型参数对象可变维度的标签，必须为4个ASCII字符。具体可支持的标签取决于加载的字体文件，如'wght'即为字重标签。 |
| float value | 可变维度标签对应的取值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontArguments或axis任意一个为NULL或者axis的长度不为4。 |

### OH\_Drawing\_FontArgumentsDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments)
```

**描述**

用于销毁一个字型参数对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象[OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontArguments为NULL。 |

### OH\_Drawing\_TypefaceIsBold()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_TypefaceIsBold(const OH_Drawing_Typeface* typeface, bool* isBold)
```

**描述**

检查字形是否为粗体。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字形对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)的指针。 |
| bool\* isBold | 表示字形是否为粗体。作为出参使用。true表示该字形是粗体，false表示该字形不是粗体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  OH\_DRAWING\_SUCCESS，表示执行成功。  OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示typeface或isBold是空指针。 |

### OH\_Drawing\_TypefaceIsItalic()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ErrorCode OH_Drawing_TypefaceIsItalic(const OH_Drawing_Typeface* typeface, bool* isItalic)
```

**描述**

检查字形是否为斜体。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字形对象[OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)的指针。 |
| bool\* isItalic | 表示字形是否为斜体。作为出参使用。true表示该字形是斜体，false表示该字形不是斜体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示typeface或isItalic是空指针。 |
