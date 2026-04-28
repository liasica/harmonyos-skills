---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/neural-network-runtime-guidelines
title: Neural Network Runtime对接AI推理框架开发指导
breadcrumb: 指南 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > Neural Network Runtime对接AI推理框架开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:14fe2987458403c809aa79bbc876e2443613aaea2e00298012f4ce4a6979ab11
---

## 场景介绍

Neural Network Runtime作为AI推理引擎和加速芯片的桥梁，为AI推理引擎提供精简的Native接口，满足推理引擎通过加速芯片执行端到端推理的需求。

本文以图1展示的Add单算子模型为例，介绍Neural Network Runtime的开发流程。Add算子包含两个输入、一个参数和一个输出，其中的activation参数用于指定Add算子中激活函数的类型。

**图1** Add单算子网络示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Y4gBevFqQGmqRfsKD2NG7A/zh-cn_image_0000002583479351.png?HW-CC-KV=V1&HW-CC-Date=20260427T235351Z&HW-CC-Expire=86400&HW-CC-Sign=29A82F28D54C8ED18E02118424909B831DA9FDB29FAE78FEB87F401F98A24906)

## 环境准备

### 环境要求

Neural Network Runtime部件的环境要求如下：

* 开发环境：Ubuntu 18.04及以上。
* 接入设备：系统定义的标准设备，系统中内置AI硬件驱动并已接入Neural Network Runtime。

由于Neural Network Runtime通过Native API对外开放，需要下载对应的SDK并通过Native开发套件编译Neural Network Runtime应用。可以使用DevEco Studio来搭建环境和编译代码。

### 环境搭建

1. 使用Ubuntu编译服务器的终端。
2. 指定native工具链路径来编译代码，可以使用DevEco Studio来下载对应的SDK来进行编译。
3. DevEco Studio安装目录下的SDK路径可以在DevEco Studio工程界面，点击File > Settings... > 在settings中搜索SDK，下载对应的SDK即可。

## 接口说明

以下为Neural Network Runtime开发流程中的常用接口，具体可见[NeuralNetworkRuntime](../harmonyos-references/capi-neuralnetworkruntime.md)。

### 结构体

| 结构体名称 | 描述 |
| --- | --- |
| typedef struct OH\_NNModel OH\_NNModel | Neural Network Runtime的模型句柄，用于构造模型。 |
| typedef struct OH\_NNCompilation OH\_NNCompilation | Neural Network Runtime的编译器句柄，用于编译AI模型。 |
| typedef struct OH\_NNExecutor OH\_NNExecutor | Neural Network Runtime的执行器句柄，用于在指定设备上执行推理计算。 |
| typedef struct NN\_QuantParam NN\_QuantParam | Neural Network Runtime的量化参数句柄，用于在构造模型时指定张量的量化参数。 |
| typedef struct NN\_TensorDesc NN\_TensorDesc | Neural Network Runtime的张量描述句柄，用于描述张量的各类属性，例如数据布局、数据类型、形状等。 |
| typedef struct NN\_Tensor NN\_Tensor | Neural Network Runtime的张量句柄，用于设置执行器的推理输入和输出张量。 |

### 模型构造接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_NNModel\_Construct() | 创建OH\_NNModel类型的模型实例。 |
| OH\_NN\_ReturnCode OH\_NNModel\_AddTensorToModel(OH\_NNModel \*model, const NN\_TensorDesc \*tensorDesc) | 向模型实例中添加张量。 |
| OH\_NN\_ReturnCode OH\_NNModel\_SetTensorData(OH\_NNModel \*model, uint32\_t index, const void \*dataBuffer, size\_t length) | 设置张量的数值。 |
| OH\_NN\_ReturnCode OH\_NNModel\_AddOperation(OH\_NNModel \*model, OH\_NN\_OperationType op, const OH\_NN\_UInt32Array \*paramIndices, const OH\_NN\_UInt32Array \*inputIndices, const OH\_NN\_UInt32Array \*outputIndices) | 向模型实例中添加算子。 |
| OH\_NN\_ReturnCode OH\_NNModel\_SpecifyInputsAndOutputs(OH\_NNModel \*model, const OH\_NN\_UInt32Array \*inputIndices, const OH\_NN\_UInt32Array \*outputIndices) | 指定模型的输入和输出张量的索引值。 |
| OH\_NN\_ReturnCode OH\_NNModel\_Finish(OH\_NNModel \*model) | 完成模型构图。 |
| void OH\_NNModel\_Destroy(OH\_NNModel \*\*model) | 销毁模型实例。 |

