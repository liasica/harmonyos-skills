---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___intergration_info
title: FG_IntegrationInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_IntegrationInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2726a6b927319baddfab50b0e76692184f22d2a780c176c787901431c1652a27
---

## 概述

PhoneTabletTV

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

**起始版本**：5.1.0(18)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](frame__generation__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_PresentMode](_graphics_accelerate.md#fg_presentmode) [presentMode](_f_g___intergration_info.md#presentmode) | 预测帧展示模式。取值为FG\_PRESENT\_BY\_SYSTEM时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。 |
| bool [textureCachedByGame](_f_g___intergration_info.md#texturecachedbygame) | 深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。  取值范围：[true, false]。 |
| bool [needFlipInputColor](_f_g___intergration_info.md#needflipinputcolor) | 输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。  取值范围：[true, false]。 |
| bool [needFlipOutputColor](_f_g___intergration_info.md#needflipoutputcolor) | 预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。  取值范围：[true, false]。 |

## 结构体成员变量说明

PhoneTabletTV

### presentMode

PhoneTabletTV

```
1. FG_PresentMode FG_IntegrationInfo::presentMode
```

**描述**

展示模式。

### textureCachedByGame

PhoneTabletTV

```
1. bool FG_IntegrationInfo::textureCachedByGame
```

**描述**

深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。

### needFlipInputColor

PhoneTabletTV

```
1. bool FG_IntegrationInfo::needFlipInputColor
```

**描述**

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。

### needFlipOutputColor

PhoneTabletTV

```
1. bool FG_IntegrationInfo::needFlipOutputColor
```

**描述**

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。
