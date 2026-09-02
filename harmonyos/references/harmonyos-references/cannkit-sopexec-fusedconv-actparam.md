---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-fusedconv-actparam
title: HiAI_SingleOpExecutorFusedConvolutionActivationParam
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 结构体 > HiAI_SingleOpExecutorFusedConvolutionActivationParam
category: harmonyos-references
scraped_at: 2026-09-02T15:03:10+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0d9a7aa497adeed07c18bb08eea1a362ec3688e48d568fa0cefe63bfa0f40dd
---

```cpp
typedef struct HiAI_SingleOpExecutorFusedConvolutionActivationParam {...} HiAI_SingleOpExecutorFusedConvolutionActivationParam
```

## 概述

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：** [CANN](cannkit.md)

**所在头文件：** [hiai\_single\_op.h](cannkit-hiai-single-op-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \* [options](cannkit-sopexec-fusedconv-actparam.md#options) | 指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [convOpDesc](cannkit-sopexec-fusedconv-actparam.md#convopdesc) | 指向卷积算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [actOpDesc](cannkit-sopexec-fusedconv-actparam.md#actopdesc) | 指向激活算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [input](cannkit-sopexec-fusedconv-actparam.md#input) | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [output](cannkit-sopexec-fusedconv-actparam.md#output) | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [filter](cannkit-sopexec-fusedconv-actparam.md#filter) | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [bias](cannkit-sopexec-fusedconv-actparam.md#bias) | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |

## 结构体成员变量说明

### actOpDesc

```cpp
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::actOpDesc
```

**描述**

指向激活算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

### bias

```cpp
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::bias
```

**描述**

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

### convOpDesc

```cpp
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::convOpDesc
```

**描述**

指向卷积算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

### filter

```cpp
HiAI_SingleOpTensor* HiAI_SingleOpExecutorFusedConvolutionActivationParam::filter
```

**描述**

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

### input

```cpp
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::input
```

**描述**

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

### options

```cpp
HiAI_SingleOpOptions* HiAI_SingleOpExecutorFusedConvolutionActivationParam::options
```

**描述**

指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

### output

```cpp
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorFusedConvolutionActivationParam::output
```

**描述**

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。
