---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-neuralupscaledescription
title: XEG_NeuralUpscaleDescription
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_NeuralUpscaleDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eb7c8ef2519351a2d374cbe2ab7b3940119307408d7da10dd3adf4e8fc37fc6e
---

## 概述

此结构体描述下发空域AI超分渲染命令时需要的图像信息。

**起始版本：** 26.0.0

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_neural\_upscale.h](xengine-kit-xeg-vulkan-neural-upscale-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-neuralupscaledescription.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NEURAL\_UPSCALE\_DESCRIPTION。 |
| const void \* [pNext](xengine-kit-xeg-neuralupscaledescription.md#pnext) | 指向扩展结构的指针。若无扩展结构，应设为nullptr。 |
| VkImageView [inputImage](xengine-kit-xeg-neuralupscaledescription.md#inputimage) | 超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现渲染失败、程序崩溃等问题。 |
| VkImageView [outputImage](xengine-kit-xeg-neuralupscaledescription.md#outputimage) | 超分输出图像的VkImageView，需要是有效的VkImageView，且格式必须是[XEG\_NeuralUpscaleCreateInfo::outputFormat](xengine-kit-xeg-neuralupscalecreateinfo.md#outputformat)指定的格式，否则会出现未定义行为，如渲染失败、程序崩溃等问题。 |
| float [sharpness](xengine-kit-xeg-neuralupscaledescription.md#sharpness) | 超分的锐化参数，建议取值范围为[0.0, 1.0]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。 |

## 结构体成员变量说明

### sType

```cpp
XEG_StructureType XEG_NeuralUpscaleDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NEURAL\_UPSCALE\_DESCRIPTION。

### pNext

```cpp
const void* XEG_NeuralUpscaleDescription::pNext
```

**描述**

指向扩展结构的指针。若无扩展结构，应设为nullptr。

### inputImage

```cpp
VkImageView XEG_NeuralUpscaleDescription::inputImage
```

**描述**

超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现渲染失败、程序崩溃等问题。

### outputImage

```cpp
VkImageView XEG_NeuralUpscaleDescription::outputImage
```

**描述**

超分输出图像的VkImageView，需要是有效的VkImageView，且格式必须是[XEG\_NeuralUpscaleCreateInfo::outputFormat](xengine-kit-xeg-neuralupscalecreateinfo.md#outputformat)指定的格式，否则会出现未定义行为，如渲染失败、程序崩溃等问题。

### sharpness

```cpp
float XEG_NeuralUpscaleDescription::sharpness
```

**描述**

超分的锐化参数，建议取值范围为[0.0, 1.0]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。
