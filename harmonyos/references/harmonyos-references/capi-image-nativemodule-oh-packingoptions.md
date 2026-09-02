---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptions
title: OH_PackingOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PackingOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a8582d080b77ef1edced53583cd9966dc67570e8028f03170275a5b831297b59
---

```c
typedef struct OH_PackingOptions OH_PackingOptions
```

## 概述

OH\_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

使用[OH\_PackingOptions\_Create](capi-image-packer-native-h.md#oh_packingoptions_create)函数创建OH\_PackingOptions对象。

使用[OH\_PackingOptions\_Release](capi-image-packer-native-h.md#oh_packingoptions_release)函数释放OH\_PackingOptions对象。

使用约束：OH\_PackingOptions用于配置ImageSource、PixelMap或Picture编码参数。

* ImageSource编码需传入[OH\_ImagePackerNative\_PackToDataFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafromimagesource)或[OH\_ImagePackerNative\_PackToFileFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefromimagesource)使用。
* PixelMap编码需传入[OH\_ImagePackerNative\_PackToDataFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmap)或[OH\_ImagePackerNative\_PackToFileFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmap)使用。
* Picture编码需传入[OH\_ImagePackerNative\_PackToDataFromPicture](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompicture)或[OH\_ImagePackerNative\_PackToFileFromPicture](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompicture)使用。
* PixelMap序列编码请使用[OH\_PackingOptionsForSequence](capi-image-nativemodule-oh-packingoptionsforsequence.md)。

资源管理：释放OH\_ImagePackerNative对象不会自动释放OH\_PackingOptions对象。OH\_PackingOptions使用完成后，应调用[OH\_PackingOptions\_Release](capi-image-packer-native-h.md#oh_packingoptions_release)释放，释放后不应继续传入图像编码接口或调用其字段获取和设置接口。

OH\_PackingOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) | mimeType | 目标编码格式的MIME类型。ImageSource或PixelMap编码支持image/jpeg、image/webp、image/png、image/heic或image/heif、image/sdr\_astc\_4x4、image/sdr\_sut\_superfast\_4x4、image/hdr\_astc\_4x4；Picture编码支持image/jpeg、image/heic或image/heif。实际支持范围以[OH\_ImagePackerNative\_GetSupportedFormats](capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats)返回结果为准。 | [OH\_PackingOptions\_GetMimeType](capi-image-packer-native-h.md#oh_packingoptions_getmimetype)、[OH\_PackingOptions\_GetMimeTypeWithNull](capi-image-packer-native-h.md#oh_packingoptions_getmimetypewithnull) | [OH\_PackingOptions\_SetMimeType](capi-image-packer-native-h.md#oh_packingoptions_setmimetype) |
| uint32\_t | quality | 编码质量，实际编码效果取决于目标编码格式。 | [OH\_PackingOptions\_GetQuality](capi-image-packer-native-h.md#oh_packingoptions_getquality) | [OH\_PackingOptions\_SetQuality](capi-image-packer-native-h.md#oh_packingoptions_setquality) |
| bool | needsPackProperties | 是否需要编码图像属性，例如Exif。 | [OH\_PackingOptions\_GetNeedsPackProperties](capi-image-packer-native-h.md#oh_packingoptions_getneedspackproperties) | [OH\_PackingOptions\_SetNeedsPackProperties](capi-image-packer-native-h.md#oh_packingoptions_setneedspackproperties) |
| int32\_t | desiredDynamicRange | 编码时期望的图片动态范围，取值见[IMAGE\_PACKER\_DYNAMIC\_RANGE](capi-image-packer-native-h.md#image_packer_dynamic_range)。 | [OH\_PackingOptions\_GetDesiredDynamicRange](capi-image-packer-native-h.md#oh_packingoptions_getdesireddynamicrange) | [OH\_PackingOptions\_SetDesiredDynamicRange](capi-image-packer-native-h.md#oh_packingoptions_setdesireddynamicrange) |

**说明** 

* 通过[OH\_PackingOptions\_SetMimeType](capi-image-packer-native-h.md#oh_packingoptions_setmimetype)设置MIME类型时，接口会拷贝传入的format->data，不会持有调用方传入的数据指针。
* 通过[OH\_PackingOptions\_GetMimeType](capi-image-packer-native-h.md#oh_packingoptions_getmimetype)或[OH\_PackingOptions\_GetMimeTypeWithNull](capi-image-packer-native-h.md#oh_packingoptions_getmimetypewithnull)获取MIME类型时，接口成功返回的format.data由接口分配，使用完成后调用方应使用free()释放。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
