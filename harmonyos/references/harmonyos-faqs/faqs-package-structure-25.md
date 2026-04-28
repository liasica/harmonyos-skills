---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-25
title: 在HAP中调用createModuleContext方法获取的Context是什么层级
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 在HAP中调用createModuleContext方法获取的Context是什么层级
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1bcbcc12958791b2f2369847d39783a92ea1b86ca5e21e205ed4695c36618f65
---

1. createModuleContext获取的是基类Context，主要用于根据不同的模块名获取相应的Context，这些Context分别指向不同的HSP。
2. HSP是一个动态共享包，包含静态资源，但本身没有上下文概念。因此，需要通过创建Context来获取资源或Module的信息。
3. createModuleContext获取的是模块级的Context，不是ApplicationContext。

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)
