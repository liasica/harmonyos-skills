---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rt-reflection-8h
title: xeg_vulkan_rt_reflection.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_rt_reflection.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36ec07fad9ba15f2cd430b05b97513da4ae71c2a8d485818f1ae4e3b2ad15b97
---

## 概述

PhonePC/2in1TabletTV

XEngine RT Reflection特性接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询 [XEG\_RT\_REFLECTION\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_rt_reflection_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_rt\_reflection.h>

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
| struct [XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md) | 此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| struct [XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md) | 此结构体描述下发光线求交命令时的输入信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)) | [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)的句柄。 |
| typedef struct [XEG\_RTReflectionCreateInfo](xengine-kit-xeg-rtreflectioncreateinfo.md) XEG\_RTReflectionCreateInfo | 此结构体描述创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| typedef struct [XEG\_RTReflectionDescription](xengine-kit-xeg-rtreflectiondescription.md) XEG\_RTReflectionDescription | 此结构体描述下发光线求交命令时的输入信息。 |
| typedef VkResult(VKAPI\_ATTR \* [PFN\_HMS\_XEG\_CreateRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_creatertreflection)) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) \*pRtReflection) | 创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。 |
| typedef VkResult (VKAPI\_ATTR \*[PFN\_HMS\_XEG\_CmdRenderRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_cmdrenderrtreflection))(VkCommandBuffer commandBuffer, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection, const void \*pDescription) | 录制计算RT反射命中信息命令的函数指针定义。 |
| typedef void (VKAPI\_ATTR \*[PFN\_HMS\_XEG\_DestroyRTReflection](xengine-kit-xengine.md#pfn_hms_xeg_destroyrtreflection))([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection) | 销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateRTReflection](xengine-kit-xengine.md#hms_xeg_creatertreflection) (VkDevice device, const void \*pCreateInfo, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) \*pRtReflection) | 创建[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRenderRTReflection](xengine-kit-xengine.md#hms_xeg_cmdrenderrtreflection) (VkCommandBuffer commandBuffer, [XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection, const void \*pDescription) | 录制计算RT反射命中信息命令。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyRTReflection](xengine-kit-xengine.md#hms_xeg_destroyrtreflection) ([XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection) rtReflection) | 销毁[XEG\_RTReflection](xengine-kit-xengine.md#xeg_rtreflection)对象。 |
