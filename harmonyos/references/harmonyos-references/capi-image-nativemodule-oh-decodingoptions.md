---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions
title: OH_DecodingOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_DecodingOptions
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce24fce9677d4a379429d13bb352f42aa28edd168c624bc6643007b5f138ce6d
---

```c
typedef struct OH_DecodingOptions OH_DecodingOptions
```

## 概述

OH\_DecodingOptions是native层封装的解码选项参数结构体，用于设置解码选项参数，在创建Pixelmap时作为入参传入，详细信息见[OH\_ImageSourceNative\_CreatePixelmap](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)。

OH\_DecodingOptions结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

使用[OH\_DecodingOptions\_Create](capi-image-source-native-h.md#oh_decodingoptions_create)函数创建OH\_DecodingOptions对象。

使用[OH\_DecodingOptions\_Release](capi-image-source-native-h.md#oh_decodingoptions_release)函数释放OH\_DecodingOptions对象。

使用约束：OH\_DecodingOptions用于配置PixelMap解码参数，通常作为[OH\_ImageSourceNative\_CreatePixelmap](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)、[OH\_ImageSourceNative\_CreatePixelmapUsingAllocator](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmapusingallocator)或[OH\_ImageSourceNative\_CreatePixelmapList](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmaplist)的入参。使用前需通过[OH\_DecodingOptions\_Create](capi-image-source-native-h.md#oh_decodingoptions_create)创建对象；使用完成后，应调用[OH\_DecodingOptions\_Release](capi-image-source-native-h.md#oh_decodingoptions_release)释放对象。

资源管理：释放OH\_ImageSourceNative或解码生成的OH\_PixelmapNative对象，不会自动释放OH\_DecodingOptions对象。OH\_DecodingOptions释放后，不应继续传入解码接口或调用其字段获取和设置接口。

OH\_DecodingOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段默认值 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- | --- |
| int32\_t | pixelFormat | 像素格式。 | RGBA\_8888 | [OH\_DecodingOptions\_GetPixelFormat](capi-image-source-native-h.md#oh_decodingoptions_getpixelformat) | [OH\_DecodingOptions\_SetPixelFormat](capi-image-source-native-h.md#oh_decodingoptions_setpixelformat) |
| uint32\_t | index | 解码图片序号。 | 0 | [OH\_DecodingOptions\_GetIndex](capi-image-source-native-h.md#oh_decodingoptions_getindex) | [OH\_DecodingOptions\_SetIndex](capi-image-source-native-h.md#oh_decodingoptions_setindex) |
| float | rotate | 旋转角度。 | 单位为角度（deg），默认值为0 | [OH\_DecodingOptions\_GetRotate](capi-image-source-native-h.md#oh_decodingoptions_getrotate) | [OH\_DecodingOptions\_SetRotate](capi-image-source-native-h.md#oh_decodingoptions_setrotate) |
| Image\_Size | desiredSize | 期望输出大小。 | 默认为原始图片尺寸。 | [OH\_DecodingOptions\_GetDesiredSize](capi-image-source-native-h.md#oh_decodingoptions_getdesiredsize) | [OH\_DecodingOptions\_SetDesiredSize](capi-image-source-native-h.md#oh_decodingoptions_setdesiredsize) |
| Image\_Region | desiredRegion | 解码区域。 | 默认为完整图片大小的区域。 | [OH\_DecodingOptions\_GetDesiredRegion](capi-image-source-native-h.md#oh_decodingoptions_getdesiredregion) | [OH\_DecodingOptions\_SetDesiredRegion](capi-image-source-native-h.md#oh_decodingoptions_setdesiredregion) |
| int32\_t | desiredDynamicRange | 期望动态范围。 | SDR | [OH\_DecodingOptions\_GetDesiredDynamicRange](capi-image-source-native-h.md#oh_decodingoptions_getdesireddynamicrange) | [OH\_DecodingOptions\_SetDesiredDynamicRange](capi-image-source-native-h.md#oh_decodingoptions_setdesireddynamicrange) |
| int32\_t | desiredColorSpace | 期望色彩空间。 | 默认色彩空间。 | [OH\_DecodingOptions\_GetDesiredColorSpace](capi-image-source-native-h.md#oh_decodingoptions_getdesiredcolorspace) | [OH\_DecodingOptions\_SetDesiredColorSpace](capi-image-source-native-h.md#oh_decodingoptions_setdesiredcolorspace) |
| Image\_Region | cropRegion | 裁剪区域。 | 默认为完整图片大小的区域。 | [OH\_DecodingOptions\_GetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_getcropregion) | [OH\_DecodingOptions\_SetCropRegion](capi-image-source-native-h.md#oh_decodingoptions_setcropregion) |
| int32\_t | cropAndScaleStrategy | 裁剪和缩放策略。 | 0 | [OH\_DecodingOptions\_GetCropAndScaleStrategy](capi-image-source-native-h.md#oh_decodingoptions_getcropandscalestrategy) | [OH\_DecodingOptions\_SetCropAndScaleStrategy](capi-image-source-native-h.md#oh_decodingoptions_setcropandscalestrategy) |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成图片解码](../harmonyos-guides/image-source-c.md)、[图片区域解码与下采样(C/C++)](../harmonyos-guides/image-region-and-downsampling-c.md)、[使用Image\_NativeModule完成HDR图片解码](../harmonyos-guides/image-hdr-decoding-c.md)
