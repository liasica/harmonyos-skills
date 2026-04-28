---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-463
title: customDialog里面页面跳转后，页面显示在弹窗下面，怎么调整
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > customDialog里面页面跳转后，页面显示在弹窗下面，怎么调整
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:02+08:00
doc_updated_at: 2026-04-27
content_hash: sha256:5ad50179f6ffe29f6f024665cc85b93ed98dd746705780f18c2802c9dad6fdb5
---

**解决措施**

当前ArkUI弹出框默认为非页面级弹出框。在页面路由跳转时若未主动调用close方法，弹出框将不会自动关闭。若需实现在跳转页面时覆盖弹出框的场景，可以使用组件导航子页面显示类型的弹窗类型（适用于需要保持导航栈关系的场景）或者页面级弹出框（适用于需要全屏模态覆盖的场景）。

**参考链接**

[页面显示类型](../harmonyos-guides/arkts-navigation-navdestination.md#页面显示类型)

[页面级弹出框](../harmonyos-guides/arkts-embedded-dialog.md)
