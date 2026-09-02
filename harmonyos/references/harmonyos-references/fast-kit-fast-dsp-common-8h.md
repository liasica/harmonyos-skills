---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-dsp-common-8h
title: fast_dsp_common.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_dsp_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:304f4941736d73ea2ee66b3138521f1205b7e0ed9e8565b1d11e17e54131c756
---

## 概述

数字信号处理（DSP）通用数据结构和工具函数定义，包括向量运算、复数处理以及二阶IIR滤波器管理。支持单精度（float）和双精度（double）算术运算。

**引用文件：** <FASTKit/fast\_dsp\_common.h>

**库：** libfast\_dsp.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](fast-kit-fast.md)

## 汇总

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [FAST\_SplitComplex](fast-kit--fast-splitcomplex.md) | 定义单精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct [FAST\_SplitComplexD](fast-kit--fast-splitcomplexd.md) | 定义双精度浮点复数信号的数据结构（分离格式：实部和虚部分开存储）。 |
| struct [FAST\_BiquadCoefficients](fast-kit--fast-biquadcoefficients.md) | 定义单精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadCoefficientsD](fast-kit--fast-biquadcoefficientsd.md) | 定义双精度二阶（biquad）IIR滤波器节的系数。 |
| struct [FAST\_BiquadState](fast-kit--fast-biquadstate.md) | 定义单精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_BiquadStateD](fast-kit--fast-biquadstated.md) | 定义双精度二阶IIR滤波器节的状态变量。 |
| struct [FAST\_Biquadm](fast-kit--fast-biquadm.md) | 定义单精度多通道、多节二阶IIR滤波器组的数据结构。 |
| struct [FAST\_BiquadmD](fast-kit--fast-biquadmd.md) | 定义双精度多通道、多节二阶IIR滤波器组的数据结构。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef struct [FAST\_SplitComplex](fast-kit--fast-splitcomplex.md) [FAST\_SplitComplex](fast-kit--fast-splitcomplex.md) | 单精度浮点复数信号结构体。 |
| typedef struct [FAST\_SplitComplexD](fast-kit--fast-splitcomplexd.md) [FAST\_SplitComplexD](fast-kit--fast-splitcomplexd.md) | 双精度浮点复数信号结构体。 |
| typedef struct [FAST\_BiquadCoefficients](fast-kit--fast-biquadcoefficients.md) [FAST\_BiquadCoefficients](fast-kit--fast-biquadcoefficients.md) | 单精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadCoefficientsD](fast-kit--fast-biquadcoefficientsd.md) [FAST\_BiquadCoefficientsD](fast-kit--fast-biquadcoefficientsd.md) | 双精度二阶IIR滤波器系数。 |
| typedef struct [FAST\_BiquadState](fast-kit--fast-biquadstate.md) [FAST\_BiquadState](fast-kit--fast-biquadstate.md) | 单精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_BiquadStateD](fast-kit--fast-biquadstated.md) [FAST\_BiquadStateD](fast-kit--fast-biquadstated.md) | 双精度二阶IIR滤波器状态。 |
| typedef struct [FAST\_Biquadm](fast-kit--fast-biquadm.md) [FAST\_Biquadm](fast-kit--fast-biquadm.md) | 单精度多通道多节IIR滤波器组。 |
| typedef struct [FAST\_BiquadmD](fast-kit--fast-biquadmd.md) [FAST\_BiquadmD](fast-kit--fast-biquadmd.md) | 双精度多通道多节IIR滤波器组。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [HMS\_FAST\_HannWindowType](fast-kit-fast.md#hms_fast_hannwindowtype-1) {  HMS\_FAST\_HANN\_DENORMALIZE\_FULL = 0x00,  HMS\_FAST\_HANN\_NORMALIZE\_FULL = 0x01,  HMS\_FAST\_HANN\_DENORMALIZE\_HALF = 0x10,  HMS\_FAST\_HANN\_NORMALIZE\_HALF = 0x11  } | 汉宁窗类型枚举。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Maxmgv](fast-kit-fast.md#hms_fast_dsp_maxmgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（单精度）。 |
| double [HMS\_FAST\_DSP\_MaxmgvD](fast-kit-fast.md#hms_fast_dsp_maxmgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Maxvi](fast-kit-fast.md#hms_fast_dsp_maxvi) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实数向量中的最大值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MaxviD](fast-kit-fast.md#hms_fast_dsp_maxvid) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实数向量中的最大值及其索引（双精度）。 |
| float [HMS\_FAST\_DSP\_Meamgv](fast-kit-fast.md#hms_fast_dsp_meamgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（单精度）。 |
| double [HMS\_FAST\_DSP\_MeamgvD](fast-kit-fast.md#hms_fast_dsp_meamgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（双精度）。 |
| float [HMS\_FAST\_DSP\_Sve](fast-kit-fast.md#hms_fast_dsp_sve) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量的和（单精度）。 |
| double [HMS\_FAST\_DSP\_SveD](fast-kit-fast.md#hms_fast_dsp_sved) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量的和（双精度）。 |
| float [HMS\_FAST\_DSP\_Svemg](fast-kit-fast.md#hms_fast_dsp_svemg) (const float\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS\_FAST\_DSP\_SvemgD](fast-kit-fast.md#hms_fast_dsp_svemgd) (const double\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS\_FAST\_DSP\_Dotpr](fast-kit-fast.md#hms_fast_dsp_dotpr) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（单精度）。 |
| double [HMS\_FAST\_DSP\_DotprD](fast-kit-fast.md#hms_fast_dsp_dotprd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsbsm](fast-kit-fast.md#hms_fast_dsp_vsbsm) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float scalar, float\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（单精度）。 |
| void [HMS\_FAST\_DSP\_VsbsmD](fast-kit-fast.md#hms_fast_dsp_vsbsmd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double scalar, double\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（双精度）。 |
| void [HMS\_FAST\_DSP\_Ctoz](fast-kit-fast.md#hms_fast_dsp_ctoz) (const float\* input, size\_t strideInput, FAST\_SplitComplex\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS\_FAST\_DSP\_CtozD](fast-kit-fast.md#hms_fast_dsp_ctozd) (const double\* input, size\_t strideInput, FAST\_SplitComplexD\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Ztoc](fast-kit-fast.md#hms_fast_dsp_ztoc) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS\_FAST\_DSP\_ZtocD](fast-kit-fast.md#hms_fast_dsp_ztocd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFilters](fast-kit-fast.md#hms_fast_biquadm_setactivefilters) (FAST\_Biquadm\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFiltersD](fast-kit-fast.md#hms_fast_biquadm_setactivefiltersd) (FAST\_BiquadmD\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingle](fast-kit-fast.md#hms_fast_biquadm_setcoeffsingle) (FAST\_Biquadm\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDouble](fast-kit-fast.md#hms_fast_biquadm_setcoeffdouble) (FAST\_Biquadm\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingleD](fast-kit-fast.md#hms_fast_biquadm_setcoeffsingled) (FAST\_BiquadmD\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDoubleD](fast-kit-fast.md#hms_fast_biquadm_setcoeffdoubled) (FAST\_BiquadmD\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_Create](fast-kit-fast.md#hms_fast_biquadm_create) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_Biquadm\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_CreateD](fast-kit-fast.md#hms_fast_biquadm_created) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_BiquadmD\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS\_FAST\_Biquadm\_Destroy](fast-kit-fast.md#hms_fast_biquadm_destroy) (FAST\_Biquadm\* filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS\_FAST\_Biquadm\_DestroyD](fast-kit-fast.md#hms_fast_biquadm_destroyd) (FAST\_BiquadmD\* filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm](fast-kit-fast.md#hms_fast_biquadm) (FAST\_Biquadm\* filter, const float\*\* input, const size\_t strideInput, float\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST\_ErrorCode](fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_BiquadmD](fast-kit-fast.md#hms_fast_biquadmd) (FAST\_BiquadmD\* filter, const double\*\* input, const size\_t strideInput, double\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvabs](fast-kit-fast.md#hms_fast_dsp_zvabs) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvabsD](fast-kit-fast.md#hms_fast_dsp_zvabsd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvmags](fast-kit-fast.md#hms_fast_dsp_zvmags) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvmagsD](fast-kit-fast.md#hms_fast_dsp_zvmagsd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvphas](fast-kit-fast.md#hms_fast_dsp_zvphas) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvphasD](fast-kit-fast.md#hms_fast_dsp_zvphasd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsmul](fast-kit-fast.md#hms_fast_dsp_vsmul) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsmulD](fast-kit-fast.md#hms_fast_dsp_vsmuld) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsdiv](fast-kit-fast.md#hms_fast_dsp_vsdiv) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsdivD](fast-kit-fast.md#hms_fast_dsp_vsdivd) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Svdiv](fast-kit-fast.md#hms_fast_dsp_svdiv) (const float scalar, const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_SvdivD](fast-kit-fast.md#hms_fast_dsp_svdivd) (const double scalar, const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsadd](fast-kit-fast.md#hms_fast_dsp_vsadd) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_VsaddD](fast-kit-fast.md#hms_fast_dsp_vsaddd) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（双精度）。 |
| void [HMS\_FAST\_DSP\_Vadd](fast-kit-fast.md#hms_fast_dsp_vadd) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（单精度）。 |
| void [HMS\_FAST\_DSP\_VaddD](fast-kit-fast.md#hms_fast_dsp_vaddd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsub](fast-kit-fast.md#hms_fast_dsp_vsub) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（单精度）。 |
| void [HMS\_FAST\_DSP\_VsubD](fast-kit-fast.md#hms_fast_dsp_vsubd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vmul](fast-kit-fast.md#hms_fast_dsp_vmul) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（单精度）。 |
| void [HMS\_FAST\_DSP\_VmulD](fast-kit-fast.md#hms_fast_dsp_vmuld) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdiv](fast-kit-fast.md#hms_fast_dsp_vdiv) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（单精度）。 |
| void [HMS\_FAST\_DSP\_VdivD](fast-kit-fast.md#hms_fast_dsp_vdivd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdist](fast-kit-fast.md#hms_fast_dsp_vdist) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数（单精度）。 |
| void [HMS\_FAST\_DSP\_VdistD](fast-kit-fast.md#hms_fast_dsp_vdistd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数（双精度）。 |
| float [HMS\_FAST\_DSP\_Svesq](fast-kit-fast.md#hms_fast_dsp_svesq) (const float\* input, size\_t stride, size\_t length) | 计算向量元素的平方和（单精度）。 |
| double [HMS\_FAST\_DSP\_SvesqD](fast-kit-fast.md#hms_fast_dsp_svesqd) (const double\* input, size\_t stride, size\_t length) | 计算向量元素的平方和（双精度）。 |
| void [HMS\_FAST\_DSP\_Minvi](fast-kit-fast.md#hms_fast_dsp_minvi) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实数向量中的最小值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MinviD](fast-kit-fast.md#hms_fast_dsp_minvid) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实数向量中的最小值及其索引（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsq](fast-kit-fast.md#hms_fast_dsp_vsq) (const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（单精度）。 |
| void [HMS\_FAST\_DSP\_VsqD](fast-kit-fast.md#hms_fast_dsp_vsqd) (const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Vabs](fast-kit-fast.md#hms_fast_dsp_vabs) (const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（单精度）。 |
| void [HMS\_FAST\_DSP\_VabsD](fast-kit-fast.md#hms_fast_dsp_vabsd) (const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（双精度）。 |
| void [HMS\_FAST\_DSP\_Vthr](fast-kit-fast.md#hms_fast_dsp_vthr) (const float\* input, size\_t strideInput, const float threshold, float\* output, size\_t strideOutput, size\_t length) | 对向量应用阈值（单精度）。 |
| void [HMS\_FAST\_DSP\_VthrD](fast-kit-fast.md#hms_fast_dsp_vthrd) (const double\* input, size\_t strideInput, const double threshold, double\* output, size\_t strideOutput, size\_t length) | 对向量应用阈值（双精度）。 |
| void [HMS\_FAST\_DSP\_Vrvrs](fast-kit-fast.md#hms_fast_dsp_vrvrs) (float\* vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（单精度）。 |
| void [HMS\_FAST\_DSP\_VrvrsD](fast-kit-fast.md#hms_fast_dsp_vrvrsd) (double\* vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（双精度）。 |
| void [HMS\_FAST\_DSP\_Vspdp](fast-kit-fast.md#hms_fast_dsp_vspdp) (const float\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将单精度向量转换为双精度向量。 |
| void [HMS\_FAST\_DSP\_Vdpsp](fast-kit-fast.md#hms_fast_dsp_vdpsp) (const double\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将双精度向量转换为单精度向量。 |
| void [HMS\_FAST\_DSP\_Vfill](fast-kit-fast.md#hms_fast_dsp_vfill) (float\* vector, size\_t stride, size\_t length, const float scalar) | 使用指定标量值填充向量（单精度）。 |
| void [HMS\_FAST\_DSP\_VfillD](fast-kit-fast.md#hms_fast_dsp_vfilld) (double\* vector, size\_t stride, size\_t length, const double scalar) | 使用指定标量值填充向量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vclr](fast-kit-fast.md#hms_fast_dsp_vclr) (float\* vector, size\_t stride, size\_t length) | 将向量所有元素清零（单精度）。 |
| void [HMS\_FAST\_DSP\_VclrD](fast-kit-fast.md#hms_fast_dsp_vclrd) (double\* vector, size\_t stride, size\_t length) | 将向量所有元素清零（双精度）。 |
| void [HMS\_FAST\_DSP\_Conv](fast-kit-fast.md#hms_fast_dsp_conv) (const float\* input, size\_t strideInput, const float\* filter, size\_t strideFilter, float\* output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（单精度）。 |
| void [HMS\_FAST\_DSP\_ConvD](fast-kit-fast.md#hms_fast_dsp_convd) (const double\* input, size\_t strideInput, const double\* filter, size\_t strideFilter, double\* output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（双精度）。 |
| void [HMS\_FAST\_DSP\_HannWindow](fast-kit-fast.md#hms_fast_dsp_hannwindow) (float\* output, size\_t length, HMS\_FAST\_HannWindowType type) | 生成汉宁窗序列（单精度）。 |
| void [HMS\_FAST\_DSP\_HannWindowD](fast-kit-fast.md#hms_fast_dsp_hannwindowd) (double\* output, size\_t length, HMS\_FAST\_HannWindowType type) | 生成汉宁窗序列（双精度）。 |
| void [HMS\_FAST\_DSP\_Mmul](fast-kit-fast.md#hms_fast_dsp_mmul) (const float\* matrixA, size\_t strideA, const float\* matrixB, size\_t strideB, float\* matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法：C = A \* B（单精度）。 |
| void [HMS\_FAST\_DSP\_MmulD](fast-kit-fast.md#hms_fast_dsp_mmuld) (const double\* matrixA, size\_t strideA, const double\* matrixB, size\_t strideB, double\* matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法：C = A \* B（双精度）。 |
| void [HMS\_FAST\_DSP\_Vvpow](fast-kit-fast.md#hms_fast_dsp_vvpow) (const float\* inputA, const float\* inputB, float\* outputC, size\_t length) | 执行向量逐元素幂运算：C[i] = pow(A[i], B[i])（单精度）。 |
| void [HMS\_FAST\_DSP\_VvpowD](fast-kit-fast.md#hms_fast_dsp_vvpowd) (const double\* inputA, const double\* inputB, double\* outputC, size\_t length) | 执行向量逐元素幂运算：C[i] = pow(A[i], B[i])（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsort](fast-kit-fast.md#hms_fast_dsp_vsort) (float\* vector, size\_t length, int order) | 对向量进行原地排序（单精度）。 |
| void [HMS\_FAST\_DSP\_VsortD](fast-kit-fast.md#hms_fast_dsp_vsortd) (double\* vector, size\_t length, int order) | 对向量进行原地排序（双精度）。 |
