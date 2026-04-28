---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-bitmap-h
title: drawing_bitmap.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_bitmap.h
category: harmonyos-references
scraped_at: 2026-04-28T08:14:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3983ba23aedbfb02aafe8324e882a8ce61af515281a7eb75cc88f3f4126c5cb1
---

## 概述

PhonePC/2in1TabletTVWearable

文件中定义了与位图相关的功能函数。

**相关示例：** [Drawing API示例(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkGraphics2D/Drawing/NDKAPIDrawing)

**引用文件：** <native\_drawing/drawing\_bitmap.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Drawing\_BitmapFormat](capi-drawing-oh-drawing-bitmapformat.md) | OH\_Drawing\_BitmapFormat | 结构体用于描述位图像素的格式，包括颜色类型和透明度类型。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreate(void)](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreate) | 用于创建一个位图对象。 |
| [void OH\_Drawing\_BitmapDestroy(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapdestroy) | 用于销毁位图对象并回收该对象占有内存。 |
| [OH\_Drawing\_Bitmap\* OH\_Drawing\_BitmapCreateFromPixels(OH\_Drawing\_Image\_Info\* imageInfo, void\* pixels, uint32\_t rowBytes)](capi-drawing-bitmap-h.md#oh_drawing_bitmapcreatefrompixels) | 用于创建一个位图对象，并将位图像素存储内存地址设置为开发者申请内存的地址。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  imageInfo、pixels任意一个为NULL或者rowBytes等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BitmapBuild(OH\_Drawing\_Bitmap\* bitmap,const uint32\_t width, const uint32\_t height, const OH\_Drawing\_BitmapFormat\* bitmapFormat)](capi-drawing-bitmap-h.md#oh_drawing_bitmapbuild) | 用于初始化位图对象的宽度和高度，并且为该位图设置像素格式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、bitmapFormat任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_BitmapGetWidth(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetwidth) | 用于获取指定位图的宽度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [uint32\_t OH\_Drawing\_BitmapGetHeight(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetheight) | 用于获取指定位图的高度。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_ColorFormat OH\_Drawing\_BitmapGetColorFormat(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetcolorformat) | 用于获取指定位图的像素存储格式。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [OH\_Drawing\_AlphaFormat OH\_Drawing\_BitmapGetAlphaFormat(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetalphaformat) | 用于获取指定位图的像素透明度分量。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void\* OH\_Drawing\_BitmapGetPixels(OH\_Drawing\_Bitmap\* bitmap)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetpixels) | 用于获取指定位图的像素地址，可以通过像素地址获取到位图的像素数据。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [void OH\_Drawing\_BitmapGetImageInfo(OH\_Drawing\_Bitmap\* bitmap, OH\_Drawing\_Image\_Info\* imageInfo)](capi-drawing-bitmap-h.md#oh_drawing_bitmapgetimageinfo) | 用于获取指定位图的信息。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、imageInfo任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |
| [bool OH\_Drawing\_BitmapReadPixels(OH\_Drawing\_Bitmap\* bitmap, const OH\_Drawing\_Image\_Info\* dstInfo,void\* dstPixels, size\_t dstRowBytes, int32\_t srcX, int32\_t srcY)](capi-drawing-bitmap-h.md#oh_drawing_bitmapreadpixels) | 将位图中的矩形区域像素数据读取到指定的内存缓冲区中。  本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。  bitmap、dstInfo、dstPixels任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Drawing\_BitmapCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Bitmap* OH_Drawing_BitmapCreate(void)
```

**描述**

用于创建一个位图对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* | 函数会返回一个指针，指针指向创建的位图对象。 |

### OH\_Drawing\_BitmapDestroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_BitmapDestroy(OH_Drawing_Bitmap* bitmap)
```

**描述**

用于销毁位图对象并回收该对象占有内存。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 8

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象的指针。 |

### OH\_Drawing\_BitmapCreateFromPixels()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_Bitmap* OH_Drawing_BitmapCreateFromPixels(OH_Drawing_Image_Info* imageInfo, void* pixels, uint32_t rowBytes)
```

**描述**

用于创建一个位图对象，并将位图像素存储内存地址设置为开发者申请内存的地址。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

imageInfo、pixels任意一个为NULL或者rowBytes等于0时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。 |
| void\* pixels | 指向像素存储的内存首地址，内存由开发者申请，保证有效性。 |
| uint32\_t rowBytes | 每行像素的大小，小于等于0时无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* | 函数返回一个指针，指针指向创建的位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)。 |

### OH\_Drawing\_BitmapBuild()

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_BitmapBuild(OH_Drawing_Bitmap* bitmap,const uint32_t width, const uint32_t height, const OH_Drawing_BitmapFormat* bitmapFormat)
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
| const uint32\_t width | 位图要初始化设置的宽度。 |
| const uint32\_t height | 位图要初始化设置的高度。 |
| const [OH\_Drawing\_BitmapFormat](capi-drawing-oh-drawing-bitmapformat.md)\* bitmapFormat | 位图要初始化设置的像素格式，包括像素的颜色类型和透明度类型。 |

### OH\_Drawing\_BitmapGetWidth()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_BitmapGetWidth(OH_Drawing_Bitmap* bitmap)
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
| uint32\_t | 函数返回位图的宽度。 |

### OH\_Drawing\_BitmapGetHeight()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Drawing_BitmapGetHeight(OH_Drawing_Bitmap* bitmap)
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
| uint32\_t | 函数返回位图的高度。 |

### OH\_Drawing\_BitmapGetColorFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_ColorFormat OH_Drawing_BitmapGetColorFormat(OH_Drawing_Bitmap* bitmap)
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

PhonePC/2in1TabletTVWearable

```
1. OH_Drawing_AlphaFormat OH_Drawing_BitmapGetAlphaFormat(OH_Drawing_Bitmap* bitmap)
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

PhonePC/2in1TabletTVWearable

```
1. void* OH_Drawing_BitmapGetPixels(OH_Drawing_Bitmap* bitmap)
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

PhonePC/2in1TabletTVWearable

```
1. void OH_Drawing_BitmapGetImageInfo(OH_Drawing_Bitmap* bitmap, OH_Drawing_Image_Info* imageInfo)
```

**描述**

用于获取指定位图的信息。

本接口会产生错误码，可以通过[OH\_Drawing\_ErrorCodeGet](capi-drawing-error-code-h.md#oh_drawing_errorcodeget)查看错误码的取值。

bitmap、imageInfo任意一个为NULL时返回OH\_DRAWING\_ERROR\_INVALID\_PARAMETER。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)的指针。 |
| [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* imageInfo | 指向图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。 |

### OH\_Drawing\_BitmapReadPixels()

PhonePC/2in1TabletTVWearable

```
1. bool OH_Drawing_BitmapReadPixels(OH_Drawing_Bitmap* bitmap, const OH_Drawing_Image_Info* dstInfo,void* dstPixels, size_t dstRowBytes, int32_t srcX, int32_t srcY)
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
| [OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)\* bitmap | 指向位图对象[OH\_Drawing\_Bitmap](capi-drawing-oh-drawing-bitmap.md)的指针。 |
| const [OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)\* dstInfo | 指向图片信息对象[OH\_Drawing\_Image\_Info](capi-drawing-oh-drawing-image-info.md)的指针。 |
| void\* dstPixels | 目标像素存储区域。 |
| size\_t dstRowBytes | 目标像素数据每行的字节数，应大于或等于图片信息对象中的最小每行字节数。 |
| int32\_t srcX | 源位图中读取像素数据的起始x轴坐标，应小于源位图的宽度。 |
| int32\_t srcY | 源位图中读取像素数据的起始y轴坐标，应小于源位图的高度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回接口调用成功与否的结果。true表示复制成功，false表示复制失败。 |
