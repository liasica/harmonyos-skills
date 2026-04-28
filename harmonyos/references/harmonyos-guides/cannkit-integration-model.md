---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-integration-model
title: 集成模型
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > App集成 > 集成模型
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:23+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa1069be362dc9f1b023c34d1a292bf7ae5b332a474ceedd107581d9454ffa20
---

模型的加载、编译和推理主要是在native层实现，应用层主要作为数据传递和展示作用。

模型推理之前需要对输入数据进行预处理以匹配模型的输入，同样对于模型的输出也需要做处理获取自己期望的结果。另外SDK中提供了设置模型编译和运行时的配置接口，开发者可根据实际需求选择使用接口。

本节阐述同步模式下单模型的使用，从流程上分别阐述每个步骤在应用层和native层的实现和调用。接口请参见[API参考](../harmonyos-references/cannkit.md)，示例请参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)，本示例支持加载离线模型对图片中的物体进行分类，App运行效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/n4dd9_zqQC2e-ogqxPasrA/zh-cn_image_0000002583479223.png?HW-CC-KV=V1&HW-CC-Date=20260427T235122Z&HW-CC-Expire=86400&HW-CC-Sign=9860C415C38302A49CF322297C5C6E38A6C229670E0AFC8D51D926678CBFE2E5)

## 预置模型

为了让App运行时能够读取到模型文件和处理推理结果，需要先把离线模型和模型对应的结果标签文件预置到工程的“entry/src/main/resources/rawfile”目录中。

本示例所使用的离线模型的转换和生成请参考[Caffe模型转换](cannkit-model-conversion-example.md#caffe模型转换)。

## 加载离线模型

在App应用创建时加载模型和读取结果标签文件。

1. 调用NAPI层的LoadModel函数，读取模型的buffer。
2. （可选）根据需要调用[HMS\_HiAIOptions\_SetOmOptions](../harmonyos-references/cannkit.md#hms_hiaioptions_setomoptions)接口，打开维测功能（如Profiling）。
3. 把模型buffer传递给HIAIModelManager类的HIAIModelManager::LoadModelFromBuffer接口，该接口调用[OH\_NNCompilation\_ConstructWithOfflineModelBuffer](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_constructwithofflinemodelbuffer)创建模型的编译实例。
4. 设置模型的deviceID。

   ```
   1. size_t deviceID = 0;
   2. const size_t *allDevicesID = nullptr;
   3. uint32_t deviceCount = 0;
   4. // 获取所有已连接设备的ID
   5. OH_NN_ReturnCode ret = OH_NNDevice_GetAllDevicesID(&allDevicesID, &deviceCount);
   6. if (ret != OH_NN_SUCCESS || allDevicesID == nullptr) {
   7. OH_LOG_ERROR(LOG_APP, "OH_NNDevice_GetAllDevicesID failed");
   8. return OH_NN_FAILED;
   9. }
   10. // 获取设备名为HIAI_F的设备ID
   11. for (uint32_t i = 0; i < deviceCount; i++) {
   12. const char *name = nullptr;
   13. // 获取指定设备的名称
   14. ret = OH_NNDevice_GetName(allDevicesID[i], &name);
   15. if (ret != OH_NN_SUCCESS || name == nullptr) {
   16. OH_LOG_ERROR(LOG_APP, "OH_NNDevice_GetName failed");
   17. return OH_NN_FAILED;
   18. }
   19. if (std::string(name) == "HIAI_F") {
   20. deviceID = allDevicesID[i];
   21. break;
   22. }
   23. }

   25. // modelData和modelSize为模型的内存地址和大小， compilation的创建可参考CANN Kit Codelab
   26. OH_NNCompilation *compilation = OH_NNCompilation_ConstructWithOfflineModelBuffer(modelData, modelSize);
   27. // 设置编译器的设备id为HIAI_F
   28. ret = OH_NNCompilation_SetDevice(compilation, deviceID);
   29. if (ret != OH_NN_SUCCESS) {
   30. OH_LOG_ERROR(LOG_APP, "OH_NNCompilation_SetDevice failed");
   31. return OH_NN_FAILED;
   32. }
   ```
5. 调用[OH\_NNCompilation\_Build](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_build)，执行模型编译。
6. 调用[OH\_NNExecutor\_Construct](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_construct)，创建模型执行器。
7. 调用[OH\_NNCompilation\_Destroy](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_destroy)，释放模型编译实例。

上述流程可参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)中entry/src/main/cpp/Classification.cpp文件中的LoadModel函数和entry/src/main/cpp/HIAIModelManager.cpp中的HIAIModelManager::LoadModelFromBuffer函数。

## 输入输出数据准备

1. 处理模型的输入，例如示例中模型的输入为1\*3\*227\*227格式Float类型的数据，需要把输入的图片转成该格式后传递到NAPI层。
2. 创建模型的输入和输出Tensor，并把应用层传递的数据填充到输入的Tensor中。

   ```
   1. // 创建输入数据
   2. size_t inputCount = 0;
   3. std::vector<NN_Tensor*> inputTensors;
   4. OH_NN_ReturnCode ret = OH_NNExecutor_GetInputCount(executor, &inputCount); // 创建executor可参考CANN Kit Codelab
   5. if (ret != OH_NN_SUCCESS || inputCount != inputData.size()) { // inputData为开发者构造的输入数据
   6. OH_LOG_ERROR(LOG_APP, "OH_NNExecutor_GetInputCount failed, size mismatch");
   7. return OH_NN_FAILED;
   8. }
   9. for (size_t i = 0; i < inputCount; ++i) {
   10. NN_TensorDesc *tensorDesc = OH_NNExecutor_CreateInputTensorDesc(executor, i); // 创建executor可参考CANN Kit Codelab
   11. NN_Tensor *tensor = OH_NNTensor_Create(deviceID, tensorDesc); // deviceID的获取方式可参考加载离线模型的步骤3或者CANN Kit Codelab
   12. if (tensor != nullptr) {
   13. inputTensors.push_back(tensor);
   14. }
   15. OH_NNTensorDesc_Destroy(&tensorDesc);
   16. }
   17. if (inputTensors.size() != inputCount) {
   18. OH_LOG_ERROR(LOG_APP, "input size mismatch");
   19. DestroyTensors(inputTensors); // DestroyTensors为释放tensor内存操作函数，具体实现可参考CANN Kit Codelab
   20. return OH_NN_FAILED;
   21. }

   23. // 初始化输入数据
   24. for (size_t i = 0; i < inputTensors.size(); ++i) {
   25. void *data = OH_NNTensor_GetDataBuffer(inputTensors[i]);
   26. size_t dataSize = 0;
   27. OH_NNTensor_GetSize(inputTensors[i], &dataSize);
   28. if (data == nullptr || dataSize != inputData[i].size()) { // inputData为模型的输入数据，使用方式可参考CANN Kit Codelab
   29. OH_LOG_ERROR(LOG_APP, "invalid data or dataSize");
   30. return OH_NN_FAILED;
   31. }
   32. memcpy(data, inputData[i].data(), inputData[i].size()); // inputData为模型的输入数据，使用方式可参考CANN Kit Codelab
   33. }

   35. // 创建输出数据，与输入数据的创建方式类似
   36. size_t outputCount = 0;
   37. std::vector<NN_Tensor*> outputTensors;
   38. ret = OH_NNExecutor_GetOutputCount(executor, &outputCount); // 创建executor可参考CANN Kit Codelab
   39. if (ret != OH_NN_SUCCESS) {
   40. OH_LOG_ERROR(LOG_APP, "OH_NNExecutor_GetOutputCount failed");
   41. DestroyTensors(inputTensors); // DestroyTensors为释放tensor内存操作函数，具体实现可参考CANN Kit Codelab
   42. return OH_NN_FAILED;
   43. }
   44. for (size_t i = 0; i < outputCount; i++) {
   45. NN_TensorDesc *tensorDesc = OH_NNExecutor_CreateOutputTensorDesc(executor, i); // 创建executor可参考CANN Kit Codelab
   46. NN_Tensor *tensor = OH_NNTensor_Create(deviceID, tensorDesc); // deviceID的获取方式可参考加载离线模型的步骤3或者CANN Kit Codelab
   47. if (tensor != nullptr) {
   48. outputTensors.push_back(tensor);
   49. }
   50. OH_NNTensorDesc_Destroy(&tensorDesc);
   51. }
   52. if (outputTensors.size() != outputCount) {
   53. DestroyTensors(inputTensors); // DestroyTensors为释放tensor内存操作函数，具体实现可参考CANN Kit Codelab
   54. DestroyTensors(outputTensors); // DestroyTensors为释放tensor内存操作函数，具体实现可参考CANN Kit Codelab
   55. OH_LOG_ERROR(LOG_APP, "output size mismatch");
   56. return OH_NN_FAILED;
   57. }
   ```

上述流程可参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)中"entry/src/main/cpp/Classification.cpp"文件中的InitIOTensors函数和"entry/src/main/cpp/HIAIModelManager.cpp"中的HIAIModelManager::InitIOTensors函数。

