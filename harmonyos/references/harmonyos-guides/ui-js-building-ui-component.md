---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-js-building-ui-component
title: 组件介绍
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (兼容JS的类Web开发范式) > 构建用户界面 > 组件介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:20+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:e27294f7b01e5c4afe88890a1f92a5f1104ed5c9eb22d84903b8d5a6d2f79caf
---

组件（Component）是构建页面的核心，每个组件通过对数据和方法的简单封装，实现独立的可视、可交互功能单元。组件之间相互独立，随取随用，也可以在需求相同的地方重复使用。

开发者还可以通过组件间合理的搭配定义满足业务需求的新组件，减少开发量，自定义组件的开发方法请参见[自定义组件](ui-js-custom-components.md)。

## 组件分类

根据组件的功能，可以分为以下六大类：

| 组件类型 | 主要组件 |
| --- | --- |
| 容器组件 | [badge](../harmonyos-references/js-components-container-badge.md)、[dialog](../harmonyos-references/js-components-container-dialog.md)、[div](../harmonyos-references/js-components-container-div.md)、[form](../harmonyos-references/js-components-container-form.md)、[list](../harmonyos-references/js-components-container-list.md)、[list-item](../harmonyos-references/js-components-container-list-item.md)、[list-item-group](../harmonyos-references/js-components-container-list-item-group.md)、[panel](../harmonyos-references/js-components-container-panel.md)、[popup](../harmonyos-references/js-components-container-popup.md)、[refresh](../harmonyos-references/js-components-container-refresh.md)、[stack](../harmonyos-references/js-components-container-stack.md)、[stepper](../harmonyos-references/js-components-container-stepper.md)、[stepper-item](../harmonyos-references/js-components-container-stepper-item.md)、[swiper](../harmonyos-references/js-components-container-swiper.md)、[tabs](../harmonyos-references/js-components-container-tabs.md)、[tab-bar](../harmonyos-references/js-components-container-tab-bar.md)、[tab-content](../harmonyos-references/js-components-container-tab-content.md) |
| 基础组件 | [button](../harmonyos-references/js-components-basic-button.md)、[chart](../harmonyos-references/js-components-basic-chart.md)、[divider](../harmonyos-references/js-components-basic-divider.md)、[image](../harmonyos-references/js-components-basic-image.md)、[image-animator](../harmonyos-references/js-components-basic-image-animator.md)、[input](../harmonyos-references/js-components-basic-input.md)、[label](../harmonyos-references/js-components-basic-label.md)、[marquee](../harmonyos-references/js-components-basic-marquee.md)、[menu](../harmonyos-references/js-components-basic-menu.md)、[option](../harmonyos-references/js-components-basic-option.md)、[picker](../harmonyos-references/js-components-basic-picker.md)、[picker-view](../harmonyos-references/js-components-basic-picker-view.md)、[piece](../harmonyos-references/js-components-basic-piece.md)、[progress](../harmonyos-references/js-components-basic-progress.md)、[qrcode](../harmonyos-references/js-components-basic-qrcode.md)、[rating](../harmonyos-references/js-components-basic-rating.md)、[richtext](../harmonyos-references/js-components-basic-richtext.md)、[search](../harmonyos-references/js-components-basic-search.md)、[select](../harmonyos-references/js-components-basic-select.md)、[slider](../harmonyos-references/js-components-basic-slider.md)、[span](../harmonyos-references/js-components-basic-span.md)、[switch](../harmonyos-references/js-components-basic-switch.md)、[text](../harmonyos-references/js-components-basic-text.md)、[textarea](../harmonyos-references/js-components-basic-textarea.md)、[toolbar](../harmonyos-references/js-components-basic-toolbar.md)、[toolbar-item](../harmonyos-references/js-components-basic-toolbar-item.md)、[toggle](../harmonyos-references/js-components-basic-toggle.md) |
| 媒体组件 | [video](../harmonyos-references/js-components-media-video.md) |
| 画布组件 | [canvas](../harmonyos-references/js-components-canvas-canvas.md) |
| 栅格组件 | [grid-container](../harmonyos-references/js-components-grid-container.md)、[grid-row](../harmonyos-references/js-components-grid-row.md)、[grid-col](../harmonyos-references/js-components-grid-col.md) |
| svg组件 | [svg](../harmonyos-references/js-components-svg.md)、[rect](../harmonyos-references/js-components-svg-rect.md)、[circle](../harmonyos-references/js-components-svg-circle.md)、[ellipse](../harmonyos-references/js-components-svg-ellipse.md)、[path](../harmonyos-references/js-components-svg-path.md)、[line](../harmonyos-references/js-components-svg-line.md)、[polyline](../harmonyos-references/js-components-svg-polyline.md)、[polygon](../harmonyos-references/js-components-svg-polygon.md)、[text](../harmonyos-references/js-components-svg-text.md)、[tspan](../harmonyos-references/js-components-svg-tspan.md)、[textPath](../harmonyos-references/js-components-svg-textpath.md)、[animate](../harmonyos-references/js-components-svg-animate.md)、[animateMotion](../harmonyos-references/js-components-svg-animatemotion.md)、[animateTransform](../harmonyos-references/js-components-svg-animatetransform.md) |
