---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-aipp-deployment
title: AIPP部署
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > AIPP部署
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a524e9f3ce0fe63e73b8230ca35922cc78bf0b423e3dc997db651a5950bb4f63
---

## 基本概念

AIPP部署是指动态AIPP推理时开发者按需配置动态AIPP参数，从而达到使能AIPP功能。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Mi0rwCa5SgKbvJbLaIH_uA/zh-cn_image_0000002589245529.png?HW-CC-KV=V1&HW-CC-Date=20260429T054058Z&HW-CC-Expire=86400&HW-CC-Sign=A92A116C025EBFA4A3F56826D169A156FA3C3FE38CC75B6F512902AFAC6E6B01)

## 接口说明

以下接口为AIPP参数设置接口，如要使用更丰富的设置和查询接口，请参见[API参考](../harmonyos-references/cannkit.md)。

**表1** CANN Kit模型推理AIPP设置相关接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| HiAI\_AippParam\* HMS\_HiAIAippParam\_Create(uint32\_t batchNum); | 动态AIPP配置实例创建。 |
| void HMS\_HiAIAippParam\_Destroy(HiAI\_AippParam\*\* aippParam); | 动态AIPP配置实例销毁。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputIndex(HiAI\_AippParam\* aippParam, uint32\_t inputIndex); | 设置动态AIPP配置作用于输入上的索引。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputAippIndex(HiAI\_AippParam\* aippParam, uint32\_t inputAippIndex); | 设置动态AIPP配置作用于该输入的多个输出分支上的索引。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputFormat(HiAI\_AippParam\* aippParam, HiAI\_ImageFormat inputFormat); | 设置输入图片的格式。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputShape(HiAI\_AippParam\* aippParam, uint32\_t srcImageW, uint32\_t srcImageH); | 设置输入图片的原始宽高。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCscConfig(HiAI\_AippParam\* aippParam, HiAI\_ImageFormat inputFormat, HiAI\_ImageFormat outputFormat, HiAI\_ImageColorSpace space); | 设置图片色域转换参数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelSwapConfig(HiAI\_AippParam\* aippParam, bool rbuvSwapSwitch, bool axSwapSwitch); | 设置图片通道交换参数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCropConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH); | 设置图片裁剪参数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetResizeConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH); | 设置图片缩放大小参数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetPadConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize); | 设置图片左右上下填充的像素数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelPadding(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t paddingValues[], uint32\_t channelCount); | 设置通道填充值。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetRotationAngle(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float rotationAngle); | 设置图片旋转参数。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMeanPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t meanPixel[], uint32\_t channelCount); | 设置图片数据类型转换的通道像素平均值。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMinPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float minPixel[], uint32\_t channelCount); | 设置图片数据类型转换的通道像素最小值。 |
| OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcVarReciPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float varReciPixel[], uint32\_t channelCount); | 设置图片数据类型转换的通道像素方差。 |
| OH\_NN\_ReturnCode HMS\_HiAITensor\_SetAippParams(NN\_Tensor\* tensor, HiAI\_AippParam\* aippParams[], size\_t aippNum); | 给输入Tensor设置AIPP参数。 |

## 开发步骤

