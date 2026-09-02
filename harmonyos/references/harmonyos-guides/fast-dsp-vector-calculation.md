---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-vector-calculation
title: 使用DSP进行向量计算
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用DSP进行向量计算
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:308ac88fbee723057f09a3c0535c79dfe46b1c619c216823c50bd5265afaf45c
---

数字信号处理（DSP）中的向量计算功能，提供涵盖向量基本算术运算、初始化与统计归约、复数运算以及信号处理与线性代数等领域的接口。当开发者需要对传感器数据、音频信号或其他数值序列进行算术运算、统计计算、复数分析、卷积、矩阵乘法或窗函数生成等操作时，可以使用向量计算接口。

向量计算支持单精度（float）和双精度（double）两种数据类型，并针对ARM NEON指令集进行了优化，在步长为1的连续存储场景下可获得显著性能提升。需要注意的是，为了提升性能，部分接口对浮点数的计算顺序进行了调整，可能影响结果精度。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

### 向量基本算术运算

涵盖所有逐元素的基础数值运算，包括标量与向量的组合运算、向量之间的四则运算、绝对值、平方、阈值以及幂运算等。

**标量与向量的运算**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vsmul](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsmul) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsmulD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsmuld) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素乘以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsdiv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsdiv) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（单精度）。 |
| void [HMS\_FAST\_DSP\_VsdivD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsdivd) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将向量的每个元素除以标量（双精度）。 |
| void [HMS\_FAST\_DSP\_Svdiv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svdiv) (const float scalar, const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_SvdivD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svdivd) (const double scalar, const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将标量除以向量的每个元素（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsadd](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsadd) (const float\* input, size\_t strideInput, const float scalar, float\* output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（单精度）。 |
| void [HMS\_FAST\_DSP\_VsaddD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsaddd) (const double\* input, size\_t strideInput, const double scalar, double\* output, size\_t strideOutput, size\_t length) | 将标量加到向量的每个元素（双精度）。 |

**向量之间的运算**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vadd](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vadd) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（单精度）。 |
| void [HMS\_FAST\_DSP\_VaddD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vaddd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素加法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsub](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsub) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（单精度）。 |
| void [HMS\_FAST\_DSP\_VsubD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsubd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素减法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vmul](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vmul) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（单精度）。 |
| void [HMS\_FAST\_DSP\_VmulD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vmuld) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素乘法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdiv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vdiv) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（单精度）。 |
| void [HMS\_FAST\_DSP\_VdivD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vdivd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 执行向量逐元素除法（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsbsm](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsbsm) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float scalar, float\* outputC, size\_t strideC, size\_t length) | 执行向量减法并缩放（单精度）。 |
| void [HMS\_FAST\_DSP\_VsbsmD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsbsmd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double scalar, double\* outputC, size\_t strideC, size\_t length) | 执行向量减法并缩放（双精度）。 |
| void [HMS\_FAST\_DSP\_Vdist](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vdist) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float\* outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数：C[i]等于A[i]与B[i]的平方和的算术开方根（单精度）。 |
| void [HMS\_FAST\_DSP\_VdistD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vdistd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double\* outputC, size\_t strideC, size\_t length) | 计算两个向量对应元素的欧几里得范数：C[i]等于A[i]与B[i]的平方和的算术开方根（双精度）。 |

