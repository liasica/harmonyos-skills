---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-470
title: 如何去掉Tabs组件自定义tabBar的自带无障碍朗读
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何去掉Tabs组件自定义tabBar的自带无障碍朗读
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:03+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3db87d401ec4dca668697b874f89481efd205f314a4f791d4271c653a274492d
---

**问题描述**

想去掉Tabs组件自定义tabBar的自带无障碍朗读，请问如何实现。

**解决措施**

可对Tabs组件设置无障碍朗读模式属性[accessibilityGroup](../harmonyos-references/ts-universal-attributes-accessibility.md#accessibilitygroup)为true。
