---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-temporal-upscale-8h
title: xeg_vulkan_temporal_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_temporal_upscale.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b5e48187b1043e93b81b6277d12d0943ca234695162a8fda39901ff69dd0858
---

## 概述

PhonePC/2in1TabletTV

XEngine时域AI超分特性接口，推荐超分倍率为[1.25, 2.0]。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_temporal\_upscale.h>

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
| struct [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) | 此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| struct [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) | 此结构体描述下发时域AI超分渲染命令时的输入信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)) | [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)的句柄。 |
| typedef struct [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) XEG\_TemporalUpscaleCreateInfo | 此结构体描述创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| typedef struct [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) XEG\_TemporalUpscaleDescription | 此结构体描述下发时域AI超分渲染命令时的输入信息。 |
| typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_createtemporalupscale)) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) \*pTemporalUpscale) | 创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。 |
| typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CmdRenderTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_cmdrendertemporalupscale)) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) \*pDescription) | 录制时域AI超分渲染命令的函数指针定义。 |
| typedef void(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_DestroyTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_destroytemporalupscale)) ([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale) | 销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateTemporalUpscale](xengine-kit-xengine.md#hms_xeg_createtemporalupscale) (VkDevice device, [XEG\_TemporalUpscaleCreateInfo](xengine-kit-xeg-temporalupscalecreateinfo.md) \*pTemporalUpscaleInfo, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) \*pTemporalUpscale) | 创建[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_CmdRenderTemporalUpscale](xengine-kit-xengine.md#hms_xeg_cmdrendertemporalupscale) (VkCommandBuffer commandBuffer, [XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale, [XEG\_TemporalUpscaleDescription](xengine-kit-xeg-temporalupscaledescription.md) \*pDescription) | 录制时域AI超分渲染命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyTemporalUpscale](xengine-kit-xengine.md#hms_xeg_destroytemporalupscale) ([XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale) temporalUpscale) | 销毁[XEG\_TemporalUpscale](xengine-kit-xengine.md#xeg_temporalupscale)对象。 |
