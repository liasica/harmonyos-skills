---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-imagerawdata
title: OH_ImageRawData
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageRawData
category: harmonyos-references
scraped_at: 2026-09-02T14:52:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d144129b0e356c9cb0335a0ccd434711661c623254bbafd376b4389cd812ebf2
---

```c
typedef struct OH_ImageRawData OH_ImageRawData
```

## 概述

OH\_ImageRawData用于承载图像中的原始数据。

使用[OH\_ImageSourceNative\_CreateImageRawData](capi-image-source-native-h.md#oh_imagesourcenative_createimagerawdata)函数从OH\_ImageSourceNative对象中创建OH\_ImageRawData对象。

使用[OH\_ImageSourceNative\_DestroyImageRawData](capi-image-source-native-h.md#oh_imagesourcenative_destroyimagerawdata)函数销毁OH\_ImageRawData对象。

资源管理：OH\_ImageRawData使用完成后，应调用[OH\_ImageSourceNative\_DestroyImageRawData](capi-image-source-native-h.md#oh_imagesourcenative_destroyimagerawdata)销毁。释放OH\_ImageSourceNative对象不会自动销毁OH\_ImageRawData对象，二者生命周期相互独立。通过[OH\_ImageSourceNative\_GetBufferFromRawData](capi-image-source-native-h.md#oh_imagesourcenative_getbufferfromrawdata)获取到的data指向OH\_ImageRawData对象内部缓冲区，调用方不应对data调用free()。OH\_ImageRawData对象销毁后，该data地址失效。如需在OH\_ImageRawData对象销毁后继续使用数据，应在销毁前自行拷贝。

OH\_ImageRawData结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段获取函数 |
| --- | --- | --- | --- |
| uint8\_t \* | data | 原始数据缓冲区首地址。 | [OH\_ImageSourceNative\_GetBufferFromRawData](capi-image-source-native-h.md#oh_imagesourcenative_getbufferfromrawdata) |
| size\_t | length | 原始数据缓冲区长度。 | [OH\_ImageSourceNative\_GetBufferFromRawData](capi-image-source-native-h.md#oh_imagesourcenative_getbufferfromrawdata) |
| uint8\_t | bitsPerPixel | 缓冲区数据中每个像素实际占用的位数。 | [OH\_ImageSourceNative\_GetBitsPerPixelFromRawData](capi-image-source-native-h.md#oh_imagesourcenative_getbitsperpixelfromrawdata) |

**起始版本：** 24

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)
