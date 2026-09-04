---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-iir-filter
title: 使用DSP进行二阶IIR滤波
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用DSP进行二阶IIR滤波
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:33+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:6b1b4c0a74edf0f1708f2a5ebe149fd2ee9cc7a19b7b2a2feed7c5e309a2ff9b
---

二阶IIR滤波器用于音频和信号处理中的滤波操作，例如实现低通、高通或带通滤波。

二阶IIR滤波器采用直接II型转置结构，支持多通道（如立体声）和多节级联（如高阶滤波器）配置。滤波器支持动态激活/旁路控制，允许运行时灵活调整滤波特性。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/fast-kit-fast.md)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_Create](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_create) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_Biquadm\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_CreateD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_created) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_BiquadmD\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS\_FAST\_Biquadm\_Destroy](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_destroy) (FAST\_Biquadm\* filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS\_FAST\_Biquadm\_DestroyD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_destroyd) (FAST\_BiquadmD\* filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingle](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingle) (FAST\_Biquadm\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDouble](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setcoeffdouble) (FAST\_Biquadm\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffSingleD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingled) (FAST\_BiquadmD\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetCoeffDoubleD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setcoeffdoubled) (FAST\_BiquadmD\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFilters](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setactivefilters) (FAST\_Biquadm\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm\_SetActiveFiltersD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm_setactivefiltersd) (FAST\_BiquadmD\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_Biquadm](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadm) (FAST\_Biquadm\* filter, const float\*\* input, const size\_t strideInput, float\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST\_ErrorCode](../harmonyos-references/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_BiquadmD](../harmonyos-references/fast-kit-fast.md#hms_fast_biquadmd) (FAST\_BiquadmD\* filter, const double\*\* input, const size\_t strideInput, double\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |

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
3. 调用HMS\_FAST\_Biquadm\_Create创建滤波器实例（单精度）或HMS\_FAST\_Biquadm\_CreateD（双精度）。
4. 调用HMS\_FAST\_Biquadm\_SetCoeffSingle设置滤波器系数。
5. 可选：调用HMS\_FAST\_Biquadm\_SetActiveFilters设置滤波器节激活掩码。
6. 调用HMS\_FAST\_Biquadm进行滤波处理。
7. 调用HMS\_FAST\_Biquadm\_Destroy销毁滤波器实例。

## 代码示例

### 单通道滤波器示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode single_channel_filter_demo() {
    // 滤波器参数：1通道，1节，最大100帧
    size_t num_channels = 1;
    size_t num_sections = 1;
    size_t max_frames = 100;

    FAST_Biquadm* filter = nullptr;
    FAST_ErrorCode ret;

    // 创建滤波器
    ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to create filter: %d\n", ret);
        return ret;
    }

    // 设置滤波器系数 (b0, b1, b2, a1, a2)
    // 低通滤波器示例系数
    float coefficients[] = {
        0.049922035f,  // b0
        0.099844069f,  // b1
        0.049922035f,  // b2
        -1.558153539f, // a1
        0.649003273f   // a2
    };

    ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to set coefficients: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    // 准备输入输出数据
    const size_t num_samples = 10;
    float input[num_samples] = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                                1.0f, 1.0f, 1.0f, 1.0f, 1.0f};
    float output[num_samples];

    const float* input_channels[] = {input};
    float* output_channels[] = {output};

    // 执行滤波
    ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to process: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    printf("Filtered output:\n");
    for (size_t i = 0; i < num_samples; ++i) {
        printf("  output[%zu] = %f\n", i, output[i]);
    }

    // 销毁滤波器
    HMS_FAST_Biquadm_Destroy(filter);

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 多通道滤波器示例

```cpp
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode multi_channel_filter_demo() {
    // 滤波器参数：2通道（立体声），2节级联，最大1000帧
    size_t num_channels = 2;
    size_t num_sections = 2;
    size_t max_frames = 1000;

    FAST_Biquadm* filter = nullptr;
    FAST_ErrorCode ret;

    // 创建滤波器
    ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to create filter: %d\n", ret);
        return ret;
    }

    // 设置滤波器系数：每个通道各 2 节，按 [通道][节] 顺序排列
    float coefficients[] = {
        // 通道0 第1节系数
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,
        // 通道0 第2节系数
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,
        // 通道1 第1节系数
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,
        // 通道1 第2节系数
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f
    };

    ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to set coefficients: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    // 准备输入输出数据
    const size_t num_samples = 100;
    float input_left[num_samples];
    float input_right[num_samples];
    float output_left[num_samples];
    float output_right[num_samples];

    // 初始化输入数据（正弦波）
    for (size_t i = 0; i < num_samples; ++i) {
        input_left[i] = sinf(i * 0.1f);
        input_right[i] = sinf(i * 0.1f + 0.5f);
    }

    const float* input_channels[] = {input_left, input_right};
    float* output_channels[] = {output_left, output_right};

    // 执行滤波
    ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to process: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    printf("Multi-channel filter processed %zu samples\n", num_samples);

    // 销毁滤波器
    HMS_FAST_Biquadm_Destroy(filter);

    return FAST_ERROR_CODE_SUCCESS;
}
```

### 动态激活滤波器节示例

```cpp
#include <cstdio>
#include <cstdlib>
#include "FASTKit/fast_dsp_common.h"

FAST_ErrorCode dynamic_filter_activation_demo() {
    // 滤波器参数：1通道，3节，最大100帧
    size_t num_channels = 1;
    size_t num_sections = 3;
    size_t max_frames = 100;

    FAST_Biquadm* filter = nullptr;
    FAST_ErrorCode ret;

    // 创建滤波器
    ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to create filter: %d\n", ret);
        return ret;
    }

    // 设置3节滤波器系数
    float coefficients[] = {
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,  // 节 0
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,  // 节 1
        0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f   // 节 2
    };

    ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to set coefficients: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    // 设置激活掩码：仅激活第0节和第2节，旁路第1节
    uint8_t active_mask[] = {1, 0, 1};
    ret = HMS_FAST_Biquadm_SetActiveFilters(filter, active_mask);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to set active filters: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    // 准备输入输出数据
    const size_t num_samples = 10;
    float input[num_samples] = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
                                1.0f, 1.0f, 1.0f, 1.0f, 1.0f};
    float output[num_samples];

    const float* input_channels[] = {input};
    float* output_channels[] = {output};

    // 执行滤波（仅通过第0节和第2节）
    ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
    if (ret != FAST_ERROR_CODE_SUCCESS) {
        printf("Failed to process: %d\n", ret);
        HMS_FAST_Biquadm_Destroy(filter);
        return ret;
    }

    printf("Filtered output with dynamic activation:\n");
    for (size_t i = 0; i < num_samples; ++i) {
        printf("  output[%zu] = %f\n", i, output[i]);
    }

    // 销毁滤波器
    HMS_FAST_Biquadm_Destroy(filter);

    return FAST_ERROR_CODE_SUCCESS;
}
```
