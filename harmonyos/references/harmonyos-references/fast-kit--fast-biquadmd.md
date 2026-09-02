---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadmd
title: FAST_BiquadmD
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadmD
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:de00bb4c85409d1f64319ad28480357bc6ad20c1b84a44efa1223c48cba743c6
---

## 概述

定义双精度多通道、多节二阶IIR滤波器组的数据结构。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_dsp\_common.h](fast-kit-fast-dsp-common-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t\* [activeFilters](fast-kit--fast-biquadmd.md#activefilters) | 活跃滤波器掩码数组。 |
| uint8\_t [isInitialized](fast-kit--fast-biquadmd.md#isinitialized) | 初始化标志。 |
| double\* [channelGains](fast-kit--fast-biquadmd.md#channelgains) | 每通道线性增益因子数组。 |
| FAST\_BiquadCoefficientsD\* [coefficients](fast-kit--fast-biquadmd.md#coefficients) | 滤波器系数数组。 |
| size\_t [maxFrames](fast-kit--fast-biquadmd.md#maxframes) | 单次处理最大采样数。 |
| size\_t [numChannels](fast-kit--fast-biquadmd.md#numchannels) | 音频或信号通道数。 |
| size\_t [numSections](fast-kit--fast-biquadmd.md#numsections) | 每通道级联的 biquad 节数。 |
| FAST\_BiquadStateD\* [states](fast-kit--fast-biquadmd.md#states) | 滤波器状态数组。 |

## 结构体成员变量说明

### activeFilters

```c
uint8_t* FAST_BiquadmD::activeFilters
```

**描述**

活跃滤波器掩码数组（大小为[numSections](fast-kit--fast-biquadmd.md#numsections)），非零表示该节滤波器处于激活状态。

### channelGains

```c
double* FAST_BiquadmD::channelGains
```

**描述**

每通道线性增益因子数组（大小为[numChannels](fast-kit--fast-biquadmd.md#numchannels)），用于对每个通道的输出进行增益调整。

### coefficients

```c
FAST_BiquadCoefficientsD* FAST_BiquadmD::coefficients
```

**描述**

滤波器系数数组（大小为[numChannels](fast-kit--fast-biquadmd.md#numchannels) \* [numSections](fast-kit--fast-biquadmd.md#numsections)），存储所有通道的所有滤波器节系数。

### isInitialized

```c
uint8_t FAST_BiquadmD::isInitialized
```

**描述**

初始化标志，值为1表示结构体已正确初始化，值为0表示未初始化。

### maxFrames

```c
size_t FAST_BiquadmD::maxFrames
```

**描述**

单次处理的最大采样数（每通道），处理长度不能超过此值。

### numChannels

```c
size_t FAST_BiquadmD::numChannels
```

**描述**

音频或信号通道数，必须大于0。

### numSections

```c
size_t FAST_BiquadmD::numSections
```

**描述**

每通道级联的biquad节数，必须大于0。

### states

```c
FAST_BiquadStateD* FAST_BiquadmD::states
```

**描述**

滤波器状态数组（大小为[numChannels](fast-kit--fast-biquadmd.md#numchannels) \* [numSections](fast-kit--fast-biquadmd.md#numsections)），存储所有通道的所有滤波器节状态变量。
