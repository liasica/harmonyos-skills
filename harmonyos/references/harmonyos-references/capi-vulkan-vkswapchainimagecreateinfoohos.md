---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkswapchainimagecreateinfoohos
title: VkSwapchainImageCreateInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkSwapchainImageCreateInfoOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0b9390932cbd0c9e669dd0dd0162b8b60d39bfcf183adda2afc8c6a571aa31eb
---

```
1. typedef struct VkSwapchainImageCreateInfoOHOS {...} VkSwapchainImageCreateInfoOHOS
```

## 概述

包含创建Image时必要的参数。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| VkSwapchainImageUsageFlagsOHOS usage | 交换链图像的使用标志。 |
