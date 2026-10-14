---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferohos
title: VkNativeBufferOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferOHOS
category: harmonyos-references
scraped_at: 2026-10-15T07:13:01+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:84bc0e36dd3bc9f5e5132663b50c7d3a458244614b31aaa68cd80bc3a0b2771f
---

```c
typedef struct VkNativeBufferOHOS {...} VkNativeBufferOHOS
```

## 概述

包含本地显存的参数。

**起始版本：** 10

**废弃版本：** 23

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| struct [OHBufferHandle\*](capi-vulkan-ohbufferhandle.md) handle | 显存句柄。 |
