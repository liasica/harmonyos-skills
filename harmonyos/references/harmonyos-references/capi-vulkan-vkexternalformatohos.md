---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkexternalformatohos
title: VkExternalFormatOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkExternalFormatOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4386d605ceedca3b4b6b45fbc94f23eae77dce82cb23f6e46c05095be8a2fcd3
---

```c
typedef struct VkExternalFormatOHOS {...} VkExternalFormatOHOS
```

## 概述

表示外部定义的格式标识符。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_EXTERNAL\_FORMAT\_OHOS。 |
| void\* pNext | pNext为空或者下一级结构体指针。 |
| uint64\_t externalFormat | 外部定义的格式标识符。 |
