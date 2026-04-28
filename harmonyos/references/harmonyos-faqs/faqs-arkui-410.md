---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-410
title: Navigation组件，如何监听页面切换后系统动画的结束时机
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件，如何监听页面切换后系统动画的结束时机
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:48+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:4c3668436971a4b377eab0c0f6b4dba51b1761427fa72e77bded058deac64df9
---

**问题描述**

业务需要在Navigation的pop动画结束时进行操作，Navigation是否有对应的动画结束时机。

**解决措施**

Navigation进行pop操作时，退场页面会在动画结束时执行onDisappear生命周期，开发者可以在onDisappear()中进行逻辑处理。

**参考链接**

[页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)
