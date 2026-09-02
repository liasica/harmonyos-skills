---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative-auxiliarypicturecopyitem
title: OH_PictureNative_AuxiliaryPictureCopyItem
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PictureNative_AuxiliaryPictureCopyItem
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:08ac0d55c81d226a5771f5c44f18feafc72bf128df6519be1a03c6111950d297
---

```c
typedef struct OH_PictureNative_AuxiliaryPictureCopyItem {...} OH_PictureNative_AuxiliaryPictureCopyItem
```

## 概述

此结构体用于在创建PictureNative对象的深拷贝时指定辅助图的拷贝规则。描述如何将辅助图从一种类型拷贝到另一种类型。

**起始版本：** 26.0.0

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](capi-picture-native-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) srcType | 源辅助图类型，指定要从源图片中拷贝的辅助图类型。  **起始版本：** 26.0.0 |
| [Image\_AuxiliaryPictureType](capi-picture-native-h.md#image_auxiliarypicturetype) dstType | 目标辅助图类型，指定拷贝的辅助图在目标图片中存储的类型。  **起始版本：** 26.0.0 |
