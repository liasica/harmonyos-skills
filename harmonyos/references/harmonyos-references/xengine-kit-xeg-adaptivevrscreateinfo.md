---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-adaptivevrscreateinfo
title: XEG_AdaptiveVRSCreateInfo
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_AdaptiveVRSCreateInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:29da32db263a3dbc034af710f1e32be52a135b76ca95aecfd30581ff0766a1bc
---

## 概述

此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_adaptive\_vrs.h](xengine-kit-xeg-vulkan-adaptive-vrs-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkExtent2D [inputSize](xengine-kit-xeg-adaptivevrscreateinfo.md#inputsize) | 上一帧渲染管线最终渲染的图像尺寸。 |
| VkRect2D [inputRegion](xengine-kit-xeg-adaptivevrscreateinfo.md#inputregion) | 上一帧渲染管线最终渲染的图像区域。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为渲染图像区域的左上角点的x与y值，extent为渲染图像区域的宽与高。 |
| int32\_t [adaptiveTileSize](xengine-kit-xeg-adaptivevrscreateinfo.md#adaptivetilesize) | 自适应VRS(Variable Rate Shading，可变速率着色)的渲染的分片大小，分片大的情况下性能会更好，但是画质会劣化。当前自适应VRS支持16和8两种规格。 |
| float [errorSensitivity](xengine-kit-xeg-adaptivevrscreateinfo.md#errorsensitivity) | 控制最终生成着色率纹理结果的阈值。该值越大，平均着色率越小，即性能更好但画质会劣化。取值范围为[0.0, 1.0]。 |
| bool [flip](xengine-kit-xeg-adaptivevrscreateinfo.md#flip) | 是否执行图像上下翻转。true表示进行图像上下翻转，false表示不进行图像上下翻转。 |

## 结构体成员变量说明

### adaptiveTileSize

```cpp
int32_t XEG_AdaptiveVRSCreateInfo::adaptiveTileSize
```

**描述**

自适应VRS（Variable Rate Shading，可变速率着色）的渲染的分片大小，分片大的情况下性能会更好，但是画质会劣化。当前自适应VRS支持16和8两种规格。

### errorSensitivity

```cpp
float XEG_AdaptiveVRSCreateInfo::errorSensitivity
```

**描述**

控制最终生成着色率纹理结果的阈值。该值越大，平均着色率越小，即性能更好但画质会劣化。取值范围为[0.0, 1.0]。

### flip

```cpp
bool XEG_AdaptiveVRSCreateInfo::flip
```

**描述**

是否执行图像上下翻转。true表示进行图像上下翻转，false表示不进行图像上下翻转。

### inputRegion

```cpp
VkRect2D XEG_AdaptiveVRSCreateInfo::inputRegion
```

**描述**

上一帧渲染管线最终渲染的图像区域。此参数存在两个结构体：VkOffset2D offset和VkExtent2D extent。其中offset为渲染图像区域的左上角点的x与y值，extent为渲染图像区域的宽与高。

### inputSize

```cpp
VkExtent2D XEG_AdaptiveVRSCreateInfo::inputSize
```

**描述**

上一帧渲染管线最终渲染的图像尺寸。
