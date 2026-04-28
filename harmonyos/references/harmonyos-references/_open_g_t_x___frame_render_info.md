---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___frame_render_info
title: OpenGTX_FrameRenderInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_FrameRenderInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b18f168d83a16129c057ad0895db1143bb68463969223dcd499ae8733340d868
---

## 概述

PhoneTabletTV

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。该参数中的相机矩阵通常用于优化渲染层降负载方案的画质效果。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_Vector3](_open_g_t_x___vector3.md) [mainCameraPosition](_open_g_t_x___frame_render_info.md#maincameraposition) | 主摄像头的位置。x, y, z的取值范围[-360,360]。 |
| [OpenGTX\_Vector3](_open_g_t_x___vector3.md) [mainCameraRotate](_open_g_t_x___frame_render_info.md#maincamerarotate) | 主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。 |

## 结构体成员变量说明

PhoneTabletTV

### mainCameraPosition

PhoneTabletTV

```
1. OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraPosition
```

**描述**

主摄像头的位置。

### mainCameraRotate

PhoneTabletTV

```
1. OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraRotate
```

**描述**

主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围[-360,360]。
