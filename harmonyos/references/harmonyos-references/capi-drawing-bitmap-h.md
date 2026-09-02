---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-bitmap-h
title: drawing_bitmap.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_bitmap.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:602050de9308a560354a32eea6bd6ae0425b0813ee7739be68b1d1c99febde3c
---

## 概述

文件中定义了位图相关的功能函数，支持位图的创建与销毁、初始化宽高与像素格式、获取位图宽度、高度、行字节数、像素存储格式、透明度分量、像素地址及位图信息，以及将位图像素数据读取到指定内存缓冲区等操作。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_bitmap.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_BitmapFormat](capi-drawing-oh-drawing-bitmapformat.md) | OH\_Drawing\_BitmapFormat | 结构体用于描述位图像素的格式，包括颜色类型和透明度类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreate(void)](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreate) | 用于创建一个位图对象。调用此方法创建的位图对象，在使用完毕后必须调用[OH\_Drawing\_BitmapDestroy](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy)进行销毁并释放内存，否则会导致内存泄漏。 |
| [void OH\_Drawing\_BitmapDestroy(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy) | 用于销毁位图对象并回收该对象占用的内存。应与[OH\_Drawing\_BitmapCreate](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreate)或[OH\_Drawing\_BitmapCreateFromPixels](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreatefrompixels)配对使用，对已创建的位图对象进行释放，避免内存泄漏。 |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreateFromPixels(OH\_Drawing\_Image\_Info\* imageInfo, void\* pixels, uint32\_t rowBytes)](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreatefrompixels) | 用于创建一个位图对象，并将位图存储像素的内存地址设置为开发者申请的内存地址。调用此方法创建的位图对象，在使用完毕后必须调用[OH\_Drawing\_BitmapDestroy](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy)进行销毁并释放内存，否则会导致内存泄漏。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  imageInfo、pixels任意一个为NULL或者rowBytes等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BitmapBuild(OH\_Drawing\_Bitmap\* bitmap, const uint32\_t width, const uint32\_t height, const OH\_Drawing\_BitmapFormat\* bitmapFormat)](capi-drawing-bitmap-h.md#oh_drawing_bitmapbuild) | 用于初始化位图对象的宽度和高度，并且为该位图设置像素格式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、bitmapFormat任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_BitmapGetWidth(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetwidth) | 用于获取指定位图的宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_BitmapGetHeight(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetheight) | 用于获取指定位图的高度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ErrorCode OH\_Drawing\_BitmapGetRowBytes(OH\_Drawing\_Bitmap\* bitmap, uint32\_t\* bytes)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetrowbytes) | 用于获取指定位图每行的字节数。 |
| [OH\_Drawing\_ColorFormat OH\_Drawing\_BitmapGetColorFormat(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetcolorformat) | 用于获取指定位图的像素存储格式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_AlphaFormat OH\_Drawing\_BitmapGetAlphaFormat(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetalphaformat) | 用于获取指定位图的像素透明度分量。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void\* OH\_Drawing\_BitmapGetPixels(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetpixels) | 用于获取指定位图的像素地址，可以通过像素地址获取到位图的像素数据。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BitmapGetImageInfo(OH\_Drawing\_Bitmap\* bitmap, OH\_Drawing\_Image\_Info\* imageInfo)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetimageinfo) | 用于获取指定位图的图片信息，包括宽度、高度、颜色类型和透明度类型等。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、imageInfo任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_BitmapReadPixels(OH\_Drawing\_Bitmap\* bitmap, const OH\_Drawing\_Image\_Info\* dstInfo, void\* dstPixels, size\_t dstRowBytes, int32\_t srcX, int32\_t srcY)](capi-drawing-bitmap-h.md#oh_drawing_bitmapreadpixels) | 将位图中的矩形区域像素数据读取到指定的内存缓冲区中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、dstInfo、dstPixels任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |

## 函数说明

### OH\_Drawing\_BitmapCreate()

```c
OH_Drawing_Bitmap* OH_Drawing_BitmapCreate(void)
```

**描述**

用于创建一个位图对象。调用此方法创建的位图对象，在使用完毕后必须调用[OH\_Drawing\_BitmapDestroy](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy)进行销毁并释放内存，否则会导致内存泄漏。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* | 函数返回指向创建的位图对象的指针。 |

### OH\_Drawing\_BitmapDestroy()

```c
void OH_Drawing_BitmapDestroy(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于销毁位图对象并回收该对象占用的内存。应与[OH\_Drawing\_BitmapCreate](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreate)或[OH\_Drawing\_BitmapCreateFromPixels](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreatefrompixels)配对使用，对已创建的位图对象进行释放，避免内存泄漏。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

### OH\_Drawing\_BitmapCreateFromPixels()

```c
OH_Drawing_Bitmap* OH_Drawing_BitmapCreateFromPixels(OH_Drawing_Image_Info* imageInfo, void* pixels, uint32_t rowBytes)
```

**描述**

用于创建一个位图对象，并将位图存储像素的内存地址设置为开发者申请的内存地址。调用此方法创建的位图对象，在使用完毕后必须调用[OH\_Drawing\_BitmapDestroy](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy)进行销毁并释放内存，否则会导致内存泄漏。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

imageInfo、pixels任意一个为NULL或者rowBytes等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针，用于指定创建位图的尺寸和像素格式信息。 |
| void\* pixels | 指向像素存储的内存首地址，内存由开发者申请，需保证内存在位图使用期间有效且大小充足。所需最小内存大小为rowBytes × imageInfo中height的值。 |
| uint32\_t rowBytes | 每行像素数据的字节数，等于0时无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* | 函数返回一个指针，指针指向创建的位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)。 |

### OH\_Drawing\_BitmapBuild()

```c
void OH_Drawing_BitmapBuild(OH_Drawing_Bitmap* bitmap, const uint32_t width, const uint32_t height, const OH_Drawing_BitmapFormat* bitmapFormat)
```

**描述**

用于初始化位图对象的宽度和高度，并且为该位图设置像素格式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap、bitmapFormat任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |
| const uint32\_t width | 位图要初始化设置的宽度，单位为物理像素px，取值需大于0。 |
| const uint32\_t height | 位图要初始化设置的高度，单位为物理像素px，取值需大于0。 |
| const [OH\_Drawing\_BitmapFormat](capi-drawing-oh-drawing-bitmapformat.md)\* bitmapFormat | 位图要初始化设置的像素格式，包括像素的颜色类型和透明度类型。 |

### OH\_Drawing\_BitmapGetWidth()

```c
uint32_t OH_Drawing_BitmapGetWidth(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于获取指定位图的宽度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数返回位图的宽度，单位为物理像素px。 |

### OH\_Drawing\_BitmapGetHeight()

```c
uint32_t OH_Drawing_BitmapGetHeight(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于获取指定位图的高度。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 函数返回位图的高度，单位为物理像素px。 |

### OH\_Drawing\_BitmapGetRowBytes()

```c
OH_Drawing_ErrorCode OH_Drawing_BitmapGetRowBytes(OH_Drawing_Bitmap* bitmap, uint32_t* bytes)
```

**描述**

用于获取指定位图每行的字节数。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |
| uint32\_t\* bytes | 指向uint32\_t变量的指针，作为出参使用，用于接收位图的行字节数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ErrorCode](capi-drawing-error-code-h.md#oh_drawing_errorcode) | 函数返回执行错误码。  返回OH\_DRAWING\_SUCCESS，表示执行成功。  返回OH\_DRAWING\_ERROR\_INCORRECT\_PARAMETER，表示参数bitmap或bytes为NULL。 |

### OH\_Drawing\_BitmapGetColorFormat()

```c
OH_Drawing_ColorFormat OH_Drawing_BitmapGetColorFormat(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于获取指定位图的像素存储格式。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_ColorFormat](capi-drawing-types-h.md#oh_drawing_colorformat) | 函数返回位图的像素存储格式，支持格式参考[OH\_Drawing\_ColorFormat](capi-drawing-types-h.md#oh_drawing_colorformat)。 |

### OH\_Drawing\_BitmapGetAlphaFormat()

```c
OH_Drawing_AlphaFormat OH_Drawing_BitmapGetAlphaFormat(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于获取指定位图的像素透明度分量。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_AlphaFormat](capi-drawing-types-h.md#oh_drawing_alphaformat) | 函数返回位图的像素透明度分量，支持格式参考[OH\_Drawing\_AlphaFormat](capi-drawing-types-h.md#oh_drawing_alphaformat)。 |

### OH\_Drawing\_BitmapGetPixels()

```c
void* OH_Drawing_BitmapGetPixels(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于获取指定位图的像素地址，可以通过像素地址获取到位图的像素数据。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| void\* | 函数返回位图的像素地址。 |

### OH\_Drawing\_BitmapGetImageInfo()

```c
void OH_Drawing_BitmapGetImageInfo(OH_Drawing_Bitmap* bitmap, OH_Drawing_Image_Info* imageInfo)
```

**描述**

用于获取指定位图的图片信息，包括宽度、高度、颜色类型和透明度类型等。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap、imageInfo任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)的指针。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。作为出参使用，用于接收获取到的图片信息。 |

### OH\_Drawing\_BitmapReadPixels()

```c
bool OH_Drawing_BitmapReadPixels(OH_Drawing_Bitmap* bitmap, const OH_Drawing_Image_Info* dstInfo, void* dstPixels, size_t dstRowBytes, int32_t srcX, int32_t srcY)
```

**描述**

将位图中的矩形区域像素数据读取到指定的内存缓冲区中。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap、dstInfo、dstPixels任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |
| const [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* dstInfo | 指向目标图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针，用于指定目标像素的格式信息及读取区域的宽高。 |
| void\* dstPixels | 指向目标像素存储区域的内存首地址，内存由开发者申请，需保证缓冲区大小足够且有效。所需最小缓冲区大小为dstRowBytes × dstInfo中height的值。 |
| size\_t dstRowBytes | 目标像素数据每行的字节数，应大于或等于图片信息对象中的最小每行字节数（由目标区域的宽度和颜色类型决定）。 |
| int32\_t srcX | 源位图中读取像素数据的起始x轴坐标，单位为物理像素px，取值范围<源位图宽度。 |
| int32\_t srcY | 源位图中读取像素数据的起始y轴坐标，单位为物理像素px，取值范围为<源位图高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 函数返回接口调用成功与否的结果。true表示读取成功，false表示读取失败。 |
