---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagesourcenative
title: OH_ImageSourceNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageSourceNative
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce8b1704933d207fd0291c5b3f893227e6658d85f7b9354c834d70d0ed0b094f
---

```c
struct OH_ImageSourceNative
```

## 概述

OH\_ImageSourceNative是native层封装的ImageSource结构体，用于创建图片数据。OH\_ImageSourceNative结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

有多种方式创建OH\_ImageSourceNative，具体如下：

| 函数 | 描述 |
| --- | --- |
| [OH\_ImageSourceNative\_CreateFromUri](capi-image-source-native-h.md#oh_imagesourcenative_createfromuri) | 通过uri创建OH\_ImageSourceNative对象。 |
| [OH\_ImageSourceNative\_CreateFromFd](capi-image-source-native-h.md#oh_imagesourcenative_createfromfd) | 通过fd创建OH\_ImageSourceNative对象。 |
| [OH\_ImageSourceNative\_CreateFromData](capi-image-source-native-h.md#oh_imagesourcenative_createfromdata) | 通过缓冲区数据创建OH\_ImageSourceNative对象。 |
| [OH\_ImageSourceNative\_CreateFromDataWithUserBuffer](capi-image-source-native-h.md#oh_imagesourcenative_createfromdatawithuserbuffer) | 通过调用方传入的数据缓存创建OH\_ImageSourceNative对象，创建过程中不拷贝该数据缓存。 |
| [OH\_ImageSourceNative\_CreateFromRawFile](capi-image-source-native-h.md#oh_imagesourcenative_createfromrawfile) | 通过图像资源文件的RawFileDescriptor创建OH\_ImageSourceNative对象。 |

使用[OH\_ImageSourceNative\_Release](capi-image-source-native-h.md#oh_imagesourcenative_release)函数释放OH\_ImageSourceNative对象。

使用约束：使用OH\_ImageSourceNative对象前，必须先通过上述接口创建对象；使用完成后，应调用[OH\_ImageSourceNative\_Release](capi-image-source-native-h.md#oh_imagesourcenative_release)释放对象。通过[OH\_ImageSourceNative\_CreateFromDataWithUserBuffer](capi-image-source-native-h.md#oh_imagesourcenative_createfromdatawithuserbuffer)创建对象时，在OH\_ImageSourceNative对象生命周期内，调用方传入的数据缓存必须保持有效，不能被释放、复用或修改为其他图片数据。

资源管理：通过OH\_ImageSourceNative解码或获取到的[OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)、[OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md)、[OH\_ImageRawData](capi-image-nativemodule-oh-imagerawdata.md)对象由调用方分别管理。释放OH\_ImageSourceNative对象不会自动释放这些对象，需要调用对应接口释放或销毁。

OH\_ImageSourceNative结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| int32\_t | delayTimeList | 图像延迟时间数组。 | [OH\_ImageSourceNative\_GetDelayTimeList](capi-image-source-native-h.md#oh_imagesourcenative_getdelaytimelist) | 获取图像延迟时间数组。 |
| OH\_ImageSource\_Info | info | ImageSource信息。 | [OH\_ImageSourceNative\_GetImageInfo](capi-image-source-native-h.md#oh_imagesourcenative_getimageinfo) | 获取指定序号的图片信息。 |
| Image\_String | value | 图像属性值。 | [OH\_ImageSourceNative\_GetImageProperty](capi-image-source-native-h.md#oh_imagesourcenative_getimageproperty) | 获取图片Exif指定属性键的值。 |
| Image\_String | value | 图像属性值。 | [OH\_ImageSourceNative\_ModifyImageProperty](capi-image-source-native-h.md#oh_imagesourcenative_modifyimageproperty) | 通过指定的键修改图片Exif属性的值。 |
| uint32\_t | frameCount | 图像帧数。 | [OH\_ImageSourceNative\_GetFrameCount](capi-image-source-native-h.md#oh_imagesourcenative_getframecount) | 获取图像帧数。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成图片解码](../harmonyos-guides/image-source-c.md)、[图片区域解码与下采样(C/C++)](../harmonyos-guides/image-region-and-downsampling-c.md)、[使用Image\_NativeModule完成动图解码](../harmonyos-guides/image-animated-decoding-c.md)、[使用Image\_NativeModule完成HDR图片解码](../harmonyos-guides/image-hdr-decoding-c.md)、[使用Image\_NativeModule完成多图对象解码](../harmonyos-guides/image-source-picture-c.md)
