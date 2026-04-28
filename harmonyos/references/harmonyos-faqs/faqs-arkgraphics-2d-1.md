---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-1
title: 如何使用EGL绘制自定义动画？请提供一个简单示例
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 如何使用EGL绘制自定义动画？请提供一个简单示例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1920dd712b291fdbf2cfdc12d4f6298b74cc3593ce639476e7e3a4db29cd5784
---

自定义动画需开发者实现。可使用OpenGL绘制。动画实现主要涉及业务逻辑，业务方需识别动画触发事件，获取动画起点和终点，根据时间轴和动画曲线计算每一帧内容，最后调用OpenGL接口绘制。

**参考链接**

[自定义渲染 (XComponent)](../harmonyos-guides/napi-xcomponent-guidelines.md)
