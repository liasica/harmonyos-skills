---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadcoefficients
title: FAST_BiquadCoefficients
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadCoefficients
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2af36aac80e2f1fd094ef5acd9b100741db5a3db3d348e75f2f67210c8cbeae8
---

## 概述

定义单精度二阶（biquad）IIR滤波器节的系数（直接I型或II型）。

传递函数：H(z) = (b0 + b1z⁻¹ + b2z⁻²) / (1 + a1z⁻¹ + a2z⁻²)

**注意** 

分母中的1实际上为系数a0归一化后的结果。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_dsp\_common.h](fast-kit-fast-dsp-common-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float [a1](fast-kit--fast-biquadcoefficients.md#a1) | z⁻¹ 分母系数。 |
| float [a2](fast-kit--fast-biquadcoefficients.md#a2) | z⁻² 分母系数。 |
| float [b0](fast-kit--fast-biquadcoefficients.md#b0) | z⁰ 分子系数。 |
| float [b1](fast-kit--fast-biquadcoefficients.md#b1) | z⁻¹ 分子系数。 |
| float [b2](fast-kit--fast-biquadcoefficients.md#b2) | z⁻² 分子系数。 |

## 结构体成员变量说明

### a1

```c
float FAST_BiquadCoefficients::a1
```

**描述**

z⁻¹ 分母系数。

### a2

```c
float FAST_BiquadCoefficients::a2
```

**描述**

z⁻² 分母系数。

### b0

```c
float FAST_BiquadCoefficients::b0
```

**描述**

z⁰ 分子系数。

### b1

```c
float FAST_BiquadCoefficients::b1
```

**描述**

z⁻¹ 分子系数。

### b2

```c
float FAST_BiquadCoefficients::b2
```

**描述**

z⁻² 分子系数。
