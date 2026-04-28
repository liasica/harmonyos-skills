---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-324
title: WaterFlow、Grid、List这些容器的使用区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > WaterFlow、Grid、List这些容器的使用区别是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6e6d42f96f5c79e1de9ea2ab25129e9c4c61e2749f7d3545338386ac87164c35
---

[WaterFlow](../harmonyos-references/ts-container-waterflow.md)适用于高度不固定的多列瀑布流布局。

[Grid](../harmonyos-references/ts-container-grid.md)专为网格布局优化，而[List](../harmonyos-references/ts-container-list.md)的[lanes](../harmonyos-references/ts-container-list.md#lanes9)属性仅提供基础多列支持，也能实现类似网格布局的效果，但是Grid组件对item的拖拽支持更好。

List适用于相同列宽，需要连续，多行呈现的列表布局场景。

| 特性 | Grid | List lanes |
| --- | --- | --- |
| 拖拽支持 | 支持 | 不支持️ |
| 布局优化 | 自动对齐 | 需手动计算 |
