---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrsdescription
title: XEG_AdaptiveVRSDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_AdaptiveVRSDescription
category: harmonyos-references
scraped_at: 2026-04-28T08:16:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4394cd5548614b0f4ba296b6e8eaaf2e4cd527cefee534e3fc586381136f98f5
---

## 概述

PhonePC/2in1TabletTV

此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_adaptive\_vrs.h](xengine-kit-xeg-vulkan-adaptive-vrs-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| float \* [reprojectionMatrix](xengine-kit-xeg-adaptivevrsdescription.md#reprojectionmatrix) | 参数可选，参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵\*上一帧的观察矩阵）\*（（当前帧的投影矩阵\*当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。 |
| VkImageView [inputColorImage](xengine-kit-xeg-adaptivevrsdescription.md#inputcolorimage) | 上一帧渲染管线最终渲染结果颜色附件的VkImageView。 |
| VkImageView [inputDepthImage](xengine-kit-xeg-adaptivevrsdescription.md#inputdepthimage) | 当前帧渲染管线深度附件的VkImageView。 |
| VkImageView [outputShadingRateImage](xengine-kit-xeg-adaptivevrsdescription.md#outputshadingrateimage) | 准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。 |

说明

对创建VkImageView的VkImage对象有以下约束：

imageType = VK\_IMAGE\_TYPE\_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

## 结构体成员变量说明

PhonePC/2in1TabletTV

### inputColorImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_AdaptiveVRSDescription::inputColorImage
```

**描述**

上一帧渲染管线最终渲染结果颜色附件的VkImageView。

### inputDepthImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_AdaptiveVRSDescription::inputDepthImage
```

**描述**

当前帧渲染管线深度附件的VkImageView。

### outputShadingRateImage

PhonePC/2in1TabletTV

```
1. VkImageView XEG_AdaptiveVRSDescription::outputShadingRateImage
```

**描述**

准备生成着色率图信息的VkImageView，此VkImageView需要用户创建并输入。

### reprojectionMatrix

PhonePC/2in1TabletTV

```
1. float* XEG_AdaptiveVRSDescription::reprojectionMatrix
```

**描述**

参数可选，参数非空时画质更优。此参数为重投影矩阵的指针，计算公式为：（上一帧投影矩阵\*上一帧的观察矩阵）\*（（当前帧的投影矩阵\*当前帧的观察矩阵）的逆矩阵），矩阵必须是4\*4列主序的矩阵。
