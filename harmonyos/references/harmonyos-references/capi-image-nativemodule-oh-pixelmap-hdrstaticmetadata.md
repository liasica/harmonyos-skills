---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-oh-pixelmap-hdrstaticmetadata
title: OH_Pixelmap_HdrStaticMetadata
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > OH_Pixelmap_HdrStaticMetadata
category: harmonyos-references
scraped_at: 2026-09-02T15:02:33+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:085bbf836e3e07b6d5aa20a6c4e9dc2f58c6ab20d38978716e9c93fbb4818666
---

```c
typedef struct OH_Pixelmap_HdrStaticMetadata {...} OH_Pixelmap_HdrStaticMetadata
```

## 概述

表示HDR\_STATIC\_METADATA关键字对应的静态元数据值，用于描述HDR显示设备的能力信息及内容亮度特征（如三基色坐标、白点坐标、最值亮度、内容最大亮度等），在调用[OH\_PixelmapNative\_SetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_setmetadata)和[OH\_PixelmapNative\_GetMetadata](capi-pixelmap-native-h.md#oh_pixelmapnative_getmetadata)时作为[OH\_Pixelmap\_HdrMetadataValue](capi-image-nativemodule-oh-pixelmap-hdrmetadatavalue.md)的成员使用。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](capi-image-nativemodule.md)

**所在头文件：** [pixelmap\_native.h](capi-pixelmap-native-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float displayPrimariesX[3] | 归一化后显示设备三基色的X坐标。数组的长度为3，按R、G、B顺序存储，以0.00002为单位，取值范围是[0.0, 0.99998]。 |
| float displayPrimariesY[3] | 归一化后显示设备三基色的Y坐标。数组的长度为3，按R、G、B顺序存储，以0.00002为单位，取值范围是[0.0, 0.99998]。 |
| float whitePointX | 归一化后白点值的X坐标。以0.00002为单位，取值范围是[0.0, 0.99998]。 |
| float whitePointY | 归一化后白点值的Y坐标。以0.00002为单位，取值范围是[0.0, 0.99998]。 |
| float maxLuminance | 图像主监视器的最大亮度。以1为单位，取值范围是[0, 65535]。单位：尼特（nit）。 |
| float minLuminance | 图像主监视器的最小亮度。以0.0001为单位，取值范围是[0, 6.5535]。单位：尼特（nit）。 |
| float maxContentLightLevel | 显示内容的最大亮度。以1为单位，取值范围是[0, 65535]。单位：尼特（nit）。 |
| float maxFrameAverageLightLevel | 显示内容的最大平均亮度。以1为单位，取值范围是[0, 65535]。单位：尼特（nit）。 |
