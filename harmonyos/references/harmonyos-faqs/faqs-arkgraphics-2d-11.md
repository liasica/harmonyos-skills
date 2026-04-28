---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-11
title: OpenGL同一个上下文在多线程中使用问题
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > OpenGL同一个上下文在多线程中使用问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:49+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:7074a212c28e20945ce80eee67aeb65fecd401aaa2ce684497b16c4ad9b12472
---

**问题现象**

在主线程中初始化EGL环境并创建上下文，然后在单独的子线程中处理渲染，这会导致黑屏。

**解决措施**

OpenGL上下文与特定线程绑定，不能在同一个上下文中并发执行多个线程的操作。

方法一：将EGL的初始化和渲染过程都放在同一个线程中处理。

方法二：当主线程完成EGL初始化和创建上下文后，调用eglMakeCurrent方法解绑主线程中的当前上下文，然后在子线程中重新绑定上下文。
