---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-80
title: ArkTS是否支持解构
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持解构
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:05+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:9931e7642c021964ff9c77cc413f3adf93e7ef99c243c3a9701a178d1a445700
---

ArkTS是静态类型语言，不支持解构。解构是基于结构兼容性的动态特性，要求解构声明中的名称与解构对象的属性名称一致。

* 不支持解构赋值：ArkTS不支持解构赋值，可使用其他方法替代，如使用临时变量。
* 不支持解构变量声明：解构声明中的名称必须与被解构对象的属性名称一致。
* 不支持参数解构的函数声明：ArkTS要求实参直接传递给函数，并映射到形参。

**参考链接**

[从TypeScript到ArkTS的适配规则](../harmonyos-guides/typescript-to-arkts-migration-guide.md)
