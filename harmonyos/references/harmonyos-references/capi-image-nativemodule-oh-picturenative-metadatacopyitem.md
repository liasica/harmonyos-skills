---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-picturenative-metadatacopyitem
title: OH_PictureNative_MetadataCopyItem
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_PictureNative_MetadataCopyItem
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:62703510799a96247e42b273b8e635b39dc32c940df0138baf4af9375c082f5c
---

```c
typedef struct OH_PictureNative_MetadataCopyItem {...} OH_PictureNative_MetadataCopyItem
```

## 概述

此结构体用于在创建PictureNative对象的深拷贝时指定元数据的拷贝规则。描述如何将元数据从一种类型拷贝到另一种类型。

**起始版本：** 26.0.0

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [picture\_native.h](capi-picture-native-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) srcType | 源元数据类型，指定要从源图片中拷贝的元数据类型。  **起始版本：** 26.0.0 |
| [Image\_MetadataType](capi-image-common-h.md#image_metadatatype) dstType | 目标元数据类型，指定拷贝的元数据在目标图片中存储的类型。  **起始版本：** 26.0.0 |