**向量变换**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vsq](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsq) (const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（单精度）。 |
| void [HMS\_FAST\_DSP\_VsqD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsqd) (const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Vabs](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vabs) (const float\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（单精度）。 |
| void [HMS\_FAST\_DSP\_VabsD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vabsd) (const double\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算向量每个元素的绝对值（双精度）。 |
| void [HMS\_FAST\_DSP\_Vthr](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vthr) (const float\* input, size\_t strideInput, const float threshold, float\* output, size\_t strideOutput, size\_t length) | 对向量应用阈值：若input[i] < threshold则取threshold，否则取原值（单精度）。 |
| void [HMS\_FAST\_DSP\_VthrD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vthrd) (const double\* input, size\_t strideInput, const double threshold, double\* output, size\_t strideOutput, size\_t length) | 对向量应用阈值：若input[i] < threshold则取threshold，否则取原值（双精度）。 |

**幂运算**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vvpow](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vvpow) (const float\* inputA, const float\* inputB, float\* outputC, size\_t length) | 执行向量逐元素幂运算：C[i]等于A[i]的B[i]次方（单精度）。 |
| void [HMS\_FAST\_DSP\_VvpowD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vvpowd) (const double\* inputA, const double\* inputB, double\* outputC, size\_t length) | 执行向量逐元素幂运算：C[i]等于A[i]的B[i]次方（双精度）。 |

### 初始化、归约与统计

包含将向量数据归纳为标量的操作、数据生成与填充、类型转换以及元素顺序调整。

**初始化/填充**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vfill](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vfill) (float\* vector, size\_t stride, size\_t length, const float scalar) | 使用指定标量值填充向量（单精度）。 |
| void [HMS\_FAST\_DSP\_VfillD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vfilld) (double\* vector, size\_t stride, size\_t length, const double scalar) | 使用指定标量值填充向量（双精度）。 |
| void [HMS\_FAST\_DSP\_Vclr](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vclr) (float\* vector, size\_t stride, size\_t length) | 将向量所有元素清零（单精度）。 |
| void [HMS\_FAST\_DSP\_VclrD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vclrd) (double\* vector, size\_t stride, size\_t length) | 将向量所有元素清零（双精度）。 |

**类型转换**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vspdp](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vspdp) (const float\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将单精度向量转换为双精度向量。 |
| void [HMS\_FAST\_DSP\_Vdpsp](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vdpsp) (const double\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将双精度向量转换为单精度向量。 |

**归约运算**

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Maxmgv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_maxmgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（单精度）。 |
| double [HMS\_FAST\_DSP\_MaxmgvD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_maxmgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量中的最大幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Maxvi](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_maxvi) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实数向量中的最大值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MaxviD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_maxvid) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实数向量中的最大值及其索引（双精度）。 |
| void [HMS\_FAST\_DSP\_Minvi](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_minvi) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实数向量中的最小值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MinviD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_minvid) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实数向量中的最小值及其索引（双精度）。 |
| float [HMS\_FAST\_DSP\_Sve](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_sve) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量的和（单精度）。 |
| double [HMS\_FAST\_DSP\_SveD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_sved) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量的和（双精度）。 |
| float [HMS\_FAST\_DSP\_Svemg](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svemg) (const float\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS\_FAST\_DSP\_SvemgD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svemgd) (const double\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS\_FAST\_DSP\_Meamgv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_meamgv) (const float\* input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（单精度）。 |
| double [HMS\_FAST\_DSP\_MeamgvD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_meamgvd) (const double\* input, size\_t stride, size\_t length) | 计算步长实数向量绝对值的均值（双精度）。 |
| float [HMS\_FAST\_DSP\_Svesq](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svesq) (const float\* input, size\_t stride, size\_t length) | 计算向量元素的平方和（单精度）。 |
| double [HMS\_FAST\_DSP\_SvesqD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_svesqd) (const double\* input, size\_t stride, size\_t length) | 计算向量元素的平方和（双精度）。 |
| float [HMS\_FAST\_DSP\_Dotpr](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_dotpr) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（单精度）。 |
| double [HMS\_FAST\_DSP\_DotprD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_dotprd) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, size\_t length) | 计算两个步长实数向量的点积（双精度）。 |

**向量元素操作**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Vrvrs](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vrvrs) (float\* vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（单精度）。 |
| void [HMS\_FAST\_DSP\_VrvrsD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vrvrsd) (double\* vector, size\_t stride, size\_t length) | 原地反转向量中元素的顺序（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsort](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsort) (float\* vector, size\_t length, int order) | 对向量进行原地排序（单精度）。 |
| void [HMS\_FAST\_DSP\_VsortD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_vsortd) (double\* vector, size\_t length, int order) | 对向量进行原地排序（双精度）。 |

### 复数运算

包含复数向量的幅度、相位计算以及复数格式转换。

**复数基础运算**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Zvabs](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvabs) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvabsD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvabsd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvmags](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvmags) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvmagsD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvmagsd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的幅值平方（双精度）。 |
| void [HMS\_FAST\_DSP\_Zvphas](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvphas) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（弧度制）（单精度）。 |
| void [HMS\_FAST\_DSP\_ZvphasD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_zvphasd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 计算复数向量的相位角（弧度制）（双精度）。 |

**复数格式转换**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Ctoz](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_ctoz) (const float\* input, size\_t strideInput, FAST\_SplitComplex\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS\_FAST\_DSP\_CtozD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_ctozd) (const double\* input, size\_t strideInput, FAST\_SplitComplexD\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Ztoc](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_ztoc) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS\_FAST\_DSP\_ZtocD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_ztocd) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（双精度）。 |

### 信号处理与线性代数

包含卷积、窗口生成和矩阵运算。

**卷积**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Conv](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_conv) (const float\* input, size\_t strideInput, const float\* filter, size\_t strideFilter, float\* output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（单精度）。 |
| void [HMS\_FAST\_DSP\_ConvD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_convd) (const double\* input, size\_t strideInput, const double\* filter, size\_t strideFilter, double\* output, size\_t strideOutput, size\_t outputLength, size\_t filterLength) | 执行两个向量的卷积运算（双精度）。 |

**窗口生成**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_HannWindow](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_hannwindow) (float\* output, size\_t length, HMS\_FAST\_HannWindowType type) | 生成汉宁窗序列（单精度）。 |
| void [HMS\_FAST\_DSP\_HannWindowD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_hannwindowd) (double\* output, size\_t length, HMS\_FAST\_HannWindowType type) | 生成汉宁窗序列（双精度）。 |

