---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-single-operator-application
title: 单算子应用
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 单算子应用
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5c9131163fd67061fd65f59d8bfcd2ed6ec7839b10437d6de0fda9727c207e7b
---

## 概述

CANN Kit提供独立的算子创建和计算通路，三方框架可以在模型加载、推理过程中，将卷积、深度卷积等算子通过单算子对接的方式迁移至NPU，经过硬件平台的加速计算，与整网模式对比灵活度更高，相比于整网CPU计算性能更优。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fO7vrAIrTzi88MeZnr3P4Q/zh-cn_image_0000002558606068.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T054100Z&HW-CC-Expire=86400&HW-CC-Sign=12E7A35CC350467F9A11E1D83B5F8720BC2B37542C80E234B237587EDB30A962)

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
1. #include "CANNKit/hiai_single_op.h"
2. #include <cstdio>
3. #include <cstdlib>
4. #include <cstring>
5. // 示例算子参数
6. // 单算子卷积模式
7. HiAI_SingleOpConvMode convMode = HIAI_SINGLEOP_CONV_MODE_DEPTHWISE;
8. int64_t strides[2] = {1, 1};
9. int64_t dilations[2] = {1, 1};
10. int64_t pads[4] = {0, 0, 0, 0};
11. int64_t groups = 1;
12. // 单算子填充模式
13. HiAI_SingleOpPadMode padMode = HIAI_SINGLEOP_PAD_MODE_SAME;
14. int64_t filterDims[4] = {8, 1, 3, 3};
15. size_t filterDataSize = 8 * 1 * 3 * 3 * sizeof(float);
16. void* filterData = malloc(filterDataSize);
17. int64_t biasDims[1] = {8};
18. size_t biasDataSize = 8 * sizeof(float);
19. void* biasData = malloc(biasDataSize);
20. int64_t inputDims[4] = {1, 8, 224, 224};
21. HiAI_SingleOpDataType inputDataType = HIAI_SINGLEOP_DT_FLOAT;
22. // 单算子张量排布格式
23. HiAI_SingleOpFormat inputFormat = HIAI_SINGLEOP_FORMAT_NCHW;
24. bool inputIsVirtual = false;
25. // 若不指定算子输出数据类型和排布格式，请设置数据类型为HIAI_SINGLEOP_DT_UNDEFINED，排布格式为HIAI_SINGLEOP_FORMAT_RESERVED
26. // 在单算子创建完成后，调用HMS_HiAISingleOpExecutor_UpdateOutputTensorDesc，将输出Tensor描述更新为硬件适配最优的数据类型和排布格式
27. int64_t outputDims[4] = {1, 8, 224, 224};
28. HiAI_SingleOpDataType outputDataType = HIAI_SINGLEOP_DT_FLOAT;
29. HiAI_SingleOpFormat outputFormat = HIAI_SINGLEOP_FORMAT_NCHW;
30. bool outputIsVirtual = false;

32. // 创建单算子执行器
33. HiAI_SingleOpOptions* options = HMS_HiAISingleOpOptions_Create();
34. HiAISingleOpDescriptor_ConvolutionParam convOpDescCreateParam = {convMode, {0}, {0}, {0}, groups, padMode};
35. memcpy(convOpDescCreateParam.strides, strides, 2 * sizeof(int64_t));
36. memcpy(convOpDescCreateParam.dilations, dilations, 2 * sizeof(int64_t));
37. memcpy(convOpDescCreateParam.pads, pads, 4 * sizeof(int64_t));
38. // 创建卷积类的描述符对象
39. HiAI_SingleOpDescriptor* convOpDesc = HMS_HiAISingleOpDescriptor_CreateConvolution(convOpDescCreateParam);
40. // 创建一个单算子tensor描述对象，根据维度、数据类型和格式
41. HiAI_SingleOpTensorDesc* filterDesc = HMS_HiAISingleOpTensorDesc_Create(filterDims, 4, HIAI_SINGLEOP_DT_FLOAT, HIAI_SINGLEOP_FORMAT_NCHW, false);
42. // 创建一个单算子tensor对象
43. HiAI_SingleOpTensor* filter = HMS_HiAISingleOpTensor_CreateFromConst(filterDesc, filterData, filterDataSize);
44. HiAI_SingleOpTensorDesc* biasDesc = HMS_HiAISingleOpTensorDesc_Create(biasDims, 1, HIAI_SINGLEOP_DT_FLOAT, HIAI_SINGLEOP_FORMAT_NCHW, false);
45. HiAI_SingleOpTensor* bias = HMS_HiAISingleOpTensor_CreateFromConst(biasDesc, biasData, biasDataSize);
46. HiAI_SingleOpTensorDesc* inputDesc = HMS_HiAISingleOpTensorDesc_Create(inputDims, 4, inputDataType, inputFormat, inputIsVirtual);
47. HiAI_SingleOpTensorDesc* outputDesc = HMS_HiAISingleOpTensorDesc_Create(outputDims, 4, outputDataType, outputFormat, outputIsVirtual);
48. // 构造单算子卷积executor参数
49. HiAI_SingleOpExecutorConvolutionParam executorCreateParam = {options, convOpDesc, inputDesc, outputDesc, filter, bias};
50. // 创建卷积单算子executor
51. HiAI_SingleOpExecutor* executor = HMS_HiAISingleOpExecutor_CreateConvolution(executorCreateParam);
52. if (executor == nullptr) {
53. printf("HMS_HiAISingleOp executor create failed. \n");
54. }
55. // 对不需要的资源建议即时销毁
56. HMS_HiAISingleOpTensorDesc_Destroy(&filterDesc);
57. HMS_HiAISingleOpTensorDesc_Destroy(&biasDesc);
58. HMS_HiAISingleOpOptions_Destroy(&options);
59. HMS_HiAISingleOpDescriptor_Destroy(&convOpDesc);
60. OH_NN_ReturnCode ret = HMS_HiAISingleOpTensor_Destroy(&filter);
61. if (ret != OH_NN_SUCCESS) {
62. printf("HMS_HiAISingleOp filter destroy failed.\n");
63. }
64. ret = HMS_HiAISingleOpTensor_Destroy(&bias);
65. if (ret != OH_NN_SUCCESS) {
66. printf("HMS_HiAISingleOp bias destroy failed.\n");
67. }

