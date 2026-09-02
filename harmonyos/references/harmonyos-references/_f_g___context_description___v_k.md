---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___context_description___v_k
title: FG_ContextDescription_VK
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_ContextDescription_VK
category: harmonyos-references
scraped_at: 2026-09-02T15:02:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6f61200c84554366336ce288462d76ac5e1a9e832bed0428f4a1547bdcf59821
---

## 概述

此结构体描述创建超帧上下文实例[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)所需的属性信息，该接口仅适配Vulkan图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_vk.h](frame__generation__vk_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkInstance [vkInstance](_f_g___context_description___v_k.md#vkinstance) | Vulkan实例，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| VkPhysicalDevice [vkPhysicalDevice](_f_g___context_description___v_k.md#vkphysicaldevice) | Vulkan物理设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| VkDevice [vkDevice](_f_g___context_description___v_k.md#vkdevice) | Vulkan逻辑设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。 |
| uint8\_t [framesInFlight](_f_g___context_description___v_k.md#framesinflight) | 设置并行渲染图像数。例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1；如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。超出取值范围返回FG\_INVALID\_PARAMETER错误码。  取值范围：[1, 2]。 |
| PFN\_vkGetInstanceProcAddr [fnVulkanLoaderFunction](_f_g___context_description___v_k.md#fnvulkanloaderfunction) | 指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。 |

## 结构体成员变量说明

### fnVulkanLoaderFunction

```c
PFN_vkGetInstanceProcAddr FG_ContextDescription_VK::fnVulkanLoaderFunction
```

**描述**

指向Vulkan的vkGetInstanceProcAddr的函数指针，不允许设置为空。

### framesInFlight

```c
uint8_t FG_ContextDescription_VK::framesInFlight
```

**描述**

设置并行渲染图像数。 例如，如果下一帧图像需要等待上一帧图像送显后再进行渲染，则framesInFlight应设置为1； 如果上一帧图像送显的同时，下一帧图像已经在进行渲染，则framesInFlight应设置为2。注意：framesInFlight不允许设置成0。超出取值范围返回FG\_INVALID\_PARAMETER错误码。

### vkDevice

```c
VkDevice FG_ContextDescription_VK::vkDevice
```

**描述**

Vulkan逻辑设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。

### vkInstance

```c
VkInstance FG_ContextDescription_VK::vkInstance
```

**描述**

Vulkan实例，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。

### vkPhysicalDevice

```c
VkPhysicalDevice FG_ContextDescription_VK::vkPhysicalDevice
```

**描述**

Vulkan物理设备句柄，需在[FG\_Context\_VK](_graphics_accelerate.md#fg_context_vk)的整个生命周期内有效。
