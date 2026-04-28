---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-shape-overview
title: 几何图形绘制概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 几何图形绘制 > 几何图形绘制概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:48+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:443b5b7c3d81798a3db4707a6588a2135e31937919e290c795d36accfb0f9924
---

绘制几何图形有两种方法：一是通过绘制组件[Shape](../harmonyos-references/ts-drawing-components-shape.md)直接绘制出几何图形；二是通过形状裁剪属性[clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)将组件裁剪成几何图形。

## 使用场景

| 绘制方式 | 使用场景 |
| --- | --- |
| [绘制几何图形 (Shape)](arkts-geometric-shape-drawing.md) | 用于创建指定形状的组件，在页面上直接绘制出几何图形。 |
| [形状裁剪 (clipShape)](arkts-clip-shape.md) | 用于将组件裁剪为指定的几何图形。 |

## 约束限制

* 对绘制组件，既可用[Shape](../harmonyos-references/ts-drawing-components-shape.md)组件作为父组件实现类似SVG的效果，也可单独使用各种形状的子组件进行绘制。
* 对形状裁剪属性，裁剪不会导致被裁剪区域无法响应绑定的手势事件。
