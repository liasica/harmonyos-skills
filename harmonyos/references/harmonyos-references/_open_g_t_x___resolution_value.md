---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___resolution_value
title: OpenGTX_ResolutionValue
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_ResolutionValue
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0dd3cc60918a5736e54bdc0c9602f8d76155d0aa402a2a57099ca3a0ced22751
---

## 概述

此结构体描述游戏应用的分辨率值。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t [height](_open_g_t_x___resolution_value.md#height) | 分辨率高度值，以px为单位，取值范围[360,7680]。 |
| int32\_t [width](_open_g_t_x___resolution_value.md#width) | 分辨率宽度值，以px为单位，取值范围[360,7680]。 |

## 结构体成员变量说明

### height

```c
int32_t OpenGTX_ResolutionValue::height
```

**描述**

分辨率高度值，以px为单位，取值范围[360,7680]。

### width

```c
int32_t OpenGTX_ResolutionValue::width
```

**描述**

分辨率宽度值，以px为单位，取值范围[360,7680]。
