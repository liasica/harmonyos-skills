---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-auxiliarypicturenative
title: OH_AuxiliaryPictureNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_AuxiliaryPictureNative
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:925b3bbc62936cba1ff2b44af5ee6d56c00ad2f8d49a158bba2542d1c27d4831
---

```c
typedef struct OH_AuxiliaryPictureNative OH_AuxiliaryPictureNative
```

## 概述

AuxiliaryPicture结构体类型，用于执行AuxiliaryPicture相关操作。

使用[OH\_AuxiliaryPictureNative\_Create](capi-picture-native-h.md#oh_auxiliarypicturenative_create)函数创建OH\_AuxiliaryPictureNative对象。

使用[OH\_PictureNative\_GetAuxiliaryPicture](capi-picture-native-h.md#oh_picturenative_getauxiliarypicture)函数从OH\_PictureNative对象中按辅助图类型获取OH\_AuxiliaryPictureNative对象。

使用[OH\_AuxiliaryPictureNative\_Release](capi-picture-native-h.md#oh_auxiliarypicturenative_release)函数释放OH\_AuxiliaryPictureNative对象。

使用约束：使用OH\_AuxiliaryPictureNative对象前，需先创建或获取对象；使用完成后，应调用[OH\_AuxiliaryPictureNative\_Release](capi-picture-native-h.md#oh_auxiliarypicturenative_release)释放对象。通过[OH\_AuxiliaryPictureNative\_Create](capi-picture-native-h.md#oh_auxiliarypicturenative_create)创建对象时，data、size和auxiliaryPicture均不能为空指针，dataLength必须大于0，type必须为当前支持的[Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype)。

资源管理：释放OH\_PictureNative对象不会自动释放已经获取出的OH\_AuxiliaryPictureNative对象；释放OH\_AuxiliaryPictureNative对象也不会从OH\_PictureNative对象中移除对应辅助图。通过[OH\_AuxiliaryPictureNative\_GetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_getinfo)获取到的OH\_AuxiliaryPictureInfo对象由调用方管理，使用完成后应调用[OH\_AuxiliaryPictureInfo\_Release](capi-picture-native-h.md#oh_auxiliarypictureinfo_release)释放。通过[OH\_AuxiliaryPictureNative\_GetMetadata](capi-picture-native-h.md#oh_auxiliarypicturenative_getmetadata)获取到的OH\_PictureMetadata对象由调用方管理，使用完成后应调用[OH\_PictureMetadata\_Release](capi-image-common-h.md#oh_picturemetadata_release)释放。接口返回失败时，输出参数的内容不能在后续流程中继续使用。

OH\_AuxiliaryPictureNative结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint8\_t | pixels | 辅助图像素数据。 | [OH\_AuxiliaryPictureNative\_ReadPixels](capi-picture-native-h.md#oh_auxiliarypicturenative_readpixels) | 读取辅助图的像素数据。 |
| uint8\_t | pixels | 辅助图像素数据。 | [OH\_AuxiliaryPictureNative\_WritePixels](capi-picture-native-h.md#oh_auxiliarypicturenative_writepixels) | 写入辅助图的像素数据。 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) | type | 辅助图类型。 | [OH\_AuxiliaryPictureNative\_GetType](capi-picture-native-h.md#oh_auxiliarypicturenative_gettype) | 获取辅助图类型。 |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) | info | 辅助图信息。 | [OH\_AuxiliaryPictureNative\_GetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_getinfo) | 获取辅助图信息。 |
| [OH\_AuxiliaryPictureInfo](capi-image-nativemodule-oh-auxiliarypictureinfo.md) | info | 辅助图信息。 | [OH\_AuxiliaryPictureNative\_SetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_setinfo) | 设置辅助图信息。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) | metadata | 辅助图元数据。 | [OH\_AuxiliaryPictureNative\_GetMetadata](capi-picture-native-h.md#oh_auxiliarypicturenative_getmetadata) | 获取辅助图的元数据。 |
| [OH\_PictureMetadata](capi-image-nativemodule-oh-picturemetadata.md) | metadata | 辅助图元数据。 | [OH\_AuxiliaryPictureNative\_SetMetadata](capi-picture-native-h.md#oh_auxiliarypicturenative_setmetadata) | 设置辅助图的元数据。 |

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](capi-picture-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成多图对象解码](../harmonyos-guides/image-source-picture-c.md)
