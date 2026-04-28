---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-faq-5
title: 集成ABR后，从游戏引擎获取到的Native纹理内容为空，该如何解决?
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏渲染加速服务 > 集成ABR后，从游戏引擎获取到的Native纹理内容为空，该如何解决?
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9c737365a37cc60bcf86124b49ee1ebe7d58a8e56d5ae988958a3b6d0295822
---

**现象描述**

以团结引擎为例，游戏应用集成ABR，在游戏引擎中通过GetNativeTexturePtr获取Buffer关联的纹理，获取到的纹理内容为空。

**原因分析**

由于ABR对Buffer进行了自适应分辨率调整，并对ABR自适应缩放后的GLES纹理进行绘制，因而原始分辨率的GLES纹理中没有内容。

**处理步骤**

为解决此问题，需要通过[HMS\_ABR\_GetScaledTexture\_GLES](../harmonyos-references/_graphics_accelerate.md#hms_abr_getscaledtexture_gles)接口获取到ABR自适应缩放后的GLES纹理索引。

```
1. // 在Buffer渲染后调用
2. GLuint originTexture;
3. GLuint scaledTexture;
4. errorCode = HMS_ABR_GetScaledTexture_GLES(context_, originTexture, &scaledTexture);
5. if (errorCode != ABR_SUCCESS) {
6. GOLOGE("HMS_ABR_GetScaledTexture_GLES execution failed, error code: %d.", errorCode);
7. }
```
