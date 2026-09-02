---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkphysicaldevicepresentationpropertiesohos
title: VkPhysicalDevicePresentationPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkPhysicalDevicePresentationPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:ac18b6b5046320fef338e37a55c4e1e955883d5e0a13592246ce3c44d9b027e9
---

```c
typedef struct VkPhysicalDevicePresentationPropertiesOHOS {...} VkPhysicalDevicePresentationPropertiesOHOS
```

## 概述

包含设备的显示属性的参数。

**起始版本：** 10

**废弃版本：** 23

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| void\* pNext | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| VkBool32 sharedImage | 共享图像标志。 |
