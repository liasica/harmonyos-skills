---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkexternalformatohos
title: VkExternalFormatOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkExternalFormatOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c6fbdfb33db95667c17f2ac9cd3e8eabc6c18343ad1bdf442977b239eda001e0
---

```
1. typedef struct VkExternalFormatOHOS {...} VkExternalFormatOHOS
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
