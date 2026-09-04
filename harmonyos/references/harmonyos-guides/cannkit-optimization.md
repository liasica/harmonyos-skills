---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-optimization
title: 异构
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 异构
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:24+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:debdfead3aeedc99e3ca5353b910ad76da38fdc04b00e5957385370c042fbf30
---

## 概述

异构是CANN Kit提供的异构计算能力，能够使开发者App在华为平台上充分享受到硬件平台的计算加速性能，同时提供非华为硬件平台的模型计算兼容性和计算加速，使开发者App开发过程归一化，不再需要为不同硬件平台适配不同模型或者计算框架，减少App开发及维护的难度。

异构的原理如下图所示，指定OP1、OP2、OP5~OPn在CPU上进行推理，OP3、OP4在NPU上进行推理。

![](https://media:401788444071716648)

实现异构可以通过在线调优方式，以下为在线调优参数设置接口，接口使用见[在线调优开发步骤](cannkit-optimization.md#在线调优开发步骤)。如要使用更丰富的设置和查询接口，请参见[API参考](../harmonyos-references/cannkit.md)。

**表1** 在线调优接口及功能介绍

| 接口名 | 描述 |
| --- | --- |
| OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningMode(OH\_NNCompilation\* compilation, HiAI\_TuningMode tuningMode); | 芯片调优模式配置。 |
| OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningCacheDir(OH\_NNCompilation\* compilation, const char\* cacheDir); | 芯片调优缓存目录配置。 |

## 在线调优开发步骤

1. 设置芯片调优模式。

   * 调用[OH\_NNCompilation\_ConstructWithOfflineModelFile](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_constructwithofflinemodelfile)，读取模型buffer，创建模型编译实例。
   * 调用[HMS\_HiAIOptions\_SetTuningMode](../harmonyos-references/cannkit.md#hms_hiaioptions_settuningmode)向模型编译实例中设置芯片调优模式调优选项。
2. 调用[HMS\_HiAIOptions\_SetTuningCacheDir](../harmonyos-references/cannkit.md#hms_hiaioptions_settuningcachedir)向模型编译实例中设置芯片调优缓存目录调优选项。
3. 执行模型编译。

   设置好所需调优选项参数后，通过调用[OH\_NNCompilation\_Build](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_build)，传入创建模型编译实例，即可执行模型编译，编译成功则返回编译后的模型指针。后续流程同[模型推理](cannkit-model-inference.md)。

## 在线调优示例说明

以下示例代码设置调优参数SetTuningMode及SetTuningCacheDir，实现在线调优。

```
// 选择辅助调优模式
OH_NN_ReturnCode ret = HMS_HiAIOptions_SetTuningMode(compilation, HIAI_TUNING_MODE_HETER);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_ERROR(LOG_APP, "HMS_HiAIOptions_SetTuningMode failed");
    return ret;
}
// 设置辅助调优的缓存目录
const char* cacheDir = "/data/storage/el2/base/files";
ret = HMS_HiAIOptions_SetTuningCacheDir(compilation, cacheDir);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_ERROR(LOG_APP, "HMS_HiAIOptions_SetTuningCacheDir failed");
    return ret;
}
return OH_NN_SUCCESS;
```
