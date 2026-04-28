---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-7
title: 如何在可滚动的容器组件中实现曝光埋点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在可滚动的容器组件中实现曝光埋点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:01+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:164f29f5a3ea514f61159bdab999154ffe4634f3f75fcf84e203801c043c2f90
---

* 组件可见范围占比可以使用onVisibleAreaChange事件来监听[组件可见区域变化事件](../harmonyos-references/ts-universal-component-visible-area-change-event.md)。
* 在 Scroll 组件中，滚动停止时有[onScrollStop](../harmonyos-references/ts-container-scroll.md#onscrollstop9)事件，可以获取组件的滑动状态。
* 组件的布局改变可以使用onAreaChange事件来监听[组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)。
