---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-temporal-upscale-8h
title: xeg_gles_temporal_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_gles_temporal_upscale.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d0e4d5ddc06173b5c7d0598e4728d8ce71bf793054582f813111eed6b1a34e2d
---

## 概述

XEngine时域AI超分特性OpenGL ES接口。推荐超分倍率为[1.25, 2.0]，使用此头文件中的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_temporal_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_gles\_temporal\_upscale.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

### 宏定义

| 名称 | 描述 |
| --- | --- |
| [XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_temporal_upscale_input_size) 0x1U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置超分输入纹理的真实宽高。 |
| [XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM](xengine-kit-xengine.md#xeg_temporal_upscale_jitter_num) 0x2U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置相机抖动的周期数，取值范围为[4, 16]，推荐8。 |
| [XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED](xengine-kit-xengine.md#xeg_temporal_upscale_depth_reversed) 0x3U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否存在深度反转。true表示存在深度反转，false表示不存在深度反转。 |
| [XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY](xengine-kit-xengine.md#xeg_temporal_upscale_reset_history) 0x4U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置是否重置历史帧数据，true表示重置，false表示不重置。在历史帧未使用超分，并且当前帧开始使用超分的情况下建议设置为true。 |
| [XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL](xengine-kit-xengine.md#xeg_temporal_upscale_steady_level) 0x5U | 用于通过[HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter)接口设置画面偏向当前帧（鬼影少但可能存在闪烁）还是历史帧（鬼影多但是更稳定）的平衡程度。取值范围为[0.0, 1.0]，如果该值不在以上范围内，则会发生未定义行为，例如渲染效果不正确或程序崩溃，值越大越偏向历史帧。建议根据实际需求选择合适的值，例如在需要减少鬼影时可设置为较小值，需要减少闪烁可以设置为较大值，推荐值为0.5。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#pfn_hms_xeg_temporalupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置时域AI超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RenderTemporalUpscale](xengine-kit-xengine.md#pfn_hms_xeg_rendertemporalupscale)) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY) | 执行时域AI超分渲染命令的函数指针定义。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_TemporalUpscaleParameter](xengine-kit-xengine.md#hms_xeg_temporalupscaleparameter) (GLenum pname, const GLvoid \*param) | 设置时域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderTemporalUpscale](xengine-kit-xengine.md#hms_xeg_rendertemporalupscale) (GLuint inputTexture, GLuint depthTexture, GLuint motionVectorTexture, GLuint dynamicMaskTexture, GLfloat jitterX, GLfloat jitterY) | 执行时域AI超分渲染命令。 |
