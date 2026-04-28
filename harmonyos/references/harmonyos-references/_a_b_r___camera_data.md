---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_a_b_r___camera_data
title: ABR_CameraData
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > ABR_CameraData
category: harmonyos-references
scraped_at: 2026-04-28T08:15:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98cf4945dfe57684d262864de47faccfb020b5b639b48ccab660f593faf87134
---

## 概述

PhoneTabletTV

此结构体描述游戏应用每帧的相机运动数据，ABR会结合相机运动数据自适应调整FrameBuffer（帧缓冲，下文简称Buffer）分辨率因子。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [abr\_base.h](abr__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [ABR\_Vector3](_a_b_r___vector3.md) [rotation](_a_b_r___camera_data.md#rotation) | 相机变换的世界空间旋转欧拉角。取值范围：[0, 360]，参数不在范围内会返回ABR\_INVALID\_PARAMETER错误码。 |
| [ABR\_Vector3](_a_b_r___vector3.md) [position](_a_b_r___camera_data.md#position) | 相机变换的世界空间位移。 |

## 结构体成员变量说明

PhoneTabletTV

### position

PhoneTabletTV

```
1. ABR_Vector3 ABR_CameraData::position
```

**描述**

相机变换的世界空间位移。

### rotation

PhoneTabletTV

```
1. ABR_Vector3 ABR_CameraData::rotation
```

**描述**

相机变换的世界空间旋转欧拉角。取值范围：[0, 360]，参数不在范围内会返回ABR\_INVALID\_PARAMETER错误码。
