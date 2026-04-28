---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-12
title: 关于GL_TEXTURE_2D和GL_TEXTURE_EXTERNAL_OES纹理类型的选择问题
breadcrumb: FAQ > 图形开发 > 2D图形（ArkGraphics 2D） > 关于GL_TEXTURE_2D和GL_TEXTURE_EXTERNAL_OES纹理类型的选择问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:49+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:e778b61aec86dab28854a7ecae5c2d92af6e4df40bb805ac7e0551b46764bc4f
---

**问题现象**

在读取相册视频、解封装、解码和OpenGL处理过程中，解码后的数据通过NativeImage中对应的生产者端NativeWindow接收，NativeImage与OpenGL纹理绑定。但测试发现，解码输出的内容并未更新到OpenGL纹理，即未能获取到OpenGL纹理数据。

**原因分析**

关于GL\_TEXTURE\_2D和GL\_TEXTURE\_EXTERNAL\_OES纹理类型的使用场景的区别：

* GL\_TEXTURE\_2D纹理类型的使用场景：适用于大多数场景，可以用于展示静态贴图、渲染2D图形和进行图像处理等操作。
* GL\_TEXTURE\_EXTERNAL\_OES纹理类型的使用场景：专门用于对外部图像或实时视频流进行处理，可以直接从BufferQueue中接收的数据渲染纹理多边形，从而提升视频处理的效率和渲染性能。例如，我们需要从Camera或外部视频源读取数据帧进行处理时，就要选用该纹理类型。

**解决措施**

在创建OH\_NativeImage并关联OpenGL时，纹理目标应选择GL\_TEXTURE\_EXTERNAL\_OES，而不是GL\_TEXTURE\_2D，因为通过NativeImage关联的OpenGL ES纹理会绑定到GL\_TEXTURE\_EXTERNAL\_OES目标上。
