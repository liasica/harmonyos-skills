---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-adaptive-vrs-8h
title: xeg_vulkan_adaptive_vrs.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_adaptive_vrs.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ee3ba197c188d3d797c3fcf58aecc9ad6bd6f217b6a051e46a65b1e316be736
---

## 概述

PhonePC/2in1TabletTV

XEngine Adaptive VRS特性Vulkan接口。使用此头文件的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_adaptive\_vrs.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) | 此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| struct [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)) | [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)的句柄。 |
| typedef struct [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) XEG\_AdaptiveVRSCreateInfo | 此结构体描述创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的参数信息，当结构体中的信息变化时，需要创建新的[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| typedef struct [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) XEG\_AdaptiveVRSDescription | 此结构体描述下发绘制着色率纹理命令需要的参数信息，每一帧都需要进行更新。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_createadaptivevrs)) (VkDevice device, const [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) \*pXegAdaptiveVRS) | 创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdDispatchAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_cmddispatchadaptivevrs)) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) \*pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyAdaptiveVRS](xengine-kit-xengine.md#pfn_hms_xeg_destroyadaptivevrs)) ([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS) | 销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_createadaptivevrs) (VkDevice device, [XEG\_AdaptiveVRSCreateInfo](xengine-kit-xeg-adaptivevrscreateinfo.md) \*pXegAdaptiveVRSCreateInfo, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) \*pXegAdaptiveVRS) | 创建[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdDispatchAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_cmddispatchadaptivevrs) (VkCommandBuffer commandBuffer, [XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS, [XEG\_AdaptiveVRSDescription](xengine-kit-xeg-adaptivevrsdescription.md) \*pXegAdaptiveVRSDescription) | 执行计算自适应可变着色率命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_destroyadaptivevrs) ([XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs) xegAdaptiveVRS) | 销毁[XEG\_AdaptiveVRS](xengine-kit-xengine.md#xeg_adaptivevrs)对象。 |
