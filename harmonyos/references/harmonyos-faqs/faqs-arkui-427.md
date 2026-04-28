---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-427
title: Tabs如何实现TabBar左对齐
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Tabs如何实现TabBar左对齐
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fba04fc1e018e28862a88637a540025dc2f197fc5681fe0091842466c5b99f7d
---

通过[TabsOptions](../harmonyos-references/ts-container-tabs.md#tabsoptions15)的barModifier属性设置TabBar的[align](../harmonyos-references/ts-universal-attributes-location.md#align)参数，可以实现页签对齐布局效果。类似于文本对齐，开发者可以自行设置居中、居上、居下、居左或者居右对齐，在RTL布局下建议使用start/end替代left/right。具体可参考示例代码：[示例16（页签对齐布局）](../harmonyos-references/ts-container-tabs.md#示例16页签对齐布局)。
