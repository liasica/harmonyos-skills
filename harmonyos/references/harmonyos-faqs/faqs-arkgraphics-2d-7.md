---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-7
title: 解码后数据帧送显的两种方式
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 解码后数据帧送显的两种方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:46+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e39fe24c44a0f2ca3700b382b5fa4c50b6612a2ac52ead652080da634d3d2872
---

* 方式一：使用 [NativeImage](../harmonyos-guides/native-image-guidelines.md) 和 [XComponent surface 模式](../harmonyos-guides/video-decoding.md#surface模式)。步骤如下：
  1. 将 NativeImage 对应的 NativeWindow 与解码器绑定（surface 模式）。
  2. 获取解码器输出的纹理。
  3. 通过 [OpenGL](../harmonyos-references/opengl.md) 将纹理写入 XComponent surface 实现显示。
* 方式二：缓冲模式 + XComponent 表面模式，解码器输出的缓冲区通过 OpenGL 写入 XComponent 表面实现显示。
