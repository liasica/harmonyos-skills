---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkmemorygetnativebufferinfoohos
title: VkMemoryGetNativeBufferInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkMemoryGetNativeBufferInfoOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:673d51f234f071180c64c3e03117fa59e80c028cbf299bd9f292b46757931064
---

```
1. typedef struct VkMemoryGetNativeBufferInfoOHOS {...} VkMemoryGetNativeBufferInfoOHOS
```

## 概述

用于从Vulkan内存中获取OH\_NativeBuffer。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_MEMORY\_GET\_NATIVE\_BUFFER\_INFO\_OHOS。 |
| const void\* pNext | 下一级结构体指针，值必须为空。 |
| VkDeviceMemory memory | VkDeviceMemory对象，值必须为一个有效的VkDeviceMemory对象。 |
