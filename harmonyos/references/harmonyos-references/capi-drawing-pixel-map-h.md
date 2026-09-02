---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-pixel-map-h
title: drawing_pixel_map.h
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > C API > 头文件 > drawing_pixel_map.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4daca73a80e279702a97c0118e875351c868388891637dcf05d164e7523572d3
---

## 概述

声明与绘图模块中的像素图对象相关的函数。支持从图像框架定义的像素图对象中获取本模块定义的像素图对象，支持解除两者之间的关系。

本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**引用文件：** <native\_drawing/drawing\_pixel\_map.h>

**库：** libnative\_drawing.so

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**相关模块：** [Drawing](capi-drawing.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [NativePixelMap\_](capi-drawing-nativepixelmap-.md) | NativePixelMap\_ | 声明由图像框架定义的像素图对象。 |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md) | OH\_PixelmapNative | 声明由图像框架定义的像素图对象。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromNativePixelMap(NativePixelMap\_\* nativePixelMap)](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromnativepixelmap) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。对象使用完毕后，调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除关系，否则会引发内存泄漏问题。 |
| [OH\_Drawing\_PixelMap\* OH\_Drawing\_PixelMapGetFromOhPixelMapNative(OH\_PixelmapNative\* pixelmapNative)](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromohpixelmapnative) | 从图像框架定义的像素图对象中获取本模块定义的像素图对象。对象使用完毕后，调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除关系，否则会引发内存泄漏问题。 |
| [void OH\_Drawing\_PixelMapDissolve(OH\_Drawing\_PixelMap\* pixelMap)](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve) | 解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系。必须先调用[OH\_Drawing\_PixelMapGetFromNativePixelMap](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromnativepixelmap)或[OH\_Drawing\_PixelMapGetFromOhPixelMapNative](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromohpixelmapnative)获取像素图对象并建立关联关系后，才能调用本方法解除该关系。 |

## 函数说明

### OH\_Drawing\_PixelMapGetFromNativePixelMap()

```c
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromNativePixelMap(NativePixelMap_* nativePixelMap)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。对象使用完毕后，调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除关系，否则会引发内存泄漏问题。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NativePixelMap\_](capi-drawing-nativepixelmap-.md)\* nativePixelMap | 指向图像框架定义的像素图对象[NativePixelMap\_](capi-drawing-nativepixelmap-.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* | 返回一个指向本模块定义的像素图对象[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。如果返回NULL，表示获取失败；原因是参数nativePixelMap为NULL。 |

### OH\_Drawing\_PixelMapGetFromOhPixelMapNative()

```c
OH_Drawing_PixelMap* OH_Drawing_PixelMapGetFromOhPixelMapNative(OH_PixelmapNative* pixelmapNative)
```

**描述**

从图像框架定义的像素图对象中获取本模块定义的像素图对象。对象使用完毕后，调用[OH\_Drawing\_PixelMapDissolve](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapdissolve)解除关系，否则会引发内存泄漏问题。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)\* pixelmapNative | 指向图像框架定义的像素图对象[OH\_PixelmapNative](capi-drawing-oh-pixelmapnative.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* | 返回一个指向本模块定义的像素图对象[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。如果返回NULL，表示获取失败；原因是参数pixelmapNative为NULL。 |

### OH\_Drawing\_PixelMapDissolve()

```c
void OH_Drawing_PixelMapDissolve(OH_Drawing_PixelMap* pixelMap)
```

**描述**

解除本模块定义的像素图对象和图像框架定义的像素图对象之间的关系。必须先调用[OH\_Drawing\_PixelMapGetFromNativePixelMap](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromnativepixelmap)或[OH\_Drawing\_PixelMapGetFromOhPixelMapNative](capi-drawing-pixel-map-h.md#oh_drawing_pixelmapgetfromohpixelmapnative)获取像素图对象并建立关联关系后，才能调用本方法解除该关系。

**系统能力：** SystemCapability.Graphic.Graphic2D.NativeDrawing

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)\* pixelMap | 指向像素图对象[OH\_Drawing\_PixelMap](capi-drawing-oh-drawing-pixelmap.md)的指针。 |
