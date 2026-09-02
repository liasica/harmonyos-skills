---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-419
title: Navigation页面接收参数一般推荐在什么生命周期接收
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Navigation页面接收参数一般推荐在什么生命周期接收
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:255319630eda5bd8542a3107d169a448f18a017fa19598b333e602a618bd7baa
---

* 页面新创建时，推荐在NavDestination的[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)生命周期中处理参数。
* API18及以下版本，单实例跳转场景需要开发者自行管理参数。
* 当同时实现onReady和onNewParam时，API version 19及以上版本会优先触发[onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)回调。
