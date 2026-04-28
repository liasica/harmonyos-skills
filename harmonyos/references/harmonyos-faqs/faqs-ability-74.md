---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-74
title: 如何在工具类中获取Context
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何在工具类中获取Context
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e344575062d7ca38d33442e14a42a22a664d783687827d1cec2619f96e97889
---

工具类中无法直接获取Context。可以在EntryAbility中获取Context并保存至AppStorage。工具类中使用AppStorage获取Context。

**参考链接**

[AppStorage：应用全局的UI状态存储](../harmonyos-guides/arkts-appstorage.md)
