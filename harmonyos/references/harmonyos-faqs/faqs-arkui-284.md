---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-284
title: struct和class的区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > struct和class的区别是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f3b9fd973d5952baa930b4f8cd83b4ff2b4e2b9d801702a5cc595a25b15136f8
---

在ArkUI框架中，struct只在自定义组件中使用，@Component装饰的struct构成的自定义组件实例，与class生成的实例具有不同的类型特性。如果开发者需要使用组件作为参数在组件之间传递，可以使用[自定义占位节点](../harmonyos-guides/arkts-user-defined-place-holder.md)。
