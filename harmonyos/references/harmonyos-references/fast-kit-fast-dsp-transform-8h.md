---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-transform-8h
title: fast_dsp_transform.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_dsp_transform.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b76f20976f8d95bca5e7115d0bcae0b57404d6cd55ef598116d5b740132256b5
---

## 概述

提供高性能数字信号处理（DSP）变换函数，包括FFT（快速傅里叶变换）、IFFT（逆快速傅里叶变换）等。

**引用文件：** <FASTKit/fast\_dsp\_transform.h>

**库：** libfast\_dsp.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 26.0.0

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig) [FAST\_FFTConfig](fast-kit-fast.md#fast_fftconfig) | 快速傅里叶变换的不透明配置。 |

### 常量

| 名称 | 描述 |
| --- | --- |
| const uint32\_t [FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n) = 16 | FFT支持的最大点数对应的以2为底的对数值。值为16，即最大点数为65536。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfig](fast-kit-fast.md#hms_fast_fft_createconfig) (FAST\_FFTConfig\*\* config, const uint32\_t log2n) | 创建单精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfigD](fast-kit-fast.md#hms_fast_fft_createconfigd) (FAST\_FFTConfig\*\* config, const uint32\_t log2n) | 创建双精度FFT配置对象（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| void [HMS\_FAST\_FFT\_DestroyConfig](fast-kit-fast.md#hms_fast_fft_destroyconfig) (FAST\_FFTConfig\* config) | 销毁FFT配置对象并释放资源。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransform](fast-kit-fast.md#hms_fast_fft_forwardtransform) (FAST\_FFTConfig\* config, const uint32\_t length, const float input[], float outputRe[], float outputIm[]) | 计算单精度实数时域信号的DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransformD](fast-kit-fast.md#hms_fast_fft_forwardtransformd) (FAST\_FFTConfig\* config, const uint32\_t length, const double input[], double outputRe[], double outputIm[]) | 计算双精度实数时域信号的DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransform](fast-kit-fast.md#hms_fast_fft_inversetransform) (FAST\_FFTConfig\* config, const uint32\_t length, const float inputRe[], const float inputIm[], float output[]) | 计算单精度复数频域序列的逆DFT。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransformD](fast-kit-fast.md#hms_fast_fft_inversetransformd) (FAST\_FFTConfig\* config, const uint32\_t length, const double inputRe[], const double inputIm[], double output[]) | 计算双精度复数频域序列的逆DFT。 |
