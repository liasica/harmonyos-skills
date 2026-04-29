---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/abr__gles_8h
title: abr_gles.h
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 头文件 > abr_gles.h
category: harmonyos-references
scraped_at: 2026-04-29T14:06:19+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:d9595db8423071227508405a0c6fa28b113656058413a3a2665f09b166c112a8
---

## 概述

PhoneTabletTV

声明OpenGL ES图形API平台的ABR接口。

**引用文件：** <graphics\_game\_sdk/abr\_gles.h>

**库：** libabr.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

## 汇总

PhoneTabletTV

### 函数

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_MarkFrameBuffer\_GLES](_graphics_accelerate.md#hms_abr_markframebuffer_gles)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context) | 标记ABR进行自适应渲染处理的GLES Buffer，需要在GLES Buffer开始渲染前调用此接口。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_GetScaledTexture\_GLES](_graphics_accelerate.md#hms_abr_getscaledtexture_gles)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, uint32\_t originTexture, uint32\_t\* scaledTexture) | 根据原始分辨率的GLES纹理索引获取ABR自适应缩放后的GLES纹理索引。调用前需确认原始纹理有效、渲染上下文有效。originTexture为原始纹理ID，该值不能为0，否则无法正确获取scaledTexure，接口功能失效；scaledTexture不能为空指针，否则会返回错误码ABR\_INVALID\_PARAMETER。 |
