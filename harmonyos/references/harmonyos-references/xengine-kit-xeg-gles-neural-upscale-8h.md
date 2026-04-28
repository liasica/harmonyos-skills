---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-neural-upscale-8h
title: xeg_gles_neural_upscale.h
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 头文件 > xeg_gles_neural_upscale.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:35db1dfa78136b06d8eb00ad81a7bec00a3214c0d901412d1e60b416f4980957
---

## 概述

PhonePC/2in1TabletTV

XEngine空域AI超分特性OpenGL ES接口，推荐超分倍率为[1.0, 1.5]。使用此头文件中的接口前需要通过[HMS\_XEG\_GetString](xengine-kit-xengine.md#hms_xeg_getstring)接口查询[XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](xengine-kit-xengine.md#xeg_neural_upscale_extension_name)扩展可用。

**引用文件**：<xengine/xeg\_gles\_neural\_upscale.h>

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
| [XEG\_NEURAL\_UPSCALE\_SCISSOR](xengine-kit-xengine.md#xeg_neural_upscale_scissor) 0x1U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的裁剪窗口参数，裁剪窗口用于确定对输入图像采样的区域。 |
| [XEG\_NEURAL\_UPSCALE\_SHARPNESS](xengine-kit-xengine.md#xeg_neural_upscale_sharpness) 0x2U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置超分的锐化度参数，锐化度的建议取值范围为[0, 1]。 |
| [XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE](xengine-kit-xengine.md#xeg_neural_upscale_input_handle) 0x4U | 用于通过[HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter)接口设置与超分输入纹理关联的OH\_NativeBuffer handle。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_NEURALUPSCALEPARAMETER](xengine-kit-xengine.md#pfn_hms_xeg_neuralupscaleparameter)) (GLenum pname, GLvoid \*param) | 设置空域AI超分输入参数的函数指针定义。 |
| typedef void(GL\_APIENTRYP [PFN\_HMS\_XEG\_RENDERNEURALUPSCALE](xengine-kit-xengine.md#pfn_hms_xeg_renderneuralupscale)) (GLuint inputTexture) | 执行空域AI超分渲染命令的函数指针定义。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_NeuralUpscaleParameter](xengine-kit-xengine.md#hms_xeg_neuralupscaleparameter) (GLenum pname, GLvoid \*param) | 设置空域AI超分输入参数。 |
| GL\_APICALL void GL\_APIENTRY [HMS\_XEG\_RenderNeuralUpscale](xengine-kit-xengine.md#hms_xeg_renderneuralupscale) (GLuint inputTexture) | 执行空域AI超分渲染命令。 |
