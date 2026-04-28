---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptions
title: OH_DecodingOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_DecodingOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:13:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:8dcd29a5000ac4fb79198dd45ab669a1ed437bbdbb6cf7acdcab659adc9436ac
---

```
1. typedef struct OH_DecodingOptions OH_DecodingOptions
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_DecodingOptions是native层封装的解码选项参数结构体，用于设置解码选项参数，在创建Pixelmap时作为入参传入，详细信息见[OH\_ImageSourceNative\_CreatePixelmap](capi-image-source-native-h.md#oh_imagesourcenative_createpixelmap)。

OH\_DecodingOptions结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH\_DecodingOptions对象使用[OH\_DecodingOptions\_Create](capi-image-source-native-h.md#oh_decodingoptions_create)函数。

释放OH\_DecodingOptions对象使用[OH\_DecodingOptions\_Release](capi-image-source-native-h.md#oh_decodingoptions_release)函数。

OH\_DecodingOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段默认值 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- | --- |
| int32\_t | pixelFormat | 像素格式 | RGBA\_8888 | [OH\_DecodingOptions\_GetPixelFormat](capi-image-source-native-h.md#oh_decodingoptions_getpixelformat) | [OH\_DecodingOptions\_SetPixelFormat](capi-image-source-native-h.md#oh_decodingoptions_setpixelformat) |
| uint32\_t | index | 解码图片序号 | 0 | [OH\_DecodingOptions\_GetIndex](capi-image-source-native-h.md#oh_decodingoptions_getindex) | [OH\_DecodingOptions\_SetIndex](capi-image-source-native-h.md#oh_decodingoptions_setindex) |
| float | rotate | 旋转角度 | 单位为deg, 默认值为0 | [OH\_DecodingOptions\_GetRotate](capi-image-source-native-h.md#oh_decodingoptions_getrotate) | [OH\_DecodingOptions\_SetRotate](capi-image-source-native-h.md#oh_decodingoptions_setrotate) |
| Image\_Size | desiredSize | 期望输出大小 | 默认为原始图片尺寸 | [OH\_DecodingOptions\_GetDesiredSize](capi-image-source-native-h.md#oh_decodingoptions_getdesiredsize) | [OH\_DecodingOptions\_SetDesiredSize](capi-image-source-native-h.md#oh_decodingoptions_setdesiredsize) |
| Image\_Region | desiredRegion | 解码区域 | 默认为完整图片大小的区域 | [OH\_DecodingOptions\_GetDesiredRegion](capi-image-source-native-h.md#oh_decodingoptions_getdesiredregion) | [OH\_DecodingOptions\_SetDesiredRegion](capi-image-source-native-h.md#oh_decodingoptions_setdesiredregion) |
| int32\_t | desiredDynamicRange | 期望动态范围 | SDR | [OH\_DecodingOptions\_GetDesiredDynamicRange](capi-image-source-native-h.md#oh_decodingoptions_getdesireddynamicrange) | [OH\_DecodingOptions\_SetDesiredDynamicRange](capi-image-source-native-h.md#oh_decodingoptions_setdesireddynamicrange) |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)
