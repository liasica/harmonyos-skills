---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/abr__base_8h
title: abr_base.h
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 头文件 > abr_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5538af16f90f935ce52493f2f339b97b91263303445581531a1e10f0ec5d5ca5
---

## 概述

PhoneTabletTV

声明不区分图形API平台的ABR（自适应稳态渲染）接口。

**引用文件：** <graphics\_game\_sdk/abr\_base.h>

**库：** libabr.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

## 汇总

PhoneTabletTV

### 结构体

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| struct [ABR\_Vector3](_a_b_r___vector3.md) | 此结构体描述ABR三维向量。 |
| struct [ABR\_CameraData](_a_b_r___camera_data.md) | 此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。 |

### 类型定义

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [ABR\_Context](_graphics_accelerate.md#abr_context) [ABR\_Context](_graphics_accelerate.md#abr_context) | 此结构体描述ABR上下文。 |
| typedef enum [ABR\_RenderAPI\_Type](_graphics_accelerate.md#abr_renderapi_type-1) [ABR\_RenderAPI\_Type](_graphics_accelerate.md#abr_renderapi_type) | 此枚举描述ABR支持的图形API类型。 |
| typedef struct [ABR\_Vector3](_a_b_r___vector3.md) [ABR\_Vector3](_graphics_accelerate.md#abr_vector3) | 此结构体描述ABR三维向量。 |
| typedef struct [ABR\_CameraData](_a_b_r___camera_data.md) [ABR\_CameraData](_graphics_accelerate.md#abr_cameradata) | 此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。 |
| typedef enum [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode) | 此枚举描述ABR接口调用错误码。 |

### 枚举

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ABR\_RenderAPI\_Type](_graphics_accelerate.md#abr_renderapi_type-1) {  RENDER\_API\_GLES = 0  } | 此枚举描述ABR支持的图形API类型。RENDER\_API\_GLES表示OpenGL ES API。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) {  ABR\_SUCCESS = 0,  ABR\_INVALID\_PARAMETER = 401,  ABR\_CONTEXT\_CONFIG\_AFTER\_ACTIVE = 1009501001,  ABR\_CONTEXT\_NOT\_CONFIG = 1009501002,  ABR\_CONTEXT\_NOT\_ACTIVE = 1009501003,  ABR\_METADATA\_INVALID = 1009501004,  ABR\_FRAMEBUFFER\_INVALID = 1009501005  } | 此枚举描述ABR接口调用错误码。 |

### 函数

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ABR\_Context](_graphics_accelerate.md#abr_context)\* [HMS\_ABR\_CreateContext](_graphics_accelerate.md#hms_abr_createcontext)([ABR\_RenderAPI\_Type](_graphics_accelerate.md#abr_renderapi_type-1) type) | 创建ABR上下文实例，每次调用会新建[ABR\_Context](_graphics_accelerate.md#abr_context)对象，并返回指向[ABR\_Context](_graphics_accelerate.md#abr_context)对象的指针。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_SetTargetFps](_graphics_accelerate.md#hms_abr_settargetfps)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, const uint32\_t targetFps) | 配置ABR上下文实例的目标帧率属性。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_SetScaleRange](_graphics_accelerate.md#hms_abr_setscalerange)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, const float minValue, const float maxValue) | 配置ABR上下文实例的Buffer分辨率因子范围属性。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_Activate](_graphics_accelerate.md#hms_abr_activate)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context) | 激活ABR上下文实例。激活ABR上下文实例前需调用[HMS\_ABR\_SetTargetFps](_graphics_accelerate.md#hms_abr_settargetfps)和[HMS\_ABR\_SetScaleRange](_graphics_accelerate.md#hms_abr_setscalerange)接口进行实例属性的配置。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_IsActive](_graphics_accelerate.md#hms_abr_isactive)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, bool\* isActive) | 查询ABR上下文实例是否处于激活状态。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_Deactivate](_graphics_accelerate.md#hms_abr_deactivate)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context) | 去激活ABR上下文实例，可通过[HMS\_ABR\_Activate](_graphics_accelerate.md#hms_abr_activate)重新激活。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_UpdateCameraData](_graphics_accelerate.md#hms_abr_updatecameradata)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, [ABR\_CameraData](_a_b_r___camera_data.md)\* data) | 更新每帧相机运动数据，ABR更新相机运动数据前需调用[HMS\_ABR\_Activate](_graphics_accelerate.md#hms_abr_activate)接口激活ABR上下文实例。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_GetScale](_graphics_accelerate.md#hms_abr_getscale)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, float\* scale) | 获取ABR Buffer分辨率因子。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_GetNextScale](_graphics_accelerate.md#hms_abr_getnextscale)([ABR\_Context](_graphics_accelerate.md#abr_context)\* context, float\* scale) | 获取下一帧的ABR Buffer分辨率因子。 |
| [ABR\_ErrorCode](_graphics_accelerate.md#abr_errorcode-1) [HMS\_ABR\_DestroyContext](_graphics_accelerate.md#hms_abr_destroycontext)([ABR\_Context](_graphics_accelerate.md#abr_context)\*\* context) | 销毁ABR上下文实例并释放内存资源。 |
