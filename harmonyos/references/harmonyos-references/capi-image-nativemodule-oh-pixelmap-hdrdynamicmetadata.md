---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrdynamicmetadata
title: OH_Pixelmap_HdrDynamicMetadata
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrDynamicMetadata
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6074a0a0539cb8f9f8da1e20ed94d47134ff9f324fb293b7459d4f61c7d4de8a
---

```c
typedef struct OH_Pixelmap_HdrDynamicMetadata {...} OH_Pixelmap_HdrDynamicMetadata
```

## 概述

表示HDR\_DYNAMIC\_METADATA关键字对应的动态元数据值，用于存储HDR图像的动态元数据。HDR动态元数据可用于在显示过程中动态调整HDR图像的显示参数，以适配不同显示设备的能力，获得更准确的HDR显示效果。在调用[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)和[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)时作为[OH\_Pixelmap\_HdrMetadataValue](capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue.md)的成员使用。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t \*data | 动态元数据值的指针，指向存储动态元数据的二进制数据缓冲区，缓冲区长度由length成员指定。 |
| uint32\_t length | 动态元数据值的长度，单位：字节（Byte），取值需与data指向的数据缓冲区实际长度一致。 |
