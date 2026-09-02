---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime
title: NeuralNetworkRuntime
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 模块 > NeuralNetworkRuntime
category: harmonyos-references
scraped_at: 2026-09-02T14:53:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d1ade9e151f6b2dbc0e9fed63148dfe89fb7bf1fd588146b43b1d14b02fadd25
---

## 概述

提供Neural Network Runtime加速模型推理的相关接口。

**起始版本：** 9

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [neural\_network\_core.h](capi-neural-network-core-h.md) | Neural Network Core模块接口定义，AI推理框架使用Neural Network Core提供的Native接口，完成模型编译，并在加速硬件上执行推理和计算。  部分接口定义从neural\_network\_runtime.h移动至此头文件统一呈现，对于此类接口，API version 11 版本之前即支持使用，各版本均可正常使用。  Neural Network Core的接口目前均不支持多线程并发调用。 |
| [neural\_network\_runtime.h](capi-neural-network-runtime-h.md) | Neural Network Runtime模块接口定义，AI推理框架使用Neural Network Runtime提供的Native接口，完成模型构建。  Neural Network Runtime的接口目前均不支持多线程并发调用。 |
| [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md) | Neural Network Runtime定义的结构体和枚举值。 |
