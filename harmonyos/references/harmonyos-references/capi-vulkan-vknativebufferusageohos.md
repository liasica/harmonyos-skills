---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos
title: VkNativeBufferUsageOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferUsageOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:de4f678a0a2ceb2093bc03e2f060b76a2cfd2bd4431d4b05c3ade33d20b879ff
---

```
1. typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
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
