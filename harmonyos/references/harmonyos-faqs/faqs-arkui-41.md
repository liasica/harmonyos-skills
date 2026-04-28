---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-41
title: 使用ForEach&LazyForEach循环渲染时，会出现更改数据源时，界面不刷新的情况。如何解决
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 使用ForEach&LazyForEach循环渲染时，会出现更改数据源时，界面不刷新的情况。如何解决
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:88b71a84aa35594522b9640b2fc40d8853b45970f4d50a5eff0bb1748bd624fe
---

ForEach/LazyForEach 刷新原理：如果未提供 keyGenerator，框架会基于 item 和 index 自动生成 key。默认的键值生成函数为 `(item: T, index: number) => index + '\_\_' + JSON.stringify(item)`。修改状态变量数据源时，ForEach 或 LazyForEach 会捕捉到 key 的变化，从而通过重建组件节点来刷新。

**参考链接**

[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[ForEach：循环渲染](../harmonyos-guides/arkts-rendering-control-foreach.md)
