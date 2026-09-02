---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vksurfacecreateinfoohos
title: VkSurfaceCreateInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkSurfaceCreateInfoOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7fddf73934c257d1d7e76b22c18459f0e2186048297db7a767537707c601a139
---

```c
typedef struct VkSurfaceCreateInfoOHOS {...} VkSurfaceCreateInfoOHOS
```

## 概述

包含创建Vulkan Surface时必要的参数。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_SURFACE\_CREATE\_INFO\_OHOS。 |
| const void\* pNext | 下一级结构体指针，值必须为空。 |
| VkSurfaceCreateFlagsOHOS flags | 预留的标志类型参数，值必须为0。 |
| [OHNativeWindow](capi-vulkan-nativewindow.md)\* window | OHNativeWindow指针。 |
