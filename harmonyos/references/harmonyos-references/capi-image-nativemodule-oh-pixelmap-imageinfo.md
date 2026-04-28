---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-imageinfo
title: OH_Pixelmap_ImageInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_ImageInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9308f8bca6a75a45cbfc6cfda5a296d7cd8be01f3b4353d5d845ab0c4d6315b0
---

```
1. struct OH_Pixelmap_ImageInfo
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_Pixelmap\_ImageInfo是native层封装的图像像素信息结构体，保存图像像素的宽高、行跨距、像素格式、是否是HDR。

创建OH\_Pixelmap\_ImageInfo对象使用[OH\_PixelmapImageInfo\_Create](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_create)函数。

释放OH\_Pixelmap\_ImageInfo对象使用[OH\_PixelmapImageInfo\_Release](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_release)函数。

OH\_Pixelmap\_ImageInfo结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽 | [OH\_PixelmapImageInfo\_GetWidth](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getwidth) | 获取图片宽。 |
| uint32\_t | height | 图片高 | [OH\_PixelmapImageInfo\_GetHeight](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getheight) | 获取图片高。 |
| uint32\_t | rowStride | 行跨距 | [OH\_PixelmapImageInfo\_GetRowStride](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getrowstride) | 获取行跨距。 |
| int32\_t | pixelFormat | 像素格式 | [OH\_PixelmapImageInfo\_GetPixelFormat](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getpixelformat) | 获取像素格式。 |
| int32\_t | alphaType | 透明度类型 | [OH\_PixelmapImageInfo\_GetAlphaType](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getalphatype) | 获取透明度类型。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息 | [OH\_PixelmapImageInfo\_GetDynamicRange](capi-pixelmap-native-h.md#oh_pixelmapimageinfo_getdynamicrange) | 获取Pixelmap是否为高动态范围的信息。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)
