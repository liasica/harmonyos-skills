---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagepackernative
title: OH_ImagePackerNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImagePackerNative
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:65205cc2770defbaf415a631eddeccc8786a05d7eda224e0d3705edab51725f7
---

```c
typedef struct OH_ImagePackerNative OH_ImagePackerNative
```

## 概述

OH\_ImagePackerNative用于将ImageSource、PixelMap、Picture或PixelMap序列编码为图片数据或文件。

使用[OH\_ImagePackerNative\_Create](capi-image-packer-native-h.md#oh_imagepackernative_create)函数创建OH\_ImagePackerNative对象。

使用[OH\_ImagePackerNative\_Release](capi-image-packer-native-h.md#oh_imagepackernative_release)函数释放OH\_ImagePackerNative对象。

资源管理：OH\_ImagePackerNative使用完成后，应调用[OH\_ImagePackerNative\_Release](capi-image-packer-native-h.md#oh_imagepackernative_release)释放。释放OH\_ImagePackerNative对象不会释放OH\_PackingOptions、OH\_PackingOptionsForSequence、OH\_ImageSourceNative、OH\_PixelmapNative或OH\_PictureNative对象。

OH\_ImagePackerNative支持的编码方式如下：

| 输入对象 | 输出位置 | 编码函数 | 描述 |
| --- | --- | --- | --- |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) | 数据缓冲区 | [OH\_ImagePackerNative\_PackToDataFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafromimagesource) | 将ImageSource编码为指定格式的数据。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) | 数据缓冲区 | [OH\_ImagePackerNative\_PackToDataFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmap) | 将PixelMap编码为指定格式的数据。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) | 数据缓冲区 | [OH\_ImagePackerNative\_PackToDataFromPicture](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompicture) | 将Picture编码为指定格式的数据，仅支持JPEG和HEIF。 |
| OH\_PixelmapNative数组 | 数据缓冲区 | [OH\_ImagePackerNative\_PackToDataFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtodatafrompixelmapsequence) | 将PixelMap序列编码为GIF格式数据。 |
| [OH\_ImageSourceNative](capi-image-nativemodule-oh-imagesourcenative.md) | 文件描述符 | [OH\_ImagePackerNative\_PackToFileFromImageSource](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefromimagesource) | 将ImageSource编码到文件中。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md) | 文件描述符 | [OH\_ImagePackerNative\_PackToFileFromPixelmap](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmap) | 将PixelMap编码到文件中。 |
| [OH\_PictureNative](capi-image-nativemodule-oh-picturenative.md) | 文件描述符 | [OH\_ImagePackerNative\_PackToFileFromPicture](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompicture) | 将Picture编码到文件中，仅支持JPEG和HEIF。 |
| OH\_PixelmapNative数组 | 文件描述符 | [OH\_ImagePackerNative\_PackToFileFromPixelmapSequence](capi-image-packer-native-h.md#oh_imagepackernative_packtofilefrompixelmapsequence) | 将PixelMap序列编码为GIF格式并写入文件。 |

获取支持编码的图片格式使用[OH\_ImagePackerNative\_GetSupportedFormats](capi-image-packer-native-h.md#oh_imagepackernative_getsupportedformats)函数。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
