---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-hps-8h
title: xeg_vulkan_hps.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_hps.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dd4e23e67ea57a46cc902025672e6d37ea262c9ce620282bece89aa264dfbc50
---

## 概述

PhonePC/2in1TabletTV

XEngine 高性能着色器接口。使用此头文件中的接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_vulkan\_hps.h>

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
| struct [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) | 此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。 |
| struct [XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md) | 此结构体描述HPS基数排序扩展结构信息。 |
| struct [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) | 此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VK\_DEFINE\_HANDLE([XEG\_HPS](xengine-kit-xengine.md#xeg_hps)) | [XEG\_HPS](xengine-kit-xengine.md#xeg_hps)的句柄。 |
| typedef struct [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) [XEG\_HPSCreateInfo](xengine-kit-xengine.md#xeg_hpscreateinfo) | 此结构体描述创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的信息。 |
| typedef struct [XEG\_HPSRadixSort](xengine-kit-xeg-hpsradixsort.md) [XEG\_HPSRadixSort](xengine-kit-xengine.md#xeg_hpsradixsort) | 此结构体描述HPS基数排序扩展结构信息。 |
| typedef struct [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) [XEG\_HPSRadixSortDescription](xengine-kit-xengine.md#xeg_hpsradixsortdescription) | 此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CreateHPS](xengine-kit-xengine.md#pfn_hms_xeg_createhps)) (VkDevice device, const [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) \*pCreateInfo, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) \*pHps) | 创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。 |
| typedef void(VKAPI\_PTR \* [PFN\_HMS\_XEG\_DestroyHPS](xengine-kit-xengine.md#pfn_hms_xeg_destroyhps)) ([XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps) | 销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象的函数指针定义。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdRadixSortHPS](xengine-kit-xengine.md#pfn_hms_xeg_cmdradixsorthps)) (VkCommandBuffer commandBuffer, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) \*pDescription) | 录制HPS排序命令的函数指针定义，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CreateHPS](xengine-kit-xengine.md#hms_xeg_createhps) (VkDevice device, const [XEG\_HPSCreateInfo](xengine-kit-xeg-hpscreateinfo.md) \*pCreateInfo, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) \*pHps) | 创建[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| VKAPI\_ATTR void VKAPI\_CALL [HMS\_XEG\_DestroyHPS](xengine-kit-xengine.md#hms_xeg_destroyhps) ([XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps) | 销毁[XEG\_HPS](xengine-kit-xengine.md#xeg_hps)对象。 |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdRadixSortHPS](xengine-kit-xengine.md#hms_xeg_cmdradixsorthps) (VkCommandBuffer commandBuffer, [XEG\_HPS](xengine-kit-xengine.md#xeg_hps) hps, const [XEG\_HPSRadixSortDescription](xengine-kit-xeg-hpsradixsortdescription.md) \*pDescription) | 录制HPS排序命令，使用此接口前需要通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](xengine-kit-xengine.md#hms_xeg_enumeratedeviceextensionproperties)接口查询是否支持[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_hps_radix_sort_extension_name)扩展。 |
