---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrsdescription
title: XEG_AdaptiveVRSDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_AdaptiveVRSDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:274e3f5bd218165c98a97d98ca0b09eba4a55a2398e7546cdcef96ee5bc5b611
---

## 概述

此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_adaptive\_vrs.h](xengine-kit-xeg-vulkan-adaptive-vrs-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float \* [reprojectionMatrix](xengine-kit-xeg-adaptivevrsdescription.md#reprojectionmatrix) | 此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵\*上一帧的观察矩阵）\*（（当前帧的投影矩阵\*当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。此参数可以设为空指针。 |
| VkImageView [inputColorImage](xengine-kit-xeg-adaptivevrsdescription.md#inputcolorimage) | 上一帧渲染管线最终渲染结果颜色附件的VkImageView。 |
| VkImageView [inputDepthImage](xengine-kit-xeg-adaptivevrsdescription.md#inputdepthimage) | 当前帧渲染管线深度附件的VkImageView。 |
| VkImageView [outputShadingRateImage](xengine-kit-xeg-adaptivevrsdescription.md#outputshadingrateimage) | 准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。 |

**说明** 

对创建VkImageView的VkImage对象有以下约束：

imageType = VK\_IMAGE\_TYPE\_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

## 结构体成员变量说明

### inputColorImage

```cpp
VkImageView XEG_AdaptiveVRSDescription::inputColorImage
```

**描述**

上一帧渲染管线最终渲染结果颜色附件的VkImageView。

### inputDepthImage

```cpp
VkImageView XEG_AdaptiveVRSDescription::inputDepthImage
```

**描述**

当前帧渲染管线深度附件的VkImageView。

### outputShadingRateImage

```cpp
VkImageView XEG_AdaptiveVRSDescription::outputShadingRateImage
```

**描述**

准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。

### reprojectionMatrix

```cpp
float* XEG_AdaptiveVRSDescription::reprojectionMatrix
```

**描述**

此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵\*上一帧的观察矩阵）\*（（当前帧的投影矩阵\*当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。此参数可以设为空指针。
