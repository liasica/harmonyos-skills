---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue
title: OH_Pixelmap_HdrMetadataValue
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrMetadataValue
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a08efac84378aefad65444162de79ce2abe7e94e2746cd77bedc1a2a137604a5
---

```c
typedef struct OH_Pixelmap_HdrMetadataValue {...} OH_Pixelmap_HdrMetadataValue
```

## 概述

Pixelmap使用的HDR元数据值，和OH\_Pixelmap\_HdrMetadataKey相对应。当传入相应的[OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)中的关键字作为入参时，可通过本结构体设置或获取对应类型的元数据值。该结构体用于[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)接口，适用于需要对HDR图像进行元数据管理与渲染处理的场景，帮助应用正确设置和获取HDR元数据以实现HDR图像的高动态范围显示效果。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_HdrMetadataType](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) type | [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)中HDR\_METADATA\_TYPE关键字对应的HDR元数据值类型，用于表示HDR元数据的类型。不同取值对应不同类型的HDR元数据，需根据HDR图像的实际元数据类型选择合适的值，并填充对应类型的元数据成员字段。 |
| [OH\_Pixelmap\_HdrStaticMetadata](capi-image-nativemodule-oh-pixelmap-hdrstaticmetadata.md) staticMetadata | [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)中HDR\_STATIC\_METADATA关键字对应的元数据值类型，用于存储HDR静态元数据。 |
| [OH\_Pixelmap\_HdrDynamicMetadata](capi-image-nativemodule-oh-pixelmap-hdrdynamicmetadata.md) dynamicMetadata | [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)中HDR\_DYNAMIC\_METADATA关键字对应的元数据值类型，用于存储HDR动态元数据，格式遵循相关HDR动态元数据标准。 |
| [OH\_Pixelmap\_HdrGainmapMetadata](capi-image-nativemodule-oh-pixelmap-hdrgainmapmetadata.md) gainmapMetadata | [OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)中HDR\_GAINMAP\_METADATA关键字对应的元数据值类型，用于存储HDR增益图元数据，参考ISO 21496-1。 |
