---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscalecreateinfo
title: XEG_TemporalUpscaleCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_TemporalUpscaleCreateInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b72b42c98bf622b0940fcd12e2619bb20fda0e3e433a51e9753229ba0d2d1e77
---

## 概述

此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_temporal\_upscale.h](xengine-kit-xeg-vulkan-temporal-upscale-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkExtent2D [inputSize](xengine-kit-xeg-temporalupscalecreateinfo.md#inputsize) | 输入图像的尺寸。支持的最大尺寸为2048 \* 1024。 |
| VkExtent2D [outputSize](xengine-kit-xeg-temporalupscalecreateinfo.md#outputsize) | 输出图像的尺寸。 |
| VkRect2D [outputRegion](xengine-kit-xeg-temporalupscalecreateinfo.md#outputregion) | 超分输出图像区域。 |
| VkFormat [outputFormat](xengine-kit-xeg-temporalupscalecreateinfo.md#outputformat) | 输出图像的格式。 |
| int [jitterNum](xengine-kit-xeg-temporalupscalecreateinfo.md#jitternum) | 相机抖动的周期数，取值范围为[4, 16]，如果该值不在范围内，则创建操作将失败，并返回错误代码VK\_ERROR\_VALIDATION\_FAILED\_EXT，推荐8。 |
| bool [isDepthReversed](xengine-kit-xeg-temporalupscalecreateinfo.md#isdepthreversed) | 是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。 |

## 结构体成员变量说明

### inputSize

```cpp
VkExtent2D XEG_TemporalUpscaleCreateInfo::inputSize
```

**描述**

输入图像的尺寸。支持的最大尺寸为2048 \* 1024。

### isDepthReversed

```cpp
bool XEG_TemporalUpscaleCreateInfo::isDepthReversed
```

**描述**

是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。

### jitterNum

```cpp
int XEG_TemporalUpscaleCreateInfo::jitterNum
```

**描述**

相机抖动的周期数，取值范围为[4, 16]，如果该值不在范围内，则创建操作将失败，并返回错误代码VK\_ERROR\_VALIDATION\_FAILED\_EXT，推荐8。

### outputFormat

```cpp
VkFormat XEG_TemporalUpscaleCreateInfo::outputFormat
```

**描述**

输出图像的格式。

### outputRegion

```cpp
VkRect2D XEG_TemporalUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像区域。

### outputSize

```cpp
VkExtent2D XEG_TemporalUpscaleCreateInfo::outputSize
```

**描述**

输出图像的尺寸。
