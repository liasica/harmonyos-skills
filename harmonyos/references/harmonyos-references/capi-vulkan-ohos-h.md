---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h
title: vulkan_ohos.h
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > vulkan_ohos.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1c84c14ffa1166e5cffc8781f0fad09602b14686006e95472032989ff35f10b
---

## 概述

PhonePC/2in1TabletTVWearable

定义了HarmonyOS平台扩展的Vulkan接口。

**引用文件：** <vulkan/vulkan\_ohos.h>

**库：** libvulkan.so

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [VkSurfaceCreateInfoOHOS](capi-vulkan-vksurfacecreateinfoohos.md) | VkSurfaceCreateInfoOHOS | 包含创建Vulkan Surface时必要的参数。 |
| [VkNativeBufferOHOS](capi-vulkan-vknativebufferohos.md) | VkNativeBufferOHOS | 包含本地显存的参数。 |
| [VkSwapchainImageCreateInfoOHOS](capi-vulkan-vkswapchainimagecreateinfoohos.md) | VkSwapchainImageCreateInfoOHOS | 包含创建Image时必要的参数。 |
| [VkPhysicalDevicePresentationPropertiesOHOS](-vulkan-vkphysicaldevicepresentationpropertiesohos.md) | VkPhysicalDevicePresentationPropertiesOHOS | 包含设备的显示属性的参数。 |
| [VkNativeBufferUsageOHOS](capi-vulkan-vknativebufferusageohos.md) | VkNativeBufferUsageOHOS | 提供HarmonyOS NativeBuffer用途的说明。 |
| [VkNativeBufferPropertiesOHOS](capi-vulkan-vknativebufferpropertiesohos.md) | VkNativeBufferPropertiesOHOS | 包含了NativeBuffer的属性。 |
| [VkNativeBufferFormatPropertiesOHOS](capi-vulkan-vknativebufferformatpropertiesohos.md) | VkNativeBufferFormatPropertiesOHOS | 包含了NativeBuffer的一些格式属性。 |
| [VkImportNativeBufferInfoOHOS](capi-vulkan-vkimportnativebufferinfoohos.md) | VkImportNativeBufferInfoOHOS | 包含了OH\_NativeBuffer结构体的指针。 |
| [VkMemoryGetNativeBufferInfoOHOS](capi-vulkan-vkmemorygetnativebufferinfoohos.md) | VkMemoryGetNativeBufferInfoOHOS | 用于从Vulkan内存中获取OH\_NativeBuffer。 |
| [VkExternalFormatOHOS](capi-vulkan-vkexternalformatohos.md) | VkExternalFormatOHOS | 表示外部定义的格式标识符。 |
| [NativeWindow](capi-vulkan-nativewindow.md) | OHNativeWindow | 本地窗口。 |
| [OHBufferHandle](capi-vulkan-ohbufferhandle.md) | - | 缓冲区句柄，用于对缓冲区的信息传递和获取。 |
| [OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md) | - | OH\_NativeBuffer结构体声明。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [VkSwapchainImageUsageFlagBitsOHOS](capi-vulkan-ohos-h.md#vkswapchainimageusageflagbitsohos) | VkSwapchainImageUsageFlagBitsOHOS | 图像使用标志位。 |

### 宏定义

| 名称 | 描述 |
| --- | --- |
| VK\_OHOS\_surface 1 | HarmonyOS平台Surface扩展宏定义。  **起始版本：** 10 |
| VK\_OHOS\_SURFACE\_SPEC\_VERSION 1 | HarmonyOS平台Surface扩展版本号。  **起始版本：** 10 |
| VK\_OHOS\_SURFACE\_EXTENSION\_NAME "VK\_OHOS\_surface" | HarmonyOS平台Surface扩展名。  **起始版本：** 10 |
| VK\_OHOS\_native\_buffer 1 | native\_buffer扩展宏定义。  **起始版本：** 10 |
| VK\_OHOS\_NATIVE\_BUFFER\_SPEC\_VERSION 1 | native\_buffer扩展版本号。  **起始版本：** 10 |
| VK\_OHOS\_NATIVE\_BUFFER\_EXTENSION\_NAME "VK\_OHOS\_native\_buffer" | native\_buffer扩展名。  **起始版本：** 10 |
| VK\_OHOS\_external\_memory 1 | HarmonyOS平台external\_memory扩展宏定义。  **起始版本：** 10 |
| VK\_OHOS\_EXTERNAL\_MEMORY\_SPEC\_VERSION 1 | HarmonyOS平台external\_memory扩展版本号。  **起始版本：** 10 |
| VK\_OHOS\_EXTERNAL\_MEMORY\_EXTENSION\_NAME "VK\_OHOS\_external\_memory" | HarmonyOS平台external\_memory扩展名。  **起始版本：** 10 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [VkResult (VKAPI\_PTR PFN\_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)](capi-vulkan-ohos-h.md#pfn_vkcreatesurfaceohos) | PFN\_vkCreateSurfaceOHOS | 创建Vulkan Surface的函数指针定义。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS\* pCreateInfo, const VkAllocationCallbacks\* pAllocator, VkSurfaceKHR\* pSurface)](capi-vulkan-ohos-h.md#vkcreatesurfaceohos) | - | 创建Vulkan Surface。 |
| [VkResult (VKAPI\_PTR PFN\_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH\_NativeBuffer buffer, VkNativeBufferPropertiesOHOS\* pProperties)](capi-vulkan-ohos-h.md#pfn_vkgetnativebufferpropertiesohos) | PFN\_vkGetNativeBufferPropertiesOHOS | 获取OH\_NativeBuffer属性的函数指针定义。 |
| [VkResult (VKAPI\_PTR PFN\_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS pInfo, struct OH\_NativeBuffer\*\* pBuffer)](capi-vulkan-ohos-h.md#pfn_vkgetmemorynativebufferohos) | PFN\_vkGetMemoryNativeBufferOHOS | 获取OH\_NativeBuffer的函数指针定义。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH\_NativeBuffer\* buffer, VkNativeBufferPropertiesOHOS\* pProperties)](capi-vulkan-ohos-h.md#vkgetnativebufferpropertiesohos) | - | 获取OH\_NativeBuffer属性。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS\* pInfo, struct OH\_NativeBuffer\*\* pBuffer)](capi-vulkan-ohos-h.md#vkgetmemorynativebufferohos) | - | 获取OH\_NativeBuffer。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t\* grallocUsage)](capi-vulkan-ohos-h.md#vkgetswapchaingrallocusageohos) | - | 根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](capi-vulkan-ohos-h.md#vkacquireimageohos) | - | 用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](capi-vulkan-ohos-h.md#vkqueuesignalreleaseimageohos) | - | 当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。 |
| [VkResult (VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vksetnativefencefdopenharmony) | VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony | 该接口已废弃。 |
| [typedef VkResult (VKAPI\_PTR PFN\_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkgetnativefencefdopenharmony) | VKAPI\_PTR \*PFN\_vkGetNativeFenceFdOpenHarmony | 该接口已废弃。 |
| [VkResult (VKAPI\_PTR PFN\_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64\_t grallocUsage)](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkgetswapchaingrallocusageohos) | VKAPI\_PTR \*PFN\_vkGetSwapchainGrallocUsageOHOS | 根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。 |
| [VkResult (VKAPI\_PTR \*PFN\_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkacquireimageohos) | VKAPI\_PTR \*PFN\_vkAcquireImageOHOS | 用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。 |
| [typedef VkResult (VKAPI\_PTR PFN\_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkqueuesignalreleaseimageohos) | VKAPI\_PTR \*PFN\_vkQueueSignalReleaseImageOHOS | 当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32\_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)](capi-vulkan-ohos-h.md#vksetnativefencefdopenharmony) | - | 该接口已废弃。 |
| [VKAPI\_ATTR VkResult VKAPI\_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32\_t waitSemaphoreCount, const VkSemaphore\* pWaitSemaphores, VkImage image, int32\_t\* pNativeFenceFd)](capi-vulkan-ohos-h.md#vkgetnativefencefdopenharmony) | - | 该接口已废弃。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### VkSwapchainImageUsageFlagBitsOHOS

```
1. enum VkSwapchainImageUsageFlagBitsOHOS
```

**描述**

图像使用标志位。

**起始版本：** 10

| 枚举项 | 描述 |
| --- | --- |
| VK\_SWAPCHAIN\_IMAGE\_USAGE\_SHARED\_BIT\_OHOS = 0x00000001 | 共享类型图像标志位。 |
| VK\_SWAPCHAIN\_IMAGE\_USAGE\_FLAG\_BITS\_MAX\_ENUM\_OHOS = 0x7FFFFFFF | 最大值。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### PFN\_vkCreateSurfaceOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkCreateSurfaceOHOS)(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

**描述**

创建Vulkan Surface的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkInstance instance | Vulkan实例。 |
| [const VkSurfaceCreateInfoOHOS](capi-vulkan-vksurfacecreateinfoohos.md)\* pCreateInfo | 一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。 |
| const VkAllocationCallbacks\* pAllocator | 用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。 |
| VkSurfaceKHR\* pSurface | 出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。 |

### vkCreateSurfaceOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkCreateSurfaceOHOS(VkInstance instance, const VkSurfaceCreateInfoOHOS* pCreateInfo, const VkAllocationCallbacks* pAllocator, VkSurfaceKHR* pSurface)
```

**描述**

创建Vulkan Surface。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkInstance instance | Vulkan实例。 |
| [const VkSurfaceCreateInfoOHOS](capi-vulkan-vksurfacecreateinfoohos.md)\* pCreateInfo | 一个VkSurfaceCreateInfoOHOS结构体的指针，包含创建Vulkan Surface时必要的参数。 |
| const VkAllocationCallbacks\* pAllocator | 用户自定义内存分配的回调函数，如果不需要可以传入NULL，接口会使用默认的内存分配函数。 |
| VkSurfaceKHR\* pSurface | 出参，用于接收创建的Vulkan Surface，类型为VkSurfaceKHR。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示分配VkSurfaceKHR内存失败。  返回VK\_ERROR\_SURFACE\_LOST\_KHR，表示操作NativeWindow失败。 |

### PFN\_vkGetNativeBufferPropertiesOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkGetNativeBufferPropertiesOHOS)(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

**描述**

获取OH\_NativeBuffer属性的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const [struct OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md)\* buffer | OH\_NativeBuffer结构体指针。 |
| [VkNativeBufferPropertiesOHOS](capi-vulkan-vknativebufferpropertiesohos.md)\* pProperties | 用于接收OH\_NativeBuffer属性的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。 |

### PFN\_vkGetMemoryNativeBufferOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkGetMemoryNativeBufferOHOS)(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

**描述**

获取OH\_NativeBuffer的函数指针定义。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| [const VkMemoryGetNativeBufferInfoOHOS](capi-vulkan-vkmemorygetnativebufferinfoohos.md)\* pInfo | VkMemoryGetNativeBufferInfoOHOS结构体对象。 |
| [struct OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md)\*\* pBuffer | 用于接收获取到的OH\_NativeBuffer。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，返回值为VK\_SUCCESS表示执行成功。 |

### vkGetNativeBufferPropertiesOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeBufferPropertiesOHOS(VkDevice device, const struct OH_NativeBuffer* buffer, VkNativeBufferPropertiesOHOS* pProperties)
```

**描述**

获取OH\_NativeBuffer属性。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| const [struct OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md)\* buffer | OH\_NativeBuffer结构体指针。 |
| [VkNativeBufferPropertiesOHOS](capi-vulkan-vknativebufferpropertiesohos.md)\* pProperties | 用于接收OH\_NativeBuffer属性的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_INVALID\_EXTERNAL\_HANDLE\_KHR，表示入参存在异常。  返回VK\_ERROR\_OUT\_OF\_DEVICE\_MEMORY，表示设备内存不足。 |

### vkGetMemoryNativeBufferOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkGetMemoryNativeBufferOHOS(VkDevice device, const VkMemoryGetNativeBufferInfoOHOS* pInfo, struct OH_NativeBuffer** pBuffer)
```

**描述**

获取OH\_NativeBuffer。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| [const VkMemoryGetNativeBufferInfoOHOS](capi-vulkan-vkmemorygetnativebufferinfoohos.md)\* pInfo | VkMemoryGetNativeBufferInfoOHOS结构体对象。 |
| [struct OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md)\*\* pBuffer | 用于接收获取到的OH\_NativeBuffer。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示pInfo入参异常，或获取的pBuffer异常。 |

### vkGetSwapchainGrallocUsageOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkGetSwapchainGrallocUsageOHOS(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)
```

**描述**

根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkFormat format | 图像格式。 |
| VkImageUsageFlags imageUsage | 图像使用标志。 |
| uint64\_t\* grallocUsage | 出参, 返回Gralloc(内存分配器)使用标志。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_INITIALIZATION\_FAILED，表示入参异常。 |

### VKAPI\_PTR \*PFN\_vkGetSwapchainGrallocUsageOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkGetSwapchainGrallocUsageOHOS)(VkDevice device, VkFormat format, VkImageUsageFlags imageUsage, uint64_t* grallocUsage)
```

**描述**

根据给定的Vulkan设备、图像格式和图像使用标志, 返回适当的Gralloc(内存分配器)使用标志。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkFormat format | 图像格式。 |
| VkImageUsageFlags imageUsage | 图像使用标志。 |
| uint64\_t\* grallocUsage | 出参, 返回Gralloc(内存分配器)使用标志。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_INITIALIZATION\_FAILED，表示入参异常。 |

### vkAcquireImageOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkAcquireImageOHOS(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

**描述**

用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkImage image | 要获取的Vulkan图像。 |
| int32\_t nativeFenceFd | 原生Fence的文件描述符。 |
| VkSemaphore semaphore | 表示图像可用状态的Vulkan Semaphore(信号量)。 |
| VkFence fence | 用于在图像获取完成时进行同步的Vulkan Fence。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示主机内存不足。 |

### VKAPI\_PTR \*PFN\_vkAcquireImageOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkAcquireImageOHOS)(VkDevice device, VkImage image, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

**描述**

用于获取交换链图像的所有权, 并将外部信号的Fence导入到VkSemaphore对象和VkFence对象中。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkDevice device | VkDevice对象。 |
| VkImage image | 要获取的Vulkan图像。 |
| int32\_t nativeFenceFd | 原生Fence的文件描述符。 |
| VkSemaphore semaphore | 表示图像可用状态的Vulkan Semaphore(信号量)。 |
| VkFence fence | 用于在图像获取完成时进行同步的Vulkan Fence。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示主机内存不足。 |

### vkQueueSignalReleaseImageOHOS()

PhonePC/2in1TabletTVWearable

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkQueueSignalReleaseImageOHOS(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

**描述**

当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkQueue queue | Vulkan队列的句柄。 |
| uint32\_t waitSemaphoreCount | 等待Semaphore(信号量)的数量。 |
| const VkSemaphore\* pWaitSemaphores | 指向等待Semaphore(信号量)数组的指针。 |
| VkImage image | 要释放的Vulkan图像句柄。 |
| int32\_t\* pNativeFenceFd | 指向Fence的文件描述符的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_DEVICE\_LOST，表示Vulkan设备链接丢失。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示主机内存不足。 |

### VKAPI\_PTR \*PFN\_vkQueueSignalReleaseImageOHOS()

PhonePC/2in1TabletTVWearable

```
1. typedef VkResult (VKAPI_PTR *PFN_vkQueueSignalReleaseImageOHOS)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

**描述**

当前图像使用完毕后，通过该函数向系统硬件缓冲区发出释放信号, 以便其他组件可以访问该图像。应用开发者无需使用该接口。

**系统能力：** SystemCapability.Graphic.Vulkan

**起始版本：** 10

**废弃版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| VkQueue queue | Vulkan队列的句柄。 |
| uint32\_t waitSemaphoreCount | 等待Semaphore(信号量)的数量。 |
| const VkSemaphore\* pWaitSemaphores | 指向等待Semaphore(信号量)数组的指针。 |
| images | 要释放的Vulkan图像句柄。 |
| int32\_t\* pNativeFenceFd | 指向Fence的文件描述符的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| VkResult | 返回一个VkResult类型的错误码，具体返回类型如下：  返回VK\_SUCCESS，表示执行成功。  返回VK\_ERROR\_DEVICE\_LOST，表示Vulkan设备链接丢失。  返回VK\_ERROR\_OUT\_OF\_HOST\_MEMORY，表示主机内存不足。 |

### VKAPI\_PTR \*PFN\_vkSetNativeFenceFdOpenHarmony()

```
1. typedef VkResult (VKAPI_PTR *PFN_vkSetNativeFenceFdOpenHarmony)(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

**描述**

该接口已废弃。

**起始版本：** 10

**废弃版本：** 10

**替代接口：** [PFN\_vkAcquireImageOHOS](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkacquireimageohos)

### VKAPI\_PTR \*PFN\_vkGetNativeFenceFdOpenHarmony()

```
1. typedef VkResult (VKAPI_PTR *PFN_vkGetNativeFenceFdOpenHarmony)(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

**描述**

该接口已废弃。

**起始版本：** 10

**废弃版本：** 10

**替代接口：** [PFN\_vkQueueSignalReleaseImageOHOS](capi-vulkan-ohos-h.md#vkapi_ptr-pfn_vkqueuesignalreleaseimageohos)

### vkSetNativeFenceFdOpenHarmony()

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkSetNativeFenceFdOpenHarmony(VkDevice device, int32_t nativeFenceFd, VkSemaphore semaphore, VkFence fence)
```

**描述**

该接口已废弃。

**起始版本：** 10

**废弃版本：** 10

**替代接口：** [vkAcquireImageOHOS](capi-vulkan-ohos-h.md#vkacquireimageohos)

### vkGetNativeFenceFdOpenHarmony()

```
1. VKAPI_ATTR VkResult VKAPI_CALL vkGetNativeFenceFdOpenHarmony(VkQueue queue, uint32_t waitSemaphoreCount, const VkSemaphore* pWaitSemaphores, VkImage image, int32_t* pNativeFenceFd)
```

**描述**

该接口已废弃。

**起始版本：** 10

**废弃版本：** 10

**替代接口：** [vkQueueSignalReleaseImageOHOS](capi-vulkan-ohos-h.md#vkqueuesignalreleaseimageohos)
