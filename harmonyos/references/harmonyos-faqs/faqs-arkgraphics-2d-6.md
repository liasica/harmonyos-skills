---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-6
title: EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a6962ea61a29146c37b9622621e0b14554945084308363c3456139af11aadc48
---

* 支持多线程，可以通过每个线程各自产生一块纹理，再将这些纹理合成到一块buffer。
* 可以使用sharedContext，另外绘制操作可通过调用OpenGL实现。
* 创建ShareContext的代码如下：

  ```ts
  void CreateShareEglContext() 
  {
    if (renderContext == nullptr) { // RenderContext is the main thread context 
      RS_LOGE("renderContext_ is nullptr");
      return;
    }
    eglShareContext = renderContext->CreateShareContext(); // Create share context 
    if (eglShareContext == EGL_NO_CONTEXT) {
      RS_LOGE("eglShareContext is EGL_NO_CONTEXT");
      return;
    }
    if (!eglMakeCurrent(renderContext->GetEGLDisplay(), EGL_NO_SURFACE, EGL_NO_SURFACE, eglShareContext)) {
      RS_LOGE("eglMakeCurrent failed");
      return;
    }
  }
  ```