### 模型编译接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_NNCompilation \*OH\_NNCompilation\_Construct(const OH\_NNModel \*model) | 基于模型实例创建OH\_NNCompilation类型的编译实例。 |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelFile(const char \*modelPath) | 基于离线模型文件路径创建OH\_NNCompilation类型的编译实例。 |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize) | 基于离线模型文件内存创建OH\_NNCompilation类型的编译实例。 |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructForCache() | 创建一个空的编译实例，以便稍后从模型缓存中恢复。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_ExportCacheToBuffer(OH\_NNCompilation \*compilation, const void \*buffer, size\_t length, size\_t \*modelSize) | 将模型缓存写入到指定内存区域。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_ImportCacheFromBuffer(OH\_NNCompilation \*compilation, const void \*buffer, size\_t modelSize) | 从指定内存区域读取模型缓存。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_AddExtensionConfig(OH\_NNCompilation \*compilation, const char \*configName, const void \*configValue, const size\_t configValueSize) | 为自定义硬件属性添加扩展配置，具体硬件的扩展属性名称和属性值需要从硬件厂商的文档中获取。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID) | 指定模型编译和计算的硬件，可通过设备管理接口获取。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetCache(OH\_NNCompilation \*compilation, const char \*cachePath, uint32\_t version) | 设置编译模型的缓存目录和版本。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetPerformanceMode(OH\_NNCompilation \*compilation, OH\_NN\_PerformanceMode performanceMode) | 设置模型计算的性能模式。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetPriority(OH\_NNCompilation \*compilation, OH\_NN\_Priority priority) | 设置模型计算的优先级。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_EnableFloat16(OH\_NNCompilation \*compilation, bool enableFloat16) | 是否以float16的浮点数精度计算。 |
| OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation) | 执行模型编译。 |
| void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation) | 销毁编译实例。 |

### 张量描述接口

| 接口名称 | 描述 |
| --- | --- |
| NN\_TensorDesc \*OH\_NNTensorDesc\_Create() | 创建一个张量描述实例，用于后续创建张量。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetName(NN\_TensorDesc \*tensorDesc, const char \*name) | 设置张量描述的名称。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetName(const NN\_TensorDesc \*tensorDesc, const char \*\*name) | 获取张量描述的名称。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetDataType(NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType dataType) | 设置张量描述的数据类型。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetDataType(const NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType \*dataType) | 获取张量描述的数据类型。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetShape(NN\_TensorDesc \*tensorDesc, const int32\_t \*shape, size\_t shapeLength) | 设置张量描述的形状。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetShape(const NN\_TensorDesc \*tensorDesc, int32\_t \*\*shape, size\_t \*shapeLength) | 获取张量描述的形状。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetFormat(NN\_TensorDesc \*tensorDesc, OH\_NN\_Format format) | 设置张量描述的数据布局。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetFormat(const NN\_TensorDesc \*tensorDesc, OH\_NN\_Format \*format) | 获取张量描述的数据布局。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetElementCount(const NN\_TensorDesc \*tensorDesc, size\_t \*elementCount) | 获取张量描述的元素个数。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetByteSize(const NN\_TensorDesc \*tensorDesc, size\_t \*byteSize) | 获取基于张量描述的形状和数据类型计算的数据占用字节数。 |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_Destroy(NN\_TensorDesc \*\*tensorDesc) | 销毁张量描述实例。 |

### 张量接口

| 接口名称 | 描述 |
| --- | --- |
| NN\_Tensor\* OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc \*tensorDesc) | 从张量描述创建张量实例，会申请设备共享内存。 |
| NN\_Tensor\* OH\_NNTensor\_CreateWithSize(size\_t deviceID, NN\_TensorDesc \*tensorDesc, size\_t size) | 按照指定内存大小和张量描述创建张量实例，会申请设备共享内存。 |
| NN\_Tensor\* OH\_NNTensor\_CreateWithFd(size\_t deviceID, NN\_TensorDesc \*tensorDesc, int fd, size\_t size, size\_t offset) | 按照指定共享内存的文件描述符和张量描述创建张量实例，从而可以复用其他张量的设备共享内存。 |
| NN\_TensorDesc\* OH\_NNTensor\_GetTensorDesc(const NN\_Tensor \*tensor) | 获取张量内部的张量描述实例指针，从而可读取张量的属性，例如数据类型、形状等。 |
| void\* OH\_NNTensor\_GetDataBuffer(const NN\_Tensor \*tensor) | 获取张量数据的内存地址，可以读写张量数据。 |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetFd(const NN\_Tensor \*tensor, int \*fd) | 获取张量数据所在共享内存的文件描述符，文件描述符fd对应了一块设备共享内存。 |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetSize(const NN\_Tensor \*tensor, size\_t \*size) | 获取张量数据所在共享内存的大小。 |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetOffset(const NN\_Tensor \*tensor, size\_t \*offset) | 获取张量数据所在共享内存上的偏移量，张量数据可使用的大小为所在共享内存的大小减去偏移量。 |
| OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor \*\*tensor) | 销毁张量实例。 |

