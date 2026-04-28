---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagenative
title: OH_ImageNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageNative
category: harmonyos-references
scraped_at: 2026-04-28T08:13:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f84517635c7fbd1f62e31149cd2b5dfe9694c009457988d1ef05d24f54e56f37
---

```
1. typedef struct OH_ImageNative OH_ImageNative
```

## 概述

PhonePC/2in1TabletTVWearable

为图像接口定义native层图像对象的别名。

此结构体内容不可直接操作，采用函数调用方式操作具体字段，结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| Image\_Size | imageSize | 图像大小 | [OH\_ImageNative\_GetImageSize](capi-image-native-h.md#oh_imagenative_getimagesize) | 获取 OH\_ImageNative 对象的 Image\_Size 信息。 |
| uint32\_t | types | 组件类型，用于描述图像颜色分量。 | [OH\_ImageNative\_GetComponentTypes](capi-image-native-h.md#oh_imagenative_getcomponenttypes) | 获取 OH\_ImageNative 对象的组件列表信息。 |
| OH\_NativeBuffer | nativeBuffer | 组件缓冲区 | [OH\_ImageNative\_GetByteBuffer](capi-image-native-h.md#oh_imagenative_getbytebuffer) | 获取 OH\_ImageNative 对象中某个组件类型所对应的缓冲区。 |
| size\_t | bufferSize | 缓冲区的大小 | [OH\_ImageNative\_GetBufferSize](capi-image-native-h.md#oh_imagenative_getbuffersize) | 获取 OH\_ImageNative 对象中某个组件类型所对应的缓冲区的大小。 |
| int32\_t | rowStride | 像素行宽 | [OH\_ImageNative\_GetRowStride](capi-image-native-h.md#oh_imagenative_getrowstride) | 获取 OH\_ImageNative 对象中某个组件类型所对应的像素行宽。 |
| int32\_t | pixelStride | 像素大小 | [OH\_ImageNative\_GetPixelStride](capi-image-native-h.md#oh_imagenative_getpixelstride) | 获取 OH\_ImageNative 对象中某个组件类型所对应的像素大小。 |

释放OH\_ImageNative对象使用[OH\_ImageNative\_Release](capi-image-native-h.md#oh_imagenative_release)函数。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_native.h](capi-image-native-h.md)
