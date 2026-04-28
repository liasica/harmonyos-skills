---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dispatch_description___g_l_e_s
title: FG_DispatchDescription_GLES
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > C API > 头文件和结构体 > 结构体 > FG_DispatchDescription_GLES
category: harmonyos-references
scraped_at: 2026-04-28T08:15:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:280ca6b5406a6687a2c9bb5bc1411eb66cf6f40bf921a917138d7ed2891b635c
---

## 概述

PhoneTabletTV

此结构体描述下发帧生成命令[HMS\_FG\_Dispatch\_GLES](_graphics_accelerate.md#hms_fg_dispatch_gles)需要的参数信息，每一帧都需要进行更新。该接口仅适配OpenGL ES图形API平台。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](_graphics_accelerate.md)

**所在头文件：** [frame\_generation\_gles.h](frame__generation__gles_8h.md)

## 汇总

PhoneTabletTV

### 成员变量

PhoneTabletTV

| 名称 | 描述 |
| --- | --- |
| uint32\_t [inputColor](_f_g___dispatch_description___g_l_e_s.md#inputcolor) | 真实渲染帧颜色缓冲区索引，支持格式包括GL\_RGBA8、GL\_R11F\_G11F\_B10F、GL\_RGBA16F。  取值范围：[0, 2^32 -1]。 |
| uint32\_t [inputDepthStencil](_f_g___dispatch_description___g_l_e_s.md#inputdepthstencil) | 真实渲染帧深度模板缓冲区索引，支持格式包括GL\_DEPTH24\_STENCIL8、GL\_DEPTH32F\_STENCIL8。  取值范围：[0, 2^32 -1]。 |
| [FG\_Mat4x4](_f_g___mat4x4.md) [viewProj](_f_g___dispatch_description___g_l_e_s.md#viewproj) | 真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| [FG\_Mat4x4](_f_g___mat4x4.md) [invViewProj](_f_g___dispatch_description___g_l_e_s.md#invviewproj) | 真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。 |
| uint32\_t [outputColor](_f_g___dispatch_description___g_l_e_s.md#outputcolor) | 预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL\_RGBA8、GL\_R11F\_G11F\_B10F、GL\_RGBA16F。  取值范围：[0, 2^32 -1]。 |

## 结构体成员变量说明

PhoneTabletTV

### inputColor

PhoneTabletTV

```
1. uint32_t FG_DispatchDescription_GLES::inputColor
```

**描述**

真实渲染帧颜色缓冲区索引，支持格式包括GL\_RGBA8、GL\_R11F\_G11F\_B10F、GL\_RGBA16F。

### inputDepthStencil

PhoneTabletTV

```
1. uint32_t FG_DispatchDescription_GLES::inputDepthStencil
```

**描述**

真实渲染帧深度模板缓冲区索引，支持格式包括GL\_DEPTH24\_STENCIL8、GL\_DEPTH32F\_STENCIL8。

### invViewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_DispatchDescription_GLES::invViewProj
```

**描述**

真实渲染帧逆视图投影矩阵，即相机裁剪空间到世界空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。

### outputColor

PhoneTabletTV

```
1. uint32_t FG_DispatchDescription_GLES::outputColor
```

**描述**

预测帧缓冲区索引，此预测帧缓冲区需要用户创建并输入，支持格式包括GL\_RGBA8、GL\_R11F\_G11F\_B10F、GL\_RGBA16F。

### viewProj

PhoneTabletTV

```
1. FG_Mat4x4 FG_DispatchDescription_GLES::viewProj
```

**描述**

真实渲染帧视图投影矩阵，即世界空间到相机裁剪空间坐标系转换矩阵，矩阵必须是4x4列主序的矩阵。
