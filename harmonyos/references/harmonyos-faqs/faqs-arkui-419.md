---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-419
title: Navigation页面接收参数一般推荐在什么生命周期接收
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation页面接收参数一般推荐在什么生命周期接收
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:12ea1022fe8caf3f03325618a679bdf66c71663c3f889ab049b2791e6cd62ec5
---

* 页面新创建时，推荐在NavDestination的[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)生命周期中处理参数。
* API18及以下版本，单实例跳转场景需要开发者自行管理参数。
* 当同时实现onReady和onNewParam时，API version 9及以上版本会优先触发[onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)回调。
