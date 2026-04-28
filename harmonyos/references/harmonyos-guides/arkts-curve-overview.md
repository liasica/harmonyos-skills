---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-curve-overview
title: 动画曲线概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画曲线 > 动画曲线概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b6ad1ad1acb9f92ef80a8ca0aa360e25d5f404ba903f9c0c18c04d60e81637c8
---

动画曲线是属性关于时间的变化函数，决定属性变化时产生动画的运动轨迹。某一时刻下动画曲线的斜率代表动画的速度，对应属性变化的快慢。一条优秀的动画曲线具备连续光滑、符合用户意图、符合物理世界客观规律的特点。开发者可结合用户的使用场景和意图，为动效选取合适的动画曲线。

根据动画曲线是否符合物理世界客观规律，可将其分为物理曲线（ArkUI当前提供了多种物理弹簧曲线）和传统曲线两种类型，具体如下。相比于传统曲线，物理曲线产生的运动轨迹更加符合用户认知，有助于创造自然生动的动画效果，建议开发者优先使用物理曲线。

* [传统曲线](arkts-traditional-curve.md)：基于数学公式，创造形状符合开发者预期的动画曲线，以三阶贝塞尔曲线为代表。
* [弹簧曲线](arkts-spring-curve.md)：阻尼弹簧曲线，简称弹簧曲线。
