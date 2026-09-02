---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-transform
title: 使用DSP进行FFT变换
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用DSP进行FFT变换
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:36+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:b67f81dcd07ccc30552ab2f3a8393dfb90f9096552ccd010e4c0ce1e06abe2de
---

从API版本26.0.0开始，新增支持快速傅里叶变换（Fast Fourier Transform，FFT）及其逆变换（Inverse Fast Fourier Transform，IFFT）功能。

数字信号处理（DSP）中的快速傅里叶变换（FFT）可将实数时域信号高效转换为频域表示；其逆变换（IFFT）则能将频域信号恢复为时域信号。当开发者需要对音频信号、传感器数据或其他时序信号进行频谱分析、频域滤波或信号重构时，可使用本接口。

FFT和IFFT功能均提供单精度（float）和双精度（double）两种数据类型的接口，基于高效算法实现时域与频域之间的相互变换。支持的最大FFT点数为2^16（即65536点）。请注意：输入信号的长度必须等于2的log2n次方，其中log2n是在创建配置时指定的参数。

## 场景介绍

FFT与IFFT变换适用于以下典型场景：

* **频谱分析**：将时域音频信号转换为频域，分析频率成分。
* **频域滤波**：在频域进行滤波操作（如去噪、回声消除）后再变换回时域。
* **信号重构**：对频域信号进行IFFT恢复时域信号，用于信号合成。
* **振动分析**：对传感器振动信号进行频谱分析，检测设备故障特征频率。

## 接口说明

具体API详见[接口文档](../harmonyos-references/fast-kit-fast-dsp-transform-8h.md)。

### 配置管理

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_createconfig) (FAST\_FFTConfig\*\* config, uint32\_t log2n) | 创建单精度FFT配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](../harmonyos-references/fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_CreateConfigD](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_createconfigd) (FAST\_FFTConfig\*\* config, uint32\_t log2n) | 创建双精度FFT配置（log2n为FFT点数对应的以2为底的对数值，必须满足0<log2n<=[FAST\_MAX\_FFT\_LOG2N](../harmonyos-references/fast-kit-fast.md#fast_max_fft_log2n)，即1到16）。 |
| void [HMS\_FAST\_FFT\_DestroyConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_destroyconfig) (FAST\_FFTConfig\* config) | 销毁FFT配置并释放资源。 |

### 正向变换

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransform](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_forwardtransform) (FAST\_FFTConfig\* config, uint32\_t length, const float input[], float outputRe[], float outputIm[]) | 计算单精度实数时域信号的DFT。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_ForwardTransformD](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_forwardtransformd) (FAST\_FFTConfig\* config, uint32\_t length, const double input[], double outputRe[], double outputIm[]) | 计算双精度实数时域信号的DFT。 |

### 逆向变换

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransform](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_inversetransform) (FAST\_FFTConfig\* config, uint32\_t length, const float inputRe[], const float inputIm[], float output[]) | 计算单精度复数频域序列的逆DFT。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_FFT\_InverseTransformD](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_inversetransformd) (FAST\_FFTConfig\* config, uint32\_t length, const double inputRe[], const double inputIm[], double output[]) | 计算双精度复数频域序列的逆DFT。 |

## 开发步骤

本小节以正向FFT计算的单精度接口为例（单精度无后缀，双精度D后缀）。

1. 在CMake脚本中链接相关动态库。

   ```cmake
   find_library(
       lib_fast_dsp
       NAMES fast_dsp
   )

   target_link_libraries(entry PRIVATE ${lib_fast_dsp})
   ```
2. 调用HMS\_FAST\_FFT\_CreateConfig（单精度）或HMS\_FAST\_FFT\_CreateConfigD（双精度）创建FFT配置实例（FAST\_FFTConfig）。
3. 根据FFT大小分配输入、输出数组。

   * 正向变换：输入数组长度为N（实数时域信号），输出实部和虚部数组长度均为N/2+1。
   * 逆变换：输入实部和虚部数组长度均为N/2+1，输出数组长度为N（实数时域信号）。
