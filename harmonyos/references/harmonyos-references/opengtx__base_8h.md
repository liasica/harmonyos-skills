---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h
title: opengtx_base.h
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 头文件 > opengtx_base.h
category: harmonyos-references
scraped_at: 2026-04-28T08:15:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a2bbad992af060d633e84868a5ffabb57756119b01608a24ebdec17b1583ede
---

## 概述

PhoneTabletTV

声明不区分OpenGL ES和Vulkan图形API平台的OpenGTX接口。

**引用文件：** <graphics\_game\_sdk/opengtx\_base.h>

**库：** libopengtx.so

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

## 汇总

PhoneTabletTV

### 结构体

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| struct [OpenGTX\_ConfigDescription](_open_g_t_x___config_description.md) | 此结构体描述OpenGTX属性配置。 |
| struct [OpenGTX\_GameSceneInfo](_open_g_t_x___game_scene_info.md) | 此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。 |
| struct [OpenGTX\_FrameRenderInfo](_open_g_t_x___frame_render_info.md) | 此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。该参数中的相机矩阵通常用于优化渲染层降负载方案的画质效果。 |
| struct [OpenGTX\_NetworkInfo](_open_g_t_x___network_info.md) | 此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。 |
| struct [OpenGTX\_ResolutionValue](_open_g_t_x___resolution_value.md) | 此结构体描述游戏应用的分辨率值。 |
| struct [OpenGTX\_Vector3](_open_g_t_x___vector3.md) | 此结构体描述OpenGTX三维向量。 |
| struct [OpenGTX\_NetworkLatency](_open_g_t_x___network_latency.md) | 此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。该参数通常用于针对性优化网络延迟。 |

