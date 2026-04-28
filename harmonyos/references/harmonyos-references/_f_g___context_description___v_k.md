---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___context_description___v_k
title: FG_ContextDescription_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ContextDescription_VK
category: harmonyos-references
scraped_at: 2026-04-28T08:15:45+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:56dd7ff7c3e75e13ddfa80708e83012d5bf6f59e9c48a44a95f984fabfcb18bc
---

## 概述

PhoneTabletTV

此结构体描述创建超帧上下文实例[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)所需的属性信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](frame__generation__vk_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| VkInstance [vkInstance](_f_g___context_description___v_k.md#vkinstance) | Vulkan实例，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| VkPhysicalDevice [vkPhysicalDevice](_f_g___context_description___v_k.md#vkphysicaldevice) | Vulkan物理设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| VkDevice [vkDevice](_f_g___context_description___v_k.md#vkdevice) | Vulkan逻辑设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| uint8\_t [framesInFlight](_f_g___context_description___v_k.md#framesinflight) | 设置并行渲染图像数。例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1；如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。超出取值范围返回FG\_INVALID\_PARAMETER错误码。  取值范围：[1, 2]。 |
| PFN\_vkGetInstanceProcAddr [fnVulkanLoaderFunction](_f_g___context_description___v_k.md#fnvulkanloaderfunction) | 指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。 |

## 结构体成员变量说明

PhoneTabletTV

### fnVulkanLoaderFunction

PhoneTabletTV

```
1. PFN_vkGetInstanceProcAddr FG_ContextDescription_VK::fnVulkanLoaderFunction
```

**描述**

指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。

### framesInFlight

PhoneTabletTV

```
1. uint8_t FG_ContextDescription_VK::framesInFlight
```

**描述**

设置并行渲染图像数。 例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1； 如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。超出取值范围返回FG\_INVALID\_PARAMETER错误码。

### vkDevice

PhoneTabletTV

```
1. VkDevice FG_ContextDescription_VK::vkDevice
```

**描述**

Vulkan逻辑设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。

### vkInstance

PhoneTabletTV

```
1. VkInstance FG_ContextDescription_VK::vkInstance
```

**描述**

Vulkan实例, 需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。

### vkPhysicalDevice

PhoneTabletTV

```
1. VkPhysicalDevice FG_ContextDescription_VK::vkPhysicalDevice
```

**描述**

Vulkan物理设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。
