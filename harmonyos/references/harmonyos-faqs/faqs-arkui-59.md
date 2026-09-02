---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-59
title: 弹窗组件无法进入onPageShow方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 弹窗组件无法进入onPageShow方法
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:20+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c2061833e96c0e1749cf496a1009b303769b715fd860de8ea5450d7a41fd4ace
---

自定义弹窗作为自定义组件的一种，拥有自定义组件生命周期aboutToAppear和aboutToDisappear。

onPageShow和onPageHide仅作为页面生命周期提供，@Entry修饰的自定义组件定义为页面，不适用于自定义弹窗。

**参考链接**

[自定义组件生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)
