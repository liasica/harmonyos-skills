---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-initializationoptions
title: OH_Pixelmap_InitializationOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_InitializationOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:96b2c3c030b9c81087d4c507fed6205857cb708dc4e1f1614c34dd630d3c77c1
---

```c
struct OH_Pixelmap_InitializationOptions
```

## 概述

OH\_Pixelmap\_InitializationOptions是Native层封装的初始化选项结构体，用于在创建Pixelmap时指定其属性，可配置图片宽高、像素格式、透明度类型等参数，适用于需要在Native层创建Pixelmap并自定义其初始化属性的场景。

使用[OH\_PixelmapInitializationOptions\_Create](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_create)函数创建OH\_Pixelmap\_InitializationOptions对象；使用完成后需调用[OH\_PixelmapInitializationOptions\_Release](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_release)函数释放资源，两者需配对使用，否则会导致内存泄漏。

OH\_Pixelmap\_InitializationOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽，单位：像素（px）。取值需大于0，最大值受系统内存限制。 | [OH\_PixelmapInitializationOptions\_GetWidth](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getwidth) | 获取图片宽。 |
| uint32\_t | width | 图片宽，单位：像素（px）。取值需大于0，最大值受系统内存限制。 | [OH\_PixelmapInitializationOptions\_SetWidth](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setwidth) | 设置图片宽。 |
| uint32\_t | height | 图片高，单位：像素（px）。取值需大于0，最大值受系统内存限制。 | [OH\_PixelmapInitializationOptions\_GetHeight](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getheight) | 获取图片高。 |
| uint32\_t | height | 图片高，单位：像素（px）。取值需大于0，最大值受系统内存限制。 | [OH\_PixelmapInitializationOptions\_SetHeight](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setheight) | 设置图片高。 |
| int32\_t | pixelFormat | 像素格式，取值参考[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。根据图片是否需要透明度通道及对内存占用的要求选择合适的像素格式，具体各枚举值的适用场景请参考PIXEL\_FORMAT枚举说明。 | [OH\_PixelmapInitializationOptions\_GetPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getpixelformat) | 获取像素格式。 |
| int32\_t | pixelFormat | 像素格式，取值参考[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。根据图片是否需要透明度通道及对内存占用的要求选择合适的像素格式，具体各枚举值的适用场景请参考PIXEL\_FORMAT枚举说明。 | [OH\_PixelmapInitializationOptions\_SetPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setpixelformat) | 设置像素格式。 |
| int32\_t | alphaType | 透明度类型，取值参考[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。根据图片是否需要预乘透明度处理选择合适的类型，具体各枚举值的适用场景请参考PIXELMAP\_ALPHA\_TYPE枚举说明。 | [OH\_PixelmapInitializationOptions\_GetAlphaType](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_getalphatype) | 获取透明度类型。 |
| int32\_t | alphaType | 透明度类型，取值参考[PIXELMAP\_ALPHA\_TYPE](capi-pixelmap-native-h.md#pixelmap_alpha_type)。根据图片是否需要预乘透明度处理选择合适的类型，具体各枚举值的适用场景请参考PIXELMAP\_ALPHA\_TYPE枚举说明。 | [OH\_PixelmapInitializationOptions\_SetAlphaType](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setalphatype) | 设置透明度类型。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)
