---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-6
title: EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > EGL绘制是否支持多线程？如何在多线程的场景下同时操作一块buffer进行图形绘制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:46+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:12c0971d1c79015e54b143fa8c0d2160340dfcd3f19c82ce45028dd065d974c0
---

* 支持多线程，可以通过每个线程各自产生一块纹理，再将这些纹理合成到一块buffer。
* 可以使用sharedContext，另外绘制操作可通过调用OpenGL实现。
* 创建ShareContext的代码如下：

  ```
  1. void CreateShareEglContext()
  2. {
  3. if (renderContext == nullptr) { // RenderContext is the main thread context
  4. RS_LOGE("renderContext_ is nullptr");
  5. return;
  6. }
  7. eglShareContext = renderContext->CreateShareContext(); // Create share context
  8. if (eglShareContext == EGL_NO_CONTEXT) {
  9. RS_LOGE("eglShareContext is EGL_NO_CONTEXT");
  10. return;
  11. }
  12. if (!eglMakeCurrent(renderContext->GetEGLDisplay(), EGL_NO_SURFACE, EGL_NO_SURFACE, eglShareContext)) {
  13. RS_LOGE("eglMakeCurrent failed");
  14. return;
  15. }
  16. }
  ```

  [CreateShare.cpp](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/Arkgraphics2D/entry/src/main/ets/pages/CreateShare.cpp#L5-L20)
