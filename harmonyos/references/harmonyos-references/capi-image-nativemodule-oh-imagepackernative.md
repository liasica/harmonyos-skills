---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagepackernative
title: OH_ImagePackerNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImagePackerNative
category: harmonyos-references
scraped_at: 2026-04-28T08:13:28+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:6f04831422a64ca57a56b42c8f8b7bde21bfc0b7df3095339a98bdc5b20c0276
---

```
1. typedef struct OH_ImagePackerNative OH_ImagePackerNative
```

## 概述

PhonePC/2in1TabletTVWearable

ImagePacker结构体类型，用于执行ImagePacker相关操作。

此结构体内容不可直接操作，采用函数调用方式操作具体字段，结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| OH\_ImageSourceNative | imageSource | 图片源 | [OH\_ImagePackerNative\_PackToDataFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafromimagesource) | 将ImageSource编码为指定格式的数据。 |
| OH\_PixelmapNative | pixelmap | native层的pixelmap | [OH\_ImagePackerNative\_PackToDataFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmap) | 将Pixelmap编码为指定格式的数据。 |
| int32\_t | imagesourceFd | ImageSource关联的文件描述符 | [OH\_ImagePackerNative\_PackToFileFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefromimagesource) | 将一个ImageSource编码到文件中。 |
| int32\_t | pixelmapFd | pixelmap关联的文件描述符 | [OH\_ImagePackerNative\_PackToFileFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmap) | 将一个Pixelmap编码到文件中。 |

创建OH\_ImagePackerNative对象使用[OH\_ImagePackerNative\_Create](capi-image-packer-native-h.md#oh_imagepackernative_create)函数。

释放OH\_ImagePackerNative对象使用[OH\_ImagePackerNative\_Release](capi-image-packer-native-h.md#oh_imagepackernative_release)函数。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
