---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-94
title: 如果有多个UIAbility，如何判断应用进入后台
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如果有多个UIAbility，如何判断应用进入后台
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:50+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:8f8f73d7a220d68ce0864cc50b76ce16540a21756aeb2e4c60298e3a5ed7c9e3
---

在多UIAbility情况下，只有当所有UIAbility均在后台时，应用才处于后台状态。

可以使用[ApplicationContext.on('abilityLifecycle')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonabilitylifecycle)接口，该方法第一个参数为'abilityLifecycle'类型，表示应用内UIAbility的生命周期，第二个参数为一个回调函数，可以监听应用前后台切换状态。
