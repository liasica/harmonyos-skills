---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-438
title: Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:85d921931804fc2cb850cc6df3506be6ccb035aa6b67227e337c99f140dbd1d7
---

开发者可设置NavPathStack上的接口[disableAnimation](../harmonyos-references/ts-basic-components-navigation.md#disableanimation11)为true来关闭路由的跳转动画，disableAnimation同时控制removeByName等路由操作的动画开关。示例代码如下：

```
1. this.pageStack.disableAnimation(true);
```
