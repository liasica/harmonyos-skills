---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-402
title: Navigation页面级弹窗，下层页面如何监听是否被Dialog覆盖
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation页面级弹窗，下层页面如何监听是否被Dialog覆盖
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:45+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:136bfe4f7aa9ad2d188c18dc22e60a14d278f3f098c34cf3d0838a2def0b8984
---

可以通过[Class (UIObserver)](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)监听[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件的生命周期。生命周期可以参考下方文档。从API17开始，新增onActive、onInactive生命周期，在Dialog弹出、销毁时会分别触发下层页面的onInactive、onActive生命周期。

**参考链接**

[页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)
