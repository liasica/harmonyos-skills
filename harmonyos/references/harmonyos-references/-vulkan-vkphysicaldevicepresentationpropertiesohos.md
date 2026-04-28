---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-vulkan-vkphysicaldevicepresentationpropertiesohos
title: VkPhysicalDevicePresentationPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkPhysicalDevicePresentationPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:902d39ea56e72868e1a6cc2202ce3a783fec1f0a40bf6b1b3d7c60c15cc1e682
---

```
1. typedef struct VkPhysicalDevicePresentationPropertiesOHOS {...} VkPhysicalDevicePresentationPropertiesOHOS
```

## 概述

包含设备的显示属性的参数。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 下一级结构体指针，pNext为空或者下一级结构体指针。 |
| VkBool32 sharedImage | 共享图像标志。 |
