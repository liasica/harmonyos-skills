---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-imagesource-info
title: OH_ImageSource_Info
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_ImageSource_Info
category: harmonyos-references
scraped_at: 2026-04-28T08:13:24+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:75f2dcb48aaadbbbe65c7be29219e377ee0519fdb5b3578a1528c333fba49ea6
---

```
1. struct OH_ImageSource_Info
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_ImageSource\_Info是native层封装的ImageSource信息结构体，OH\_ImageSource\_Info结构体不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建OH\_ImageSource\_Info对象使用[OH\_ImageSourceInfo\_Create](capi-image-source-native-h.md#oh_imagesourceinfo_create)函数。

释放OH\_ImageSource\_Info对象使用[OH\_ImageSourceInfo\_Release](capi-image-source-native-h.md#oh_imagesourceinfo_release)函数。调用该接口之后，与OH\_ImageSource\_Info结构体相关的属性均会被释放。因此在调用该接口前，请务必确认相关属性已不再被需要或对相关属性已完成深拷贝操作。

OH\_ImageSource\_Info结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| uint32\_t | width | 图片宽度 | [OH\_ImageSourceInfo\_GetWidth](capi-image-source-native-h.md#oh_imagesourceinfo_getwidth) | 获取图片的宽。 |
| uint32\_t | height | 图片高度 | [OH\_ImageSourceInfo\_GetHeight](capi-image-source-native-h.md#oh_imagesourceinfo_getheight) | 获取图片的高。 |
| bool | isHdr | 是否为高动态范围（HDR）的信息 | [OH\_ImageSourceInfo\_GetDynamicRange](capi-image-source-native-h.md#oh_imagesourceinfo_getdynamicrange) | 获取图片是否为高动态范围的信息。 |
| [Image\_MimeType](capi-image-nativemodule-image-string.md) | mimeType | 图片源的MIME类型 | [OH\_ImageSourceInfo\_GetMimetype](capi-image-source-native-h.md#oh_imagesourceinfo_getmimetype) | 获取图片的MimeType。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_source\_native.h](capi-image-source-native-h.md)
