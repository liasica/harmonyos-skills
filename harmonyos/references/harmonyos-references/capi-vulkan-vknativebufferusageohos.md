---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos
title: VkNativeBufferUsageOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferUsageOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c9fa93b2e82a056ed9d59af5e0ecfc772f60a370e17e84a6b6e1cd4907543755
---

```c
typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```

## 概述

提供HarmonyOS NativeBuffer用途的说明。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_NATIVE\_BUFFER\_USAGE\_OHOS。 |
| void\* pNext | 下一级结构体指针。 |
| uint64\_t OHOSNativeBufferUsage | NativeBuffer的用途说明。 |
