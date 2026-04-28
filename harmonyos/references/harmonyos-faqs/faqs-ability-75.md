---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-75
title: ApplicationContext、UIAbilityContext、Context的区别是什么
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > ApplicationContext、UIAbilityContext、Context的区别是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a789d210bfa17ff94b02132b0a7d7b79795c8b204e9681be14b14a40fa3851b9
---

* ApplicationContext 和 UIAbilityContext 都继承自基类 Context，不同的 Context 具有不同的属性和方法。

  ApplicationContext：应用级别的Context，提供了订阅应用组件生命周期变化、系统内存变化和应用系统环境变化的能力。可以在UIAbility、ExtensionAbility、AbilityStage中获取。
* UIAbilityContext：每个UIAbility包含一个Context属性，用于操作应用组件和获取组件配置信息。

**参考链接**

[应用上下文Context](../harmonyos-guides/application-context-stage.md)
