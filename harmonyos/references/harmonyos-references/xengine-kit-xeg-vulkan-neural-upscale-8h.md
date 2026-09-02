---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-neural-upscale-8h
title: xeg_vulkan_neural_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_neural_upscale.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:40b4aa030348635de95a776ea31a56046ef52ad051658140d5e5aded9936fd62
---

## 概述

XEngine空域AI超分特性Vulkan接口。使用此头文件的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_neural_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_neural\_upscale.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 26.0.0

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_NeuralUpscaleCreateInfo](xengine-kit-xeg-neuralupscalecreateinfo.md) | 此结构体描述创建[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象。 |
| struct [XEG\_NeuralUpscaleDescription](xengine-kit-xeg-neuralupscaledescription.md) | 此结构体描述下发空域AI超分渲染命令时需要的图像信息。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)) | [XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)的句柄。 |
| typedef struct [XEG\_NeuralUpscaleCreateInfo](xengine-kit-xeg-neuralupscalecreateinfo.md) XEG\_NeuralUpscaleCreateInfo | 此结构体描述创建[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象。 |
| typedef struct [XEG\_NeuralUpscaleDescription](xengine-kit-xeg-neuralupscaledescription.md) XEG\_NeuralUpscaleDescription | 此结构体描述下发空域AI超分渲染命令时需要的图像信息。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateNeuralUpscale](xengine-kit-xengine.md#pfn_hms_xeg_createneuralupscale)) (VkDevice device, const [XEG\_NeuralUpscaleCreateInfo](xengine-kit-xeg-neuralupscalecreateinfo.md) \*pCreateInfo, [XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) \*pNeuralUpscale) | 创建[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderNeuralUpscale](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderneuralupscale)) (VkCommandBuffer commandBuffer, [XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) neuralUpscale, const [XEG\_NeuralUpscaleDescription](xengine-kit-xeg-neuralupscaledescription.md) \*pDescription) | 执行空域AI超分渲染命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyNeuralUpscale](xengine-kit-xengine.md#pfn_hms_xeg_destroyneuralupscale)) ([XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) neuralUpscale) | 销毁[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象的函数指针定义。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateNeuralUpscale](xengine-kit-xengine.md#hms_xeg_createneuralupscale)(VkDevice device, const [XEG\_NeuralUpscaleCreateInfo](xengine-kit-xeg-neuralupscalecreateinfo.md) \*pCreateInfo, [XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) \*pNeuralUpscale) | 创建[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderNeuralUpscale](xengine-kit-xengine.md#hms_xeg_cmdrenderneuralupscale)(VkCommandBuffer commandBuffer, [XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) neuralUpscale, const [XEG\_NeuralUpscaleDescription](xengine-kit-xeg-neuralupscaledescription.md) \*pDescription) | 执行空域AI超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyNeuralUpscale](xengine-kit-xengine.md#hms_xeg_destroyneuralupscale)([XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale) neuralUpscale) | 销毁[XEG\_NeuralUpscale](xengine-kit-xengine.md#xeg_neuralupscale)对象。 |
