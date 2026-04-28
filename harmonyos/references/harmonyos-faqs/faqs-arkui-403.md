---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-403
title: Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation管理的页面生命周期是什么，需要什么回调监听页面生命周期
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:46+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:fa7dd490066e55b9754cf74cd872ae8332b14870ec02534d162e16475ae0e51c
---

Navigation组件作为路由容器的实现，其生命周期承载在[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件上，以组件事件的形式开放。Navigation管理的页面生命周期包括onAppear（通用生命周期事件）、onShown（NavDestination组件布局显示之后执行）、onActive（NavDestination处于激活态触发）等等，具体可参考下方文档。可以通过[Class (UIObserver)](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)监听NavDestination组件的生命周期。

**参考链接**

[组件导航(Navigation) (推荐)](../harmonyos-guides/arkts-navigation-navigation.md)

[页面生命周期](../harmonyos-guides/arkts-navigation-navdestination.md#页面生命周期)
