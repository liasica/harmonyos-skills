---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-49
title: AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > AppStorage是否支持线程间共享对象，如果不支持，推荐替代方案是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d83bdebb0d7f1c6346079fe8ab6ee701b17c4631c77e33a8396c438bfc06f42b
---

AppStorage 支持应用主线程中多个 UIAbility 实例之间的状态共享。AppStorage 是与 UI 相关的数据，必须在 UI 线程中运行，无法与其他线程共享。当前没有替代方案。

**参考链接**

[AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md)