### 执行推理接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_NNExecutor \*OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation) | 创建OH\_NNExecutor类型的执行器实例。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputShape(OH\_NNExecutor \*executor, uint32\_t outputIndex, int32\_t \*\*shape, uint32\_t \*shapeLength) | 获取输出张量的维度信息，用于输出张量具有动态形状的情况。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputCount(const OH\_NNExecutor \*executor, size\_t \*inputCount) | 获取输入张量的数量。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputCount(const OH\_NNExecutor \*executor, size\_t \*outputCount) | 获取输出张量的数量。 |
| NN\_TensorDesc\* OH\_NNExecutor\_CreateInputTensorDesc(const OH\_NNExecutor \*executor, size\_t index) | 由指定索引值创建一个输入张量的描述，用于读取张量的属性或创建张量实例。 |
| NN\_TensorDesc\* OH\_NNExecutor\_CreateOutputTensorDesc(const OH\_NNExecutor \*executor, size\_t index) | 由指定索引值创建一个输出张量的描述，用于读取张量的属性或创建张量实例。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputDimRange(const OH\_NNExecutor \*executor, size\_t index, size\_t \*\*minInputDims, size\_t \*\*maxInputDims, size\_t \*shapeLength) | 获取所有输入张量的维度范围。当输入张量具有动态形状时，不同设备可能支持不同的维度范围。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnRunDone(OH\_NNExecutor \*executor, NN\_OnRunDone onRunDone) | 设置异步推理结束后的回调处理函数，回调函数定义详见接口文档。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnServiceDied(OH\_NNExecutor \*executor, NN\_OnServiceDied onServiceDied) | 设置异步推理执行期间设备驱动服务突然死亡时的回调处理函数，回调函数定义详见接口文档。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor[], size\_t inputCount, NN\_Tensor \*outputTensor[], size\_t outputCount) | 执行同步推理。 |
| OH\_NN\_ReturnCode OH\_NNExecutor\_RunAsync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor[], size\_t inputCount, NN\_Tensor \*outputTensor[], size\_t outputCount, int32\_t timeout, void \*userData) | 执行异步推理。 |
| void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor) | 销毁执行器实例。 |

### 设备管理接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetAllDevicesID(const size\_t \*\*allDevicesID, uint32\_t \*deviceCount) | 获取对接到Neural Network Runtime的所有硬件ID。 |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetName(size\_t deviceID, const char \*\*name) | 获取指定硬件的名称。 |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetType(size\_t deviceID, OH\_NN\_DeviceType \*deviceType) | 获取指定硬件的类别信息。 |

## 开发步骤

Neural Network Runtime的开发流程主要包含**模型构造**、**模型编译**和**推理执行**三个阶段。以下开发步骤以Add单算子模型为例，介绍调用Neural Network Runtime接口，开发应用的过程。

1. 创建应用样例文件。

   首先，创建Neural Network Runtime应用样例的源文件。在项目目录下执行以下命令，创建nnrt\_example/目录，并在目录下创建 nnrt\_example.cpp 源文件。

   ```
   1. mkdir ~/nnrt_example && cd ~/nnrt_example
   2. touch nnrt_example.cpp
   ```
2. 导入Neural Network Runtime。

   在 nnrt\_example.cpp 文件的开头添加以下代码，引入Neural Network Runtime。

   ```
   1. #include <iostream>
   2. #include <cstdarg>
   3. #include "neural_network_runtime/neural_network_runtime.h"
   ```
