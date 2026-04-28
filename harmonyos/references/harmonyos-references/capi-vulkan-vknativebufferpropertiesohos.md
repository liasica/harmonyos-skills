---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferpropertiesohos
title: VkNativeBufferPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e9a76e46beceb9ec384508ab349d392f3d0f347f0d36b4c4d32dcdec8ec9884f
---

```
1. typedef struct VkNativeBufferPropertiesOHOS {...} VkNativeBufferPropertiesOHOS
```

## 概述

包含了NativeBuffer的属性。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| void\* pNext | 下一级结构体指针。 |
| VkDeviceSize allocationSize | 占用的内存大小。 |
| uint32\_t memoryTypeBits | 内存类型。 |
