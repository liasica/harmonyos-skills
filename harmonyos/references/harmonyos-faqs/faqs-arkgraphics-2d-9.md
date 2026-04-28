---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-9
title: 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_SURFACE （300d）。日志显示：QEGLPlatformContext: eglSwapBuffers failed: 300d。
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 使用eglSwapBuffers API，eglSwapBuffers执行报错错误码：EGL_BAD_SURFACE （300d）。日志显示：QEGLPlatformContext: eglSwapBuffers failed: 300d。
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c9839b1a358c07c4f244c26cf48a7b2ac865a106efdbaff6e9a0725fcfa789e4
---

如果surface不是EGL绘图表面，系统会返回EGL\_BAD\_SURFACE错误。建议检查eglCreateWindowSurface、eglCreatePixmapSurface和eglCreatePbufferSurface的参数设置。
