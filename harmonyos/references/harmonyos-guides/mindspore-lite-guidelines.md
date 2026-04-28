---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-guidelines
title: 使用MindSpore Lite进行模型推理 (C/C++)
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > 模型部署 > 使用MindSpore Lite进行模型推理 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6cfb337efd713c929963b2c55abe51991c5bf6f5c7c74aa8baee77294ff4709b
---

## 场景介绍

MindSpore Lite是一款AI引擎，它提供了面向不同硬件设备AI模型推理的功能，目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用。

本文介绍使用MindSpore Lite推理引擎进行模型推理的通用开发流程。

## 基本概念

在进行开发前，请先了解以下概念。

**张量**：它与数组和矩阵非常相似，是MindSpore Lite网络运算中的基本数据结构。

**Float16推理模式**： Float16又称半精度，它使用16比特表示一个数。Float16推理模式表示推理的时候用半精度进行推理。

## 接口说明

这里给出MindSpore Lite推理的通用开发流程中涉及的一些接口，具体请见下列表格。更多接口及详细内容，请见[MindSpore](../harmonyos-references/capi-mindspore.md)。

### Context 相关接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_AI\_ContextHandle OH\_AI\_ContextCreate() | 创建一个上下文的对象。注意：此接口需跟OH\_AI\_ContextDestroy配套使用。 |
| void OH\_AI\_ContextSetThreadNum(OH\_AI\_ContextHandle context, int32\_t thread\_num) | 设置运行时的线程数量。 |
| void OH\_AI\_ContextSetThreadAffinityMode(OH\_AI\_ContextHandle context, int mode) | 设置运行时线程绑定CPU核心的策略，按照CPU物理核频率分为大、中、小三种类型的核心，并且仅需绑大核或者绑中核，不需要绑小核。 |
| OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type) | 创建一个运行时设备信息对象。 |
| void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context) | 释放上下文对象。 |
| void OH\_AI\_DeviceInfoSetEnableFP16(OH\_AI\_DeviceInfoHandle device\_info, bool is\_fp16) | 设置是否开启Float16推理模式，仅CPU/GPU设备可用。 |
| void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info) | 添加运行时设备信息。 |

### Model 相关接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_AI\_ModelHandle OH\_AI\_ModelCreate() | 创建一个模型对象。 |
| OH\_AI\_Status OH\_AI\_ModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context) | 通过模型文件加载并编译MindSpore Lite模型。 |
| void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model) | 释放一个模型对象。 |

### Tensor 相关接口

| 接口名称 | 描述 |
| --- | --- |
| OH\_AI\_TensorHandleArray OH\_AI\_ModelGetInputs(const OH\_AI\_ModelHandle model) | 获取模型的输入张量数组结构体。 |
| int64\_t OH\_AI\_TensorGetElementNum(const OH\_AI\_TensorHandle tensor) | 获取张量元素数量。 |
| const char \*OH\_AI\_TensorGetName(const OH\_AI\_TensorHandle tensor) | 获取张量的名称。 |
| OH\_AI\_DataType OH\_AI\_TensorGetDataType(const OH\_AI\_TensorHandle tensor) | 获取张量数据类型。 |
| void \*OH\_AI\_TensorGetMutableData(const OH\_AI\_TensorHandle tensor) | 获取可变的张量数据指针。 |

## 开发步骤

使用MindSpore Lite进行模型推理的开发流程如下图所示。

**图 1** 使用MindSpore Lite进行模型推理的开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/c4T5qJalRQSz7SD5lIP8yg/zh-cn_image_0000002552799696.png?HW-CC-KV=V1&HW-CC-Date=20260427T235346Z&HW-CC-Expire=86400&HW-CC-Sign=41B968D14846A8879BE9AF3C732F6DF19104E3EF06957254DF3CA12CF4B0C0AA)

进入主要流程之前需要先引用相关的头文件，并编写函数生成随机的输入，具体如下：