**矩阵运算**

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Mmul](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_mmul) (const float\* matrixA, size\_t strideA, const float\* matrixB, size\_t strideB, float\* matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法（单精度）。 |
| void [HMS\_FAST\_DSP\_MmulD](../harmonyos-references/fast-kit-fast.md#hms_fast_dsp_mmuld) (const double\* matrixA, size\_t strideA, const double\* matrixB, size\_t strideB, double\* matrixC, size\_t strideC, size\_t rowsM, size\_t colsN, size\_t colsP) | 执行矩阵乘法（双精度）。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```cmake
   find_library(
       lib_fast_dsp
       NAMES fast_dsp
   )
   target_link_libraries(entry PRIVATE ${lib_fast_dsp})
   ```
2. 引入头文件。

   ```cpp
   #include "FASTKit/fast_dsp_common.h"
   ```
3. 根据数据类型选择对应的函数（单精度无后缀，双精度带D后缀）。
4. 调用向量计算函数，注意设置正确的stride参数（连续存储时stride为1）。
5. 检查返回结果。

## 代码示例

### 最大值查找示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode max_value_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算最大幅值（绝对值最大值）
    float max_magnitude = HMS_FAST_DSP_Maxmgv(input, stride, length);
    printf("Max magnitude: %f\n", max_magnitude);  // 输出5.0

    // 查找最大值及其索引
    float max_value = 0.0f;
    size_t max_index = 0;
    HMS_FAST_DSP_Maxvi(input, stride, length, &max_value, &max_index);
    printf("Max value: %f at index %zu\n", max_value, max_index);  // 输出5.0 at index 4

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 统计计算示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode statistics_demo() {
    // 定义输入向量
    float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
    size_t length = sizeof(input) / sizeof(float);
    size_t stride = 1;

    // 计算向量总和
    float sum = HMS_FAST_DSP_Sve(input, stride, length);
    printf("Sum: %f\n", sum);  // 输出3.0

    // 计算绝对值之和（L1范数）
    float sum_abs = HMS_FAST_DSP_Svemg(input, stride, length);
    printf("Sum of absolute values: %f\n", sum_abs);  // 输出15.0

    // 计算绝对值均值
    float mean_abs = HMS_FAST_DSP_Meamgv(input, stride, length);
    printf("Mean of absolute values: %f\n", mean_abs);  // 输出3.0

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 向量运算示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode vector_operations_demo() {
    // 定义两个输入向量
    float inputA[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
    float inputB[] = {0.5f, 1.0f, 1.5f, 2.0f, 2.5f};
    size_t length = 5;
    size_t stride = 1;

    // 计算点积
    float dot_product = HMS_FAST_DSP_Dotpr(inputA, stride, inputB, stride, length);
    printf("Dot product: %f\n", dot_product);  // 输出27.5

    // 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * 2.0
    float outputC[5];
    float scalar = 2.0f;
    HMS_FAST_DSP_Vsbsm(inputA, stride, inputB, stride, scalar, outputC, stride, length);

    printf("Vector subtraction result:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  outputC[%zu] = %f\n", i, outputC[i]);
    }
    // 输出: 1.0, 2.0, 3.0, 4.0, 5.0

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 复数格式转换示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode complex_conversion_demo() {
    // 定义交错格式复数输入 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    size_t length = 3;  // 3个复数
    size_t stride_input = 1;

    // 准备分离格式输出
    float real_array[3];
    float imag_array[3];
    FAST_SplitComplex split_output = {
        .real = real_array,
        .imag = imag_array
    };
    size_t stride_output = 1;

    // 转换为分离格式
    HMS_FAST_DSP_Ctoz(interleaved, stride_input, &split_output, stride_output, length);

    printf("Split format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, real_array[i], imag_array[i]);
    }
    /* xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        Split format:
        Complex[0] = 1.000000 + 2.000000i
        Complex[1] = 3.000000 + 4.000000i
        Complex[2] = 5.000000 + 6.000000i
     */

    // 转换回交错格式
    float interleaved_output[6];
    HMS_FAST_DSP_Ztoc(&split_output, stride_output, interleaved_output, stride_input, length);

    printf("Interleaved format:\n");
    for (size_t i = 0; i < length; ++i) {
        printf("  Complex[%zu] = %f + %fi\n", i, interleaved_output[i * 2], interleaved_output[i * 2 + 1]);
    }

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 非连续存储示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode strided_access_demo() {
    // 定义交错存储的复数数据 (real, imag, real, imag...)
    float interleaved[] = {1.0f, 10.0f, 2.0f, 20.0f, 3.0f, 30.0f, 4.0f, 40.0f, 5.0f, 50.0f};
    size_t length = 5;  // 5个实数值
    size_t stride = 2;  // 步长为2，跳过虚部

    // 计算实部向量的最大幅值
    float max_magnitude = HMS_FAST_DSP_Maxmgv(interleaved, stride, length);
    printf("Max magnitude of real parts: %f\n", max_magnitude);  // 输出5.0

    return FAST_ERROR_CODE_SUCCESS;
}
```
