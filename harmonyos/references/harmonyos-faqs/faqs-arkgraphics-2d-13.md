---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-13
title: 一个EGLSurface支持同时显屏和输出到编码器吗
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 一个EGLSurface支持同时显屏和输出到编码器吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:48+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:10ff069a87d0483fbfa8439fb178e811925a4bc19bec0a4bbad8c3fb1b5d5133
---

不支持EglSurface同时用于显屏和编码器输出。

**原因分析**

显屏和输出到编码器使用同一个EGLSurface会导致缓冲区无法正常运转。EGLSurface中的生产者和消费者是一对一的关系，一个生产者不能对应多个消费者。

**解决措施**

OpenGL处理后，显屏和输出到编码器是支持的。需要创建两个EGLSurface来处理，并使用eglMakeCurrent方法选择每次需要消费的EGLSurface。
