---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit--fast-biquadstate
title: FAST_BiquadState
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 结构体 > FAST_BiquadState
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eae7c57555e5a654560da0df296556f2b0657265b1e9e79f60e4914f8b643e8e
---

## 概述

定义单精度二阶IIR滤波器节的状态变量。

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](fast-kit-fast.md)

**所在头文件：** [fast\_dsp\_common.h](fast-kit-fast-dsp-common-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float [d1](fast-kit--fast-biquadstate.md#d1) | 第一个延迟单元（y[n-1]）。 |
| float [d2](fast-kit--fast-biquadstate.md#d2) | 第二个延迟单元（y[n-2]）。 |

## 结构体成员变量说明

### d1

```c
float FAST_BiquadState::d1
```

**描述**

第一个延迟单元，存储上一时刻的输出值y[n-1]。

### d2

```c
float FAST_BiquadState::d2
```

**描述**

第二个延迟单元，存储上上时刻的输出值y[n-2]。
