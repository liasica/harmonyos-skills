---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-420
title: Navigation页面参数如何管理？如：传递参数、参数返回、参数获取
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation页面参数如何管理？如：传递参数、参数返回、参数获取
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:51+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:60ff05e17adc4c1c918c3e575e20b87a5bdd3ea993bca30001dd335d81272bf6
---

* 传递参数：
  1. Navigation路由跳转api（[页面跳转](../harmonyos-guides/arkts-routing.md#页面跳转)相关接口：pushPath、pushPathByName、pushDestination和pushDestinationByName）支持参数传递，开发者可直接使用相关接口进行传参。
  2. 开发者可通过AppStorage自行管理参数。例如：在跳转发生时存参数，并通知目标页面取用参数。
* 接收参数-push场景下：
  1. 页面新创建时，推荐在NavDestination的[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)生命周期中处理参数。
  2. API18及以下版本，单实例跳转场景需要开发者自行管理参数。例如，通过appStorage来保存、取用路由参数。
  3. 自API19起，开发者可以在NavDestination的[onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)回调中处理单实例跳转的参数。
* pop返回场景下：
  1. 自API15起，推荐开发者使用[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)处理返回场景的路由参数。
