---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-decodingoptionsforpicture
title: OH_DecodingOptionsForPicture
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_DecodingOptionsForPicture
category: harmonyos-references
scraped_at: 2026-09-02T14:52:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc3e1f84eca98dfb269f4497355c4785d8abb6438a8514f457a333f72d9ad85a
---

```c
struct OH_DecodingOptionsForPicture
```

## 概述

Picture解码参数结构体。

使用[OH\_DecodingOptionsForPicture\_Create](capi-image-source-native-h.md#oh_decodingoptionsforpicture_create)函数创建OH\_DecodingOptionsForPicture对象。

使用[OH\_DecodingOptionsForPicture\_Release](capi-image-source-native-h.md#oh_decodingoptionsforpicture_release)函数释放OH\_DecodingOptionsForPicture对象。

资源管理：释放OH\_ImageSourceNative或解码生成的OH\_PictureNative对象，不会自动释放OH\_DecodingOptionsForPicture对象。OH\_DecodingOptionsForPicture释放后，不应继续传入Picture解码接口或调用其字段获取和设置接口。

OH\_DecodingOptionsForPicture结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 字段默认值 | 字段获取函数 | 字段设置函数 |
| --- | --- | --- | --- | --- | --- |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype)数组 | desiredAuxiliaryPictures | 期望在Picture解码结果中包含的辅助图类型，可用于只解码调用方需要的增益图、深度图等辅助图。 | 空集合，即不指定任何辅助图类型；解码Picture时会按全部支持的辅助图类型处理。 | [OH\_DecodingOptionsForPicture\_GetDesiredAuxiliaryPictures](capi-image-source-native-h.md#oh_decodingoptionsforpicture_getdesiredauxiliarypictures) | [OH\_DecodingOptionsForPicture\_SetDesiredAuxiliaryPictures](capi-image-source-native-h.md#oh_decodingoptionsforpicture_setdesiredauxiliarypictures) |

**起始版本：** 13

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)

**相关开发指导：** [使用Image\_NativeModule完成多图对象解码](../harmonyos-guides/image-source-picture-c.md)
