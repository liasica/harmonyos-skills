---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-convparam
title: HiAI_SingleOpExecutorConvolutionParam
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 结构体 > HiAI_SingleOpExecutorConvolutionParam
category: harmonyos-references
scraped_at: 2026-04-28T08:18:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eacb6c07c1e508bcd3fe149052bbec22bbf877e20eca5b2ad043b875dfa1acdb
---

## 概述

PhonePC/2in1TabletTV

[HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：** [CANN](cannkit.md)

**所在头文件：** [hiai\_single\_op.h](cannkit-hiai-single-op-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \* [options](cannkit-sopexec-convparam.md#options) | 指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [opDesc](cannkit-sopexec-convparam.md#opdesc) | 指向卷积算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [input](cannkit-sopexec-convparam.md#input) | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [output](cannkit-sopexec-convparam.md#output) | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [filter](cannkit-sopexec-convparam.md#filter) | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [bias](cannkit-sopexec-convparam.md#bias) | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### bias

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::bias
```

**描述**

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

### filter

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::filter
```

**描述**

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

### input

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::input
```

**描述**

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

### opDesc

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorConvolutionParam::opDesc
```

**描述**

指向卷积算子对应的[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

### options

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpOptions* HiAI_SingleOpExecutorConvolutionParam::options
```

**描述**

指向[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

### output

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::output
```

**描述**

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。
