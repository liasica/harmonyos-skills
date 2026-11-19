---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-poly
title: FAST_Poly
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_Poly
category: harmonyos-references
scraped_at: 2026-11-19T09:53:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce4460696b04280022914d2ce3c7ebafe0c18edc09a735c4261eaf892fde2255
---

## 概述

定义稀疏格式多项式的数据结构。多项式![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/X3ZHAU-GQEG1riZPxrK57Q/zh-cn_image_0000002791568170.png?HW-CC-KV=V1&HW-CC-Date=20261119T015302Z&HW-CC-Expire=31536000000&HW-CC-Sign=60942E67299619D596F8A34715AB55B2C00CC8B969F9EFDB899FDE0F0A1C5997)由系数数组coeff和指数数组pow共同描述，且需按指数升序排列。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_solver\_polynomial.h](fast-kit-fast-solver-polynomial-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double \* [coeff](fast-kit--fast-poly.md#coeff) | 多项式的系数数组。 |
| uint32\_t \* [pow](fast-kit--fast-poly.md#pow) | 多项式的指数数组。 |
| size\_t [length](fast-kit--fast-poly.md#length) | 多项式的项数。 |

## 结构体成员变量说明

### coeff

```c
double * FAST_Poly::coeff
```

**描述**

多项式的系数数组，与pow数组一一对应，表示对应指数项的系数值。

### length

```c
size_t FAST_Poly::length
```

**描述**

多项式的项数，即coeff和pow数组的长度。

### pow

```c
uint32_t * FAST_Poly::pow
```

**描述**

多项式的指数数组，与coeff数组一一对应，且需按指数升序排列。
