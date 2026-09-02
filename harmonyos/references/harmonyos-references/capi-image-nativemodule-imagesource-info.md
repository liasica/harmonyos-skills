---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-imagesource-info
title: OH_ImageSource_Info
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageSource_Info
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:79bb030414125aec1c2c460195dc192da0a4fd40498f8ed1f72d965a67e7453c
---

```c
struct OH_ImageSource_Info
```

## 概述

OH\_ImageSource\_Info是native层封装的ImageSource信息结构体，OH\_ImageSource\_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

使用[OH\_ImageSourceInfo\_Create](capi-image-source-native-h.md#oh_imagesourceinfo_create)函数创建OH\_ImageSource\_Info对象。

使用[OH\_ImageSourceNative\_GetImageInfo](capi-image-source-native-h.md#oh_imagesourcenative_getimageinfo)函数将OH\_ImageSourceNative中的图像信息写入创建好的OH\_ImageSource\_Info对象。

使用[OH\_ImageSourceInfo\_Release](capi-image-source-native-h.md#oh_imagesourceinfo_release)函数释放OH\_ImageSource\_Info对象。

使用约束：OH\_ImageSource\_Info对象通常配合[OH\_ImageSourceNative\_GetImageInfo](capi-image-source-native-h.md#oh_imagesourcenative_getimageinfo)使用，用于承载指定序号图片的宽、高、动态范围和MIME类型等信息。使用前需通过[OH\_ImageSourceInfo\_Create](capi-image-source-native-h.md#oh_imagesourceinfo_create)创建对象；使用完成后，应调用[OH\_ImageSourceInfo\_Release](capi-image-source-native-h.md#oh_imagesourceinfo_release)释放对象。

OH\_ImageSource\_Info结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽度。 | [OH\_ImageSourceInfo\_GetWidth](capi-image-source-native-h.md#oh_imagesourceinfo_getwidth) | 获取图片的宽。 |
| uint32\_t | height | 图片高度。 | [OH\_ImageSourceInfo\_GetHeight](capi-image-source-native-h.md#oh_imagesourceinfo_getheight) | 获取图片的高。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息。 | [OH\_ImageSourceInfo\_GetDynamicRange](capi-image-source-native-h.md#oh_imagesourceinfo_getdynamicrange) | 获取图片是否为高动态范围的信息。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) | mimeType | 图片源的MIME类型。 | [OH\_ImageSourceInfo\_GetMimeType](capi-image-source-native-h.md#oh_imagesourceinfo_getmimetype) | 获取图片的MimeType。 |

**说明** 

通过[OH\_ImageSourceInfo\_GetMimeType](capi-image-source-native-h.md#oh_imagesourceinfo_getmimetype)获取到的mimeType.data指向OH\_ImageSource\_Info对象内部持有的内存。调用[OH\_ImageSourceInfo\_Release](capi-image-source-native-h.md#oh_imagesourceinfo_release)释放OH\_ImageSource\_Info后，该地址会失效；如需在释放后继续使用MIME类型数据，应在释放前自行深拷贝。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成图片解码](../harmonyos-guides/image-source-c.md)、[图片区域解码与下采样(C/C++)](../harmonyos-guides/image-region-and-downsampling-c.md)、[使用Image\_NativeModule完成动图解码](../harmonyos-guides/image-animated-decoding-c.md)、[使用Image\_NativeModule完成HDR图片解码](../harmonyos-guides/image-hdr-decoding-c.md)
