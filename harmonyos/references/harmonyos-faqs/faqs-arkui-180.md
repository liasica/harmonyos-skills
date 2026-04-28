---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-180
title: 子组件事件能否传递到父组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 子组件事件能否传递到父组件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:47+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:54872f04ad03aad2a3339652861703d7633ceced11a9c35239d0664355bffad5
---

ArkUI目前不支持直接的事件传递链机制。可以通过状态同步@Link或@Provide和@Consume进行父子组件间的状态通知，结合@Watch将状态变量的修改在组件间传递，实现类似功能。

**参考链接**

[@Link装饰器：父子双向同步](../harmonyos-guides/arkts-link.md)

[@Provide装饰器和@Consume装饰器：与后代组件双向同步](../harmonyos-guides/arkts-provide-and-consume.md)

[@Watch装饰器：状态变量更改通知](../harmonyos-guides/arkts-watch.md)
