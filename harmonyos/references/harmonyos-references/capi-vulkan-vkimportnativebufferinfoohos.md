---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkimportnativebufferinfoohos
title: VkImportNativeBufferInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkImportNativeBufferInfoOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:85373b775127fd476091b29ce6b009b7fabd7b2bd5700f9397175decb9bd893b
---

```c
typedef struct VkImportNativeBufferInfoOHOS {...} VkImportNativeBufferInfoOHOS
```

## 概述

包含了OH\_NativeBuffer结构体的指针。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针。 |
| struct [OH\_NativeBuffer](capi-vulkan-oh-nativebuffer.md)\* buffer | OH\_NativeBuffer结构体的指针。 |
