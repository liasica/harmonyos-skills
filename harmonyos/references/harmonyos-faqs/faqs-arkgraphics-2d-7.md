---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-7
title: 解码后数据帧送显的两种方式
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 解码后数据帧送显的两种方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:48+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4457c95a4e429b22cf886b5e7f4e89e2e2fa8388726c103a9704d5a98bfda7fa
---

方式一：使用 [NativeImage](../harmonyos-guides/native-image-guidelines.md) 和 [XComponent surface 模式](../harmonyos-guides/video-decoding.md#surface模式)。步骤如下：

1. 将 NativeImage 对应的 NativeWindow 与解码器绑定（surface 模式）。
2. 获取解码器输出的纹理。
3. 通过 [OpenGL](../harmonyos-references/opengl.md) 将纹理写入 XComponent surface 实现显示。

方式二：缓冲模式 + XComponent 表面模式，解码器输出的缓冲区通过 OpenGL 写入 XComponent 表面实现显示。
