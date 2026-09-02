---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___intergration_info
title: FG_IntegrationInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_IntegrationInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6f19358260ca284cca2e81b65525ee2abba66bdb2e15e5bd1eeacc6a95fac528
---

## 概述

此结构体描述超帧集成的信息。包括送显模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

**起始版本**：5.1.0(18)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](frame__generation__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FG\_PresentMode](_graphics_accelerate.md#fg_presentmode) [presentMode](_f_g___intergration_info.md#presentmode) | 预测帧展示模式。 |
| bool [textureCachedByGame](_f_g___intergration_info.md#texturecachedbygame) | 深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。  false：算法自行缓存和管理纹理，默认值。  true：直接使用游戏缓存，不再额外缓存。 |
| bool [needFlipInputColor](_f_g___intergration_info.md#needflipinputcolor) | 输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。  false：不需要翻转，默认值。  true：需要翻转。 |
| bool [needFlipOutputColor](_f_g___intergration_info.md#needflipoutputcolor) | 预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。  false：不需要翻转，默认值。  true：需要翻转。 |

## 结构体成员变量说明

### presentMode

```c
FG_PresentMode FG_IntegrationInfo::presentMode
```

**描述**

预测帧展示模式。

### textureCachedByGame

```c
bool FG_IntegrationInfo::textureCachedByGame
```

**描述**

深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。

### needFlipInputColor

```c
bool FG_IntegrationInfo::needFlipInputColor
```

**描述**

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。

### needFlipOutputColor

```c
bool FG_IntegrationInfo::needFlipOutputColor
```

**描述**

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。
