---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___network_latency
title: OpenGTX_NetworkLatency
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_NetworkLatency
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26c375053d561ee0591123718736f588633754214e14357d0344da1a31a552b0
---

## 概述

此结构体描述当前设备网络延迟信息，游戏应用获取到网络延迟后传递此参数。该参数通常用于针对性优化网络延迟。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [total](_open_g_t_x___network_latency.md#total) | 游戏的总时延，单位：ms，取值范围：[0,200]。 |
| int32\_t [up](_open_g_t_x___network_latency.md#up) | 游戏上行时延，单位：ms，取值范围：[0,200]。 |
| int32\_t [down](_open_g_t_x___network_latency.md#down) | 游戏下行时延，单位：ms，取值范围：[0,200]。 |

## 结构体成员变量说明

### down

```c
int32_t OpenGTX_NetworkLatency::down
```

**描述**

游戏下行时延，单位：ms，取值范围：[0,200]。

### total

```c
int32_t OpenGTX_NetworkLatency::total
```

**描述**

游戏的总时延，单位：ms，取值范围：[0,200]。

### up

```c
int32_t OpenGTX_NetworkLatency::up
```

**描述**

游戏上行时延，单位：ms，取值范围：[0,200]。
