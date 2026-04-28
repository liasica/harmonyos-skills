---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-222
title: @Style 和 @Extend 是否支持export导出
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > @Style 和 @Extend 是否支持export导出
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:58+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e02bf3e8fe76d70756275aaeb9667d4f97acc9521ca3c7734f59f1c57cd4b55
---

1.@Styles 和 @Extend 目前不支持 export 导出，后续这两个装饰器将不再演进。

2.推荐使用新的样式复用方法。通过attributeModifier属性动态设置组件，并通过自定义类继承基础组件的Modifier，在类中设置复用的属性，自定义类没有导出限制。然而，虽然推荐使用attributeModifier，但需注意其目前不支持事件和手势处理，这两个功能的需求正在跟踪中。

**参考链接**

[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)