1. 调用[HMS\_HiAIAippParam\_Create](../harmonyos-references/cannkit.md#hms_hiaiaippparam_create)创建动态AIPP配置实例。
2. 设置与计算图关联的配置。

   * 调用[HMS\_HiAIAippParam\_SetInputIndex](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setinputindex)设置此动态AIPP配置所在输入的索引。
   * 调用[HMS\_HiAIAippParam\_SetInputAippIndex](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setinputaippindex)设置此动态AIPP配置所在某个输入的输出分支索引。
3. 设置动态AIPP输入图片相关配置。

   * 调用[HMS\_HiAIAippParam\_SetInputFormat](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setinputformat)设置输入图片的格式。
   * 调用[HMS\_HiAIAippParam\_SetInputShape](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setinputshape)设置输入图片原始宽高。
4. 开发者按需设置以下动态AIPP功能参数。

   * 调用[HMS\_HiAIAippParam\_SetChannelSwapConfig](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setchannelswapconfig)设置通道交换参数。
   * 调用[HMS\_HiAIAippParam\_SetCscConfig](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setcscconfig)设置图片色域转换参数。
   * 调用[HMS\_HiAIAippParam\_SetCropConfig](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setcropconfig)设置图片裁剪参数。
   * 调用[HMS\_HiAIAippParam\_SetResizeConfig](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setresizeconfig)设置图片缩放大小参数。
   * 调用[HMS\_HiAIAippParam\_SetPadConfig](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setpadconfig)设置图片填充大小参数。
   * 调用[HMS\_HiAIAippParam\_SetChannelPadding](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setchannelpadding)设置各通道上的填充值参数。
   * 调用[HMS\_HiAIAippParam\_SetRotationAngle](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setrotationangle)设置旋转角度。
   * 调用[HMS\_HiAIAippParam\_SetDtcMeanPixel](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setdtcmeanpixel)设置数据类型转换通道像素平均值。
   * 调用[HMS\_HiAIAippParam\_SetDtcMinPixel](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setdtcminpixel)设置数据类型转换通道像素最小值。
   * 调用[HMS\_HiAIAippParam\_SetDtcVarReciPixel](../harmonyos-references/cannkit.md#hms_hiaiaippparam_setdtcvarrecipixel)设置数据类型转换通道像素方差。
5. 将AIPP配置设置到[NN\_Tensor](../harmonyos-references/capi-neuralnetworkruntime-nn-tensor.md)。

   通过构造输入输出Tensor后，调用[HMS\_HiAITensor\_SetAippParams](../harmonyos-references/cannkit.md#hms_hiaitensor_setaippparams)给输入Tensor设置AIPP参数。
6. 执行模型推理。
7. 调用[HMS\_HiAIAippParam\_Destroy](../harmonyos-references/cannkit.md#hms_hiaiaippparam_destroy)销毁动态AIPP配置实例。

## 示例说明

假定当前有一个模型，训练时采用的训练集为RGB888的图片，使能了动态AIPP之后，可以接收YUYV类型的图片作为模型推理的输入。当用于模型推理的图片尺寸与训练集不一致时，还可以使用AIPP的裁剪、缩放和填充功能，改变输入图片尺寸。以下示例代码基于NDK接口，实现AIPP的裁剪、缩放和填充等功能，将一张YUYV尺寸为480x480的图片预处理为224x224的输入。

```
1. #include "neural_network_runtime/neural_network_core.h"
2. #include "CANNKit/hiai_aipp_param.h"
3. #include "CANNKit/hiai_tensor.h"
4. #include <vector>

6. constexpr uint32_t BATCH_NUM = 1;
7. // 创建一个batch数为1的动态aipp配置实例
8. HiAI_AippParam* aippPara = HMS_HiAIAippParam_Create(BATCH_NUM);
9. // 在多个输入情况下，设置索引以确定该AippParam对象作用于第几个输入
10. uint32_t inputIndex = 0;
11. OH_NN_ReturnCode ret = HMS_HiAIAippParam_SetInputIndex(aippPara, inputIndex);
12. // 在data有多个输出分支时，设置AippParam对象作用域该输入的第几个输出分支
13. uint32_t validInputAippIndex = 0;
14. HMS_HiAIAippParam_SetInputAippIndex(aippPara, validInputAippIndex);
15. // 设置AippParam对象的输入图像格式
16. HMS_HiAIAippParam_SetInputFormat(aippPara, HIAI_YUV420SP_U8);
17. // 设置AippParam对象的输入图像宽高
18. HMS_HiAIAippParam_SetInputShape(aippPara, 224, 224);
19. // 设置AippParam对象的CSC色域转换参数
20. HMS_HiAIAippParam_SetCscConfig(aippPara, HIAI_YUV420SP_U8, HIAI_RGB888_U8, HIAI_JPEG);
21. // 设置AippParam对象RB/UV通道交换
22. HMS_HiAIAippParam_SetChannelSwapConfig(aippPara, true, false);
23. // 设置AippParam对象第0个索引batch的crop参数
24. HMS_HiAIAippParam_SetCropConfig(aippPara, 0, 0, 0, 100, 100);
25. // 设置AippParam对象第0个索引batch的resize参数
26. HMS_HiAIAippParam_SetResizeConfig(aippPara, 0, 110, 110);
27. // 设置AippParam对象第0个索引batch的通道padding填充值
28. HMS_HiAIAippParam_SetPadConfig(aippPara, 0, 1, 1, 1, 1);
29. // 设置AippParam对象第0个索引batch的旋转角度
30. HMS_HiAIAippParam_SetRotationAngle(aippPara, 0, 90.0);
31. // 设置AippParam对象第0个batch的数据类型转换通道像素平均值
32. constexpr unsigned int chnNum = 4;
33. unsigned int pixelMeanPara[chnNum] = {1, 2, 3, 4};
34. HMS_HiAIAippParam_SetDtcMeanPixel(aippPara, 0, pixelMeanPara, chnNum);

36. // 准备输入Tensor
37. size_t inputCount = 0;
38. ret = OH_NNExecutor_GetInputCount(executor, &inputCount); // 创建executor可参考CANN Kit Codelab
39. std::vector<NN_Tensor *> inputTensors;
40. for (size_t i = 0; i < inputCount; ++i) {
41. // 创建executor可参考CANN Kit Codelab
42. NN_TensorDesc* desc = OH_NNExecutor_CreateInputTensorDesc(executor, i);
43. NN_Tensor* tensor = OH_NNTensor_Create(deviceID, desc); // 获取deviceID可参考CANN Kit Codelab
44. inputTensors.push_back(tensor);
45. }
46. // 准备aipp输入Tensor
47. HiAI_AippParam* aippParas[1] = {aippPara};
48. NN_Tensor* tensor = nullptr;
49. ret = HMS_HiAITensor_SetAippParams(tensor, aippParas, 1);
50. if (ret != OH_NN_SUCCESS ) {
51. return;
52. }
53. inputTensors.push_back(tensor);

55. // 准备输出Tensor
56. size_t outputCount = 0;
57. ret = OH_NNExecutor_GetOutputCount(executor, &outputCount); // 创建executor可参考CANN Kit Codelab
58. std::vector<NN_Tensor *> outputTensors;
59. for (size_t i = 0; i < outputCount; i++) {
60. NN_TensorDesc* desc = OH_NNExecutor_CreateOutputTensorDesc(executor, i); // 创建executor可参考CANN Kit Codelab
61. NN_Tensor* tensor = OH_NNTensor_Create(deviceID, desc); // 获取deviceID可参考CANN Kit Codelab
62. outputTensors.push_back(tensor);
63. }
64. // 执行推理
65. ret = OH_NNExecutor_RunSync(executor_, inputTensors.data(), 1, outputTensors.data(), 1);
66. if (ret != OH_NN_SUCCESS ) {
67. return;
68. }
69. if (aippPara != nullptr) {
70. HMS_HiAIAippParam_Destroy(&aippPara);
71. }
```
