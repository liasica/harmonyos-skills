---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-414
title: 如何监听Navigation页面栈变化
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何监听Navigation页面栈变化
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7c41ce64b3f3dda72b4cb4ac7ab4af900e63cb8a617ee4bb90baa29454d7914a
---

通过[uiObserver.on('navDestinationSwitch')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12-1)方法，可以监听Navigation的页面切换事件，当Navigation组件发生页面跳转时触发该事件，典型场景包括页面访问统计、页面生命周期管理等。
