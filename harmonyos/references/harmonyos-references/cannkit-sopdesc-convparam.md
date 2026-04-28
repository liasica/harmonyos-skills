---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopdesc-convparam
title: HiAISingleOpDescriptor_ConvolutionParam
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 结构体 > HiAISingleOpDescriptor_ConvolutionParam
category: harmonyos-references
scraped_at: 2026-04-28T08:18:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb21595b9f9bdcc55dcb6629ad006365fd53e0a4ccbfbce032e554d209f77f89
---

## 概述

PhonePC/2in1TabletTV

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：** [CANN](cannkit.md)

**所在头文件：** [hiai\_single\_op.h](cannkit-hiai-single-op-8h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_SingleOpConvMode](cannkit.md#hiai_singleopconvmode) [convMode](cannkit-sopdesc-convparam.md#convmode) | 卷积模式。 |
| int64\_t [strides](cannkit-sopdesc-convparam.md#strides) [2] | 卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。 |
| int64\_t [dilations](cannkit-sopdesc-convparam.md#dilations) [2] | 卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。 |
| int64\_t [pads](cannkit-sopdesc-convparam.md#pads) [4] | 各个轴起始和末尾的填充长度，是一个长度为4的int数组[h\_begin, h\_end, w\_begin, w\_end]。该值仅在**padMode**为**HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC**时生效。 |
| int64\_t [groups](cannkit-sopdesc-convparam.md#groups) | 输入通道被划分成的组数。若**convMode**为**HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**，**groups**不生效。 |
| [HiAI\_SingleOpPadMode](cannkit.md#hiai_singleoppadmode) [padMode](cannkit-sopdesc-convparam.md#padmode) | 输入的填充方式。对于**HIAI\_SINGLEOP\_CONV\_MODE\_COMMON**和**HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**， 支持**0** (SPECIFIC)，**1** (SAME)，**2** (SAME\_UPPER)，**3** (SAME\_LOWER)和**4** (VALID)。对于 **HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED**, 支持**0** (SPECIFIC)，**1** (SAME)和**4** (VALID)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTV

### convMode

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpConvMode HiAISingleOpDescriptor_ConvolutionParam::convMode
```

**描述**

卷积模式。

### dilations

PhonePC/2in1TabletTV

```
1. int64_t HiAISingleOpDescriptor_ConvolutionParam::dilations[2]
```

**描述**

卷积核在高度和宽度上的扩张率，是一个长度为2的int数组[dilationHeight, dilationWidth]。

### groups

PhonePC/2in1TabletTV

```
1. int64_t HiAISingleOpDescriptor_ConvolutionParam::groups
```

**描述**

输入通道被划分成的组数。若**convMode**为**HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**，**groups**不生效。

### padMode

PhonePC/2in1TabletTV

```
1. HiAI_SingleOpPadMode HiAISingleOpDescriptor_ConvolutionParam::padMode
```

**描述**

输入的填充方式。对于**HIAI\_SINGLEOP\_CONV\_MODE\_COMMON**和**HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**， 支持**0** (SPECIFIC)，**1** (SAME)，**2** (SAME\_UPPER)，**3** (SAME\_LOWER)和**4** (VALID)。对于 **HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED**, 支持**0** (SPECIFIC)，**1** (SAME)和**4** (VALID)。

### pads

PhonePC/2in1TabletTV

```
1. int64_t HiAISingleOpDescriptor_ConvolutionParam::pads[4]
```

**描述**

各个轴起始和末尾的填充长度，是一个长度为4的int数组[h\_begin, h\_end, w\_begin, w\_end]。该值仅在**padMode**为**HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC**时生效。

### strides

PhonePC/2in1TabletTV

```
1. int64_t HiAISingleOpDescriptor_ConvolutionParam::strides[2]
```

**描述**

卷积核在高度和宽度上的移动步幅，是一个长度为2的int数组[strideHeight, strideWidth]。