3. 定义日志打印、设置输入数据、数据打印等辅助函数。

   ```
   1. // 返回值检查宏
   2. #define CHECKNEQ(realRet, expectRet, retValue, ...) \
   3. do { \
   4. if ((realRet) != (expectRet)) { \
   5. printf(__VA_ARGS__); \
   6. return (retValue); \
   7. } \
   8. } while (0)

   10. #define CHECKEQ(realRet, expectRet, retValue, ...) \
   11. do { \
   12. if ((realRet) == (expectRet)) { \
   13. printf(__VA_ARGS__); \
   14. return (retValue); \
   15. } \
   16. } while (0)

   18. // 设置输入数据用于推理
   19. OH_NN_ReturnCode SetInputData(NN_Tensor* inputTensor[], size_t inputSize)
   20. {
   21. OH_NN_DataType dataType(OH_NN_FLOAT32);
   22. OH_NN_ReturnCode ret{OH_NN_FAILED};
   23. size_t elementCount = 0;
   24. for (size_t i = 0; i < inputSize; ++i) {
   25. // 获取张量的数据内存
   26. auto data = OH_NNTensor_GetDataBuffer(inputTensor[i]);
   27. CHECKEQ(data, nullptr, OH_NN_FAILED, "Failed to get data buffer.");
   28. // 获取张量的描述
   29. auto desc = OH_NNTensor_GetTensorDesc(inputTensor[i]);
   30. CHECKEQ(desc, nullptr, OH_NN_FAILED, "Failed to get desc.");
   31. // 获取张量的数据类型
   32. ret = OH_NNTensorDesc_GetDataType(desc, &dataType);
   33. CHECKNEQ(ret, OH_NN_SUCCESS, OH_NN_FAILED, "Failed to get data type.");
   34. // 获取张量的元素个数
   35. ret = OH_NNTensorDesc_GetElementCount(desc, &elementCount);
   36. CHECKNEQ(ret, OH_NN_SUCCESS, OH_NN_FAILED, "Failed to get element count.");
   37. switch(dataType) {
   38. case OH_NN_FLOAT32: {
   39. float* floatValue = reinterpret_cast<float*>(data);
   40. for (size_t j = 0; j < elementCount; ++j) {
   41. floatValue[j] = static_cast<float>(j);
   42. }
   43. break;
   44. }
   45. case OH_NN_INT32: {
   46. int* intValue = reinterpret_cast<int*>(data);
   47. for (size_t j = 0; j < elementCount; ++j) {
   48. intValue[j] = static_cast<int>(j);
   49. }
   50. break;
   51. }
   52. default:
   53. return OH_NN_FAILED;
   54. }
   55. }
   56. return OH_NN_SUCCESS;
   57. }

   59. OH_NN_ReturnCode Print(NN_Tensor* outputTensor[], size_t outputSize)
   60. {
   61. OH_NN_DataType dataType(OH_NN_FLOAT32);
   62. OH_NN_ReturnCode ret{OH_NN_FAILED};
   63. size_t elementCount = 0;
   64. for (size_t i = 0; i < outputSize; ++i) {
   65. auto data = OH_NNTensor_GetDataBuffer(outputTensor[i]);
   66. CHECKEQ(data, nullptr, OH_NN_FAILED, "Failed to get data buffer.");
   67. auto desc = OH_NNTensor_GetTensorDesc(outputTensor[i]);
   68. CHECKEQ(desc, nullptr, OH_NN_FAILED, "Failed to get desc.");
   69. ret = OH_NNTensorDesc_GetDataType(desc, &dataType);
   70. CHECKNEQ(ret, OH_NN_SUCCESS, OH_NN_FAILED, "Failed to get data type.");
   71. ret = OH_NNTensorDesc_GetElementCount(desc, &elementCount);
   72. CHECKNEQ(ret, OH_NN_SUCCESS, OH_NN_FAILED, "Failed to get element count.");
   73. switch(dataType) {
   74. case OH_NN_FLOAT32: {
   75. float* floatValue = reinterpret_cast<float*>(data);
   76. for (size_t j = 0; j < elementCount; ++j) {
   77. std::cout << "Output index: " << j << ", value is: " << floatValue[j] << "." << std::endl;
   78. }
   79. break;
   80. }
   81. case OH_NN_INT32: {
   82. int* intValue = reinterpret_cast<int*>(data);
   83. for (size_t j = 0; j < elementCount; ++j) {
   84. std::cout << "Output index: " << j << ", value is: " << intValue[j] << "." << std::endl;
   85. }
   86. break;
   87. }
   88. default:
   89. return OH_NN_FAILED;
   90. }
   91. }

   93. return OH_NN_SUCCESS;
   94. }
   ```
