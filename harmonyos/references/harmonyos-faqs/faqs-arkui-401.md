---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-401
title: 如何监听Navigation页面的生命周期
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听Navigation页面的生命周期
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:45+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:fadada479020d81d06c7a853f55e5eee6358cf4e5996362f7ec8aec1fcd6efc7
---

[Navigation](../harmonyos-guides/arkts-navigation-navigation.md)作为路由容器，其生命周期承载在[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件上，以组件事件的形式开放。可以通过[Class (UIObserver)](../harmonyos-references/arkts-apis-uicontext-uiobserver.md)监听NavDestination组件的生命周期。具体方式可以参考[页面监听和查询](../harmonyos-guides/arkts-navigation-navdestination.md#页面监听和查询)。
