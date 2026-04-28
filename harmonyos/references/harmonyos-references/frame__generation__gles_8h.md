---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__gles_8h
title: frame_generation_gles.h
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 头文件 > frame_generation_gles.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:42+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:346f1f257ff6211534d4425271587dcf653e63d13bd856234f681b58fcd44071
---

## 概述

PhoneTabletTV

声明OpenGL ES图形API平台的超帧接口。

**引用文件：** <graphics\_game\_sdk/frame\_generation\_gles.h>

**库：** libframegeneration.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

## 汇总

PhoneTabletTV

### 结构体

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| struct [FG\_DispatchDescription\_GLES](_f_g___dispatch_description___g_l_e_s.md) | 此结构体描述下发帧生成命令[HMS\_FG\_Dispatch\_GLES](_graphics_accelerate.md#hms_fg_dispatch_gles)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。 |

### 类型定义

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles) [FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles) | 此结构体描述超帧上下文，该接口仅适配OpenGL ES图形API平台。 |
| typedef struct [FG\_DispatchDescription\_GLES](_f_g___dispatch_description___g_l_e_s.md) [FG\_DispatchDescription\_GLES](_graphics_accelerate.md#fg_dispatchdescription_gles) | 此结构体描述下发帧生成命令[HMS\_FG\_Dispatch\_GLES](_graphics_accelerate.md#hms_fg_dispatch_gles)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。 |
| typedef enum [FG\_ImageFormat\_GLES](_graphics_accelerate.md#fg_imageformat_gles-1) [FG\_ImageFormat\_GLES](_graphics_accelerate.md#fg_imageformat_gles) | 此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。 |

### 枚举

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_ImageFormat\_GLES](_graphics_accelerate.md#fg_imageformat_gles-1) {  FG\_FORMAT\_R8G8B8A8\_UNORM = 0,  FG\_FORMAT\_R11G11B10\_SFLOAT = 1,  FG\_FORMAT\_R16G16B16A16\_SFLOAT = 2  } | 此枚举描述真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式。该接口仅适配OpenGL ES图形API平台。 |

### 函数

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* [HMS\_FG\_CreateContext\_GLES](_graphics_accelerate.md#hms_fg_createcontext_gles)(void) | 创建超帧上下文实例，调用成功则返回指向[FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)对象的指针，失败返回nullptr。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetAlgorithmMode\_GLES](_graphics_accelerate.md#hms_fg_setalgorithmmode_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, const [FG\_AlgorithmModeInfo](_f_g___algorithm_mode_info.md)\* predictionModeInfo) | 设置超帧预测算法模式和运动估计模式，必选。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetResolution\_GLES](_graphics_accelerate.md#hms_fg_setresolution_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, const [FG\_ResolutionInfo](_f_g___resolution_info.md)\* resolutionInfo) | 设置超帧输入输出图像分辨率，必选。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetCvvZSemantic\_GLES](_graphics_accelerate.md#hms_fg_setcvvzsemantic_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, [FG\_CvvZSemantic](_graphics_accelerate.md#fg_cvvzsemantic-1) semantic) | 设置超帧齐次裁剪空间Z/W范围及深度测试函数，可选调用，未调用则默认模式设置为FG\_CVV\_Z\_SEMANTIC\_MINUS\_ONE\_TO\_ONE\_FORWARD\_Z。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetImageFormat\_GLES](_graphics_accelerate.md#hms_fg_setimageformat_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, [FG\_ImageFormat\_GLES](_graphics_accelerate.md#fg_imageformat_gles-1) format) | 设置真实渲染帧颜色缓冲区和预测帧缓冲区的图像格式，可选调用，未调用则模式默认设置为FG\_FORMAT\_R8G8B8A8\_UNORM。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetDepthStencilYDirectionInverted\_GLES](_graphics_accelerate.md#hms_fg_setdepthstencilydirectioninverted_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, bool inverted) | 设置颜色缓冲区相对深度模板缓冲区基于y轴翻转的标志位，可选调用，未调用则默认无翻转。如果渲染管线中颜色缓冲区相对深度模板缓冲区基于y轴翻转了180度，则设为true；如果颜色缓冲区与深度模板缓冲区绘制方向一致则设为false。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_Activate\_GLES](_graphics_accelerate.md#hms_fg_activate_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context) | 激活超帧上下文实例。已激活的超帧实例可调用[HMS\_FG\_Dispatch\_GLES](_graphics_accelerate.md#hms_fg_dispatch_gles)接口生成预测帧， 激活超帧上下文实例前必须先调用[HMS\_FG\_SetAlgorithmMode\_GLES](_graphics_accelerate.md#hms_fg_setalgorithmmode_gles)和[HMS\_FG\_SetResolution\_GLES](_graphics_accelerate.md#hms_fg_setresolution_gles)接口完成配置。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_Deactivate\_GLES](_graphics_accelerate.md#hms_fg_deactivate_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context) | 去激活超帧上下文实例，可通过[HMS\_FG\_Activate\_GLES](_graphics_accelerate.md#hms_fg_activate_gles)接口重新激活。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_IsActive\_GLES](_graphics_accelerate.md#hms_fg_isactive_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, bool\* isActive) | 查询超帧上下文实例是否处于激活状态。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_Dispatch\_GLES](_graphics_accelerate.md#hms_fg_dispatch_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, const [FG\_DispatchDescription\_GLES](_f_g___dispatch_description___g_l_e_s.md)\* desc) | 配置帧预测所需的参数信息，生成预测帧，当前处于激活状态时有效，该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_SetExtendedCameraInfo\_GLES](_graphics_accelerate.md#hms_fg_setextendedcamerainfo_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, const [FG\_PerFrameExtendedCameraInfo](_f_g___per_frame_extended_camera_info.md)\* info) | 设置超帧相机扩展属性信息，当视图投影矩阵的平移分量非常大时，提供该信息以获得更加准确的超帧效果。可选调用，该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode-1) [HMS\_FG\_DestroyContext\_GLES](_graphics_accelerate.md#hms_fg_destroycontext_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\*\* context) | 销毁超帧上下文实例并释放内存资源。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode) [HMS\_FG\_SetIntegrationMode\_GLES](_graphics_accelerate.md#hms_fg_setintegrationmode_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, const [FG\_IntegrationInfo](_f_g___intergration_info.md)\* integrationInfo) | 设置超帧集成信息，当[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION时，[FG\_IntegrationInfo](_f_g___intergration_info.md)中的presentMode、needDepthAndColorCache、needFlipColorTexture成员才会生效。其他情况下这些参数应忽略或设置为默认值。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode) [HMS\_FG\_SetUiPredictionEnabled\_GLES](_graphics_accelerate.md#hms_fg_setuipredictionenabled_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, bool isEnabled) | 选择是否启用UI预测功能，这个功能只能在系统送显模式下启用，在游戏送显模式下无效。UI预测功能启用后，画面中2D UI内容可以与主画面一样做预测、帧生成；如不启用该功能，预测帧会复用真实帧的UI进行展示。该接口仅适配OpenGL ES图形API平台。 |
| [FG\_ErrorCode](_graphics_accelerate.md#fg_errorcode) [HMS\_FG\_SetTargetFps\_GLES](_graphics_accelerate.md#hms_fg_settargetfps_gles)([FG\_Context\_GLES](_graphics_accelerate.md#fg_context_gles)\* context, int targetFps) | 设置超帧后的目标帧率，这个设置仅在系统显示模式下生效，对游戏显示模式无影响。参数targetFps的取值范围[30, 144]旨在确保在不同平台上的性能稳定性和用户体验一致性。开发者应根据实际业务场景选择合适的帧率。该接口在游戏初次上架之后生效且仅适配OpenGL ES图形API平台。 |
