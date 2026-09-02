---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h
title: xeg_vulkan_extension.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_extension.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1b0328d1c189eb7030c01c736a9daf2296d0d92284f1bd942a3cb0e9c3b9d256
---

## 概述

XEngine扩展特性查询接口（Vulkan）。

**引用文件**：<xengine/xeg\_vulkan\_extension.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [XEG\_MAX\_EXTENSION\_NAME\_SIZE](xengine-kit-xengine.md#xeg_max_extension_name_size) 256 | XEngine扩展特性名称支持的最大长度。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) XEG\_ExtensionProperties | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#pfn_hms_xeg_enumeratedeviceextensionproperties)) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) \*pProperties) | XEngine Vulkan扩展特性查询接口函数指针定义。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](xengine-kit-xeg-extensionproperties.md) \*pProperties) | XEngine Vulkan扩展特性查询接口。 |
