---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-118
title: UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > UIContext与Ability的关系，列举常见UIContext、Ability、UIAbilityContext的关系
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:55c256b9c195e0e4d61661cae0139da4c9c48b7224aeaac98a13d8b94497525d
---

1. Ability的上下文是AbilityContext。ArkUI实例的上下文是[UIContext](../harmonyos-guides/arkts-global-interface.md)，由窗口创建并管理所有UI对象。窗口可以通过[windowStage.loadContent](../harmonyos-references/arkts-apis-window-window.md#loadcontent9)拉起ArkUI实例。
2. Ability是应用管理生命周期的对象，持有window对象。
3. UIAbility的上下文是UIAbilityContext。UIContext与UIAbilityContext没有直接联系，无法互相转化。
