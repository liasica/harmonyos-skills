---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-324
title: WaterFlow、Grid、List这些容器的使用区别是什么
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > WaterFlow、Grid、List这些容器的使用区别是什么
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:3b8fdfd2228d6cf6e37894c3fe19c07029416ede7f67f6d7d8b032559a9f2f6f
---

[WaterFlow](../harmonyos-references/ts-container-waterflow.md)、[Grid](../harmonyos-references/ts-container-grid.md)、[List](../harmonyos-references/ts-container-list.md)是三种不同的布局容器，它们的使用区别主要在于排列方式和适用场景的不同，具体如下：

|  | WaterFlow | Grid | List |
| --- | --- | --- | --- |
| **排列方式** | 瀑布流布局，按从上到下、从左到右的顺序排列，子组件高度不固定，容器智能计算并将新子组件放入当前累计高度最小的列，以消除布局留白。 | 网格布局，基于二维网格系统进行布局，将容器划分为有规律的行和列。 | 线性布局，沿垂直或水平方向进行单向性排列。 |
| **适用场景** | 适用于需要展示高度不固定元素的场景，如图片墙、电商商品展示、资讯类信息流等。 | 适用于固定行列的网格状界面，如九宫格图片展示、日历、计算器等。 | 适用于相同列宽，需要连续多行呈现的列表布局场景，如新闻列表、聊天记录、通讯录等。 |