69. // 创建输入/输出Tensor
70. HiAI_SingleOpTensor* input = HMS_HiAISingleOpTensor_CreateFromTensorDesc(inputDesc);
71. HMS_HiAISingleOpTensorDesc_Destroy(&inputDesc);
72. HiAI_SingleOpTensor* output = HMS_HiAISingleOpTensor_CreateFromTensorDesc(outputDesc);
73. HMS_HiAISingleOpTensorDesc_Destroy(&outputDesc);
74. // 单算子输入Tensor和输出Tensor的内存必须为ION内存以节省拷贝开销
75. // 创建输入Tensor成功后，可以使用以下方式获取输入Tensor内的ION内存地址进行输入数据填装
76. // 输出Tensor内的ION内存地址也可以用以下方式获取，在推理计算成功后用于输出数据读取
77. HiAI_SingleOpBuffer* inputBuffer = HMS_HiAISingleOpTensor_GetBuffer(input);
78. void* inputData = HMS_HiAISingleOpBuffer_GetData(inputBuffer);
79. size_t inputDataSize = HMS_HiAISingleOpBuffer_GetSize(inputBuffer);
80. memset(inputData, 0, inputDataSize);

82. // 查询单算子执行器所需的ION内存工作空间的字节大小
83. size_t workspaceSize = HMS_HiAISingleOpExecutor_GetWorkspaceSize(executor);
84. // 若存在多个单算子执行器，各个执行器的工作空间内存可以复用，只需要申请所需的最大工作空间即可
85. HiAI_SingleOpBuffer* workspaceBuffer = HMS_HiAISingleOpBuffer_Create(workspaceSize);
86. void* workspace = HMS_HiAISingleOpBuffer_GetData(workspaceBuffer);
87. ret = HMS_HiAISingleOpExecutor_Init(executor, workspace, workspaceSize);
88. if (ret != OH_NN_SUCCESS) {
89. printf("HMS_HiAISingleOp executor init failed.\n");
90. }

92. // 执行推理运算
93. HiAI_SingleOpTensor* inputs[] = {input};
94. HiAI_SingleOpTensor* outputs[] = {output};
95. ret = HMS_HiAISingleOpExecutor_Execute(executor, inputs, 1, outputs, 1);
96. if (ret != OH_NN_SUCCESS) {
97. printf("HMS_HiAISingleOp executor execute failed.\n");
98. }

100. // 卸载单算子执行器，释放资源
101. ret = HMS_HiAISingleOpTensor_Destroy(&input);
102. if (ret != OH_NN_SUCCESS) {
103. printf("HMS_HiAISingleOp input destroy failed.\n");
104. }
105. ret = HMS_HiAISingleOpTensor_Destroy(&output);
106. if (ret != OH_NN_SUCCESS) {
107. printf("HMS_HiAISingleOp output destroy failed.\n");
108. }
109. ret = HMS_HiAISingleOpBuffer_Destroy(&workspaceBuffer);
110. if (ret != OH_NN_SUCCESS) {
111. printf("HMS_HiAISingleOp workspaceBuffer destroy failed.\n");
112. }
113. ret = HMS_HiAISingleOpExecutor_Destroy(&executor);
114. if (ret != OH_NN_SUCCESS) {
115. printf("HMS_HiAISingleOp executor destroy failed.\n");
116. }
117. free(filterData);
118. free(biasData);
```
