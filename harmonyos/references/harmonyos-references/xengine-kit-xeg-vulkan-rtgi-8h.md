---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h
title: xeg_vulkan_rtgi.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_rtgi.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:224c9c0ca31fe62d729b35304cac15b017d3ba1b365d0e3049f05c65bc2ab62d
---

## 概述

PhonePC/2in1TabletTV

XEngine光线追踪全局光照特性Vulkan接口，提供动态漫反射全局光照（DDGI）及神经网络全局光照（NNGI）两种特性。使用此头文件的接口前，需要先调用[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询扩展[XEG\_RTGI\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rtgi_extension_name)可用。

**引用文件**：<xengine/xeg\_vulkan\_rtgi.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_DDGIVolumeEntryParameters](xengine-kit-xeg-ddgivolumeentryparameters.md) | 此结构体描述每一个DDGI体积的必要参数。 |
| struct [XEG\_DDGICreateInfo](xengine-kit-xeg-ddgicreateinfo.md) | 此结构体描述创建具有DDGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| struct [XEG\_DDGIDescription](xengine-kit-xeg-ddgidescription.md) | 此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。 |
| struct [XEG\_NNGICreateInfo](xengine-kit-xeg-nngicreateinfo.md) | 此结构体描述创建具有NNGI特性的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| struct [XEG\_NNGIDescription](xengine-kit-xeg-nngidescription.md) | 此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)) | [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)的句柄。 |
| typedef enum [XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode) XEG\_RTGIQualityMode | 输出图像质量模式的枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateRTGI](xengine-kit-xengine.md#pfn_hms_xeg_creatertgi)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) \*pRtGI) | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyRTGI](xengine-kit-xengine.md#pfn_hms_xeg_destroyrtgi)) ([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI) | 销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRenderRTGI](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtgi)) (VkCommandBuffer commandBuffer, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI, const void \*pDescription) | 执行渲染命令的函数指针定义。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_RTGIQualityMode](xengine-kit-xengine.md#xeg_rtgiqualitymode) { XEG\_RTGI\_QUALITY\_MODE\_QUALITY = 0, XEG\_RTGI\_QUALITY\_MODE\_BALANCED = 1, XEG\_RTGI\_QUALITY\_MODE\_PERFORMANCE = 2 } | 输出图像质量模式的枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTGI](xengine-kit-xengine.md#hms_xeg_creatertgi) (VkDevice device, const void \*pCreateInfo, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) \*pRtGI) | 创建[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTGI](xengine-kit-xengine.md#hms_xeg_destroyrtgi) ([XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI) | 销毁[XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTGI](xengine-kit-xengine.md#hms_xeg_cmdrenderrtgi) (VkCommandBuffer commandBuffer, [XEG\_RTGI](xengine-kit-xengine.md#xeg_rtgi) rtGI, const void \*pDescription) | 执行渲染命令。 |
