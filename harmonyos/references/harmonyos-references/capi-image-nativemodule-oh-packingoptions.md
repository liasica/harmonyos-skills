---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-packingoptions
title: OH_PackingOptions
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PackingOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:13:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e36ce55185d569fb24c96dbab3520b86a9483093c0396e747f0641cd6a44d087
---

```
1. typedef struct OH_PackingOptions OH_PackingOptions
```

## 概述

PhonePC/2in1TabletTVWearable

OH\_PackingOptions是native层封装的图像编码选项结构体，不可直接操作，而是采用函数调用方式创建、释放结构体以及操作具体字段。

创建PackingOptions结构体的对象使用[OH\_PackingOptions\_Create](capi-image-packer-native-h.md#oh_packingoptions_create)函数。

释放OH\_PackingOptions对象使用[OH\_PackingOptions\_Release](capi-image-packer-native-h.md#oh_packingoptions_release)函数。

OH\_PackingOptions结构体内容和操作方式如下：

| 字段类型 | 字段名称 | 字段描述 | 操作函数 | 函数描述 |
| --- | --- | --- | --- | --- |
| Image\_MimeType | mimeType | MIME类型 | [OH\_PackingOptions\_GetMimeType](capi-image-packer-native-h.md#oh_packingoptions_getmimetype) | 获取MIME类型。 |
| Image\_MimeType | mimeType | MIME类型 | [OH\_PackingOptions\_SetMimeType](capi-image-packer-native-h.md#oh_packingoptions_setmimetype) | 设置MIME类型。 |
| uint32\_t | quality | 编码质量 | [OH\_PackingOptions\_GetQuality](capi-image-packer-native-h.md#oh_packingoptions_getquality) | 获取编码质量。 |
| uint32\_t | quality | 编码质量 | [OH\_PackingOptions\_SetQuality](capi-image-packer-native-h.md#oh_packingoptions_setquality) | 设置编码质量。 |
| int32\_t | desiredDynamicRange | 图片动态范围 | [OH\_PackingOptions\_GetDesiredDynamicRange](capi-image-packer-native-h.md#oh_packingoptions_getdesireddynamicrange) | 获取编码时期望的图片动态范围。 |
| int32\_t | desiredDynamicRange | 图片动态范围 | [OH\_PackingOptions\_SetDesiredDynamicRange](capi-image-packer-native-h.md#oh_packingoptions_setdesireddynamicrange) | 设置编码时期望的图片动态范围。 |

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [image\_packer\_native.h](capi-image-packer-native-h.md)