4. 构造模型。

   使用Neural Network Runtime的模型构造接口，构造Add单算子样例模型。

   ```
   1. OH_NN_ReturnCode BuildModel(OH_NNModel** pmodel)
   2. {
   3. // 创建模型实例model，进行模型构造
   4. OH_NNModel* model = OH_NNModel_Construct();
   5. CHECKEQ(model, nullptr, OH_NN_FAILED, "Create model failed.");

   7. // 添加Add算子的第一个输入张量，类型为float32，张量形状为[1, 2, 2, 3]
   8. NN_TensorDesc* tensorDesc = OH_NNTensorDesc_Create();
   9. CHECKEQ(tensorDesc, nullptr, OH_NN_FAILED, "Create TensorDesc failed.");

   11. int32_t inputDims[4] = {1, 2, 2, 3};
   12. auto returnCode = OH_NNTensorDesc_SetShape(tensorDesc, inputDims, 4);
   13. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc shape failed.");

   15. returnCode = OH_NNTensorDesc_SetDataType(tensorDesc, OH_NN_FLOAT32);
   16. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc data type failed.");

   18. returnCode = OH_NNTensorDesc_SetFormat(tensorDesc, OH_NN_FORMAT_NONE);
   19. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc format failed.");

   21. returnCode = OH_NNModel_AddTensorToModel(model, tensorDesc);
   22. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Add first TensorDesc to model failed.");

   24. returnCode = OH_NNModel_SetTensorType(model, 0, OH_NN_TENSOR);
   25. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set model tensor type failed.");

   27. // 添加Add算子的第二个输入张量，类型为float32，张量形状为[1, 2, 2, 3]
   28. tensorDesc = OH_NNTensorDesc_Create();
   29. CHECKEQ(tensorDesc, nullptr, OH_NN_FAILED, "Create TensorDesc failed.");

   31. returnCode = OH_NNTensorDesc_SetShape(tensorDesc, inputDims, 4);
   32. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc shape failed.");

   34. returnCode = OH_NNTensorDesc_SetDataType(tensorDesc, OH_NN_FLOAT32);
   35. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc data type failed.");

   37. returnCode = OH_NNTensorDesc_SetFormat(tensorDesc, OH_NN_FORMAT_NONE);
   38. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc format failed.");

   40. returnCode = OH_NNModel_AddTensorToModel(model, tensorDesc);
   41. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Add second TensorDesc to model failed.");

   43. returnCode = OH_NNModel_SetTensorType(model, 1, OH_NN_TENSOR);
   44. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set model tensor type failed.");

   46. // 添加Add算子的参数张量，该参数张量用于指定激活函数的类型，张量的数据类型为int8。
   47. tensorDesc = OH_NNTensorDesc_Create();
   48. CHECKEQ(tensorDesc, nullptr, OH_NN_FAILED, "Create TensorDesc failed.");

   50. int32_t activationDims = 1;
   51. returnCode = OH_NNTensorDesc_SetShape(tensorDesc, &activationDims, 1);
   52. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc shape failed.");

   54. returnCode = OH_NNTensorDesc_SetDataType(tensorDesc, OH_NN_INT8);
   55. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc data type failed.");

   57. returnCode = OH_NNTensorDesc_SetFormat(tensorDesc, OH_NN_FORMAT_NONE);
   58. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc format failed.");

   60. returnCode = OH_NNModel_AddTensorToModel(model, tensorDesc);
   61. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Add second TensorDesc to model failed.");

   63. returnCode = OH_NNModel_SetTensorType(model, 2, OH_NN_ADD_ACTIVATIONTYPE);
   64. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set model tensor type failed.");

   66. // 将激活函数类型设置为OH_NN_FUSED_NONE，表示该算子不添加激活函数。
   67. int8_t activationValue = OH_NN_FUSED_NONE;
   68. returnCode = OH_NNModel_SetTensorData(model, 2, &activationValue, sizeof(int8_t));
   69. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set model tensor data failed.");

   71. // 设置Add算子的输出张量，类型为float32，张量形状为[1, 2, 2, 3]
   72. tensorDesc = OH_NNTensorDesc_Create();
   73. CHECKEQ(tensorDesc, nullptr, OH_NN_FAILED, "Create TensorDesc failed.");

   75. returnCode = OH_NNTensorDesc_SetShape(tensorDesc, inputDims, 4);
   76. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc shape failed.");

   78. returnCode = OH_NNTensorDesc_SetDataType(tensorDesc, OH_NN_FLOAT32);
   79. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc data type failed.");

   81. returnCode = OH_NNTensorDesc_SetFormat(tensorDesc, OH_NN_FORMAT_NONE);
   82. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set TensorDesc format failed.");

   84. returnCode = OH_NNModel_AddTensorToModel(model, tensorDesc);
   85. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Add forth TensorDesc to model failed.");

   87. returnCode = OH_NNModel_SetTensorType(model, 3, OH_NN_TENSOR);
   88. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Set model tensor type failed.");

   90. // 指定Add算子的输入张量、参数张量和输出张量的索引
   91. uint32_t inputIndicesValues[2] = {0, 1};
   92. uint32_t paramIndicesValues = 2;
   93. uint32_t outputIndicesValues = 3;
   94. OH_NN_UInt32Array paramIndices = {&paramIndicesValues, 1};
   95. OH_NN_UInt32Array inputIndices = {inputIndicesValues, 2};
   96. OH_NN_UInt32Array outputIndices = {&outputIndicesValues, 1};

   98. // 向模型实例添加Add算子
   99. returnCode = OH_NNModel_AddOperation(model, OH_NN_OPS_ADD, &paramIndices, &inputIndices, &outputIndices);
   100. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Add operation to model failed.");

   102. // 设置模型实例的输入张量、输出张量的索引
   103. returnCode = OH_NNModel_SpecifyInputsAndOutputs(model, &inputIndices, &outputIndices);
   104. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Specify model inputs and outputs failed.");

   106. // 完成模型实例的构建
   107. returnCode = OH_NNModel_Finish(model);
   108. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "Build model failed.");

   110. // 返回模型实例
   111. *pmodel = model;
   112. return OH_NN_SUCCESS;
   113. }
   ```
