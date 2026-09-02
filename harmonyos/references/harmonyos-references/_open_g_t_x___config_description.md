---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description
title: OpenGTX_ConfigDescription
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_ConfigDescription
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dcf3290461bbf81e55fb7e4016beffdf4ada536c2c7c6d22aaafc25bb8a5bb3e
---

## 概述

此结构体描述OpenGTX属性配置。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_LTPO\_Mode](_graphics_accelerate.md#opengtx_ltpo_mode-1) [mode](_open_g_t_x___config_description.md#mode) | LTPO方案模式，支持场景模式、触控模式、自适应模式。 |
| int32\_t [targetFPS](_open_g_t_x___config_description.md#targetfps) | 游戏应用目标帧率，取值范围[30,144]。 |
| char\* [packageName](_open_g_t_x___config_description.md#packagename) | 游戏包名，字节长度范围[1,256]。 |
| char\* [appVersion](_open_g_t_x___config_description.md#appversion) | 游戏应用版本号，字节长度范围[1,256]。 |
| [OpenGTX\_EngineType](_graphics_accelerate.md#opengtx_enginetype-1) [engineType](_open_g_t_x___config_description.md#enginetype) | 游戏引擎类型。 |
| char\* [engineVersion](_open_g_t_x___config_description.md#engineversion) | 游戏引擎版本号，字节长度范围[0,256]。 |
| [OpenGTX\_GameType](_graphics_accelerate.md#opengtx_gametype-1) [gameType](_open_g_t_x___config_description.md#gametype) | 游戏类型。 |
| [OpenGTX\_PictureQualityMaxLevel](_graphics_accelerate.md#opengtx_picturequalitymaxlevel-1) [pictureQualityMaxLevel](_open_g_t_x___config_description.md#picturequalitymaxlevel) | 图像质量。 |
| [OpenGTX\_ResolutionValue](_open_g_t_x___resolution_value.md) [resolutionMaxValue](_open_g_t_x___config_description.md#resolutionmaxvalue) | 游戏应用支持的最高分辨率，取值范围360p-8k。 |
| int32\_t [gameMainThreadId](_open_g_t_x___config_description.md#gamemainthreadid) | 游戏应用的逻辑线程ID，取值范围[0,∞)。 |
| int32\_t [gameRenderThreadId](_open_g_t_x___config_description.md#gamerenderthreadid) | 游戏应用的渲染线程ID，取值范围[0,∞)。 |
| int32\_t [gameKeyThreadIds](_open_g_t_x___config_description.md#gamekeythreadids5) [5] | 游戏应用的关键线程ID列表，取值范围[0,∞)。 |
| bool [vulkanSupport](_open_g_t_x___config_description.md#vulkansupport) | 是否支持Vulkan。  取值范围：[true, false]。 |

## 结构体成员变量说明

### appVersion

```c
char* OpenGTX_ConfigDescription::appVersion
```

**描述**

游戏应用版本号，字节长度范围[1,256]。

### engineType

```c
OpenGTX_EngineType OpenGTX_ConfigDescription::engineType
```

**描述**

游戏引擎类型。

### engineVersion

```c
char* OpenGTX_ConfigDescription::engineVersion
```

**描述**

游戏引擎版本号，字节长度范围[0,256]。

### gameKeyThreadIds[5]

```c
int32_t OpenGTX_ConfigDescription::gameKeyThreadIds[5]
```

**描述**

游戏应用的关键线程ID列表，取值范围[0,∞)。

### gameMainThreadId

```c
int32_t OpenGTX_ConfigDescription::gameMainThreadId
```

**描述**

游戏应用的逻辑线程ID，取值范围[0,∞)。

### gameRenderThreadId

```c
int32_t OpenGTX_ConfigDescription::gameRenderThreadId
```

**描述**

游戏应用的渲染线程ID，取值范围[0,∞)。

### gameType

```c
OpenGTX_GameType OpenGTX_ConfigDescription::gameType
```

**描述**

游戏类型。

### mode

```c
OpenGTX_LTPO_Mode OpenGTX_ConfigDescription::mode
```

**描述**

LTPO方案模式，支持场景模式、触控模式、自适应模式。

### packageName

```c
char* OpenGTX_ConfigDescription::packageName
```

**描述**

游戏包名，字节长度范围[1,256]。

### pictureQualityMaxLevel

```c
OpenGTX_PictureQualityMaxLevel OpenGTX_ConfigDescription::pictureQualityMaxLevel
```

**描述**

图像质量。

### resolutionMaxValue

```c
OpenGTX_ResolutionValue OpenGTX_ConfigDescription::resolutionMaxValue
```

**描述**

游戏应用支持的最高分辨率，取值范围360p-8k。

### targetFPS

```c
int32_t OpenGTX_ConfigDescription::targetFPS
```

**描述**

游戏应用目标帧率，取值范围[30,144]。

### vulkanSupport

```c
bool OpenGTX_ConfigDescription::vulkanSupport
```

**描述**

是否支持Vulkan。