4. 调用HMS\_FAST\_FFT\_ForwardTransform/HMS\_FAST\_FFT\_ForwardTransformD计算FFT，或调用HMS\_FAST\_FFT\_InverseTransform/HMS\_FAST\_FFT\_InverseTransformD计算IFFT。
5. 调用HMS\_FAST\_FFT\_DestroyConfig销毁FFT配置实例，释放内部资源。

## 代码示例

### 单精度FFT变换示例

```cpp
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include "FASTKit/fast_dsp_transform.h"

FAST_ErrorCode fft_single_precision_demo() {
    const uint32_t log2n = 4;  // FFT大小N=16
    const uint32_t length = 1 << log2n;
    const uint32_t freq_size = length / 2 + 1;

    FAST_FFTConfig *config = nullptr;
    float *input = nullptr;
    float *freqRe = nullptr;
    float *freqIm = nullptr;
    float *output = nullptr;
    FAST_ErrorCode ret = FAST_ERROR_CODE_SUCCESS;

    do {
        // 创建配置
        ret = HMS_FAST_FFT_CreateConfig(&config, log2n);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("CreateConfig failed: %d\n", ret);
            break; // 失败即跳出，去最后的清理区
        }

        // 分配内存
        input = (float *)malloc(length * sizeof(float));
        freqRe = (float *)malloc(freq_size * sizeof(float));
        freqIm = (float *)malloc(freq_size * sizeof(float));
        output = (float *)malloc(length * sizeof(float));

        // 检查分配结果
        if (!input || !freqRe || !freqIm || !output) {
            printf("Memory allocation failed!\n");
            ret = FAST_ERROR_CODE_FAIL;
            break;
        }

        // 初始化数据
        for (uint32_t i = 0; i < length; ++i) input[i] = (float)i;

        // 正向FFT：时域->频域
        ret = HMS_FAST_FFT_ForwardTransform(config, length, input, freqRe, freqIm);
        if (ret == FAST_ERROR_CODE_SUCCESS) {
            // 打印FFT计算结果
            printf("Frequency domain (first 5 bins):\n");
            for (uint32_t i = 0; i < 5 && i < freq_size; ++i) {
                printf("  Bin %u: (%.4f, %.4fi)\n", i, freqRe[i], freqIm[i]);
            }
        } else {
            printf("ForwardTransform failed: %d\n", ret);
            break;
        }

        // 逆向FFT：频域->时域
        ret = HMS_FAST_FFT_InverseTransform(config, length, freqRe, freqIm, output);
        if (ret == FAST_ERROR_CODE_SUCCESS) {
            // 打印IFFT计算结果
            printf("Reconstruction (normalized):\n  Original:  ");
            for (uint32_t i = 0; i < length; ++i) printf("%.4f ", input[i]);
            printf("\n  Recovered: ");
            for (uint32_t i = 0; i < length; ++i) printf("%.4f ", output[i]);
            printf("\n");
        } else {
            printf("InverseTransform failed: %d\n", ret);
            break;
        }

    } while (0);

    if (input) free(input);
    if (freqRe) free(freqRe);
    if (freqIm) free(freqIm);
    if (output) free(output);
    if (config) HMS_FAST_FFT_DestroyConfig(config);

    return ret;
}
```

### 双精度FFT变换示例

