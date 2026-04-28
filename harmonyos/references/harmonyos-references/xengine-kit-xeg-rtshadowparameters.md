---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowparameters
title: XEG_RTShadowParameters
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTShadowParameters
category: harmonyos-references
scraped_at: 2026-04-28T08:16:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6a5db5b55dcaff9a88ec57d7616db95563f036550a70a8831cff2f59063107de
---

## 概述

PhonePC/2in1TabletTV

光线追踪阴影（Shadow）算法参数。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_visible\_mask.h](xengine-kit-xeg-vulkan-rt-visible-mask-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| float [rayTMax](xengine-kit-xeg-rtshadowparameters.md#raytmax) | 阴影光线的tMax值。 |
| float [rayTMin](xengine-kit-xeg-rtshadowparameters.md#raytmin) | 阴影光线的tMin值。 |
| float [sunDirection](xengine-kit-xeg-rtshadowparameters.md#sundirection) [3] | 方向光的方向。 |
| float [raySourceAngleInDegree](xengine-kit-xeg-rtshadowparameters.md#raysourceangleindegree) = 0.0f | 沿光源方向进行阴影采样的角度范围，值越大，半影区域越大。此参数的值将被限制在[0.0, 90.0]范围内。默认值为0.0。 |
| uint32\_t [shadowCullMask](xengine-kit-xeg-rtshadowparameters.md#shadowcullmask) = 0x5FF | 配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数，高24bit表示rayFlags，低8bit表示cullMask。 默认值为0x5FF，即 ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF。 |
| float [shadowCullDistance](xengine-kit-xeg-rtshadowparameters.md#shadowculldistance) | 阴影剔除的世界空间距离，场景中像素超过此距离时不计算阴影，必须大于0。 |
| uint32\_t [rayPerPixel](xengine-kit-xeg-rtshadowparameters.md#rayperpixel) = 1 | 每像素采样数，当前仅支持1spp。默认值为1。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### rayPerPixel

PhonePC/2in1TabletTV

```
1. uint32_t XEG_RTShadowParameters::rayPerPixel = 1
```

**描述**

每像素采样数，当前仅支持1spp。默认值为1。

### raySourceAngleInDegree

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowParameters::raySourceAngleInDegree = 0.0f
```

**描述**

沿光源方向进行阴影采样的角度范围，值越大，半影区域越大。此参数的值将被限制在[0.0, 90.0]范围内。默认值为0.0。

### rayTMax

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowParameters::rayTMax
```

**描述**

阴影光线的tMax值。

### rayTMin

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowParameters::rayTMin
```

**描述**

阴影光线的tMin值。

### shadowCullDistance

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowParameters::shadowCullDistance
```

**描述**

阴影剔除的世界空间距离，场景中像素超过此距离时不计算阴影，必须大于0。

### shadowCullMask

PhonePC/2in1TabletTV

```
1. uint32_t XEG_RTShadowParameters::shadowCullMask = 0x5FF
```

**描述**

配置光线查询[rayQueryInitializeEXT](https://github.com/KhronosGroup/GLSL/blob/main/extensions/ext/GLSL_EXT_ray_query.txt)函数中的rayFlags和cullMask参数，高24bit表示rayFlags，低8bit表示cullMask。 默认值为0x5FF，即 ((gl\_RayFlagsOpaqueEXT | gl\_RayFlagsTerminateOnFirstHitEXT) << 8) | 0xFF。

### sunDirection

PhonePC/2in1TabletTV

```
1. float XEG_RTShadowParameters::sunDirection[3]
```

**描述**

方向光的方向。
