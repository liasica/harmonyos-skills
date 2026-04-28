---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-common-8h
title: xeg_vulkan_common.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_vulkan_common.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cd589be7f1a9bc607847bd4264cc475fd013cd28079bbbd7f6351419f291b9d7
---

## 概述

PhonePC/2in1TabletTV

包含XEngine中Vulkan相关的通用类型定义。

**引用文件**：<xengine/xeg\_vulkan\_common.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype) XEG\_StructureType | XEngine结构体类型的枚举。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_CmdSetSynchronization](xengine-kit-xengine.md#pfn_hms_xeg_cmdsetsynchronization)) (VkCommandBuffer commandBuffer, const void \*xegHandle) | 设置同步信号，等待渲染结果写入指定图像的函数指针定义。使用RTGI特性时，为等待GI渲染结果到写入指定图像。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_StructureType](xengine-kit-xengine.md#xeg_structuretype) {  XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_CREATE\_INFO = 0, XEG\_STRUCTURE\_TYPE\_RT\_SHADOWAO\_DESCRIPTION = 1, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_CREATE\_INFO = 2, XEG\_STRUCTURE\_TYPE\_RT\_REFLECTION\_DESCRIPTION = 3,  XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO = 4, XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION = 5, XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO = 6, XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION = 7,  XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO = 1001, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT = 1002, XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION = 1003  } | XEngine结构体类型的枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_CmdSetSynchronization](xengine-kit-xengine.md#hms_xeg_cmdsetsynchronization) (VkCommandBuffer commandBuffer, const void \*xegHandle) | 设置同步信号，等待渲染结果写入指定图像。使用RTGI特性时，为等待GI渲染结果写入指定图像。 |
