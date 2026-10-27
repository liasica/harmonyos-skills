---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0027
title: ForEach与LazyForEach界面不刷新问题排查
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > ForEach与LazyForEach界面不刷新问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:00+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:65409698a7fc2d477a70a0210c0bb3f200fddd2332f9acb56d1871e9944b50fc
---

**Q：使用ForEach&LazyForEach循环渲染时，会出现更改数据源时，界面不刷新的情况。如何解决？**

**A**：ForEach/LazyForEach 刷新原理：如果未提供 keyGenerator，框架会基于 item 和 index 自动生成 key。默认的键值生成函数为 `(item: T, index: number) => index + '\_\_' + JSON.stringify(item)`。修改状态变量数据源时，ForEach 或 LazyForEach 会捕捉到 key 的变化，从而通过重建组件节点来刷新。

参考链接：[LazyForEach：数据懒加载](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)、[ForEach：循环渲染](../harmonyos-guides/arkts-rendering-control-foreach.md)。
