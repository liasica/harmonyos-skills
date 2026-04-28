---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-10
title: 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_ALLOC。
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_ALLOC。
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:49+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:747869a72d07082b7339d9e3310b69b57966788738119faad1eddeab3fbea254
---

编码器通过 OH\_VideoEncoder\_GetSurface(encoder\_, &NativeWindow) 获取 NativeWindow，使用该 NativeWindow 创建 Encoder 的 EGLSurface 来接收 OpenGL 的纹理数据。若未调用 OH\_NativeWindow\_NativeWindowHandleOpt(nativeWindow, SET\_BUFFER\_GEOMETRY, height, width) 设置 buffer 大小，在调用 eglSwapBuffers API 时会报错。
