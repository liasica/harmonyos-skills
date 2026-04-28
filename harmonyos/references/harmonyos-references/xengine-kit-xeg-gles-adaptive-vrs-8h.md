---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-adaptive-vrs-8h
title: xeg_gles_adaptive_vrs.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_gles_adaptive_vrs.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5fc58ec3f5177645007d71345b9ba07b5da1dad13e1cd23fa2839ec134c3c85
---

## 概述

PhonePC/2in1TabletTV

XEngine VRS特性接口。使用此头文件的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_ADAPTIVE\_VRS\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_adaptive_vrs_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_gles\_adaptive\_vrs.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](xengine-kit-xengine.md)

## 汇总

PhonePC/2in1TabletTV

### 宏定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [XEG\_ADAPTIVE\_VRS\_INPUT\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_input_size) 0x1U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_SIZE参数，表示上一帧渲染管线最终渲染的图像宽度和高度。 |
| [XEG\_ADAPTIVE\_VRS\_INPUT\_REGION](xengine-kit-xengine.md#xeg_adaptive_vrs_input_region) 0x2U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的INPUT\_REGION参数，表示上一帧渲染管线最终渲染的图像区域。 |
| [XEG\_ADAPTIVE\_VRS\_TEXEL\_SIZE](xengine-kit-xengine.md#xeg_adaptive_vrs_texel_size) 0x3U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的TEXEL\_SIZE参数。 |
| [XEG\_ADAPTIVE\_VRS\_ERROR\_SENSITIVITY](xengine-kit-xengine.md#xeg_adaptive_vrs_error_sensitivity) 0x4U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的ERROR\_SENSITIVITY参数，表示控制生成着色率图像的阈值。该值越大，平均着色率越小，即性能会越好但画质会劣化。建议取值范围为[0, 1]。 |
| [XEG\_ADAPTIVE\_VRS\_FLIP](xengine-kit-xengine.md#xeg_adaptive_vrs_flip) 0x5U | 用于设置[HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter)接口的FLIP参数，该参数用于控制是否执行图像上下翻转。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_ADAPTIVEVRSPARAMETER](xengine-kit-xengine.md#pfn_hms_xeg_adaptivevrsparameter)) (GLenum pname, GLvoid \*param) | 设置自适应VRS输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_DISPATCHADAPTIVEVRS](xengine-kit-xengine.md#pfn_hms_xeg_dispatchadaptivevrs)) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage) | 计算着色率图像的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_APPLYADAPTIVEVRS](xengine-kit-xengine.md#pfn_hms_xeg_applyadaptivevrs)) (GLuint shadingRateImage) | 将着色率图像应用到渲染目标中的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_AdaptiveVRSParameter](xengine-kit-xengine.md#hms_xeg_adaptivevrsparameter) (GLenum pname, GLvoid \*param) | 设置自适应VRS的参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_DispatchAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_dispatchadaptivevrs) (GLfloat \*reprojectionMatrix, GLuint inputColorImage, GLuint inputDepthImage, GLuint shadingRateImage) | 计算着色率图像。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_ApplyAdaptiveVRS](xengine-kit-xengine.md#hms_xeg_applyadaptivevrs) (GLuint shadingRateImage) | 将着色率图像应用到渲染目标中。 |
