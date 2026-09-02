---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___frame_render_info
title: OpenGTX_FrameRenderInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > OpenGTX_FrameRenderInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:538f4fc3a5a4fc4bb5bdaf4432cf33140b06145831c66e7580f8f1e616f72700
---

## 概述

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。该参数中的相机矩阵通常用于优化渲染层降负载方案的画质效果。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [opengtx\_base.h](opengtx__base_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OpenGTX\_Vector3](_open_g_t_x___vector3.md) [mainCameraPosition](_open_g_t_x___frame_render_info.md#maincameraposition) | 主摄像头的位置。x、y、z的取值范围均为[-360, 360]，超出取值范围则该值不生效，并且返回[401](errorcode-universal.md#section401-参数检查失败)错误码。单位：deg。 |
| [OpenGTX\_Vector3](_open_g_t_x___vector3.md) [mainCameraRotate](_open_g_t_x___frame_render_info.md#maincamerarotate) | 主摄像头的转动，包括偏航、俯仰、侧滚。x、y、z的取值范围均为[-360, 360]，超出取值范围则该值不生效，并且返回[401](errorcode-universal.md#section401-参数检查失败)错误码。单位：deg。 |

## 结构体成员变量说明

### mainCameraPosition

```c
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraPosition
```

**描述**

主摄像头的位置。x、y、z的取值范围均为[-360, 360]，超出取值范围则该值不生效，并且返回[401](errorcode-universal.md#section401-参数检查失败)错误码。单位：deg。

### mainCameraRotate

```c
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraRotate
```

**描述**

主摄像头的转动，包括偏航、俯仰、侧滚。x、y、z的取值范围均为[-360, 360]，超出取值范围则该值不生效，并且返回[401](errorcode-universal.md#section401-参数检查失败)错误码。单位：deg。