```cpp
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include "FASTKit/fast_dsp_transform.h"

FAST_ErrorCode fft_double_precision_demo() {
    const uint32_t log2n = 4;  // FFT大小N=16
    const uint32_t length = 1 << log2n;
    const uint32_t freq_size = length / 2 + 1;

    FAST_FFTConfig *config = nullptr;
    double *input = nullptr;
    double *freqRe = nullptr;
    double *freqIm = nullptr;
    double *output = nullptr;
    FAST_ErrorCode ret = FAST_ERROR_CODE_SUCCESS;

    do {
        // 创建配置
        ret = HMS_FAST_FFT_CreateConfigD(&config, log2n);
        if (ret != FAST_ERROR_CODE_SUCCESS) {
            printf("CreateConfig failed: %d\n", ret);
            break; // 失败即跳出，去最后的清理区
        }

        // 分配内存
        input = (double *)malloc(length * sizeof(double));
        freqRe = (double *)malloc(freq_size * sizeof(double));
        freqIm = (double *)malloc(freq_size * sizeof(double));
        output = (double *)malloc(length * sizeof(double));

        // 检查分配结果
        if (!input || !freqRe || !freqIm || !output) {
            printf("Memory allocation failed!\n");
            ret = FAST_ERROR_CODE_FAIL;
            break;
        }

        // 初始化数据
        for (uint32_t i = 0; i < length; ++i) input[i] = (double)i;

        // 正向FFT：时域->频域
        ret = HMS_FAST_FFT_ForwardTransformD(config, length, input, freqRe, freqIm);
        if (ret == FAST_ERROR_CODE_SUCCESS) {
            // 打印FFT计算结果
            printf("Frequency domain (first 5 bins):\n");
            for (uint32_t i = 0; i < 5 && i < freq_size; ++i) {
                printf("  Bin %u: (%.4f, %.4fi)\n", i, freqRe[i], freqIm[i]);
            }
        } else {
            printf("ForwardTransform failed: %d\n", ret);
            break;
        }

        // 逆向FFT：频域->时域
        ret = HMS_FAST_FFT_InverseTransformD(config, length, freqRe, freqIm, output);
        if (ret == FAST_ERROR_CODE_SUCCESS) {
            // 打印IFFT计算结果
            printf("Reconstruction (normalized):\n  Original:  ");
            for (uint32_t i = 0; i < length; ++i) printf("%.4f ", input[i]);
            printf("\n  Recovered: ");
            for (uint32_t i = 0; i < length; ++i) printf("%.4f ", output[i]);
            printf("\n");
        } else {
            printf("InverseTransform failed: %d\n", ret);
            break;
        }

    } while (0);

    if (input) free(input);
    if (freqRe) free(freqRe);
    if (freqIm) free(freqIm);
    if (output) free(output);
    if (config) HMS_FAST_FFT_DestroyConfig(config);

    return ret;
}
```

## 注意事项

1. **FFT大小限制**：log2n必须在1到16之间，即FFT大小N的范围是2到65536。
2. **输入长度匹配**：正向和逆向变换的输入长度必须与创建配置时指定的log2n一致（length=2^log2n）。
3. **输出数组大小**：对于实数输入的FFT，输出数组大小为length/2+1，因为实信号的频谱具有共轭对称性。
4. **内存管理**：使用完FFT配置后务必调用[HMS\_FAST\_FFT\_DestroyConfig](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_destroyconfig)释放资源。
5. **精度选择**：单精度版本计算速度更快，双精度版本精度更高，根据应用场景选择合适的版本。
6. **线程安全性**：在多线程环境中，严禁多个线程同时操作同一个[FAST\_FFTConfig](../harmonyos-references/fast-kit-fast.md#fast_fftconfig)配置对象。包括并发调用[HMS\_FAST\_FFT\_ForwardTransform](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_forwardtransform)（前向变换）、[HMS\_FAST\_FFT\_InverseTransform](../harmonyos-references/fast-kit-fast.md#hms_fast_fft_inversetransform)（逆变换）及其对应的双精度接口。为确保多线程环境下的计算稳定性，建议采取以下方案：

   * 每个线程独立创建自己的[FAST\_FFTConfig](../harmonyos-references/fast-kit-fast.md#fast_fftconfig)对象（推荐，无锁且高性能）；
   * 或通过互斥锁外部保护所有对该配置对象的调用。
