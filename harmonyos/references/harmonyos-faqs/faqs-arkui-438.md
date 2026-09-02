---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-438
title: Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation组件NavPathStack removeByName默认会有底部滑入滑出的动画，如何关闭动画
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6f960f6c0c18f9e763d4e7dd25a1f77712080ae481759d2dd5b546f7f97314bb
---

开发者可设置NavPathStack上的接口[disableAnimation](../harmonyos-references/ts-basic-components-navigation.md#disableanimation11)为true来关闭路由的跳转动画，disableAnimation同时控制removeByName等路由操作的动画开关。示例代码如下：

```typescript
this.pageStack.disableAnimation(true);
```
