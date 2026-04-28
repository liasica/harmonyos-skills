---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-single-op-8h
title: hiai_single_op.h
breadcrumb: API参考 > AI > CANN Kit（CANN异构计算框架服务） > C API > 头文件和结构体 > 头文件 > hiai_single_op.h
category: harmonyos-references
scraped_at: 2026-04-28T08:18:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:196c60f17f1da7ba72d3627e3e2464f76616b4acabe6362f48018caff0b47e68
---

## 概述

PhonePC/2in1TabletTV

定义CANN Kit单算子接口，用于单算子的创建、计算以及Tensor和Buffer的管理。

**引用文件：** <CANNKit/hiai\_single\_op.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 5.0.0(12)

**相关模块：** [CANN](cannkit.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| struct [HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) | [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。 |
| struct [HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) | [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。 |
| struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) | [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef struct [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) | 单算子Tensor描述的句柄。 |
| typedef struct [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) | 单算子Buffer句柄。 |
| typedef struct [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) | 单算子Tensor句柄。 |
| typedef struct [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) | 单算子选项句柄。 |
| typedef struct [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) | 单算子的算子描述句柄。 |
| typedef struct [HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) | [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) | [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) | [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)输入参数。 |
| typedef struct [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) | 单算子执行器句柄。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) {  HIAI\_SINGLEOP\_DT\_FLOAT = 0,  HIAI\_SINGLEOP\_DT\_FLOAT16 = 1,  HIAI\_SINGLEOP\_DT\_UNDEFINED = 17  } | 单算子张量数据类型枚举。 |
| [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) {  HIAI\_SINGLEOP\_FORMAT\_NCHW = 0,  HIAI\_SINGLEOP\_FORMAT\_NHWC = 1,  HIAI\_SINGLEOP\_FORMAT\_ND = 2,  HIAI\_SINGLEOP\_FORMAT\_NC1HWC0 = 3,  HIAI\_SINGLEOP\_FORMAT\_NC4HW4 = 28,  HIAI\_SINGLEOP\_FORMAT\_NC8HW8 = 31,  HIAI\_SINGLEOP\_FORMAT\_RESERVED = 255  } | 单算子张量排布格式枚举。 |
| [HiAI\_SingleOpConvMode](cannkit.md#hiai_singleopconvmode) {  HIAI\_SINGLEOP\_CONV\_MODE\_COMMON = 0,  HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED = 1,  HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE = 2  } | 单算子卷积模式枚举。 |
| [HiAI\_SingleOpPadMode](cannkit.md#hiai_singleoppadmode) {  HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC = 0,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME = 1,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER = 2,  HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER = 3,  HIAI\_SINGLEOP\_PAD\_MODE\_VALID = 4  } | 单算子填充模式枚举。 |
| [HiAI\_SingleOpActivationType](cannkit.md#hiai_singleopactivationtype) {  HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU = 0,  HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6 = 1  } | 单算子激活模式枚举。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) {  HIAI\_SINGLEOP\_OPTIMIZED = 0,  HIAI\_SINGLEOP\_COMMON = 1,  HIAI\_SINGLEOP\_UNSUPPORTED = 2  } | 单算子支持状态枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensorDesc\_Create](cannkit.md#hms_hiaisingleoptensordesc_create) (const int64\_t \*dims, size\_t dimNum, [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) dataType, [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) format, bool isVirtual) | 创建[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。 |
| size\_t [HMS\_HiAISingleOpTensorDesc\_GetDimensionCount](cannkit.md#hms_hiaisingleoptensordesc_getdimensioncount) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度数量。 |
| int64\_t [HMS\_HiAISingleOpTensorDesc\_GetDimension](cannkit.md#hms_hiaisingleoptensordesc_getdimension) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc, size\_t index) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)指定索引的维度长度。 |
| [HiAI\_SingleOpDataType](cannkit.md#hiai_singleopdatatype) [HMS\_HiAISingleOpTensorDesc\_GetDataType](cannkit.md#hms_hiaisingleoptensordesc_getdatatype) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的数据类型。 |
| [HiAI\_SingleOpFormat](cannkit.md#hiai_singleopformat) [HMS\_HiAISingleOpTensorDesc\_GetFormat](cannkit.md#hms_hiaisingleoptensordesc_getformat) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的排布格式。 |
| bool [HMS\_HiAISingleOpTensorDesc\_IsVirtual](cannkit.md#hms_hiaisingleoptensordesc_isvirtual) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)是否为虚拟张量。 |
| size\_t [HMS\_HiAISingleOpTensorDesc\_GetByteSize](cannkit.md#hms_hiaisingleoptensordesc_getbytesize) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*tensorDesc) | 查询基于[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)的维度和数据类型计算的数据占用字节数。 |
| void [HMS\_HiAISingleOpTensorDesc\_Destroy](cannkit.md#hms_hiaisingleoptensordesc_destroy) ([HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*\*tensorDesc) | 释放[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)对象。 |
| [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpBuffer\_Create](cannkit.md#hms_hiaisingleopbuffer_create) (size\_t dataSize) | 按照指定的内存大小创建[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。 |
| size\_t [HMS\_HiAISingleOpBuffer\_GetSize](cannkit.md#hms_hiaisingleopbuffer_getsize) (const [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*buffer) | 查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的字节大小。 |
| void \* [HMS\_HiAISingleOpBuffer\_GetData](cannkit.md#hms_hiaisingleopbuffer_getdata) (const [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*buffer) | 查询[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpBuffer\_Destroy](cannkit.md#hms_hiaisingleopbuffer_destroy) ([HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \*\*buffer) | 释放[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](cannkit.md#hms_hiaisingleoptensor_createfromtensordesc) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](cannkit.md#hms_hiaisingleoptensor_createfromsingleopbuffer) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、[HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer)的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromConst](cannkit.md#hms_hiaisingleoptensor_createfromconst) (const [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize) | 根据[HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc)、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensor\_GetTensorDesc](cannkit.md#hms_hiaisingleoptensor_gettensordesc) (const [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*tensor) | 获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Tensor描述。 |
| [HiAI\_SingleOpBuffer](cannkit.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpTensor\_GetBuffer](cannkit.md#hms_hiaisingleoptensor_getbuffer) (const [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*tensor) | 获取[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)的Buffer。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpTensor\_Destroy](cannkit.md#hms_hiaisingleoptensor_destroy) ([HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*\*tensor) | 释放[HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor)对象。 |
| [HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \* [HMS\_HiAISingleOpOptions\_Create](cannkit.md#hms_hiaisingleopoptions_create) (void) | 创建[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。 |
| void [HMS\_HiAISingleOpOptions\_Destroy](cannkit.md#hms_hiaisingleopoptions_destroy) ([HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions) \*\*options) | 释放[HiAI\_SingleOpOptions](cannkit.md#hiai_singleopoptions)对象。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateConvolution](cannkit.md#hms_hiaisingleopdescriptor_createconvolution) ([HiAISingleOpDescriptor\_ConvolutionParam](cannkit-sopdesc-convparam.md) param) | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。 |
| [HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateActivation](cannkit.md#hms_hiaisingleopdescriptor_createactivation) ([HiAI\_SingleOpActivationType](cannkit.md#hiai_singleopactivationtype) activationType, float coef) | 创建激活函数类的描述符对象。 |
| void [HMS\_HiAISingleOpDescriptor\_Destroy](cannkit.md#hms_hiaisingleopdescriptor_destroy) ([HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor) \*\*opDesc) | 释放[HiAI\_SingleOpDescriptor](cannkit.md#hiai_singleopdescriptor)对象。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckConvolution](cannkit.md#hms_hiaisingleopexecutor_precheckconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) param) | 预查询卷积算子的支持状态。 |
| [HiAI\_SingleOpSupportStatus](cannkit.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_precheckfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) param) | 预查询卷积和激活融合算子的支持状态。 |
| [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateConvolution](cannkit.md#hms_hiaisingleopexecutor_createconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](cannkit-sopexec-convparam.md) param) | 创建卷积类算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。 |
| [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](cannkit-sopexec-fusedconv-actparam.md) param) | 创建卷积和激活融合算子对应的[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](cannkit.md#hms_hiaisingleopexecutor_updateoutputtensordesc) (const [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, uint32\_t index, [HiAI\_SingleOpTensorDesc](cannkit.md#hiai_singleoptensordesc) \*output) | 更新[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)的输出tensor描述。 |
| size\_t [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](cannkit.md#hms_hiaisingleopexecutor_getworkspacesize) (const [HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor) | 查询[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)所需的ION内存工作空间的字节大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Init](cannkit.md#hms_hiaisingleopexecutor_init) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, void \*workspace, size\_t workspaceSize) | 加载[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Execute](cannkit.md#hms_hiaisingleopexecutor_execute) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*executor, [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*input[], int32\_t inputNum, [HiAI\_SingleOpTensor](cannkit.md#hiai_singleoptensor) \*output[], int32\_t outputNum) | 执行同步运算推理。 |
| OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Destroy](cannkit.md#hms_hiaisingleopexecutor_destroy) ([HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor) \*\*executor) | 销毁[HiAI\_SingleOpExecutor](cannkit.md#hiai_singleopexecutor)对象，释放执行器占用的内存。 |
