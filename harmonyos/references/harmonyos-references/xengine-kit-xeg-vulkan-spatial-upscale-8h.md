---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-spatial-upscale-8h
title: xeg_vulkan_spatial_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_spatial_upscale.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0bd7dc49fbc002871501b0cc04d2b1decf3ee987da336a99fd0e60ad08484a6
---

## 概述

PhonePC/2in1TabletTV

XEngine空域GPU超分特性Vulkan接口。使用此头文件的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_SPATIAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_spatial_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_spatial\_upscale.h>

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
| struct [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) | 此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| struct [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) | 此结构体描述下发空域GPU超分渲染命令时需要的图像信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)) | [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)的句柄。 |
| typedef struct [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) XEG\_SpatialUpscaleCreateInfo | 此结构体描述创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| typedef struct [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) XEG\_SpatialUpscaleDescription | 此结构体描述下发空域GPU超分渲染命令时需要的图像信息。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateSpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_createspatialupscale)) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) \*pXegSpatialUpscale) | 创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderSpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderspatialupscale)) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) \*pXegSpatialUpscaleDescription) | 执行空域GPU超分渲染命令的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroySpatialUpscale](xengine-kit-xengine.md#pfn_hms_xeg_destroyspatialupscale)) ([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale) | 销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateSpatialUpscale](xengine-kit-xengine.md#hms_xeg_createspatialupscale) (VkDevice device, const [XEG\_SpatialUpscaleCreateInfo](xengine-kit-xeg-spatialupscalecreateinfo.md) \*pXegSpatialUpscaleCreateInfo, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) \*pXegSpatialUpscale) | 创建[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderSpatialUpscale](xengine-kit-xengine.md#hms_xeg_cmdrenderspatialupscale) (VkCommandBuffer commandBuffer, [XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale, [XEG\_SpatialUpscaleDescription](xengine-kit-xeg-spatialupscaledescription.md) \*pXegSpatialUpscaleDescription) | 执行空域GPU超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroySpatialUpscale](xengine-kit-xengine.md#hms_xeg_destroyspatialupscale) ([XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale) xegSpatialUpscale) | 销毁[XEG\_SpatialUpscale](xengine-kit-xengine.md#xeg_spatialupscale)对象。 |