## 同步推理离线模型

说明

如果不更换模型，则首次编译加载完成后可多次推理，即一次编译加载，多次推理。

调用[OH\_NNExecutor\_RunSync](../harmonyos-references/capi-neural-network-core-h.md#oh_nnexecutor_runsync)，完成模型的同步推理。

可参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)中"entry/src/main/cpp/Classification.cpp"文件中的RunModel函数和"entry/src/main/cpp/HIAIModelManager.cpp"中的HIAIModelManager::RunModel函数。

## 模型输出后处理

1. 调用[OH\_NNTensor\_GetDataBuffer](../harmonyos-references/capi-neural-network-core-h.md#oh_nntensor_getdatabuffer)，获取输出的Tensor，在输出Tensor中会得到模型的输出数据。
2. 对输出数据进行相应的处理可得到期望的结果。

   例如本示例demo中模型的输出是1000个label的概率，期望得到这1000个结果中概率最大的三个标签。
3. 销毁申请的Tensor资源和执行器实例。

上述流程可参见[SampleCode](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp)中"entry/src/main/cpp/Classification.cpp"文件中的GetResult、UnloadModel函数和"entry/src/main/cpp/HIAIModelManager.cpp"中的HIAIModelManager::GetResult、HIAIModelManager::UnloadModel函数。

说明

开发者可根据需要自行设置模型推理优先级。使用[OH\_NNCompilation\_SetPriority](../harmonyos-references/capi-neural-network-core-h.md#oh_nncompilation_setpriority)接口，默认值为OH\_NN\_PRIORITY\_NONE，本接口应在模型推理前调用。
