---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-rtshadowaodenoiserparameters
title: XEG_RTShadowAODenoiserParameters
breadcrumb: API参考 > 图形 > XEngine Kit（GPU加速引擎服务） > C API > 头文件和结构体 > 结构体 > XEG_RTShadowAODenoiserParameters
category: harmonyos-references
scraped_at: 2026-09-02T15:02:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8288c4ce12b3c70869750f80d18d92cca2f97b5093400ab3df42be09684c32b3
---

## 概述

光线追踪阴影和环境光遮蔽算法去噪参数。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](xengine-kit-xengine.md)

**所在头文件：** [xeg\_vulkan\_rt\_visible\_mask.h](xengine-kit-xeg-vulkan-rt-visible-mask-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| float [temporalBlendFactor](xengine-kit-xeg-rtshadowaodenoiserparameters.md#temporalblendfactor) = 0.075f | 时域滤波时当前帧与历史帧混合的权重系数。一致性校验通过后，权重值越大，越多采用当前帧的信息。此参数的值将被限制在[0.01, 1.0]范围内。默认值为0.075。 |
| float [positionConstantDistance](xengine-kit-xeg-rtshadowaodenoiserparameters.md#positionconstantdistance) = 1.0f | 时域滤波中根据世界空间距离进行一致性校验的阈值，必须大于等于0，如果传负值将被视为0。默认值为1.0。 |
| uint32\_t [spatialDenoiseTimes](xengine-kit-xeg-rtshadowaodenoiserparameters.md#spatialdenoisetimes) = 2 | 空域滤波器执行的次数。次数越多生成的阴影和环境光遮蔽噪声越少，但可能会导致降噪结果更模糊。此参数的值将被限制在[0, 5]范围内。默认值为2。 |
| float [ghostingAlpha](xengine-kit-xeg-rtshadowaodenoiserparameters.md#ghostingalpha) = 0.0f | 时域滤波器中控制运动物体引入的鬼影问题。值为0时，不解决运动物体引入的鬼影问题。值越高，鬼影问题解决的越好，但降噪结果会稍微劣化。此参数的值将被限制在[0.0, 1.0]范围内。默认值为0.0。 |
| float [spatialNormalWeight](xengine-kit-xeg-rtshadowaodenoiserparameters.md#spatialnormalweight) = 1.0f | 空域滤波器使用的法线权重信息，值越大，法线权重越高，画质越锐利。此参数的值将被限制在[0.0, 1.0]范围内。默认值为1.0。 |
| uint32\_t [spatialMaxKernelStep](xengine-kit-xeg-rtshadowaodenoiserparameters.md#spatialmaxkernelstep) = 0 | 空域滤波器采样步长，值越大，采样范围越大。此参数的值将被限制在[0, 4]范围内。默认值为0。 |

## 结构体成员变量说明

### ghostingAlpha

```cpp
float XEG_RTShadowAODenoiserParameters::ghostingAlpha = 0.0f
```

**描述**

时域滤波器中控制运动物体引入的鬼影问题。值为0时，不解决运动物体引入的鬼影问题。值越高，鬼影问题解决的越好，但降噪结果会稍微劣化。此参数的值将被限制在[0.0, 1.0]范围内。默认值为0.0。

### positionConstantDistance

```cpp
float XEG_RTShadowAODenoiserParameters::positionConstantDistance = 1.0f
```

**描述**

时域滤波中根据世界空间距离进行一致性校验的阈值，必须大于等于0，如果传负值将被视为0。默认值为1.0。

### spatialDenoiseTimes

```cpp
uint32_t XEG_RTShadowAODenoiserParameters::spatialDenoiseTimes = 2
```

**描述**

空域滤波器执行的次数。次数越多生成的阴影和环境光遮蔽噪声越少，但可能会导致降噪结果更模糊。此参数的值将被限制在[0, 5]范围内。默认值为2。

### spatialMaxKernelStep

```cpp
uint32_t XEG_RTShadowAODenoiserParameters::spatialMaxKernelStep = 0
```

**描述**

空域滤波器采样步长，值越大，采样范围越大。此参数的值将被限制在[0, 4]范围内。默认值为0。

### spatialNormalWeight

```cpp
float XEG_RTShadowAODenoiserParameters::spatialNormalWeight = 1.0f
```

**描述**

空域滤波器使用的法线权重信息，值越大，法线权重越高，画质越锐利。此参数的值将被限制在[0.0, 1.0]范围内。默认值为1.0。

### temporalBlendFactor

```cpp
float XEG_RTShadowAODenoiserParameters::temporalBlendFactor = 0.075f
```

**描述**

时域滤波时当前帧与历史帧混合的权重系数。一致性校验通过后，权重值越大，越多采用当前帧的信息。此参数的值将被限制在[0.01, 1.0]范围内。默认值为0.075。
