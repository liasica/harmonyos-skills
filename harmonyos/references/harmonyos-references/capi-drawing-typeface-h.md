---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-typeface-h
title: drawing_typeface.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_typeface.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:44+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:77279ddcd5520c4dcd2d831e4c587cbc7d9d9be19e7957604312d6a174d76f87
---

## 概述

文件中定义了与字体相关的功能函数，支持创建默认字体、从文件或内存流创建指定字体、通过字型参数自定义字体的可变维度，以及查询字体的粗体、斜体属性等。

不同的平台有自己的默认字体，也可以从ttf文件解析出三方指定字体，如宋体、黑体字体等。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_typeface.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateDefault(void)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatedefault) | 用于创建一个默认的字体对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFile(const char\* path, int index)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfile) | 通过文件创建一个字体对象。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromFileWithArguments(const char\* path, const OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfilewitharguments) | 从指定文件路径创建带有字型参数的字体对象。  如果字体对象不支持字型参数中描述的可变维度，此函数将会创建默认字型参数的字体对象。  在这种情况下，此函数将提供与[OH\_Drawing\_TypefaceCreateFromFile](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromfile)相同的功能。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromCurrent(const OH\_Drawing\_Typeface\* current, const OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromcurrent) | 通过已存在的字体对象创建带有字型参数的字体对象。 |
| [OH\_Drawing\_Typeface\* OH\_Drawing\_TypefaceCreateFromStream(OH\_Drawing\_MemoryStream\* memoryStream, int32\_t index)](capi-drawing-typeface-h.md#oh_drawing_typefacecreatefromstream) | 通过内存流创建一个字体对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  memoryStream为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_TypefaceDestroy(OH\_Drawing\_Typeface\* typeface)](capi-drawing-typeface-h.md#oh_drawing_typefacedestroy) | 用于销毁字体对象并回收该对象占用的内存。 |
| [OH\_Drawing\_FontArguments\* OH\_Drawing\_FontArgumentsCreate(void)](capi-drawing-typeface-h.md#oh_drawing_fontargumentscreate) | 用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsAddVariation(OH\_Drawing\_FontArguments\* fontArguments,const char\* axis, float value)](capi-drawing-typeface-h.md#oh_drawing_fontargumentsaddvariation) | 给字型参数对象添加可变维度。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_FontArgumentsDestroy(OH\_Drawing\_FontArguments\* fontArguments)](capi-drawing-typeface-h.md#oh_drawing_fontargumentsdestroy) | 用于销毁一个字型参数对象。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_TypefaceIsBold(const OH\_Drawing\_Typeface\* typeface, bool\* isBold)](capi-drawing-typeface-h.md#oh_drawing_typefaceisbold) | 检查字体是否为粗体。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_TypefaceIsItalic(const OH\_Drawing\_Typeface\* typeface, bool\* isItalic)](capi-drawing-typeface-h.md#oh_drawing_typefaceisitalic) | 检查字体是否为斜体。 |

## 函数说明

### OH\_Drawing\_TypefaceCreateDefault()

```c
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateDefault(void)
```

**描述**

用于创建一个默认的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象。 |

### OH\_Drawing\_TypefaceCreateFromFile()

```c
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFile(const char* path, int index)
```

**描述**

通过文件创建一个字体对象。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

path为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* path | 指向字体文件路径的指针。支持绝对路径，文件格式支持ttf、otf、ttc等字体文件。 |
| int index | 文件索引，取值为非负整数，表示字体文件中的字体索引。对于单字体文件取值为0，对于字体集合文件取值范围为[0, 字体数量-1]。传入无效索引时创建字体对象失败，返回空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象OH\_Drawing\_Typeface。 |

### OH\_Drawing\_TypefaceCreateFromFileWithArguments()

```c
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromFileWithArguments(const char* path, const OH_Drawing_FontArguments* fontArguments)
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
| const [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象OH\_Drawing\_FontArguments的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象OH\_Drawing\_Typeface。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的文件路径对象指针或字型参数为空、传入的路径无效。 |

### OH\_Drawing\_TypefaceCreateFromCurrent()

```c
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromCurrent(const OH_Drawing_Typeface* current, const OH_Drawing_FontArguments* fontArguments)
```

**描述**

通过已存在的字体对象创建带有字型参数的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* current | 指向字体对象OH\_Drawing\_Typeface的指针。 |
| const [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象OH\_Drawing\_FontArguments的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象OH\_Drawing\_Typeface。  如果返回的对象指针为空，则表示字体对象创建失败。失败的原因可能为：没有可用的内存、传入的字体对象指针或字型参数为空、传入的字体对象不支持字型参数对象中描述的可变维度。 |

### OH\_Drawing\_TypefaceCreateFromStream()

```c
OH_Drawing_Typeface* OH_Drawing_TypefaceCreateFromStream(OH_Drawing_MemoryStream* memoryStream, int32_t index)
```

**描述**

通过内存流创建一个字体对象。如果内存流是无效的字体文件，返回空指针。内存流传入后，所有权转移，开发者不能再释放它。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

memoryStream为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_MemoryStream](capi-drawing-oh-drawing-memorystream.md)\* memoryStream | 指向内存流对象OH\_Drawing\_MemoryStream的指针。 |
| int32\_t index | 内存流索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* | 函数返回一个指针，指针指向创建的字体对象。 |

### OH\_Drawing\_TypefaceDestroy()

```c
void OH_Drawing_TypefaceDestroy(OH_Drawing_Typeface* typeface)
```

**描述**

用于销毁字体对象并回收该对象占用的内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字体对象的指针。 |

### OH\_Drawing\_FontArgumentsCreate()

```c
OH_Drawing_FontArguments* OH_Drawing_FontArgumentsCreate(void)
```

**描述**

用于创建一个字型参数对象。字型参数用于创建带有自定义属性的字体对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* | 函数返回一个指针，指针指向创建的字型参数对象。 |

### OH\_Drawing\_FontArgumentsAddVariation()

```c
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsAddVariation(OH_Drawing_FontArguments* fontArguments, const char* axis, float value)
```

**描述**

给字型参数对象添加可变维度。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象OH\_Drawing\_FontArguments的指针。 |
| const char\* axis | 字型参数对象可变维度的标签，必须为4个ASCII字符。具体可支持的标签取决于加载的字体文件，如'wght'即为字重标签。 |
| float value | 可变维度标签对应的取值，取值范围取决于轴标签和加载的字体文件中该可变维度标签定义的最小值与最大值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontArguments或axis任意一个为NULL或者axis的长度不为4。 |

### OH\_Drawing\_FontArgumentsDestroy()

```c
OH_Drawing_ErrorCode OH_Drawing_FontArgumentsDestroy(OH_Drawing_FontArguments* fontArguments)
```

**描述**

用于销毁一个字型参数对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_FontArguments](capi-drawing-oh-drawing-fontarguments.md)\* fontArguments | 指向字型参数对象OH\_Drawing\_FontArguments的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER，表示参数fontArguments为NULL。 |

### OH\_Drawing\_TypefaceIsBold()

```c
OH_Drawing_ErrorCode OH_Drawing_TypefaceIsBold(const OH_Drawing_Typeface* typeface, bool* isBold)
```

**描述**

检查字体是否为粗体。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字体对象OH\_Drawing\_Typeface的指针。 |
| bool\* isBold | 表示字体是否为粗体。作为出参使用。true表示该字体是粗体，false表示该字体不是粗体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示typeface或isBold是空指针。 |

### OH\_Drawing\_TypefaceIsItalic()

```c
OH_Drawing_ErrorCode OH_Drawing_TypefaceIsItalic(const OH_Drawing_Typeface* typeface, bool* isItalic)
```

**描述**

检查字体是否为斜体。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_Drawing\_Typeface](capi-drawing-oh-drawing-typeface.md)\* typeface | 指向字体对象OH\_Drawing\_Typeface的指针。 |
| bool\* isItalic | 表示字体是否为斜体。作为出参使用。true表示该字体是斜体，false表示该字体不是斜体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行结果。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示typeface或isItalic是空指针。 |
