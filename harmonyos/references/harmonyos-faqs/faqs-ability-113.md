---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-113
title: HarmonyOS提供了两种页面加载方式，两者有何区别，怎么选择
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > HarmonyOS提供了两种页面加载方式，两者有何区别，怎么选择
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:e8cbe317b530be372123bcd2dc84b83c8e555547affe8c0c6f31fa0daea34e8c
---

**问题描述**

HarmonyOS提供了两种页面加载方式，一种是一个UIAbility绑定多个页面，页面之间可以实现跳转；另一种是一个 UIAbility 绑定一个页面，通过跳转 UIAbility 实现页面加载。请问这两种方式有什么区别？一般怎么做选择？

**解决方案**

区别：

一个UIAbility绑定多个page页面：资源占用较少，切换速度快，Page之间的跳转轻量，适用于频繁切换的场景。

一个UIAbility绑定一个page页面：资源占用较高，切换速度较慢，适用于需要独立生命周期管理的复杂业务逻辑。

选择建议

1. 功能模块化且频繁切换：
   * 选择一个UIAbility绑定多个Page页面。
   * 适用于导航栏切换、Tab页切换等场景。
2. 独立功能且生命周期管理复杂：
   * 选择一个UIAbility绑定一个Page页面。
   * 适用于独立功能模块和复杂业务逻辑等场景。
