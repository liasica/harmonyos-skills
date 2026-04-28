---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscalecreateinfo
title: XEG_SpatialUpscaleCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_SpatialUpscaleCreateInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:16:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:89e1a3830c7302a2279068f747f39f86ac8770f12e559a34d893f106df3381a7
---

## 概述

PhonePC/2in1TabletTV

此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_spatial\_upscale.h](xengine-kit-xeg-vulkan-spatial-upscale-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VkExtent2D [inputSize](xengine-kit-xeg-spatialupscalecreateinfo.md#inputsize) | 超分输入图像的尺寸，必须与超分输入图像的VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。 |
| VkRect2D [inputRegion](xengine-kit-xeg-spatialupscalecreateinfo.md#inputregion) | 超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkExtent2D [outputSize](xengine-kit-xeg-spatialupscalecreateinfo.md#outputsize) | 超分输出图像的尺寸，必须与超分结果VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。 |
| VkRect2D [outputRegion](xengine-kit-xeg-spatialupscalecreateinfo.md#outputregion) | 超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。 |
| VkFormat [format](xengine-kit-xeg-spatialupscalecreateinfo.md#format) | 超分输入图像的格式。 |
| float [sharpness](xengine-kit-xeg-spatialupscalecreateinfo.md#sharpness) | 超分的锐化参数，建议取值范围为[0, 1]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### format

PhonePC/2in1TabletTV

```
1. VkFormat XEG_SpatialUpscaleCreateInfo::format
```

**描述**

超分输入图像的格式。

### inputRegion

PhonePC/2in1TabletTV

```
1. VkRect2D XEG_SpatialUpscaleCreateInfo::inputRegion
```

**描述**

超分输入图像的采样区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

### inputSize

PhonePC/2in1TabletTV

```
1. VkExtent2D XEG_SpatialUpscaleCreateInfo::inputSize
```

**描述**

超分输入图像的尺寸，必须与超分输入图像的VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。

### outputRegion

PhonePC/2in1TabletTV

```
1. VkRect2D XEG_SpatialUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像的绘制区域，图像超分区域参数必须大于0且小于等于图像尺寸，否则会导致渲染失败或者渲染效果不合预期，此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为图像区域的左上角点的x与y值，extent为图像区域的宽与高。

### outputSize

PhonePC/2in1TabletTV

```
1. VkExtent2D XEG_SpatialUpscaleCreateInfo::outputSize
```

**描述**

超分输出图像的尺寸，必须与超分结果VkimageView的尺寸一致，否则会导致未定义问题，如超分失败、程序崩溃等。

### sharpness

PhonePC/2in1TabletTV

```
1. float XEG_SpatialUpscaleCreateInfo::sharpness
```

**描述**

超分的锐化参数，建议取值范围为[0, 1]，不同风格图像锐化值需要调整，否则会导致过度锐化现象，如出现大量噪点。
