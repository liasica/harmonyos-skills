---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-407
title: Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation路由，下层页面通过什么周期方法感知上层NavDestinationMode.DIALOG的弹出以及销毁
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:47+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:818210047b8ce3f41e4f143f7f664a9a8625cf1d7aa54467689caa20ef55efbe
---

开发者可以使用observer对navDestination的生命周期进行统一管理，可参考：[on('navDestinationUpdate')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11)。

从API17开始，新增[onActive](../harmonyos-references/ts-basic-components-navdestination.md#onactive17)、[onInactive](../harmonyos-references/ts-basic-components-navdestination.md#oninactive17)生命周期，dialog销毁、弹出时会分别触发下层页面的onActive、onInactive生命周期。
