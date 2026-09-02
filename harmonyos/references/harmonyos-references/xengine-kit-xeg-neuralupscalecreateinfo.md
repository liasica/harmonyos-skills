---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-neuralupscalecreateinfo
title: XEG_NeuralUpscaleCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_NeuralUpscaleCreateInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:437484b95ea01daf8b72f7bb82aca4785addcb2ddc10289a619106a74cb7120c
---

## 概述

此结构体描述创建[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象。

**起始版本：** 26.0.0

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_neural\_upscale.h](xengine-kit-xeg-vulkan-neural-upscale-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-neuralupscalecreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NEURAL\_UPSCALE\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-neuralupscalecreateinfo.md#pnext) | 指向扩展结构的指针。若无扩展结构，应设为nullptr。 |
| VkExtent2D [inputSize](xengine-kit-xeg-neuralupscalecreateinfo.md#inputsize) | 超分输入图像的尺寸，必须与超分输入图像的VkImageView的尺寸一致，否则会导致超分失败、程序崩溃等问题。 |
| VkRect2D [inputRegion](xengine-kit-xeg-neuralupscalecreateinfo.md#inputregion) | 超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染效果不符合预期、渲染失败等问题。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkExtent2D [outputSize](xengine-kit-xeg-neuralupscalecreateinfo.md#outputsize) | 超分输出图像的尺寸，必须与超分结果VkImageView的尺寸一致，否则会导致超分失败、程序崩溃等问题。 |
| VkRect2D [outputRegion](xengine-kit-xeg-neuralupscalecreateinfo.md#outputregion) | 超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染效果不符合预期、渲染失败等问题。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkFormat [outputFormat](xengine-kit-xeg-neuralupscalecreateinfo.md#outputformat) | 超分输出图像的格式。 |

## 结构体成员变量说明

### sType

```cpp
XEG_StructureType XEG_NeuralUpscaleCreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NEURAL\_UPSCALE\_CREATE\_INFO。

### pNext

```cpp
const void* XEG_NeuralUpscaleCreateInfo::pNext
```

**描述**

指向扩展结构的指针。若无扩展结构，应设为nullptr。

### inputSize

```cpp
VkExtent2D XEG_NeuralUpscaleCreateInfo::inputSize
```

**描述**

超分输入图像的尺寸，必须与超分输入图像的VkImageView的尺寸一致，否则会导致超分失败、程序崩溃等问题。

### inputRegion

```cpp
VkRect2D XEG_NeuralUpscaleCreateInfo::inputRegion
```

**描述**

超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染效果不符合预期、渲染失败等问题。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

### outputSize

```cpp
VkExtent2D XEG_NeuralUpscaleCreateInfo::outputSize
```

**描述**

超分输出图像的尺寸，必须与超分结果VkImageView的尺寸一致，否则会导致超分失败、程序崩溃等问题。

### outputRegion

```cpp
VkRect2D XEG_NeuralUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染效果不符合预期、渲染失败等问题。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

### outputFormat

```cpp
VkFormat XEG_NeuralUpscaleCreateInfo::outputFormat
```

**描述**

超分输出图像的格式。