### 类型定义

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode) | 此枚举描述OpenGTX接口调用错误码。 |
| typedef enum [OpenGTX\_LTPO\_Mode](_graphics_accelerate.md#opengtx_ltpo_mode-1) [OpenGTX\_LTPO\_Mode](_graphics_accelerate.md#opengtx_ltpo_mode) | 此枚举描述OpenGTX\_LTPO模式类型，以控制游戏中的帧率。 |
| typedef enum [OpenGTX\_EngineType](_graphics_accelerate.md#opengtx_enginetype-1) [OpenGTX\_EngineType](_graphics_accelerate.md#opengtx_enginetype) | 此枚举描述游戏应用的底层游戏引擎类型。 |
| typedef enum [OpenGTX\_GameType](_graphics_accelerate.md#opengtx_gametype-1) [OpenGTX\_GameType](_graphics_accelerate.md#opengtx_gametype) | 此枚举描述游戏应用的类型。 |
| typedef enum [OpenGTX\_SceneID](_graphics_accelerate.md#opengtx_sceneid-1) [OpenGTX\_SceneID](_graphics_accelerate.md#opengtx_sceneid) | 此枚举描述OpenGTX算法的游戏场景类型。 |
| typedef enum [OpenGTX\_PictureQualityMaxLevel](_graphics_accelerate.md#opengtx_picturequalitymaxlevel-1) [OpenGTX\_PictureQualityMaxLevel](_graphics_accelerate.md#opengtx_picturequalitymaxlevel) | 此枚举描述游戏应用的图像质量。 |
| typedef enum [OpenGTX\_TempLevel](_graphics_accelerate.md#opengtx_templevel-1) [OpenGTX\_TempLevel](_graphics_accelerate.md#opengtx_templevel) | 此枚举描述设备的温度级别。 |
| typedef struct [OpenGTX\_Context](_graphics_accelerate.md#opengtx_context) [OpenGTX\_Context](_graphics_accelerate.md#opengtx_context) | 此结构体描述OpenGTX上下文。 |
| typedef struct [OpenGTX\_ConfigDescription](_open_g_t_x___config_description.md) [OpenGTX\_ConfigDescription](_graphics_accelerate.md#opengtx_configdescription) | 此结构体描述OpenGTX属性配置。 |
| typedef struct [OpenGTX\_GameSceneInfo](_open_g_t_x___game_scene_info.md) [OpenGTX\_GameSceneInfo](_graphics_accelerate.md#opengtx_gamesceneinfo) | 此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。 |
| typedef struct [OpenGTX\_FrameRenderInfo](_open_g_t_x___frame_render_info.md) [OpenGTX\_FrameRenderInfo](_graphics_accelerate.md#opengtx_framerenderinfo) | 此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。该参数中的相机矩阵通常用于优化渲染层降负载方案的画质效果。 |
| typedef struct [OpenGTX\_NetworkInfo](_open_g_t_x___network_info.md) [OpenGTX\_NetworkInfo](_graphics_accelerate.md#opengtx_networkinfo) | 此结构体描述当前设备网络信息，游戏应用获取到网络信息后传递此参数。 |
| typedef struct [OpenGTX\_ResolutionValue](_open_g_t_x___resolution_value.md) [OpenGTX\_ResolutionValue](_graphics_accelerate.md#opengtx_resolutionvalue) | 此结构体描述游戏应用的分辨率值。 |
| typedef struct [OpenGTX\_Vector3](_open_g_t_x___vector3.md) [OpenGTX\_Vector3](_graphics_accelerate.md#opengtx_vector3) | 此结构体描述OpenGTX三维向量。 |
| typedef struct [OpenGTX\_NetworkLatency](_open_g_t_x___network_latency.md) [OpenGTX\_NetworkLatency](_graphics_accelerate.md#opengtx_networklatency) | 此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。该参数通常用于针对性优化网络延迟。 |
| typedef void(\* [OpenGTX\_DeviceInfoCallback](_graphics_accelerate.md#opengtx_deviceinfocallback)) ([OpenGTX\_TempLevel](_graphics_accelerate.md#opengtx_templevel-1)) | 设备的温度信息回调。 |

### 枚举

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) {  OPENGTX\_SUCCESS = 0,  OPENGTX\_INVALID\_PARAMETER = 401,  OPENGTX\_CONTEXT\_NOT\_CONFIG = 1009502001,  OPENGTX\_CONTEXT\_NOT\_ACTIVE = 1009502002  } | 此枚举描述OpenGTX接口调用错误码。 |
| [OpenGTX\_LTPO\_Mode](_graphics_accelerate.md#opengtx_ltpo_mode-1) {  SCENE\_MODE = 0x0001,  TOUCH\_MODE = 0x0010,  ADAPTIVE\_MODE = 0x0100  } | 此枚举描述OpenGTX\_LTPO模式类型，以控制游戏中的帧率。 |
| [OpenGTX\_EngineType](_graphics_accelerate.md#opengtx_enginetype-1) {  UNITY = 1,  UNREAL = 2,  MESSIAH = 3,  COCOS = 4,  OTHERS\_ENGINE = 100  } | 此枚举描述游戏应用的底层游戏引擎类型。 |
| [OpenGTX\_GameType](_graphics_accelerate.md#opengtx_gametype-1) {  MOBA = 1,  RPG = 2,  FPS = 3,  RAC = 4,  OTHERS\_TYPE = 100  } | 此枚举描述游戏应用的类型。 |
| [OpenGTX\_SceneID](_graphics_accelerate.md#opengtx_sceneid-1) {  LOGIN = 1,  GAME\_INTERFACE = 2,  LOADING = 3,  PLAYING = 4,  SPECTATOR = 5,  DEATH = 6,  HEAVY\_LOAD = 7,  OTHERS\_SCENE = 100  } | 此枚举描述OpenGTX算法的游戏场景类型。 |
| [OpenGTX\_PictureQualityMaxLevel](_graphics_accelerate.md#opengtx_picturequalitymaxlevel-1) {  SD = 1,  HD = 2,  FHD = 3,  QHD = 4,  UHD = 5  } | 此枚举描述游戏应用的图像质量。 |
| [OpenGTX\_TempLevel](_graphics_accelerate.md#opengtx_templevel-1) {  TEMP\_LEVEL1 = 1,  TEMP\_LEVEL2 = 2,  TEMP\_LEVEL3 = 3,  TEMP\_LEVEL4 = 4,  TEMP\_LEVEL5 = 5,  TEMP\_LEVEL6 = 6  } | 此枚举描述设备的温度级别。 |

### 函数

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* [HMS\_OpenGTX\_CreateContext](_graphics_accelerate.md#hms_opengtx_createcontext)([OpenGTX\_DeviceInfoCallback](_graphics_accelerate.md#opengtx_deviceinfocallback) deviceInfoCallback) | 创建OpenGTX上下文实例，每次调用会新建[OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)对象，并返回指向[OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)对象的指针。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_Activate](_graphics_accelerate.md#hms_opengtx_activate)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context) | 激活OpenGTX上下文实例。使用OpenGTX上下文实例前需要激活实例。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_Deactivate](_graphics_accelerate.md#hms_opengtx_deactivate)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context) | 去激活OpenGTX上下文实例，可通过[HMS\_OpenGTX\_Activate](_graphics_accelerate.md#hms_opengtx_activate)重新激活。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_SetConfiguration](_graphics_accelerate.md#hms_opengtx_setconfiguration)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context, const [OpenGTX\_ConfigDescription](_open_g_t_x___config_description.md)\* config) | 初始化OpenGTX上下文实例，配置OpenGTX实例属性。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_DispatchFrameRenderInfo](_graphics_accelerate.md#hms_opengtx_dispatchframerenderinfo)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context, const [OpenGTX\_FrameRenderInfo](_open_g_t_x___frame_render_info.md)\* frameRenderInfo) | 设置OpenGTX运行所需的场景渲染关键信息，每帧变化均需要更新。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_DispatchGameSceneInfo](_graphics_accelerate.md#hms_opengtx_dispatchgamesceneinfo)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context, const [OpenGTX\_GameSceneInfo](_open_g_t_x___game_scene_info.md)\* gameSceneInfo) | 设置OpenGTX运行所需的游戏场景信息。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_DispatchNetworkInfo](_graphics_accelerate.md#hms_opengtx_dispatchnetworkinfo)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\* context, const [OpenGTX\_NetworkInfo](_open_g_t_x___network_info.md)\* networkInfo) | 设置OpenGTX运行所需的网络延迟信息。 |
| [OpenGTX\_ErrorCode](_graphics_accelerate.md#opengtx_errorcode-1) [HMS\_OpenGTX\_DestroyContext](_graphics_accelerate.md#hms_opengtx_destroycontext)([OpenGTX\_Context](_graphics_accelerate.md#opengtx_context)\*\* context) | 销毁OpenGTX上下文实例并释放内存资源。 |
