---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-262
title: 如何使用Navigation的navPathStack参数
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何使用Navigation的navPathStack参数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b53c9ebb05676614326183043ded31b231f2f2a21a9f23a49f650d96a7514401
---

在已通过navPathStack获取到NavDestination集合后，可通过以下方法查询参数：

* 使用[getParamByIndex](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)获取指定索引的NavDestination页面的参数信息；
* 使用[getParamByName](../harmonyos-references/ts-basic-components-navigation.md#getparambyname10)获取所有名为name的NavDestination页面的参数信息。

**参考链接**

[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)
