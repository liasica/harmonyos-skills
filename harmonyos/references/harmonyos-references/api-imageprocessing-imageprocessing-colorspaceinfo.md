---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/api-imageprocessing-imageprocessing-colorspaceinfo
title: ImageProcessing_ColorSpaceInfo
breadcrumb: API参考 > 媒体 > Image Kit（图片处理服务） > C API > 结构体 > ImageProcessing_ColorSpaceInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:13:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:428b66e979dbb4f520ce41b257082f32dad0a031d9a86ff7fcc7b91ef7c03f8b
---

```
1. typedef struct ImageProcessing_ColorSpaceInfo {...} ImageProcessing_ColorSpaceInfo
```

## 概述

PhonePC/2in1TabletTV

色彩空间信息，用于色彩空间转换能力查询。

**参考：**

[OH\_ImageProcessing\_IsColorSpaceConversionSupported](capi-image-processing-h.md#oh_imageprocessing_iscolorspaceconversionsupported), [OH\_ImageProcessing\_IsCompositionSupported](capi-image-processing-h.md#oh_imageprocessing_iscompositionsupported), [OH\_ImageProcessing\_IsDecompositionSupported](capi-image-processing-h.md#oh_imageprocessing_isdecompositionsupported)

**起始版本：** 13

**相关模块：** [ImageProcessing](capi-imageprocessing.md)

**所在头文件：** [image\_processing\_types.h](capi-image-processing-types-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t metadataType | 定义元数据类型，参考[OH\_Pixelmap\_HdrMetadataKey](capi-pixelmap-native-h.md#oh_pixelmap_hdrmetadatakey)。 |
| int32\_t colorSpace | 定义色彩空间，参考[ColorSpaceName](capi-native-color-space-manager-h.md#colorspacename)。 |
| int32\_t pixelFormat | 定义像素格式，参考[PIXEL\_FORMAT](capi-pixelmap-native-h.md#pixel_format)。 |
