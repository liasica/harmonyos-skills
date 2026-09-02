---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-imageinfo
title: OH_Pixelmap_ImageInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_ImageInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:73567adf5a3f4b17afed2b9f0e725f4112b3a4ac11abcc357aaee7be7886f286
---

```c
struct OH_Pixelmap_ImageInfo
```

## 概述

OH\_Pixelmap\_ImageInfo是Native层封装的图像像素信息结构体，保存图像像素的宽高、行跨距、像素格式、透明度类型、是否为HDR等信息，适用于在Native层查询Pixelmap属性的场景。

创建OH\_Pixelmap\_ImageInfo对象使用[OH\_PixelmapImageInfo\_Create](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_create)函数，使用完成后需调用[OH\_PixelmapImageInfo\_Release](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_release)函数释放资源，两者需配对使用，否则会导致内存泄漏。

OH\_Pixelmap\_ImageInfo结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽，单位：像素（px）。 | [OH\_PixelmapImageInfo\_GetWidth](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getwidth) | 获取图片宽。 |
| uint32\_t | height | 图片高，单位：像素（px）。 | [OH\_PixelmapImageInfo\_GetHeight](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getheight) | 获取图片高。 |
| uint32\_t | rowStride | 行跨距，表示内存中每行像素所占的空间。单位：字节（Byte）。受内存对齐影响，该值可能大于图片宽度对应的实际像素数据字节数。 | [OH\_PixelmapImageInfo\_GetRowStride](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getrowstride) | 获取行跨距。 |
| int32\_t | pixelFormat | 像素格式，表示像素数据的颜色通道排列和位深信息，取值参考[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 | [OH\_PixelmapImageInfo\_GetPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getpixelformat) | 获取像素格式。 |
| int32\_t | alphaType | 透明度类型，取值参考[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。 | [OH\_PixelmapImageInfo\_GetAlphaType](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphatype) | 获取透明度类型。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息。true表示是HDR，false表示非HDR。 | [OH\_PixelmapImageInfo\_GetDynamicRange](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getdynamicrange) | 获取Pixelmap是否为高动态范围的信息。返回true表示是HDR，返回false表示非HDR。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)
