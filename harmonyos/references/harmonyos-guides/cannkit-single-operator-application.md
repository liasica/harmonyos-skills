---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-single-operator-application
title: 单算子应用
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 单算子应用
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:34+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:260a50e8ea2fe1db7e91285db97650b491d506ef93547d89d84c63404dad0e00
---

## 概述

CANN Kit提供独立的算子创建和计算通路，三方框架可以在模型加载、推理过程中，将卷积、深度卷积等算子通过单算子对接的方式迁移至NPU，经过硬件平台的加速计算，与整网模式对比灵活度更高，相比于整网CPU计算性能更优。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/UVNUsDcRRpiX1luiiL6yRg/zh-cn_image_0000002736314393.jpg)

以下为单算子Tensor创建，单算子执行器创建、加载、执行接口，接口使用请参见[开发步骤](cannkit-single-operator-application.md#开发步骤)。如要使用更丰富的设置和查询接口，请参见[API参考](../harmonyos-references/cannkit.md)。

**表1** 单算子接口及功能介绍

| 接口名 | 描述 |
| --- | --- |
| HiAI\_SingleOpTensorDesc \* HMS\_HiAISingleOpTensorDesc\_Create (const int64\_t \*dims, size\_t dimNum, HiAI\_SingleOpDataType dataType, HiAI\_SingleOpFormat format, bool isVirtual); | 创建HiAI\_SingleOpTensorDesc对象。 |
| void HMS\_HiAISingleOpTensorDesc\_Destroy (HiAI\_SingleOpTensorDesc \*\*tensorDesc); | 释放HiAI\_SingleOpTensorDesc对象。 |
| HiAI\_SingleOpBuffer \* HMS\_HiAISingleOpBuffer\_Create (size\_t dataSize); | 按照指定的内存大小创建HiAI\_SingleOpBuffer对象。 |
| size\_t HMS\_HiAISingleOpBuffer\_GetSize (const HiAI\_SingleOpBuffer \*buffer); | 查询HiAI\_SingleOpBuffer的字节大小。 |
| void \* HMS\_HiAISingleOpBuffer\_GetData (const HiAI\_SingleOpBuffer \*buffer); | 查询HiAI\_SingleOpBuffer的内存地址。 |
| OH\_NN\_ReturnCode HMS\_HiAISingleOpBuffer\_Destroy (HiAI\_SingleOpBuffer \*\*buffer); | 释放HiAI\_SingleOpBuffer对象。 |
| HiAI\_SingleOpTensor \* HMS\_HiAISingleOpTensor\_CreateFromTensorDesc (const HiAI\_SingleOpTensorDesc \*desc); | 根据HiAI\_SingleOpTensorDesc创建HiAI\_SingleOpTensor对象。 |
| HiAI\_SingleOpTensor \* HMS\_HiAISingleOpTensor\_CreateFromConst (const HiAI\_SingleOpTensorDesc \*desc, void \*data, size\_t dataSize); | 根据HiAI\_SingleOpTensorDesc、常量数据（如卷积权重、偏置等）的内存地址和数据大小创建HiAI\_SingleOpTensor对象。 |
| HiAI\_SingleOpTensorDesc \* HMS\_HiAISingleOpTensor\_GetTensorDesc (const HiAI\_SingleOpTensor \*tensor); | 获取HiAI\_SingleOpTensor的Tensor描述。 |
| HiAI\_SingleOpBuffer \* HMS\_HiAISingleOpTensor\_GetBuffer (const HiAI\_SingleOpTensor \*tensor); | 获取HiAI\_SingleOpTensor的Buffer。 |
| OH\_NN\_ReturnCode HMS\_HiAISingleOpTensor\_Destroy (HiAI\_SingleOpTensor \*\*tensor); | 释放HiAI\_SingleOpTensor对象。 |
| HiAI\_SingleOpOptions \* HMS\_HiAISingleOpOptions\_Create (void); | 创建HiAI\_SingleOpOptions对象。 |
| void HMS\_HiAISingleOpOptions\_Destroy (HiAI\_SingleOpOptions \*\*options); | 释放HiAI\_SingleOpOptions对象。 |
| HiAI\_SingleOpDescriptor\* HMS\_HiAISingleOpDescriptor\_CreateConvolution(HiAISingleOpDescriptor\_ConvolutionParam param); | 创建卷积类（普通卷积、转置卷积、深度卷积）的描述符对象。 |
| void HMS\_HiAISingleOpDescriptor\_Destroy (HiAI\_SingleOpDescriptor \*\*opDesc); | 释放HiAI\_SingleOpDescriptor对象。 |
| HiAI\_SingleOpExecutor\* HMS\_HiAISingleOpExecutor\_CreateConvolution(HiAI\_SingleOpExecutorConvolutionParam param); | 创建卷积类算子对应的HiAI\_SingleOpExecutor对象。 |
| size\_t HMS\_HiAISingleOpExecutor\_GetWorkspaceSize (const HiAI\_SingleOpExecutor \*executor); | 查询HiAI\_SingleOpExecutor所需的ION内存工作空间的字节大小。 |
| OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Init (HiAI\_SingleOpExecutor \*executor, void \*workspace, size\_t workspaceSize); | 加载HiAI\_SingleOpExecutor。 |
| OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Execute (HiAI\_SingleOpExecutor \*executor, HiAI\_SingleOpTensor \*input[], int32\_t inputNum, HiAI\_SingleOpTensor \*output[], int32\_t outputNum); | 执行同步运算推理。 |
| OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Destroy (HiAI\_SingleOpExecutor \*\*executor); | 销毁HiAI\_SingleOpExecutor对象，释放执行器占用的内存。 |

## 开发步骤

以下开发步骤以卷积单算子为例。

1. 创建单算子执行器。

   1. 调用[HMS\_HiAISingleOpOptions\_Create](../harmonyos-references/cannkit.md#hms_hiaisingleopoptions_create)，创建单算子配置对象。
   2. 调用[HMS\_HiAISingleOpDescriptor\_CreateConvolution](../harmonyos-references/cannkit.md#hms_hiaisingleopdescriptor_createconvolution)，创建卷积类算子描述符对象。
   3. 调用[HMS\_HiAISingleOpTensor\_CreateFromConst](../harmonyos-references/cannkit.md#hms_hiaisingleoptensor_createfromconst)，分别创建卷积算子的权重、偏置单算子Tensor。
   4. 调用[HMS\_HiAISingleOpTensorDesc\_Create](../harmonyos-references/cannkit.md#hms_hiaisingleoptensordesc_create)，分别创建单算子输入Tensor、输出Tensor的描述对象。
   5. 调用[HMS\_HiAISingleOpExecutor\_CreateConvolution](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_createconvolution)，将上述创建好的卷积类算子描述符对象、卷积算子的权重Tensor、卷积算子的偏置Tensor、输入Tensor描述、输出Tensor描述作为输入，创建单算子执行器；

      如果需要创建卷积算子与激活算子的融合算子执行器，还需要调用[HMS\_HiAISingleOpDescriptor\_CreateActivation](../harmonyos-references/cannkit.md#hms_hiaisingleopdescriptor_createactivation)，创建激活类算子描述符对象，然后调用[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation)创建融合算子执行器。
   6. 创建成功后，调用[HMS\_HiAISingleOpDescriptor\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleopdescriptor_destroy)释放算子描述符对象，调用[HMS\_HiAISingleOpOptions\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleopoptions_destroy)释放单算子创建配置对象。
2. 创建输入/输出Tensor。

   1. 调用[HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](../harmonyos-references/cannkit.md#hms_hiaisingleoptensor_createfromtensordesc)，分别创建单算子输入Tensor、输出Tensor。
   2. 创建成功后，调用[HMS\_HiAISingleOpTensorDesc\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleoptensordesc_destroy)释放Tensor描述符对象。
   3. 调用[HMS\_HiAISingleOpTensor\_GetBuffer](../harmonyos-references/cannkit.md#hms_hiaisingleoptensor_getbuffer)，获取输入/输出Tensor内部的Buffer对象。
   4. 调用[HMS\_HiAISingleOpBuffer\_GetData](../harmonyos-references/cannkit.md#hms_hiaisingleopbuffer_getdata)，获取申请好的输入/输出ION内存地址，可用于该单算子在模型整网推理中的输入写入、输出读取。
3. 加载单算子执行器。

   1. 调用[HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_getworkspacesize)，获取已创建的单算子执行器在执行推理计算时需要的ION内存工作空间大小。
   2. 调用[HMS\_HiAISingleOpBuffer\_Create](../harmonyos-references/cannkit.md#hms_hiaisingleopbuffer_create)，根据单算子执行器所需的ION内存工作空间大小创建足够的工作空间。
   3. 调用[HMS\_HiAISingleOpBuffer\_GetData](../harmonyos-references/cannkit.md#hms_hiaisingleopbuffer_getdata)，获取申请好的ION内存工作空间的地址。
   4. 调用[HMS\_HiAISingleOpExecutor\_Init](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_init)，使用工作空间内存地址、工作空间大小，加载创建好的单算子执行器。
4. 执行推理运算。

   调用[HMS\_HiAISingleOpExecutor\_Execute](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_execute)，执行同步运算推理。
5. 卸载单算子执行器，释放资源。

   * 调用[HMS\_HiAISingleOpTensor\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleoptensor_destroy)，释放输入、输出Tensor对象
   * 调用[HMS\_HiAISingleOpBuffer\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleopbuffer_destroy)，释放工作空间。
   * 调用[HMS\_HiAISingleOpExecutor\_Destroy](../harmonyos-references/cannkit.md#hms_hiaisingleopexecutor_destroy)，释放执行器对象。

## 示例说明

假定现在有一个深度卷积算子，输入维度为1x8x224x224，输入NCHW格式排布的float32类型数据，准备好NCHW排布的权重与偏置数据，调用单算子接口推理运算获得NCHW格式float32类型的输出可以参考如下示例代码：

```
// 示例算子参数
// 单算子卷积模式
HiAI_SingleOpConvMode convMode = HIAI_SINGLEOP_CONV_MODE_DEPTHWISE;
int64_t strides[2] = {1, 1};
int64_t dilations[2] = {1, 1};
int64_t pads[4] = {0, 0, 0, 0};
int64_t groups = 1;
// 单算子填充模式
HiAI_SingleOpPadMode padMode = HIAI_SINGLEOP_PAD_MODE_SAME;
int64_t filterDims[4] = {8, 1, 3, 3};
size_t filterDataSize = 8 * 1 * 3 * 3 * sizeof(float);
void *filterData = malloc(filterDataSize);
// ...
int64_t biasDims[1] = {8};
size_t biasDataSize = 8 * sizeof(float);
void *biasData = malloc(biasDataSize);
// ...
int64_t inputDims[4] = {1, 8, 224, 224};
HiAI_SingleOpDataType inputDataType = HIAI_SINGLEOP_DT_FLOAT;
// 单算子张量排布格式
HiAI_SingleOpFormat inputFormat = HIAI_SINGLEOP_FORMAT_NCHW;
bool inputIsVirtual = false;
// 若不指定算子输出数据类型和排布格式，请设置数据类型为HIAI_SINGLEOP_DT_UNDEFINED，排布格式为HIAI_SINGLEOP_FORMAT_RESERVED
// 在单算子创建完成后，调用HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc，将输出Tensor描述更新为硬件适配最优的数据类型和排布格式
int64_t outputDims[4] = {1, 8, 224, 224};
HiAI_SingleOpDataType outputDataType = HIAI_SINGLEOP_DT_FLOAT;
HiAI_SingleOpFormat outputFormat = HIAI_SINGLEOP_FORMAT_NCHW;
bool outputIsVirtual = false;

// 创建单算子执行器
options_ = HMS_HiAISingleOpOptions_Create();
HiAISingleOpDescriptor_ConvolutionParam convOpDescCreateParam = {convMode, {0}, {0}, {0}, groups, padMode};
memcpy(convOpDescCreateParam.strides, strides, opDescSize * sizeof(int64_t));
memcpy(convOpDescCreateParam.dilations, dilations, opDescSize * sizeof(int64_t));
memcpy(convOpDescCreateParam.pads, pads, tensorSize * sizeof(int64_t));
// 创建卷积类的描述符对象
convOpDesc_ = HMS_HiAISingleOpDescriptor_CreateConvolution(convOpDescCreateParam);
// 创建一个单算子tensor描述对象，根据维度、数据类型和格式
filterDesc_ = HMS_HiAISingleOpTensorDesc_Create(filterDims, tensorSize, inputDataType, inputFormat, false);
// 创建一个单算子tensor对象
filter_ = HMS_HiAISingleOpTensor_CreateFromConst(filterDesc_, filterData, filterDataSize);
biasDesc_ = HMS_HiAISingleOpTensorDesc_Create(biasDims, 1, outputDataType, outputFormat, false);
bias_ = HMS_HiAISingleOpTensor_CreateFromConst(biasDesc_, biasData, biasDataSize);
inputDesc_ = HMS_HiAISingleOpTensorDesc_Create(inputDims, tensorSize, inputDataType, inputFormat, inputIsVirtual);
outputDesc_ = HMS_HiAISingleOpTensorDesc_Create(outputDims, tensorSize, outputDataType, outputFormat,
                                                outputIsVirtual);
// 构造单算子卷积 executor参数
executorCreateParam_ = {options_, convOpDesc_, inputDesc_, outputDesc_, filter_, bias_};
// ...
// 创建卷积单算子executor
executor_ = HMS_HiAISingleOpExecutor_CreateConvolution(executorCreateParam_);
if (executor_ == nullptr) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp executor create failed");
    // ...
}
// 对不需要的资源建议即时销毁
HMS_HiAISingleOpTensorDesc_Destroy(&filterDesc_);
HMS_HiAISingleOpTensorDesc_Destroy(&biasDesc_);
HMS_HiAISingleOpOptions_Destroy(&options_);
HMS_HiAISingleOpDescriptor_Destroy(&convOpDesc_);
ret = HMS_HiAISingleOpTensor_Destroy(&filter_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp filter destroy failed");
    // ...
}
ret = HMS_HiAISingleOpTensor_Destroy(&bias_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp bias destroy failed");
    // ...
}
// ...
// 统计算子构图耗时
std::chrono::system_clock::time_point createTimeBegin = std::chrono::system_clock::now();
// 创建输入/输出Tensor
input_ = HMS_HiAISingleOpTensor_CreateFromTensorDesc(inputDesc_);
output_ = HMS_HiAISingleOpTensor_CreateFromTensorDesc(outputDesc_);
// 单算子输入Tensor和输出Tensor的内存必须为ION内存以节省拷贝开销
// 创建输入Tensor成功后，可以使用以下方式获取输入Tensor内的ION内存地址进行输入数据填装
// 输出Tensor内的ION内存地址也可以用以下方式获取，在推理计算成功后用于输出数据读取
HiAI_SingleOpBuffer *inputBuffer = HMS_HiAISingleOpTensor_GetBuffer(input_);
void *inputData = HMS_HiAISingleOpBuffer_GetData(inputBuffer);
size_t inputDataSize = HMS_HiAISingleOpBuffer_GetSize(inputBuffer);
memset(inputData, 0, inputDataSize);
std::chrono::system_clock::time_point createTimeEnd = std::chrono::system_clock::now();
createTensorTime = GetRunTime(createTimeBegin, createTimeEnd);

HMS_HiAISingleOpTensorDesc_Destroy(&inputDesc_);
HMS_HiAISingleOpTensorDesc_Destroy(&outputDesc_);
// ...
// 查询单算子执行器所需的ION内存工作空间的字节大小
size_t workspaceSize = HMS_HiAISingleOpExecutor_GetWorkspaceSize(executor_);
// 若存在多个单算子执行器，各个执行器的工作空间内存可以复用，只需要申请所需的最大工作空间即可
workspaceBuffer_ = HMS_HiAISingleOpBuffer_Create(workspaceSize);
void *workspace = HMS_HiAISingleOpBuffer_GetData(workspaceBuffer_);
// 在调用该接口之前，需要申请执行器所需的工作空间内存
OH_NN_ReturnCode ret = HMS_HiAISingleOpExecutor_Init(executor_, workspace, workspaceSize);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp executor init failed");
    // ...
}
// ...
// 多轮多次执行推理运算，统计算子的推理耗时
for (size_t i = 0; i < times; i++) {
    for (size_t j = 0; j < opNum; j++) {
        // 执行推理运算
        HiAI_SingleOpTensor *inputs[] = {input_};
        HiAI_SingleOpTensor *outputs[] = {output_};
        std::chrono::system_clock::time_point executeTimeBegin = std::chrono::system_clock::now();
        OH_NN_ReturnCode ret = HMS_HiAISingleOpExecutor_Execute(executor_, inputs, 1, outputs, 1);
        if (ret != OH_NN_SUCCESS) {
            OH_LOG_ERROR(LOG_APP, "HMS_HiAISingleOp executor execute failed");
            // ...
        }
        std::chrono::system_clock::time_point executeTimeEnd = std::chrono::system_clock::now();
        auto executeElapsedTime = GetRunTime(executeTimeBegin, executeTimeEnd);
        OH_LOG_INFO(LOG_APP, "idx-%zu execute succ: %llu us", j, executeElapsedTime);
        aveTime[j] += executeElapsedTime;
    }
    OH_LOG_INFO(LOG_APP, "------ Round %zu ------ ", i);
}
// ...
// 统计算子资源释放耗时
std::chrono::system_clock::time_point destroyTimeBegin = std::chrono::system_clock::now();
// 销毁输入Tensor，释放资源
OH_NN_ReturnCode ret = HMS_HiAISingleOpTensor_Destroy(&input_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp input_ destroy failed");
    // ...
}
// 销毁输出Tensor，释放资源
ret = HMS_HiAISingleOpTensor_Destroy(&output_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp output_ destroy failed");
    // ...
}
// 释放单算子Buffer对象
ret = HMS_HiAISingleOpBuffer_Destroy(&workspaceBuffer_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp workspaceBuffer_ destroy failed");
    // ...
}
// 销毁单算子执行器，释放执行器占用的内存
ret = HMS_HiAISingleOpExecutor_Destroy(&executor_);
if (ret != OH_NN_SUCCESS) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp executor destroy failed");
    // ...
}
std::chrono::system_clock::time_point destroyTimeEnd = std::chrono::system_clock::now();
destroyTime = GetRunTime(destroyTimeBegin, destroyTimeEnd);
// ...
// 汇总各阶段耗时结果
std::vector<float> outputs(returnArraySize, 0);
if (!times_) {
    OH_LOG_ERROR(LOG_APP, "iteration times_ is not initialized or is zero");
    return outputs;
}
if (aveTime.empty()) {
    OH_LOG_INFO(LOG_APP, "HMS_HiAISingleOp_GetResult failed");
    return outputs;
}
// 获取构图时间，微妙转秒
createTensorTime /= 1000000.0f;
outputs[0] = createTensorTime;
// 获取推理时间
executeTime = 0;
for (size_t i = 0; i < opNum; i++) {
    aveTime[i] /= times_;
    OH_LOG_INFO(LOG_APP, "idx-%zu average time: %.2f us", i, aveTime[i]);
    executeTime += aveTime[i];
}
OH_LOG_INFO(LOG_APP, "op average time sum: %.2f us", executeTime);
executeTime /= 1000000.0f;
outputs[1] = executeTime;
// 获取资源释放时间
destroyTime /= 1000000.0f;
outputs[2] = destroyTime;
OH_LOG_INFO(LOG_APP, "GetResult success");
return outputs;
```
