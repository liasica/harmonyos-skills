---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferformatpropertiesohos
title: VkNativeBufferFormatPropertiesOHOS
breadcrumb: API参考 > 标准库 > Vulkan > Vulkan扩展能力 > VkNativeBufferFormatPropertiesOHOS
category: harmonyos-references
scraped_at: 2026-04-28T08:19:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:649df17789a25740b0f25c796029875a511943a78bc3999f85f6353bfc7bffc3
---

```
1. typedef struct VkNativeBufferFormatPropertiesOHOS {...} VkNativeBufferFormatPropertiesOHOS
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
