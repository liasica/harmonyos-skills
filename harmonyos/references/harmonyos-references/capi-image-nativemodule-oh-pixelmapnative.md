---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmapnative
title: OH_PixelmapNative
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PixelmapNative
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8931d250d94119ee1599d61c80130f1d99a310119dda6959f830b3e7b5399442
---

```c
struct OH_PixelmapNative
```

## 概述

OH\_PixelmapNative是Native层封装的图像解码后无压缩的位图格式结构体，支持像素数据读写、不透明度设置、缩放、平移、旋转、翻转、裁剪等操作，适用于需要在Native层对Pixelmap进行像素级处理与变换的场景。

创建OH\_PixelmapNative需要使用[OH\_PixelmapNative\_CreatePixelmap](capi-pixelmap-native-h.md#oh_pixelmapnative_createpixelmap)系列函数，该函数在未指定源像素格式时，会默认按BGRA\_8888格式解析源像素数据。使用完毕后，必须调用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)函数释放资源，两者需配对使用，否则会导致内存泄漏。

OH\_PixelmapNative结构体的部分相关函数和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint8\_t | data | 图像像素数据，当未指定源像素格式时，默认按BGRA\_8888格式解析。 | [OH\_PixelmapNative\_ReadPixels](capi-pixelmap-native-h.md#oh_pixelmapnative_readpixels) | 读取Pixelmap的像素数据，结果写入缓冲区中。 |
| uint8\_t | data | 图像像素数据，当未指定源像素格式时，默认按BGRA\_8888格式解析。 | [OH\_PixelmapNative\_WritePixels](capi-pixelmap-native-h.md#oh_pixelmapnative_writepixels) | 将缓冲区中的像素数据写入Pixelmap。 |
| [OH\_Pixelmap\_ImageInfo](capi-image-nativemodule-oh-pixelmap-imageinfo.md) | imageInfo | 图像像素信息。 | [OH\_PixelmapNative\_GetImageInfo](capi-pixelmap-native-h.md#oh_pixelmapnative_getimageinfo) | 获取图像像素信息。 |
| float | alphaRate | 不透明度，取值范围(0.0, 1.0]，1.0表示完全不透明。 | [OH\_PixelmapNative\_Opacity](capi-pixelmap-native-h.md#oh_pixelmapnative_opacity) | 设置不透明度，使Pixelmap达到对应的不透明效果。 |
| float, float | scaleX, scaleY | scaleX为沿X轴的缩放比例、scaleY为沿Y轴的缩放比例，取值范围(0, +∞)，1.0表示不缩放。 | [OH\_PixelmapNative\_Scale](capi-pixelmap-native-h.md#oh_pixelmapnative_scale) | 根据输入的缩放比例对图像进行缩放。 |
| float, float | x, y | x平移量、y平移量，单位：像素（px）。正值x表示向右平移，负值x表示向左平移；正值y表示向下平移，负值y表示向上平移。 | [OH\_PixelmapNative\_Translate](capi-pixelmap-native-h.md#oh_pixelmapnative_translate) | 根据输入的平移距离对图片进行位置变换。 |
| float | angle | 旋转角度，单位：角度（°），正值表示顺时针方向旋转，负值表示逆时针方向旋转。 | [OH\_PixelmapNative\_Rotate](capi-pixelmap-native-h.md#oh_pixelmapnative_rotate) | 根据输入的角度对图片进行旋转。 |
| bool, bool | shouldFlipHorizontally, shouldFlipVertically | 是否水平翻转图像、是否垂直翻转图像。true表示翻转，false表示不翻转。 | [OH\_PixelmapNative\_Flip](capi-pixelmap-native-h.md#oh_pixelmapnative_flip) | 根据输入的水平/垂直翻转标志对图片进行翻转。 |
| [Image\_Region](capi-image-nativemodule-image-region.md) | region | 裁剪区间，包含起始坐标(x,y)和宽高，宽高需为正值且裁剪区域需在图像范围内，参考[Image\_Region](capi-image-nativemodule-image-region.md)。 | [OH\_PixelmapNative\_Crop](capi-pixelmap-native-h.md#oh_pixelmapnative_crop) | 根据输入的区域信息对图片进行裁剪。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)
