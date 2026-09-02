---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturemetadata
title: OH_PictureMetadata
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PictureMetadata
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93af57eb2c1a2f0d4d001745a7b11c2b67c61ee45947a74271abe67578276f6f
---

```c
typedef struct OH_PictureMetadata OH_PictureMetadata
```

## 概述

OH\_PictureMetadata用于承载Picture元数据。

有多种方式创建和获取OH\_PictureMetadata：

| 函数 | 描述 |
| --- | --- |
| [OH\_PictureMetadata\_Create()](capi-image-common-h.md#oh_picturemetadata_create) | 创建OH\_PictureMetadata指针。 |
| [OH\_PictureMetadata\_Clone()](capi-image-common-h.md#oh_picturemetadata_clone) | 拷贝元数据。 |
| [OH\_PictureNative\_GetMetadata()](capi-picture-native-h.md#oh_picturenative_getmetadata) | 获取主图的元数据。 |
| [OH\_AuxiliaryPictureNative\_GetMetadata()](capi-picture-native-h.md#oh_auxiliarypicturenative_getmetadata) | 获取辅助图的元数据。 |

使用[OH\_PictureMetadata\_Release()](capi-image-common-h.md#oh_picturemetadata_release)函数释放OH\_PictureMetadata对象。

资源管理：通过[OH\_PictureMetadata\_Create()](capi-image-common-h.md#oh_picturemetadata_create)、[OH\_PictureMetadata\_Clone()](capi-image-common-h.md#oh_picturemetadata_clone)、[OH\_PictureNative\_GetMetadata()](capi-picture-native-h.md#oh_picturenative_getmetadata)或[OH\_AuxiliaryPictureNative\_GetMetadata()](capi-picture-native-h.md#oh_auxiliarypicturenative_getmetadata)获取到的OH\_PictureMetadata对象由调用方管理，使用完成后应调用[OH\_PictureMetadata\_Release()](capi-image-common-h.md#oh_picturemetadata_release)释放。通过[OH\_PictureNative\_SetMetadata()](capi-picture-native-h.md#oh_picturenative_setmetadata)或[OH\_AuxiliaryPictureNative\_SetMetadata()](capi-picture-native-h.md#oh_auxiliarypicturenative_setmetadata)设置元数据时，接口不会释放传入的OH\_PictureMetadata对象。

OH\_PictureMetadata结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| [Image\_String](capi-image-nativemodule-image-string.md) | property | 元数据属性。 | [OH\_PictureMetadata\_GetProperty()](capi-image-common-h.md#oh_picturemetadata_getproperty)、[OH\_PictureMetadata\_GetPropertyWithNull()](capi-image-common-h.md#oh_picturemetadata_getpropertywithnull) | [OH\_PictureMetadata\_SetProperty()](capi-image-common-h.md#oh_picturemetadata_setproperty) |
| OH\_PictureMetadata | metadata | 元数据对象副本。 | [OH\_PictureMetadata\_Clone()](capi-image-common-h.md#oh_picturemetadata_clone) | - |

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_common.h](capi-image-common-h.md)
