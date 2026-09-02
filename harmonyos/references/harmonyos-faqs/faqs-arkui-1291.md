---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1291
title: ForEach和LazyForEach的区别
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ForEach和LazyForEach的区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e5d4cb4a2eb1f653aa4f9a5719e23a4a80ed8149d71be9611b7ba088773602b1
---

## 问题现象

ForEach和LazyForEach有什么区别，在具体场景下应该怎么选择？

## 背景知识

* [ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)：ForEach接口基于数组循环渲染，需要与容器组件配合使用，且接口返回的组件应当是允许包含在ForEach父容器组件中的子组件。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)：LazyForEach从数据源中按需迭代数据，并在每次迭代时创建相应组件。

## 解决方案

ForEach和LazyForEach是两种不同的迭代模式，核心区别在于执行时机和数据处理方式。以下从多个维度对比两者的差异，并分析各自的适用场景。

* ForEach的适用场景。
  + 场景一：小数据集遍历。场景描述： 处理一个长度为100的列表（无需担心内存问题）。
  + 场景二：需要频繁快速交互的组件。场景描述： 需要频繁快速跳转、定位到某个位置，全量渲染的组件响应更快。
* LazyForEach的适用场景。
  + 场景一：大数据集处理。场景描述： 数据量特别大的列表，避免一次性加载全量数据造成卡顿。
  + 场景二：流式数据（如实时数据流）。场景描述： 分页加载的实时数据，或实时推送的新数据（如聊天消息）等。

## 常见FAQ

Q：ForEach遍历大概25000条数据，耗时2秒多，导致页面卡住，如何解决？

A：在初始化渲染时，ForEach会加载数据源的所有数据，导致页面卡顿。如果数据源非常大或有特定的性能需求，建议使用[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)。LazyForEach从提供的数据源中按需迭代数据，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会进行组件销毁回收以降低内存占用。

## 总结

| 场景类型 | ForEach | LazyForEach |
| --- | --- | --- |
| 小数据量列表 | 推荐 | 不推荐（无性能优势） |
| 大数据量列表 | 不推荐（容易造成滚动卡顿） | 推荐 |
| 静态数据（很少更新） | 推荐 | 不推荐（没有性能优势） |
| 动态数据（频繁更新） | 不推荐（每次更新需渲染所有项，性能很差） | 推荐 |
| 需要频繁交互、跳转的列表 | 推荐 | 不推荐（频繁跳转频繁渲染，生命周期不稳定且浪费资源） |
