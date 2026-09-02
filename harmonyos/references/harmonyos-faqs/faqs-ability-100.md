---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-100
title: 如何获取当前页面对应的UIAbility名称
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何获取当前页面对应的UIAbility名称
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a26f67a1cfe71351b59e3bf352f894dd32da9732cf83a3dd4e8924179ba13e3b
---

可以通过[bundleManager](../harmonyos-references/js-apis-bundlemanager.md)的getBundleInfoForSelf()接口获取当前应用的[AbilityInfo](../harmonyos-references/js-apis-bundlemanager-abilityinfo.md)信息，其中参数bundleFlags需要包含GET\_BUNDLE\_INFO\_WITH\_HAP\_MODULE和GET\_BUNDLE\_INFO\_WITH\_ABILITY。AbilityInfo中包含当前应用的Ability名称、Bundle名称等信息。
