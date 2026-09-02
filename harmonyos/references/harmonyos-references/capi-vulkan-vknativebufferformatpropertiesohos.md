---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferformatpropertiesohos
title: VkNativeBufferFormatPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferFormatPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-09-02T15:03:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1ff44d5d3782d2b4ac8e26fcb5fad90199b06b1489073de8bea1b8ed740ff159
---

```c
typedef struct VkNativeBufferFormatPropertiesOHOS {...} VkNativeBufferFormatPropertiesOHOS
```

## 概述

包含了NativeBuffer的一些格式属性。

**起始版本：** 10

**相关模块：** [Vulkan](capi-vulkan.md)

**所在头文件：** [vulkan\_ohos.h](capi-vulkan-ohos-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| VkStructureType sType | 结构体类型。 |
| void\* pNext | 下一级结构体指针。 |
| VkFormat format | 格式说明。 |
| uint64\_t externalFormat | 外部定义的格式标识符。 |
| VkFormatFeatureFlags formatFeatures | 描述了与externalFormat对应的能力。 |
| VkComponentMapping samplerYcbcrConversionComponents | 表示一组VkComponentSwizzle。 |
| VkSamplerYcbcrModelConversion suggestedYcbcrModel | 色彩模型。 |
| VkSamplerYcbcrRange suggestedYcbcrRange | 色彩数值范围。 |
| VkChromaLocation suggestedXChromaOffset | X色度偏移。 |
| VkChromaLocation suggestedYChromaOffset | Y色度偏移。 |
