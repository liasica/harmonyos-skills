---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-inference
title: 模型推理
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 模型推理
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e15b1f85f16a8bdc213df896b85325a8ceff8d61e3f209ddba82ac08b9319ece
---

## 基本概念

该场景是基本模型的使用场景，主要包含模型的编译和推理，其他场景是基础场景的一个扩展和功能增强。

## 业务流程

模型推理的主要开发流程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/LpT-AtNHSyu0Fqyxgv3mEg/zh-cn_image_0000002583439265.png?HW-CC-KV=V1&HW-CC-Date=20260427T235120Z&HW-CC-Expire=86400&HW-CC-Sign=71D1C1DEEF41E7F5655DDB8F3D75898D57A000E48A90DF2398761E6C6649E66C)

## 接口说明

以下接口为主要流程接口，如要使用更丰富的编译、加载和执行时的配置，请参见[API参考](../harmonyos-references/cannkit.md)。

**表1** CANN Kit模型推理相关接口功能介绍

| 接口名 | 描述 |
| --- | --- |
| OH\_NNCompilation\* OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize); | 根据模型buffer创建模型编译实例。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID); | 设置模型编译和执行的目标设备。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation); | 执行模型编译，生成编译后的模型保存在compilation中。 |
| OH\_NNExecutor\* OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation); | 根据编译后的模型，创建模型推理的执行器。 |
| NN\_Tensor\* OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc\* tensorDesc); | 构造输入输出Tensor。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor[], size\_t inputCount, NN\_Tensor \*outputTensor[], size\_t outputCount); | 执行模型的同步推理。 |
| void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation); | 销毁模型编译实例。 |
| OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor\*\* tensor); | 销毁输入输出Tensor。 |
| void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor); | 销毁模型推理的执行器。 |

## 开发步骤

以下为模型推理的主要开发步骤，具体实现请参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)。

1. 准备模型和开发环境。

   * 准备离线模型(OM模型)，可以通过tools\_omg工具生成或从[Model Zoo](cannkit-model-zoo.md)获取。
   * 下载并配置[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) 环境，确保可以正常开发和调试HarmonyOS应用。
2. [创建DevEco Studio项目](cannkit-creating-a-project.md)。
3. 创建模型编译实例。

   调用[OH\_NNCompilation\_ConstructWithOfflineModelBuffer](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_constructwithofflinemodelbuffer)读取模型buffer，创建模型编译实例。或者通过调用[OH\_NNCompilation\_ConstructWithOfflineModelFile](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_constructwithofflinemodelfile)直接读取模型文件，创建模型编译实例。
4. 选择目标device。

   调用[OH\_NNDevice\_GetAllDevicesID](../harmonyos-references/capi-neural-network-core-h.md#oh_nndevice_getalldevicesid)，获取所有的设备ID，查找name为"HIAI\_F"字段的设备ID，记录并通过[OH\_NNCompilation\_SetDevice](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_setdevice)设置到步骤3创建的编译实例中。
5. 执行模型编译。

   调用[OH\_NNCompilation\_Build](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_build)，传入步骤3创建的模型编译实例，即可执行模型编译，编译后的模型数据仍然保存在模型编译实例中。
6. 创建模型执行器。

   调用[OH\_NNExecutor\_Construct](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_construct)，创建编译后模型对应的执行器实例。执行器创建完成后即可调用[OH\_NNCompilation\_Destroy](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_destroy)销毁模型编译实例。
7. 构造输入输出Tensor。

   调用[OH\_NNExecutor\_GetInputCount](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_getinputcount)，查询输入的个数，通过[OH\_NNExecutor\_CreateInputTensorDesc](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_createinputtensordesc)获取到对应索引的TensorDesc，根据该TensorDesc通过[OH\_NNTensor\_Create](../harmonyos-references/capi-neural-network-core-h.md#oh_nntensor_create)创建Tensor，即可向Tensor中写入实际数据。输出Tensor的构造与输入Tensor的构造过程一致。
8. 执行模型推理。

   调用[OH\_NNExecutor\_RunSync](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_runsync)，执行模型的同步推理功能，模型的输出数据保存在outputTensors中。开发者可根据需要对输出数据做相应的处理以得到期望的内容。
9. 销毁实例。

   * 调用[OH\_NNExecutor\_Destroy](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_destroy)，销毁创建的模型执行器实例。
   * 调用[OH\_NNTensor\_Destroy](../harmonyos-references/capi-neural-network-core-h.md#oh_nntensor_destroy)，销毁创建的输入输出Tensor。
