---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferohos
title: VkNativeBufferOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c6809674bd171266a30fb026e1fb7069c59073e379a54bcdf1ac26732bbe44bd
---

```c
typedef struct VkNativeBufferOHOS {...} VkNativeBufferOHOS
```

## 概述

包含本地显存的参数。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| struct [OHBufferHandle\*](capi-vulkan-ohbufferhandle.md) handle | 显存句柄。 |
