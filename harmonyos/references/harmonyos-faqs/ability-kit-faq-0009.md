---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/ability-kit-faq-0009
title: UIAbility生命周期变化订阅常见问题
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 常见问题 > UIAbility生命周期变化订阅常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:10:24+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:006e121515f50553ad8626f4a6aab747a19883a32d3673208dce9827f82b4c82
---

**Q：如何在页面中订阅UIAbility实例的生命周期变化？**

**A**：通过ApplicationContext模块提供的ApplicationContext.on()方法，可以订阅进程内UIAbility的生命周期变化。

参考链接：[监听UIAbility生命周期变化](../harmonyos-guides/application-context-stage.md#监听uiability生命周期变化)，[ApplicationContext.on](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)。
