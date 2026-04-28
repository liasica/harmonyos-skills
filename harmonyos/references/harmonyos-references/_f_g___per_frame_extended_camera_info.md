---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___per_frame_extended_camera_info
title: FG_PerFrameExtendedCameraInfo
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_PerFrameExtendedCameraInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:15:47+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:2bcb607e11ac4cb1fe8c4d525276de2357f02cc97b418716544d3adb8681321f
---

## 概述

PhoneTabletTV

此结构体描述相机扩展信息。当视图投影矩阵的平移分量非常大时（超过十万），可以提供更加详细的相机信息以获得更加准确的超帧预测效果。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_base.h](frame__generation__base_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| [FG\_Mat4x4](_f_g___mat4x4.md) proj | 相机投影矩阵，即从视图空间到裁剪空间坐标系的转换矩阵。 |
| [FG\_Mat4x4](_f_g___mat4x4.md) translatedInvViewProj | 平移视图投影矩阵的逆矩阵，即从裁剪空间到以相机为中心的世界空间坐标系的转换矩阵。 |
| [FG\_Mat4x4](_f_g___mat4x4.md) translatedView | 平移视图矩阵，即从以相机为中心的世界空间到视图空间坐标系的转换矩阵。 |
| [FG\_Mat4x4](_f_g___mat4x4.md) translatedViewProj | 平移视图投影矩阵，即从以相机为中心的世界空间到裁剪空间坐标系的转换矩阵。 |
| [FG\_Vec3D](_f_g___vec3_d.md) worldPosition | 相机世界空间坐标。 |

## 结构体成员变量说明

PhoneTabletTV

### proj

PhoneTabletTV

```
1. FG_Mat4x4 FG_PerFrameExtendedCameraInfo::proj
```

**描述**

相机投影矩阵，即从视图空间到裁剪空间坐标系的转换矩阵。

### translatedInvViewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedInvViewProj
```

**描述**

平移视图投影矩阵的逆矩阵，即从裁剪空间到以相机为中心的世界空间坐标系的转换矩阵。

### translatedView

PhoneTabletTV

```
1. FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedView
```

**描述**

平移视图矩阵，即从以相机为中心的世界空间到视图空间坐标系的转换矩阵。

### translatedViewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_PerFrameExtendedCameraInfo::translatedViewProj
```

**描述**

平移视图投影矩阵，即从以相机为中心的世界空间到裁剪空间坐标系的转换矩阵。

### worldPosition

PhoneTabletTV

```
1. FG_Vec3D FG_PerFrameExtendedCameraInfo::worldPosition
```

**描述**

相机世界空间坐标。
