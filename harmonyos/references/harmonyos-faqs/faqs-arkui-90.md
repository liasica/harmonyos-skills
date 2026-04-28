---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-90
title: 如何获取可滚动组件的当前滚动偏移量
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何获取可滚动组件的当前滚动偏移量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d7352d99b166bd94727b751cede043ac2bb494a4c63d4aa1bee54ee193f1899e
---

1. 可滚动组件在初始化时可设置scroller参数，绑定滚动控制器。
2. 通过控制器的currentOffset方法可获取水平和竖直方向的滚动偏移量。

**参考链接**

[Scroll](../harmonyos-references/ts-container-scroll.md)
