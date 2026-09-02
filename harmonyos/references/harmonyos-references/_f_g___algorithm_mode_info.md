---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___algorithm_mode_info
title: FG_AlgorithmModeInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_AlgorithmModeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:47+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e24cbb2e0e181d7da7a2174c9ade78acffb1049a0c52f58b9829eab099a71c57
---

## 概述

此结构体描述超帧算法模式信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](frame__generation__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [FG\_PredictionMode](_graphics_accelerate.md#fg_predictionmode-1) [predictionMode](_f_g___algorithm_mode_info.md#predictionmode) | 超帧预测算法模式，支持内插模式和外插模式。 |
| [FG\_MeMode](_graphics_accelerate.md#fg_memode-1) [meMode](_f_g___algorithm_mode_info.md#memode) | 超帧运动估计算法模式，支持基础模式和增强模式。 |

## 结构体成员变量说明

### meMode

```c
FG_MeMode FG_AlgorithmModeInfo::meMode
```

**描述**

超帧运动估计算法模式，支持基础模式和增强模式。

### predictionMode

```c
FG_PredictionMode FG_AlgorithmModeInfo::predictionMode
```

**描述**

超帧预测算法模式，支持内插模式和外插模式。
