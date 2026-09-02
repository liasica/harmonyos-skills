---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative
title: OH_PictureNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PictureNative
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c63c908623659dc592bd937f187236293c0916ba04a94b4284a52707e02d67e2
---

```c
struct OH_PictureNative
```

## 概述

Picture结构体类型，用于执行picture相关操作。

Picture为多图对象结构体，包含主图、辅助图和元数据。

主图包含图像的大部分信息，主要用于显示图像内容。

辅助图用于存储与主图相关但不同的数据，展示图像更丰富的信息。

元数据一般用来存储关于图像文件的信息。

有多种方式创建OH\_PictureNative，具体如下：

| 函数 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative\_CreatePicture](capi-image-source-native-h.md#oh_imagesourcenative_createpicture) | 通过图片解码创建OH\_PictureNative对象。 |
| [OH\_ImageSourceNative\_CreatePictureAtIndex](capi-image-source-native-h.md#oh_imagesourcenative_createpictureatindex) | 通过指定序号的图片解码创建OH\_PictureNative对象。 |
| [OH\_PictureNative\_CreatePicture](capi-picture-native-h.md#oh_picturenative_createpicture) | 通过主图OH\_PixelmapNative对象创建OH\_PictureNative对象。 |

使用[OH\_PictureNative\_Release](capi-picture-native-h.md#oh_picturenative_release)函数释放OH\_PictureNative对象。

使用约束：使用OH\_PictureNative对象前，需先创建对象；使用完成后，应调用[OH\_PictureNative\_Release](capi-picture-native-h.md#oh_picturenative_release)释放对象。通过[OH\_ImageSourceNative\_CreatePicture](capi-image-source-native-h.md#oh_imagesourcenative_createpicture)或[OH\_ImageSourceNative\_CreatePictureAtIndex](capi-image-source-native-h.md#oh_imagesourcenative_createpictureatindex)解码Picture时，图片源格式需支持Picture解码。通过[OH\_PictureNative\_CreatePicture](capi-picture-native-h.md#oh_picturenative_createpicture)创建Picture时，mainPixelmap和picture均不能为空指针。

资源管理：释放OH\_ImageSourceNative对象不会自动释放已创建的OH\_PictureNative对象。通过OH\_PictureNative获取到的OH\_PixelmapNative、OH\_AuxiliaryPictureNative和OH\_PictureMetadata对象由调用方管理，使用完成后需分别调用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)、[OH\_AuxiliaryPictureNative\_Release](capi-picture-native-h.md#oh_auxiliarypicturenative_release)和[OH\_PictureMetadata\_Release](capi-image-common-h.md#oh_picturemetadata_release)释放。获取PixelMap、辅助图或元数据的接口返回失败时，输出参数的内容不能在后续流程中继续使用。

OH\_PictureNative结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| OH\_PixelmapNative | mainPixelmap | Picture主图。 | [OH\_PictureNative\_GetMainPixelmap](capi-picture-native-h.md#oh_picturenative_getmainpixelmap) | 获取主图的OH\_PixelmapNative对象。 |
| OH\_PixelmapNative | hdrPixelmap | HDR合成图。 | [OH\_PictureNative\_GetHdrComposedPixelmap](capi-picture-native-h.md#oh_picturenative_gethdrcomposedpixelmap) | 获取HDR合成后的OH\_PixelmapNative对象。 |
| OH\_PixelmapNative | hdrPixelmap | HDR合成图。 | [OH\_PictureNative\_GetHdrComposedPixelmapWithOptions](capi-picture-native-h.md#oh_picturenative_gethdrcomposedpixelmapwithoptions) | 按OH\_ComposeOptions配置获取HDR合成后的OH\_PixelmapNative对象。 |
| OH\_PixelmapNative | gainmapPixelmap | 增益图。 | [OH\_PictureNative\_GetGainmapPixelmap](capi-picture-native-h.md#oh_picturenative_getgainmappixelmap) | 获取增益图的OH\_PixelmapNative对象。 |
| OH\_AuxiliaryPictureNative | auxiliaryPicture | 辅助图。 | [OH\_PictureNative\_SetAuxiliaryPicture](capi-picture-native-h.md#oh_picturenative_setauxiliarypicture) | 设置辅助图。 |
| OH\_AuxiliaryPictureNative | auxiliaryPicture | 辅助图。 | [OH\_PictureNative\_GetAuxiliaryPicture](capi-picture-native-h.md#oh_picturenative_getauxiliarypicture) | 根据类型获取辅助图。 |
| OH\_PictureMetadata | metadata | 主图元数据。 | [OH\_PictureNative\_GetMetadata](capi-picture-native-h.md#oh_picturenative_getmetadata) | 获取主图的元数据。 |
| OH\_PictureMetadata | metadata | 主图元数据。 | [OH\_PictureNative\_SetMetadata](capi-picture-native-h.md#oh_picturenative_setmetadata) | 设置主图的元数据。 |

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](capi-picture-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成多图对象解码](../harmonyos-guides/image-source-picture-c.md)