5. 查询Neural Network Runtime已经对接的AI加速芯片。

   Neural Network Runtime支持通过HDI接口，对接多种AI加速芯片。在执行模型编译前，需要查询当前设备下，Neural Network Runtime已经对接的AI加速芯片。每个AI加速芯片对应唯一的ID值，在编译阶段需要通过设备ID，指定模型编译的芯片。

   ```
   1. void GetAvailableDevices(std::vector<size_t>& availableDevice)
   2. {
   3. availableDevice.clear();

   5. // 获取可用的硬件ID
   6. const size_t* devices = nullptr;
   7. uint32_t deviceCount = 0;
   8. OH_NN_ReturnCode ret = OH_NNDevice_GetAllDevicesID(&devices, &deviceCount);
   9. if (ret != OH_NN_SUCCESS) {
   10. std::cout << "GetAllDevicesID failed, get no available device." << std::endl;
   11. return;
   12. }

   14. for (uint32_t i = 0; i < deviceCount; i++) {
   15. availableDevice.emplace_back(devices[i]);
   16. }
   17. }
   ```
6. 在指定的设备上编译模型。

   Neural Network Runtime使用抽象的模型表达描述AI模型的拓扑结构。在AI加速芯片上执行前，需要通过Neural Network Runtime提供的编译模块来创建编译实例，并由编译实例将抽象的模型表达下发至芯片驱动层，转换成可以直接推理计算的格式，即模型编译。

   ```
   1. OH_NN_ReturnCode CreateCompilation(OH_NNModel* model, const std::vector<size_t>& availableDevice,
   2. OH_NNCompilation** pCompilation)
   3. {
   4. // 创建编译实例compilation，将构图的模型实例或MSLite传下来的模型实例传入
   5. OH_NNCompilation* compilation = OH_NNCompilation_Construct(model);
   6. CHECKEQ(compilation, nullptr, OH_NN_FAILED, "OH_NNCore_ConstructCompilationWithNNModel failed.");

   8. // 设置编译的硬件、缓存路径、性能模式、计算优先级、是否开启float16低精度计算等选项
   9. // 选择在第一个设备上编译模型
   10. auto returnCode = OH_NNCompilation_SetDevice(compilation, availableDevice[0]);
   11. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_SetDevice failed.");

   13. // 将模型编译结果缓存在/data/local/tmp目录下，版本号指定为1
   14. returnCode = OH_NNCompilation_SetCache(compilation, "/data/local/tmp", 1);
   15. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_SetCache failed.");

   17. // 设置硬件性能模式
   18. returnCode = OH_NNCompilation_SetPerformanceMode(compilation, OH_NN_PERFORMANCE_EXTREME);
   19. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_SetPerformanceMode failed.");

   21. // 设置推理执行优先级
   22. returnCode = OH_NNCompilation_SetPriority(compilation, OH_NN_PRIORITY_HIGH);
   23. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_SetPriority failed.");

   25. // 是否开启FP16计算模式
   26. returnCode = OH_NNCompilation_EnableFloat16(compilation, false);
   27. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_EnableFloat16 failed.");

   29. // 执行模型编译
   30. returnCode = OH_NNCompilation_Build(compilation);
   31. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNCompilation_Build failed.");

   33. *pCompilation = compilation;
   34. return OH_NN_SUCCESS;
   35. }
   ```
7. 创建执行器。

   完成模型编译后，需要调用Neural Network Runtime的执行模块，通过编译实例创建执行器。模型推理阶段中的设置模型输入、触发推理计算以及获取模型输出等操作均需要围绕执行器完成。

   ```
   1. OH_NNExecutor* CreateExecutor(OH_NNCompilation* compilation)
   2. {
   3. // 通过编译实例compilation创建执行器executor
   4. OH_NNExecutor *executor = OH_NNExecutor_Construct(compilation);
   5. CHECKEQ(executor, nullptr, nullptr, "OH_NNExecutor_Construct failed.");
   6. return executor;
   7. }
   ```
