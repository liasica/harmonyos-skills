---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscaledescription
title: XEG_SpatialUpscaleDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_SpatialUpscaleDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6377c5460f3af6ae38f1d0c54af2a074373099d428ecd766e4e6e0fc9c82ce92
---

## 概述

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_spatial\_upscale.h](xengine-kit-xeg-vulkan-spatial-upscale-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkImageView [inputImage](xengine-kit-xeg-spatialupscaledescription.md#inputimage) | 超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |
| VkImageView [outputImage](xengine-kit-xeg-spatialupscaledescription.md#outputimage) | 超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |

**说明** 

对创建VkImageView的VkImage对象有以下约束：

imageType = VK\_IMAGE\_TYPE\_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

## 结构体成员变量说明

### inputImage

```cpp
VkImageView XEG_SpatialUpscaleDescription::inputImage
```

**描述**

超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。

### outputImage

```cpp
VkImageView XEG_SpatialUpscaleDescription::outputImage
```

**描述**

超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。
