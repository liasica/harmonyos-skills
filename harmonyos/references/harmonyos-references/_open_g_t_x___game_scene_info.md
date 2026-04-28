---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___game_scene_info
title: OpenGTX_GameSceneInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_GameSceneInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8de496f3d902e13333fd42bdb5e4111e088cfc003121e2b99dc15e28658d45e
---

## 概述

PhoneTabletTV

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_SceneID](_graphics_accelerate.md#opengtx_sceneid-1) [sceneID](_open_g_t_x___game_scene_info.md#sceneid) | 游戏场景类型。 |
| char\* [description](_open_g_t_x___game_scene_info.md#description) | 对游戏场景的描述，字节长度范围[0,256]。 |
| int32\_t [recommendFPS](_open_g_t_x___game_scene_info.md#recommendfps) | 当前场景的建议帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。 |
| int32\_t [minFPS](_open_g_t_x___game_scene_info.md#minfps) | 当前场景预期的最小帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。 |
| int32\_t [maxFPS](_open_g_t_x___game_scene_info.md#maxfps) | 当前场景预期的最大帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。 |
| [OpenGTX\_ResolutionValue](_open_g_t_x___resolution_value.md) [resolutionCurValue](_open_g_t_x___game_scene_info.md#resolutioncurvalue) | 当前场景的分辨率，取值范围360p-8k。 |

## 结构体成员变量说明

PhoneTabletTV

### description

PhoneTabletTV

```
1. char* OpenGTX_GameSceneInfo::description
```

**描述**

对游戏场景的描述，字节长度范围[0,256]。

### maxFPS

PhoneTabletTV

```
1. int32_t OpenGTX_GameSceneInfo::maxFPS
```

**描述**

当前场景预期的最大帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。

### minFPS

PhoneTabletTV

```
1. int32_t OpenGTX_GameSceneInfo::minFPS
```

**描述**

当前场景预期的最小帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。

### recommendFPS

PhoneTabletTV

```
1. int32_t OpenGTX_GameSceneInfo::recommendFPS
```

**描述**

当前场景的建议帧率。取值范围0、[30,[targetFPS](_open_g_t_x___config_description.md#targetfps)]，若设置0则该值不生效。

### resolutionCurValue

PhoneTabletTV

```
1. OpenGTX_ResolutionValue OpenGTX_GameSceneInfo::resolutionCurValue
```

**描述**

当前场景的分辨率，取值范围360p-8k。

### sceneID

PhoneTabletTV

```
1. OpenGTX_SceneID OpenGTX_GameSceneInfo::sceneID
```

**描述**

游戏场景类型。
