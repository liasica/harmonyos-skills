---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkswapchainimagecreateinfoohos
title: VkSwapchainImageCreateInfoOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkSwapchainImageCreateInfoOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:a4744f1ed11114873ec66e76d4e2907b0197af2994ce215b3eaf058479180cca
---

```c
typedef struct VkSwapchainImageCreateInfoOHOS {...} VkSwapchainImageCreateInfoOHOS
```

## 概述

包含创建Image时必要的参数。

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
| VkSwapchainImageUsageFlagsOHOS usage | 交换链图像的使用标志。 |
