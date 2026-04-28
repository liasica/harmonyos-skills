---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reduce-layout-nodes
title: 布局节点减少
breadcrumb: 最佳实践 > 性能 > 性能优化 > 布局节点减少
category: best-practices
scraped_at: 2026-04-28T08:22:24+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:09a8a5dd75538663d76c2dd724f989ca8d8c1e3022f13d64a99cbed719b541ac
---

在进行页面布局开发时，应该尽量减少布局节点，避免系统绘制更多的布局组件，达到优化渲染性能、减少内存占用的目的。具体提高渲染性能的优化原理请参阅[ArkUI框架执行流程](bpta-improve-layout-performance.md#section16114121365117)。

## 优先使用@Builder方法代替自定义组件

由于@Builder不涉及生命周期，在自定义组件大量嵌套的场景中，更加轻量级的@Builder在性能方面更加出色。因此，当自定义组件不涉及到状态变量和自定义生命周期时，可以优先使用@Builder替换自定义组件，提升性能。具体的原理与优化案例请参阅[优先使用@Builder方法代替自定义组件](bpta-component-nesting-optimization.md#section1012953161217)。

## 合理使用布局容器组件

进行UI布局时，子组件根据父组件的布局算法排列，然后按规则摆放位置。不同的布局容器对性能的影响不同。根据场景选择合适的布局，除非必要，尽量避免使用性能差的布局组件。

复杂布局提供场景化能力，解决多种布局场景问题。不当使用高级组件可能增加性能消耗。具体案例与实验数据参见[选择合适的布局组件](bpta-improve-layout-performance.md#section5837111044912)。

## 布局优化

在进行UI布局时，额外的节点数会导致更多计算，影响性能。应该进行布局优化，主要有如下几种优化方式：

* 移除冗余节点、使用扁平化布局减少节点数。具体案例请参阅[精简节点数](bpta-improve-layout-performance.md#section9293918175210)。
* 自定义组件自身为非渲染节点，仅是组件树和状态数据的组合，常规使用自定义组件时并不会产生多余的节点。但是给自定义组件添加属性后，会将自定义组件作为一个整体节点进行处理。需通过优化手段[减少自定义组件产生多余节点](bpta-component-nesting-optimization.md#section25911641123713)。
* 在组件嵌套的情况中，可以找到一些无用的容器组件嵌套。在考虑组件嵌套优化中，可以[删除无用的Stack/Column/Row嵌套](bpta-component-nesting-optimization.md#section1012993119126)，移除冗余节点，从而避免冗余节点对性能的消耗。
* 实际上有些场景直接使用组件属性或借助系统API的能力即可实现，例如使用[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)属性可以实现浮层场景，使用[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)可以实现颜色叠加效果。[优先使用组件属性代替嵌套组件](bpta-component-nesting-optimization.md)方式可以减少布局嵌套组件的使用，从而精简节点数。
