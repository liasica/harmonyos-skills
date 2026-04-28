---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-305
title: 如何通过路由的方式打开半屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何通过路由的方式打开半屏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:17+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:87bc89c6394308e5ab4938d5d9ab9672af8c6f42cedb1d726f7db1117f7c24ff
---

统一使用导航组件（Navigation）进行操作，组件导航中参考页面显示类型的弹窗类型为 NavDestinationMode.DIALOG，DIALOG默认透明，进出路由栈不影响下层NavDestination的生命周期。

**参考链接**

[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)
