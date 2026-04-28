---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-42
title: 在使用Canvas的场景中，如何主动控制组件刷新UI
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 在使用Canvas的场景中，如何主动控制组件刷新UI
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:cb9b564c8ff93b2eae13ba8ccbc148e3036208a288b6a4a6a901cf9d263d1bc5
---

Canvas组件最终的显示内容分两种：

一是组件的通用属性包括背景色、边框等渲染属性，这些属性可以通过状态变量驱动更新。

二是通过CanvasRenderingContext2D绘制接口由应用自行绘制的内容。该接口在调用时不会响应状态变量，会在下一帧自动刷新绘制内容，无需开发者主动控制刷新。

**参考链接**

[CanvasRenderingContext2D](../harmonyos-references/ts-canvasrenderingcontext2d.md)
