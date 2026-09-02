---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo
title: XEG_NNGICreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_NNGICreateInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4914486e19d32fc8ab94141c4939cc0348b9adcef993c70e1c40c68a9b055588
---

## 概述

此结构体描述创建具有NNGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rtgi.h](xengine-kit-xeg-vulkan-rtgi-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| XEG\_StructureType [sType](xengine-kit-xeg-nngicreateinfo.md#stype) | 识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO。 |
| const void \* [pNext](xengine-kit-xeg-nngicreateinfo.md#pnext) | 指向扩展结构的指针。 |
| XEG\_RTGIQualityMode [qualityMode](xengine-kit-xeg-nngicreateinfo.md#qualitymode) | 输出图像的质量模式，必须为[XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode)中的枚举值。 |
| VkExtent2D [inferenceInputSize](xengine-kit-xeg-nngicreateinfo.md#inferenceinputsize) | 推理输入图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的推理输入图像的分辨率保持一致。 |
| VkExtent2D [inferenceOutputSize](xengine-kit-xeg-nngicreateinfo.md#inferenceoutputsize) | 推理输出图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。 |
| VkExtent2D [trainingSize](xengine-kit-xeg-nngicreateinfo.md#trainingsize) | 训练图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。 |

## 结构体成员变量说明

### inferenceInputSize

```cpp
VkExtent2D XEG_NNGICreateInfo::inferenceInputSize
```

**描述**

推理输入图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的推理输入图像的分辨率保持一致。

### inferenceOutputSize

```cpp
VkExtent2D XEG_NNGICreateInfo::inferenceOutputSize
```

**描述**

推理输出图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。

### pNext

```cpp
const void* XEG_NNGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

### qualityMode

```cpp
XEG_RTGIQualityMode XEG_NNGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode)中的枚举值。

### sType

```cpp
XEG_StructureType XEG_NNGICreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO。

### trainingSize

```cpp
VkExtent2D XEG_NNGICreateInfo::trainingSize
```

**描述**

训练图像的分辨率，必须与[XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。
