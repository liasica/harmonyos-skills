---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-image-nativemodule-oh-pixelmap-hdrmetadatavalue
title: OH_Pixelmap_HdrMetadataValue
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrMetadataValue
category: harmonyos-references
scraped_at: 2026-04-28T08:13:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:54436d0db01f74157623ca243fb9f20651c18dd6b995912bed37c90f4abd51a5
---

```
1. typedef struct OH_Pixelmap_HdrMetadataValue {...} OH_Pixelmap_HdrMetadataValue
```

## 概述

PhonePC/2in1TabletTVWearable

Pixelmap使用的HDR元数据值，和OH\_Pixelmap\_HdrMetadataKey关键字相对应。用于[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)及[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)，有相应[OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)关键字作为入参时，设置或获取到本结构体中相对应的元数据类型的值。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_Pixelmap\_HdrMetadataType](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatatype) type | HDR\_METADATA\_TYPE关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrStaticMetadata](i-image-nativemodule-oh-pixelmap-hdrstaticmetadata.md) staticMetadata | HDR\_STATIC\_METADATA关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrDynamicMetadata](-image-nativemodule-oh-pixelmap-hdrdynamicmetadata.md) dynamicMetadata | HDR\_DYNAMIC\_METADATA关键字对应的具体值。 |
| [OH\_Pixelmap\_HdrGainmapMetadata](-image-nativemodule-oh-pixelmap-hdrgainmapmetadata.md) gainmapMetadata | HDR\_GAINMAP\_METADATA关键字对应的具体值。 |