8. 执行推理计算，并打印推理结果。

   通过执行模块提供的接口，将推理计算所需要的输入数据传递给执行器，触发执行器完成一次推理计算，获取模型的推理结果并打印。

   ```
   1. OH_NN_ReturnCode Run(OH_NNExecutor* executor, const std::vector<size_t>& availableDevice)
   2. {
   3. // 从executor获取输入输出信息
   4. // 获取输入张量的个数
   5. size_t inputCount = 0;
   6. auto returnCode = OH_NNExecutor_GetInputCount(executor, &inputCount);
   7. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNExecutor_GetInputCount failed.");
   8. std::vector<NN_TensorDesc*> inputTensorDescs;
   9. NN_TensorDesc* tensorDescTmp = nullptr;
   10. for (size_t i = 0; i < inputCount; ++i) {
   11. // 创建输入张量的描述
   12. tensorDescTmp = OH_NNExecutor_CreateInputTensorDesc(executor, i);
   13. CHECKEQ(tensorDescTmp, nullptr, OH_NN_FAILED, "OH_NNExecutor_CreateInputTensorDesc failed.");
   14. inputTensorDescs.emplace_back(tensorDescTmp);
   15. }
   16. // 获取输出张量的个数
   17. size_t outputCount = 0;
   18. returnCode = OH_NNExecutor_GetOutputCount(executor, &outputCount);
   19. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNExecutor_GetOutputCount failed.");
   20. std::vector<NN_TensorDesc*> outputTensorDescs;
   21. for (size_t i = 0; i < outputCount; ++i) {
   22. // 创建输出张量的描述
   23. tensorDescTmp = OH_NNExecutor_CreateOutputTensorDesc(executor, i);
   24. CHECKEQ(tensorDescTmp, nullptr, OH_NN_FAILED, "OH_NNExecutor_CreateOutputTensorDesc failed.");
   25. outputTensorDescs.emplace_back(tensorDescTmp);
   26. }

   28. // 创建输入和输出张量
   29. NN_Tensor* inputTensors[inputCount];
   30. NN_Tensor* tensor = nullptr;
   31. for (size_t i = 0; i < inputCount; ++i) {
   32. tensor = nullptr;
   33. tensor = OH_NNTensor_Create(availableDevice[0], inputTensorDescs[i]);
   34. CHECKEQ(tensor, nullptr, OH_NN_FAILED, "OH_NNTensor_Create failed.");
   35. inputTensors[i] = tensor;
   36. }
   37. NN_Tensor* outputTensors[outputCount];
   38. for (size_t i = 0; i < outputCount; ++i) {
   39. tensor = nullptr;
   40. tensor = OH_NNTensor_Create(availableDevice[0], outputTensorDescs[i]);
   41. CHECKEQ(tensor, nullptr, OH_NN_FAILED, "OH_NNTensor_Create failed.");
   42. outputTensors[i] = tensor;
   43. }

   45. // 设置输入张量的数据
   46. returnCode = SetInputData(inputTensors, inputCount);
   47. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "SetInputData failed.");

   49. // 执行推理
   50. returnCode = OH_NNExecutor_RunSync(executor, inputTensors, inputCount, outputTensors, outputCount);
   51. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNExecutor_RunSync failed.");

   53. // 打印输出张量的数据
   54. Print(outputTensors, outputCount);

   56. // 清理输入和输出张量以及张量描述
   57. for (size_t i = 0; i < inputCount; ++i) {
   58. returnCode = OH_NNTensor_Destroy(&inputTensors[i]);
   59. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNTensor_Destroy failed.");
   60. returnCode = OH_NNTensorDesc_Destroy(&inputTensorDescs[i]);
   61. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNTensorDesc_Destroy failed.");
   62. }
   63. for (size_t i = 0; i < outputCount; ++i) {
   64. returnCode = OH_NNTensor_Destroy(&outputTensors[i]);
   65. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNTensor_Destroy failed.");
   66. returnCode = OH_NNTensorDesc_Destroy(&outputTensorDescs[i]);
   67. CHECKNEQ(returnCode, OH_NN_SUCCESS, OH_NN_FAILED, "OH_NNTensorDesc_Destroy failed.");
   68. }

   70. return OH_NN_SUCCESS;
   71. }
   ```