```
1. #include <stdlib.h>
2. #include <stdio.h>
3. #include <unistd.h>
4. #include "mindspore/model.h"

6. //生成随机的输入
7. int GenerateInputDataWithRandom(OH_AI_TensorHandleArray inputs) {
8. for (size_t i = 0; i < inputs.handle_num; ++i) {
9. float *input_data = (float *)OH_AI_TensorGetMutableData(inputs.handle_list[i]);
10. if (input_data == NULL) {
11. printf("MSTensorGetMutableData failed.\n");
12. return OH_AI_STATUS_LITE_ERROR;
13. }
14. int64_t num = OH_AI_TensorGetElementNum(inputs.handle_list[i]);
15. const int divisor = 10;
16. for (size_t j = 0; j < num; j++) {
17. input_data[j] = (float)(rand() % divisor) / divisor;  // 0--0.9f
18. }
19. }
20. return OH_AI_STATUS_SUCCESS;
21. }
```

然后进入主要的开发步骤，具体包括模型的准备、读取、编译、推理和释放，具体开发过程及细节请见下文的开发步骤及示例。

1. 模型准备。

   需要的模型可以直接下载，也可以通过模型转换工具获得。

   * 下载模型的格式若为.ms，则可以直接使用。本文以mobilenetv2.ms为例。
   * 如果是第三方框架的模型，比如 TensorFlow、TensorFlow Lite、Caffe、ONNX等，可以使用[模型转换工具](https://www.mindspore.cn/lite/docs/zh-CN/master/use/downloads.html#2-3-0)转换为.ms格式的模型文件。
2. 创建上下文，设置线程数、设备类型等参数。

   以下介绍两种典型情形。

   情形1：仅创建CPU推理上下文。

   ```
   1. // 创建并配置上下文，设置运行时的线程数量为2，绑核策略为大核优先
   2. OH_AI_ContextHandle context = OH_AI_ContextCreate();
   3. if (context == NULL) {
   4. printf("OH_AI_ContextCreate failed.\n");
   5. return OH_AI_STATUS_LITE_ERROR;
   6. }
   7. const int thread_num = 2;
   8. OH_AI_ContextSetThreadNum(context, thread_num);
   9. OH_AI_ContextSetThreadAffinityMode(context, 1);
   10. //设置运行设备为CPU，不使用Float16推理
   11. OH_AI_DeviceInfoHandle cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
   12. if (cpu_device_info == NULL) {
   13. printf("OH_AI_DeviceInfoCreate failed.\n");
   14. OH_AI_ContextDestroy(&context);
   15. return OH_AI_STATUS_LITE_ERROR;
   16. }
   17. OH_AI_DeviceInfoSetEnableFP16(cpu_device_info, false);
   18. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);
   ```

   情形2：创建NNRT（Neural Network Runtime）和CPU异构推理上下文。

   NNRT是面向AI领域的跨芯片推理计算运行时，一般来说，NNRT对接的加速硬件如NPU，推理能力较强，但支持的算子规格少；而通用CPU推理能力较弱，但支持算子规格更全面。MindSpore Lite支持配置NNRT硬件和CPU异构推理：优先将模型算子调度到NNRT推理，若某些算子NNRT不支持，将其调度到CPU进行推理。通过下面的操作即可配置NNRT/CPU异构推理。

   ```
   1. // 创建并配置上下文，设置运行时的线程数量为2，绑核策略为大核优先
   2. OH_AI_ContextHandle context = OH_AI_ContextCreate();
   3. if (context == NULL) {
   4. printf("OH_AI_ContextCreate failed.\n");
   5. return OH_AI_STATUS_LITE_ERROR;
   6. }
   7. // 优先使用NNRT推理。
   8. // 这里利用查找到的第一个ACCELERATORS类别的NNRT硬件，来创建nnrt设备信息，并设置硬件使用高性能模式推理。还可以通过如：OH_AI_GetAllNNRTDeviceDescs()接口获取当前环境中所有NNRT硬件的描述信息，按设备名、类型等信息查找，找到某一具体设备作为NNRT推理硬件。
   9. OH_AI_DeviceInfoHandle nnrt_device_info = OH_AI_CreateNNRTDeviceInfoByType(OH_AI_NNRTDEVICE_ACCELERATOR);
   10. if (nnrt_device_info == NULL) {
   11. printf("OH_AI_DeviceInfoCreate failed.\n");
   12. OH_AI_ContextDestroy(&context);
   13. return OH_AI_STATUS_LITE_ERROR;
   14. }
   15. OH_AI_DeviceInfoSetPerformanceMode(nnrt_device_info, OH_AI_PERFORMANCE_HIGH);
   16. OH_AI_ContextAddDeviceInfo(context, nnrt_device_info);

   18. // 其次设置CPU推理。
   19. OH_AI_DeviceInfoHandle cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
   20. if (cpu_device_info == NULL) {
   21. printf("OH_AI_DeviceInfoCreate failed.\n");
   22. OH_AI_ContextDestroy(&context);
   23. return OH_AI_STATUS_LITE_ERROR;
   24. }
   25. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);
   ```
3. 创建、加载与编译模型。

   调用OH\_AI\_ModelBuildFromFile加载并编译模型。

   本例中传入OH\_AI\_ModelBuildFromFile的argv[1]参数是从控制台中输入的模型文件路径。

   ```
   1. // 创建模型
   2. OH_AI_ModelHandle model = OH_AI_ModelCreate();
   3. if (model == NULL) {
   4. printf("OH_AI_ModelCreate failed.\n");
   5. OH_AI_ContextDestroy(&context);
   6. return OH_AI_STATUS_LITE_ERROR;
   7. }

   9. // 加载与编译模型，模型的类型为OH_AI_MODELTYPE_MINDIR
   10. if (access(argv[1], F_OK) != 0) {
   11. printf("model file not exists.\n");
   12. OH_AI_ModelDestroy(&model);
   13. OH_AI_ContextDestroy(&context);
   14. return OH_AI_STATUS_LITE_ERROR;
   15. }
   16. int ret = OH_AI_ModelBuildFromFile(model, argv[1], OH_AI_MODELTYPE_MINDIR, context);
   17. if (ret != OH_AI_STATUS_SUCCESS) {
   18. printf("OH_AI_ModelBuildFromFile failed, ret: %d.\n", ret);
   19. OH_AI_ModelDestroy(&model);
   20. OH_AI_ContextDestroy(&context);
   21. return ret;
   22. }
   ```
4. 输入数据。

   模型执行之前需要向输入的张量中填充数据。本例使用随机的数据对模型进行填充。

   ```
   1. // 获得输入张量
   2. OH_AI_TensorHandleArray inputs = OH_AI_ModelGetInputs(model);
   3. if (inputs.handle_list == NULL) {
   4. printf("OH_AI_ModelGetInputs failed, ret: %d.\n", ret);
   5. OH_AI_ModelDestroy(&model);
   6. OH_AI_ContextDestroy(&context);
   7. return ret;
   8. }
   9. // 使用随机数据填充张量
   10. ret = GenerateInputDataWithRandom(inputs);
   11. if (ret != OH_AI_STATUS_SUCCESS) {
   12. printf("GenerateInputDataWithRandom failed, ret: %d.\n", ret);
   13. OH_AI_ModelDestroy(&model);
   14. OH_AI_ContextDestroy(&context);
   15. return ret;
   16. }
   ```
5. 执行推理。

   使用OH\_AI\_ModelPredict接口进行模型推理。

   ```
   1. // 执行模型推理
   2. OH_AI_TensorHandleArray outputs;
   3. ret = OH_AI_ModelPredict(model, inputs, &outputs, NULL, NULL);
   4. if (ret != OH_AI_STATUS_SUCCESS) {
   5. printf("OH_AI_ModelPredict failed, ret: %d.\n", ret);
   6. OH_AI_ModelDestroy(&model);
   7. OH_AI_ContextDestroy(&context);
   8. return ret;
   9. }
   ```
6. 获取输出。

   模型推理结束之后，可以通过输出张量得到推理结果。

   ```
   1. // 获取模型的输出张量，并打印
   2. for (size_t i = 0; i < outputs.handle_num; ++i) {
   3. OH_AI_TensorHandle tensor = outputs.handle_list[i];
   4. long long element_num = OH_AI_TensorGetElementNum(tensor);
   5. printf("Tensor name: %s, tensor size is %zu ,elements num: %lld.\n", OH_AI_TensorGetName(tensor),
   6. OH_AI_TensorGetDataSize(tensor), element_num);
   7. const float *data = (const float *)OH_AI_TensorGetData(tensor);
   8. if (data == NULL) {
   9. printf("OH_AI_TensorGetData failed.\n");
   10. OH_AI_ModelDestroy(&model);
   11. OH_AI_ContextDestroy(&context);
   12. return OH_AI_STATUS_LITE_ERROR;
   13. }
   14. printf("output data is:\n");
   15. const int max_print_num = 50;
   16. for (int j = 0; j < element_num && j <= max_print_num; ++j) {
   17. printf("%f ", data[j]);
   18. }
   19. printf("\n");
   20. }
   ```
7. 释放模型。

   不再使用MindSpore Lite推理框架时，需要释放已经创建的模型。

   ```
   1. // 释放模型和上下文
   2. OH_AI_ModelDestroy(&model);
   3. OH_AI_ContextDestroy(&context);
   ```

## 调测验证

1. 编写CMakeLists.txt。

   ```
   1. cmake_minimum_required(VERSION 3.14)
   2. project(Demo)

   4. add_executable(demo main.c)

   6. target_link_libraries(
   7. demo
   8. mindspore_lite_ndk
   9. pthread
   10. dl
   11. )
   ```

   * 使用ohos-sdk交叉编译，需要指定CMake的工具链路径，即：-DCMAKE\_TOOLCHAIN\_FILE="/{sdkPath}/native/build/cmake/ohos.toolchain.cmake"。

     其中，sdkPath为DevEco Studio安装目录下的SDK路径，可在DevEco Studio工程界面，点击**File** > **Settings...** > **HarmonyOS SDK**，查看**Location**获取。
   * 工具链默认编译64位的程序，如果要编译32位，需要添加：-DOHOS\_ARCH="armeabi-v7a"。
2. 运行。

   * 使用hdc\_std连接设备，并将demo和mobilenetv2.ms推送到设备中的相同目录。
   * 使用hdc\_std shell进入设备，并进入demo所在的目录执行如下命令，即可得到结果。

   ```
   1. ./demo mobilenetv2.ms
   ```

   得到如下输出:

   ```
   1. # ./demo ./mobilenetv2.ms
   2. Tensor name: Softmax-65, tensor size is 4004 ,elements num: 1001.
   3. output data is:
   4. 0.000018 0.000012 0.000026 0.000194 0.000156 0.001501 0.000240 0.000825 0.000016 0.000006 0.000007 0.000004 0.000004 0.000004 0.000015 0.000099 0.000011 0.000013 0.000005 0.000023 0.000004 0.000008 0.000003 0.000003 0.000008 0.000014 0.000012 0.000006 0.000019 0.000006 0.000018 0.000024 0.000010 0.000002 0.000028 0.000372 0.000010 0.000017 0.000008 0.000004 0.000007 0.000010 0.000007 0.000012 0.000005 0.000015 0.000007 0.000040 0.000004 0.000085 0.000023
   ```
