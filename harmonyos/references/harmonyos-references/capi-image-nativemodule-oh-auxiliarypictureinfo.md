---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-auxiliarypictureinfo
title: OH_AuxiliaryPictureInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_AuxiliaryPictureInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0d64b05dd0259cb75ebb2ea89e6a5e8a07585b0e4018efb2275b5ffb65409f13
---

```c
typedef struct OH_AuxiliaryPictureInfo OH_AuxiliaryPictureInfo
```

## 概述

AuxiliaryPictureInfo结构体类型，用于执行AuxiliaryPictureInfo相关操作。

使用[OH\_AuxiliaryPictureInfo\_Create](capi-picture-native-h.md#oh_auxiliarypictureinfo_create)函数创建OH\_AuxiliaryPictureInfo对象。

使用[OH\_AuxiliaryPictureNative\_GetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_getinfo)函数从OH\_AuxiliaryPictureNative对象中获取OH\_AuxiliaryPictureInfo对象。

使用[OH\_AuxiliaryPictureInfo\_Release](capi-picture-native-h.md#oh_auxiliarypictureinfo_release)函数释放OH\_AuxiliaryPictureInfo对象。

使用约束：使用OH\_AuxiliaryPictureInfo对象前，需先创建或获取对象；使用完成后，应调用[OH\_AuxiliaryPictureInfo\_Release](capi-picture-native-h.md#oh_auxiliarypictureinfo_release)释放对象。调用[OH\_AuxiliaryPictureInfo\_GetType](capi-picture-native-h.md#oh_auxiliarypictureinfo_gettype)、[OH\_AuxiliaryPictureInfo\_GetSize](capi-picture-native-h.md#oh_auxiliarypictureinfo_getsize)、[OH\_AuxiliaryPictureInfo\_GetRowStride](capi-picture-native-h.md#oh_auxiliarypictureinfo_getrowstride)或[OH\_AuxiliaryPictureInfo\_GetPixelFormat](capi-picture-native-h.md#oh_auxiliarypictureinfo_getpixelformat)时，输出参数不允许传入nullptr；接口返回失败时，输出参数的内容不能在后续流程中继续使用。只有在明确辅助图实际状态与OH\_AuxiliaryPictureInfo对象信息不一致或有明确业务诉求时，才需要手动设置OH\_AuxiliaryPictureInfo。

资源管理：[OH\_AuxiliaryPictureNative\_GetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_getinfo)成功返回的OH\_AuxiliaryPictureInfo对象由调用方管理。通过[OH\_AuxiliaryPictureNative\_SetInfo](capi-picture-native-h.md#oh_auxiliarypicturenative_setinfo)设置辅助图信息时，接口会读取并保存OH\_AuxiliaryPictureInfo中的信息值，接口返回后调用方仍需自行管理该OH\_AuxiliaryPictureInfo对象的生命周期。

OH\_AuxiliaryPictureInfo结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) | type | 辅助图类型。 | [OH\_AuxiliaryPictureInfo\_GetType](capi-picture-native-h.md#oh_auxiliarypictureinfo_gettype) | [OH\_AuxiliaryPictureInfo\_SetType](capi-picture-native-h.md#oh_auxiliarypictureinfo_settype) |
| [Image\_Size](capi-image-nativemodule-image-size.md) | size | 辅助图尺寸。 | [OH\_AuxiliaryPictureInfo\_GetSize](capi-picture-native-h.md#oh_auxiliarypictureinfo_getsize) | [OH\_AuxiliaryPictureInfo\_SetSize](capi-picture-native-h.md#oh_auxiliarypictureinfo_setsize) |
| uint32\_t | rowStride | 行跨距，内存中每行像素所占的空间。 | [OH\_AuxiliaryPictureInfo\_GetRowStride](capi-picture-native-h.md#oh_auxiliarypictureinfo_getrowstride) | [OH\_AuxiliaryPictureInfo\_SetRowStride](capi-picture-native-h.md#oh_auxiliarypictureinfo_setrowstride) |
| [PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format) | pixelFormat | 像素格式。 | [OH\_AuxiliaryPictureInfo\_GetPixelFormat](capi-picture-native-h.md#oh_auxiliarypictureinfo_getpixelformat) | [OH\_AuxiliaryPictureInfo\_SetPixelFormat](capi-picture-native-h.md#oh_auxiliarypictureinfo_setpixelformat) |

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](capi-picture-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成多图对象解码](../harmonyos-guides/image-source-picture-c.md)