9. 构建端到端模型构造-编译-执行流程。

   步骤4-步骤8实现了模型的模型构造、编译和执行流程，并封装成多个函数，便于模块化开发。以下示例代码将串联这些函数， 形成一个完整的Neural Network Runtime使用流程。

   ```
   1. int main(int argc, char** argv)
   2. {
   3. OH_NNModel* model = nullptr;
   4. OH_NNCompilation* compilation = nullptr;
   5. OH_NNExecutor* executor = nullptr;
   6. std::vector<size_t> availableDevices;

   8. // 模型构造
   9. OH_NN_ReturnCode ret = BuildModel(&model);
   10. if (ret != OH_NN_SUCCESS) {
   11. std::cout << "BuildModel failed." << std::endl;
   12. OH_NNModel_Destroy(&model);
   13. return -1;
   14. }

   16. // 获取可执行的设备
   17. GetAvailableDevices(availableDevices);
   18. if (availableDevices.empty()) {
   19. std::cout << "No available device." << std::endl;
   20. OH_NNModel_Destroy(&model);
   21. return -1;
   22. }

   24. // 模型编译
   25. ret = CreateCompilation(model, availableDevices, &compilation);
   26. if (ret != OH_NN_SUCCESS) {
   27. std::cout << "CreateCompilation failed." << std::endl;
   28. OH_NNModel_Destroy(&model);
   29. OH_NNCompilation_Destroy(&compilation);
   30. return -1;
   31. }

   33. // 销毁模型实例
   34. OH_NNModel_Destroy(&model);

   36. // 创建模型的推理执行器
   37. executor = CreateExecutor(compilation);
   38. if (executor == nullptr) {
   39. std::cout << "CreateExecutor failed, no executor is created." << std::endl;
   40. OH_NNCompilation_Destroy(&compilation);
   41. return -1;
   42. }

   44. // 销毁编译实例
   45. OH_NNCompilation_Destroy(&compilation);

   47. // 使用上一步创建的执行器，执行推理计算
   48. ret = Run(executor, availableDevices);
   49. if (ret != OH_NN_SUCCESS) {
   50. std::cout << "Run failed." << std::endl;
   51. OH_NNExecutor_Destroy(&executor);
   52. return -1;
   53. }

   55. // 销毁执行器实例
   56. OH_NNExecutor_Destroy(&executor);

   58. return 0;
   59. }
   ```

## 调测验证

1. 准备应用样例的编译配置文件。

   新建一个 CMakeLists.txt 文件，为开发步骤中的应用样例文件 nnrt\_example.cpp 添加编译配置。以下提供简单的 CMakeLists.txt 示例：

   ```
   1. cmake_minimum_required(VERSION 3.16)
   2. project(nnrt_example C CXX)

   4. add_executable(nnrt_example
   5. ./nnrt_example.cpp
   6. )

   8. target_link_libraries(nnrt_example
   9. neural_network_runtime
   10. neural_network_core
   11. )
   ```
2. 编译应用样例。

   执行以下命令，在当前目录下新建build/目录，在build/目录下编译 nnrt\_example.cpp，得到二进制文件 nnrt\_example。

   ```
   1. mkdir build && cd build
   2. cmake -DCMAKE_TOOLCHAIN_FILE={交叉编译工具链的路径}/build/cmake/ohos.toolchain.cmake -DOHOS_ARCH=arm64-v8a -DOHOS_PLATFORM=OHOS -DOHOS_STL=c++_static ..
   3. make
   ```
3. 执行以下代码，将样例推送到设备上执行。

   ```
   1. # 将编译得到的 `nnrt_example` 推送到设备上，执行样例。
   2. hdc_std file send ./nnrt_example /data/local/tmp/.

   4. # 给测试用例可执行文件加上权限。
   5. hdc_std shell "chmod +x /data/local/tmp/nnrt_example"

   7. # 执行测试用例
   8. hdc_std shell "/data/local/tmp/nnrt_example"
   ```

   如果样例执行正常，应该得到以下输出。

   ```
   1. Output index: 0, value is: 0.000000.
   2. Output index: 1, value is: 2.000000.
   3. Output index: 2, value is: 4.000000.
   4. Output index: 3, value is: 6.000000.
   5. Output index: 4, value is: 8.000000.
   6. Output index: 5, value is: 10.000000.
   7. Output index: 6, value is: 12.000000.
   8. Output index: 7, value is: 14.000000.
   9. Output index: 8, value is: 16.000000.
   10. Output index: 9, value is: 18.000000.
   11. Output index: 10, value is: 20.000000.
   12. Output index: 11, value is: 22.000000.
   ```
4. 检查模型缓存（可选）。

   如果在调测环境下，Neural Network Runtime对接的HDI服务支持模型缓存功能，执行完 nnrt\_example, 可以在 /data/local/tmp 目录下找到生成的缓存文件。

   说明

   模型的IR需要传递到硬件驱动层，由HDI服务将统一的IR图，编译成硬件专用的计算图，编译的过程非常耗时。Neural Network Runtime支持计算图缓存的特性，可以将HDI服务编译生成的计算图，缓存到设备存储中。当下一次在同一个加速芯片上编译同一个模型时，通过指定缓存的路径，Neural Network Runtime可以直接加载缓存文件中的计算图，减少编译消耗的时间。

   检查缓存目录下的缓存文件：

   ```
   1. ls /data/local/tmp
   ```

   以下为打印结果：

   ```
   1. # 0.nncache 1.nncache 2.nncache cache_info.nncache
   ```

   如果缓存不再使用，需要手动删除缓存，可以参考以下命令，删除缓存文件。

   ```
   1. rm /data/local/tmp/*nncache
   ```
