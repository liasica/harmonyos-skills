---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-guidelines-based-native
title: 使用MindSpore Lite实现图像分类（C/C++）
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > 使用MindSpore Lite实现图像分类（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3de2d96f61b8a41f08003a83eb58d149209c911c3d700ee58917b67f317e6906
---

## 场景说明

开发者可以使用[MindSpore](../harmonyos-references/capi-mindspore.md)，在UI代码中直接集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现图像分类的应用。

图像分类可实现对图像中物体的识别，在医学影像分析、自动驾驶、电子商务、人脸识别等领域有广泛的应用。

## 基本概念

* N-API：用于构建ArkTS本地化组件的一套接口。可利用N-API，将C/C++开发的库封装成ArkTS模块。

## 开发流程

1. 选择图像分类模型。
2. 在端侧使用MindSpore Lite推理模型，实现对选择的图片进行分类。

## 开发步骤

本文以对相册的一张图片进行推理为例，提供使用MindSpore Lite实现图像分类的开发指导。

### 选择模型

本示例程序中使用的图像分类模型文件为[mobilenetv2.ms](https://download.mindspore.cn/model_zoo/official/lite/mobilenetv2_openimage_lite/1.5/mobilenetv2.ms)，放置在entry/src/main/resources/rawfile工程目录下。

如果开发者有其他图像分类的预训练模型，请参考[MindSpore Lite 模型转换](mindspore-lite-converter-guidelines.md)介绍，将原始模型转换成.ms格式。

### 编写推理代码

在 entry/src/main/cpp/mslite\_napi.cpp，调用[MindSpore](../harmonyos-references/capi-mindspore.md)实现端侧推理，推理代码流程如下。

1. 引用对应的头文件

   ```
   1. #include <iostream>
   2. #include <sstream>
   3. #include <cstdlib>
   4. #include <hilog/log.h>
   5. #include <rawfile/raw_file_manager.h>
   6. #include <mindspore/types.h>
   7. #include <mindspore/model.h>
   8. #include <mindspore/context.h>
   9. #include <mindspore/status.h>
   10. #include <mindspore/tensor.h>
   11. #include "napi/native_api.h"
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L16-L28)
2. 读取模型文件

   ```
   1. #define LOGI(...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   2. #define LOGD(...) ((void)OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   3. #define LOGW(...) ((void)OH_LOG_Print(LOG_APP, LOG_WARN, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   4. #define LOGE(...) ((void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L30-L35)

   ```
   1. void *ReadModelFile(NativeResourceManager *nativeResourceManager, const std::string &modelName, size_t *modelSize)
   2. {
   3. auto rawFile = OH_ResourceManager_OpenRawFile(nativeResourceManager, modelName.c_str());
   4. if (rawFile == nullptr) {
   5. LOGE("MS_LITE_ERR: Open model file failed");
   6. OH_ResourceManager_CloseRawFile(rawFile);
   7. return nullptr;
   8. }
   9. long fileSize = OH_ResourceManager_GetRawFileSize(rawFile);
   10. if (fileSize <= 0) {
   11. LOGE("MS_LITE_ERR: FileSize not correct");
   12. }
   13. void *modelBuffer = malloc(fileSize);
   14. if (modelBuffer == nullptr) {
   15. LOGE("MS_LITE_ERR: malloc failed");
   16. }
   17. int ret = OH_ResourceManager_ReadRawFile(rawFile, modelBuffer, fileSize);
   18. if (ret == 0) {
   19. LOGE("MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed");
   20. OH_ResourceManager_CloseRawFile(rawFile);
   21. return nullptr;
   22. }
   23. OH_ResourceManager_CloseRawFile(rawFile);
   24. *modelSize = fileSize;
   25. return modelBuffer;
   26. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L57-L84)
3. 创建上下文，设置线程数、设备类型等参数，并加载模型。本样例模型，不支持使用NNRt推理。

   ```
   1. void DestroyModelBuffer(void **buffer)
   2. {
   3. if (buffer == nullptr) {
   4. return;
   5. }
   6. free(*buffer);
   7. *buffer = nullptr;
   8. }

   10. OH_AI_ContextHandle CreateMSLiteContext(void *modelBuffer)
   11. {
   12. // Set executing context for model.
   13. auto context = OH_AI_ContextCreate();
   14. if (context == nullptr) {
   15. DestroyModelBuffer(&modelBuffer);
   16. LOGE("MS_LITE_ERR: Create MSLite context failed.\n");
   17. return nullptr;
   18. }
   19. // 本样例模型，不支持配置OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_NNRT)
   20. auto cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);

   22. OH_AI_DeviceInfoSetEnableFP16(cpu_device_info, true);
   23. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);

   25. LOGI("MS_LITE_LOG: Build MSLite context success.\n");
   26. return context;
   27. }

   29. OH_AI_ModelHandle CreateMSLiteModel(void *modelBuffer, size_t modelSize, OH_AI_ContextHandle context)
   30. {
   31. // Create model
   32. auto model = OH_AI_ModelCreate();
   33. if (model == nullptr) {
   34. DestroyModelBuffer(&modelBuffer);
   35. LOGE("MS_LITE_ERR: Allocate MSLite Model failed.\n");
   36. return nullptr;
   37. }

   39. // Build model object
   40. // `OH_AI_MODELTYPE_MINDIR` 适用于 `.ms` 模型文件格式
   41. auto build_ret = OH_AI_ModelBuild(model, modelBuffer, modelSize, OH_AI_MODELTYPE_MINDIR, context);
   42. DestroyModelBuffer(&modelBuffer);
   43. if (build_ret != OH_AI_STATUS_SUCCESS) {
   44. OH_AI_ModelDestroy(&model);
   45. LOGE("MS_LITE_ERR: Build MSLite model failed.\n");
   46. return nullptr;
   47. }
   48. LOGI("MS_LITE_LOG: Build MSLite model success.\n");
   49. return model;
   50. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L86-L136)
4. 设置模型输入数据，执行模型推理。

   ```
   1. constexpr int K_NUM_PRINT_OF_OUT_DATA = 20;
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L37-L39)

   ```
   1. // 设置模型输入数据
   2. int FillInputTensor(OH_AI_TensorHandle input, std::vector<float> input_data)
   3. {
   4. if (OH_AI_TensorGetDataType(input) == OH_AI_DATATYPE_NUMBERTYPE_FLOAT32) {
   5. float *data = (float *)OH_AI_TensorGetMutableData(input);
   6. for (size_t i = 0; i < OH_AI_TensorGetElementNum(input); i++) {
   7. data[i] = input_data[i];
   8. }
   9. return OH_AI_STATUS_SUCCESS;
   10. } else {
   11. return OH_AI_STATUS_LITE_ERROR;
   12. }
   13. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L41-L55)

   ```
   1. // 执行模型推理
   2. int RunMSLiteModel(OH_AI_ModelHandle model, std::vector<float> input_data)
   3. {
   4. // Set input data for model.
   5. auto inputs = OH_AI_ModelGetInputs(model);
   6. auto ret = FillInputTensor(inputs.handle_list[0], input_data);
   7. if (ret != OH_AI_STATUS_SUCCESS) {
   8. LOGE("MS_LITE_ERR: RunMSLiteModel set input error.\n");
   9. return OH_AI_STATUS_LITE_ERROR;
   10. }

   12. // Get model output.
   13. auto outputs = OH_AI_ModelGetOutputs(model);

   15. // Predict model.
   16. auto predict_ret = OH_AI_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
   17. if (predict_ret != OH_AI_STATUS_SUCCESS) {
   18. LOGE("MS_LITE_ERR: MSLite Predict error.\n");
   19. return OH_AI_STATUS_LITE_ERROR;
   20. }
   21. LOGI("MS_LITE_LOG: Run MSLite model Predict success.\n");

   23. // Print output tensor data.
   24. LOGI("MS_LITE_LOG: Get model outputs:\n");
   25. for (size_t i = 0; i < outputs.handle_num; i++) {
   26. auto tensor = outputs.handle_list[i];
   27. LOGI("MS_LITE_LOG: - Tensor %{public}d name is: %{public}s.\n", static_cast<int>(i),
   28. OH_AI_TensorGetName(tensor));
   29. LOGI("MS_LITE_LOG: - Tensor %{public}d size is: %{public}d.\n", static_cast<int>(i),
   30. (int)OH_AI_TensorGetDataSize(tensor));
   31. LOGI("MS_LITE_LOG: - Tensor data is:\n");
   32. auto out_data = reinterpret_cast<const float *>(OH_AI_TensorGetData(tensor));
   33. std::stringstream outStr;
   34. for (int i = 0; (i < OH_AI_TensorGetElementNum(tensor)) && (i <= K_NUM_PRINT_OF_OUT_DATA); i++) {
   35. outStr << out_data[i] << " ";
   36. }
   37. LOGI("MS_LITE_LOG: %{public}s", outStr.str().c_str());
   38. }
   39. return OH_AI_STATUS_SUCCESS;
   40. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L138-L179)
5. 调用以上方法，实现完整的模型推理流程。

   ```
   1. static napi_value RunDemo(napi_env env, napi_callback_info info)
   2. {
   3. // run demo
   4. napi_value error_ret;
   5. napi_create_int32(env, -1, &error_ret);
   6. // 传入数据处理
   7. size_t argc = 2;
   8. napi_value argv[2] = {nullptr};
   9. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   10. bool isArray = false;
   11. napi_is_array(env, argv[0], &isArray);
   12. uint32_t length = 0;
   13. // 获取数组的长度
   14. napi_get_array_length(env, argv[0], &length);
   15. LOGI("MS_LITE_LOG: argv array length = %{public}d", length);
   16. std::vector<float> input_data;
   17. double param = 0;
   18. for (int i = 0; i < length; i++) {
   19. napi_value value;
   20. napi_get_element(env, argv[0], i, &value);
   21. napi_get_value_double(env, value, &param);
   22. input_data.push_back(static_cast<float>(param));
   23. }
   24. std::stringstream outstr;
   25. for (int i = 0; i < K_NUM_PRINT_OF_OUT_DATA; i++) {
   26. outstr << input_data[i] << " ";
   27. }
   28. LOGI("MS_LITE_LOG: input_data = %{public}s", outstr.str().c_str());
   29. // Read model file
   30. const std::string modelName = "mobilenetv2.ms";
   31. LOGI("MS_LITE_LOG: Run model: %{public}s", modelName.c_str());
   32. size_t modelSize;
   33. auto resourcesManager = OH_ResourceManager_InitNativeResourceManager(env, argv[1]);
   34. auto modelBuffer = ReadModelFile(resourcesManager, modelName, &modelSize);
   35. if (modelBuffer == nullptr) {
   36. LOGE("MS_LITE_ERR: Read model failed");
   37. return error_ret;
   38. }
   39. LOGI("MS_LITE_LOG: Read model file success");

   41. auto context = CreateMSLiteContext(modelBuffer);
   42. if (context == nullptr) {
   43. LOGE("MS_LITE_ERR: MSLiteFwk Build context failed.\n");
   44. return error_ret;
   45. }
   46. auto model = CreateMSLiteModel(modelBuffer, modelSize, context);
   47. if (model == nullptr) {
   48. OH_AI_ContextDestroy(&context);
   49. LOGE("MS_LITE_ERR: MSLiteFwk Build model failed.\n");
   50. return error_ret;
   51. }
   52. int ret = RunMSLiteModel(model, input_data);
   53. if (ret != OH_AI_STATUS_SUCCESS) {
   54. OH_AI_ModelDestroy(&model);
   55. OH_AI_ContextDestroy(&context);
   56. LOGE("MS_LITE_ERR: RunMSLiteModel failed.\n");
   57. return error_ret;
   58. }
   59. napi_value out_data;
   60. napi_create_array(env, &out_data);
   61. auto outputs = OH_AI_ModelGetOutputs(model);
   62. OH_AI_TensorHandle output_0 = outputs.handle_list[0];
   63. float *output0Data = reinterpret_cast<float *>(OH_AI_TensorGetMutableData(output_0));
   64. for (size_t i = 0; i < OH_AI_TensorGetElementNum(output_0); i++) {
   65. napi_value element;
   66. napi_create_double(env, static_cast<double>(output0Data[i]), &element);
   67. napi_set_element(env, out_data, i, element);
   68. }
   69. OH_AI_ModelDestroy(&model);
   70. OH_AI_ContextDestroy(&context);
   71. LOGI("MS_LITE_LOG: Exit runDemo()");
   72. return out_data;
   73. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/cpp/mslite_napi.cpp#L181-L255)
6. 编写CMake脚本，链接MindSpore Lite动态库。

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.4.1)
   3. project(MindSporeLiteCDemo)

   5. set(NATIVERENDER_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   7. if(DEFINED PACKAGE_FIND_FILE)
   8. include(${PACKAGE_FIND_FILE})
   9. endif()

   11. include_directories(${NATIVERENDER_PATH}
   12. ${NATIVERENDER_PATH}/include)

   14. add_library(entry SHARED mslite_napi.cpp)
   15. target_link_libraries(entry PUBLIC mindspore_lite_ndk)
   16. target_link_libraries(entry PUBLIC hilog_ndk.z)
   17. target_link_libraries(entry PUBLIC rawfile.z)
   18. target_link_libraries(entry PUBLIC ace_napi.z)
   ```

### 使用N-API将C++动态库封装成ArkTS模块

1. 在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：

   ```
   1. export const runDemo: (a: number[], b:Object) => Array<number>;
   ```
2. 在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：

   ```
   1. {
   2. "name": "libentry.so",
   3. "types": "./Index.d.ts",
   4. "version": "1.0.0",
   5. "description": "MindSpore Lite inference module"
   6. }
   ```

### 实现图像输入和预处理，并执行推理

1. 此处以获取相册图片为例，调用[@ohos.file.picker](../harmonyos-references/js-apis-file-picker.md) 实现相册图片文件的选择。
2. 根据模型的输入尺寸，调用[@ohos.multimedia.image](../harmonyos-references/arkts-apis-image.md) （实现图片处理）、[@ohos.file.fs](../harmonyos-references/js-apis-file-fs.md) （实现基础文件操作） API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
3. 在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。

```
1. // Index.ets
2. import msliteNapi from 'libentry.so';
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { image } from '@kit.ImageKit';
6. import { fileIo } from '@kit.CoreFileKit';
7. import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
8. import { hilog } from '@kit.PerformanceAnalysisKit';

10. const TAG = 'MindSporeLite';
11. const PERMISSIONS: Permissions[] = ['ohos.permission.READ_IMAGEVIDEO'];

13. @Entry
14. @Component
15. struct Index {
16. @State message: string = 'MindSporeLite C Demo';
17. @State modelName: string = 'mobilenetv2.ms';
18. @State modelInputHeight: number = 224;
19. @State modelInputWidth: number = 224;
20. @State uris: Array<string> = [];
21. @State max: number = 0;
22. @State maxIndex: number = 0;
23. @State maxArray: Array<number> = [];
24. @State maxIndexArray: Array<number> = [];

26. build() {
27. Row() {
28. Column() {
29. Text(this.message)
30. Button() {
31. Text('photo')
32. .fontSize(30)
33. .fontWeight(FontWeight.Bold)
34. }
35. .onClick(() => {
36. let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
37. if (resMgr === null || resMgr === undefined){
38. hilog.error(0xFF00, TAG, '%{public}s', `MS_LITE_ERR: get resMgr failed.`);
39. return
40. }

42. // 获取相册图片
43. // 1.创建图片文件选择实例
44. let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();

46. // 2.设置选择媒体文件类型为IMAGE，设置选择媒体文件的最大数目
47. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
48. photoSelectOptions.maxSelectNumber = 1;

50. // 3.创建图库选择器实例，调用select()接口拉起图库界面进行文件选择。文件选择成功后，返回photoSelectResult结果集。
51. let photoPicker = new photoAccessHelper.PhotoViewPicker();
52. photoPicker.select(photoSelectOptions,
53. async (err: BusinessError, photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
54. if (err) {
55. hilog.error(0xFF00, TAG, '%{public}s',
56. `MS_LITE_ERR: PhotoViewPicker.select failed with err: ${JSON.stringify(err)}`);
57. return;
58. }
59. hilog.info(0xFF00, TAG, '%{public}s',
60. `MS_LITE_LOG: PhotoViewPicker.select successfully, uri: ${JSON.stringify(photoSelectResult)}`);
61. this.uris = photoSelectResult.photoUris;
62. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: uri: ${this.uris}`);

64. // 预处理图片数据
65. try {
66. // 1.使用fileIo.openSync接口，通过uri打开这个文件得到fd
67. let file = fileIo.openSync(this.uris[0], fileIo.OpenMode.READ_ONLY);
68. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: file fd: ${file.fd}`);

70. // 2.通过fd使用fileIo.readSync接口读取这个文件内的数据
71. let inputBuffer = new ArrayBuffer(4096000);
72. let readLen = fileIo.readSync(file.fd, inputBuffer);
73. hilog.info(0xFF00, TAG, '%{public}s',
74. `MS_LITE_LOG: readSync data to file succeed and inputBuffer size is: ${readLen}`);

76. // 3.通过PixelMap预处理
77. let imageSource = image.createImageSource(file.fd);
78. if (imageSource === undefined) {
79. hilog.error(0xFF00, TAG, '%{public}s', `MS_LITE_ERR: createImageSource failed.`);
80. return
81. }
82. imageSource.createPixelMap({ editable: true }).then((pixelMap) => {
83. pixelMap.getImageInfo().then((info) => {
84. hilog.info(0xFF00, TAG, '%{public}s',
85. `MS_LITE_LOG: info.width = ${info.size.width}`);
86. hilog.info(0xFF00, TAG, '%{public}s',
87. `MS_LITE_LOG: info.height = ${info.size.height}`);

89. // 4.根据模型输入的尺寸，将图片裁剪为对应的size，获取图片buffer数据readBuffer
90. pixelMap.scale(256.0 / info.size.width, 256.0 / info.size.height).then(() => {
91. pixelMap.crop({
92. x: 16,
93. y: 16,
94. size: { height: this.modelInputHeight, width: this.modelInputWidth }
95. }).then(async () => {
96. let info = await pixelMap.getImageInfo();
97. hilog.info(0xFF00, TAG, '%{public}s',
98. `MS_LITE_LOG: crop info.width = ${info.size.width}`);
99. hilog.info(0xFF00, TAG, '%{public}s',
100. `MS_LITE_LOG: crop info.height = ${info.size.height}`);
101. // 需要创建的像素buffer大小
102. let readBuffer = new ArrayBuffer(this.modelInputHeight * this.modelInputWidth * 4);
103. await pixelMap.readPixelsToBuffer(readBuffer);
104. hilog.info(0xFF00, TAG, '%{public}s',
105. `MS_LITE_LOG: Succeeded in reading image pixel data, buffer: ${readBuffer.byteLength}`);
106. // 处理readBuffer，转换成float32格式，并进行标准化处理
107. const imageArr =
108. new Uint8Array(readBuffer.slice(0, this.modelInputHeight * this.modelInputWidth * 4));
109. hilog.info(0xFF00, TAG, '%{public}s',
110. `MS_LITE_LOG: imageArr length: ${imageArr.length}`);

112. let means = [0.485, 0.456, 0.406];
113. let stds = [0.229, 0.224, 0.225];
114. let float32View = new Float32Array(this.modelInputHeight * this.modelInputWidth * 3);
115. let index = 0;
116. for (let i = 0; i < imageArr.length; i++) {
117. if ((i + 1) % 4 === 0) {
118. float32View[index] = (imageArr[i - 3] / 255.0 - means[0]) / stds[0]; // B
119. float32View[index+1] = (imageArr[i - 2] / 255.0 - means[1]) / stds[1]; // G
120. float32View[index+2] = (imageArr[i - 1] / 255.0 - means[2]) / stds[2]; // R
121. index += 3;
122. }
123. }
124. hilog.info(0xFF00, TAG, '%{public}s',
125. `MS_LITE_LOG: float32View length: ${float32View.length}`);
126. let printStr = 'float32View data:';
127. for (let i = 0; i < 20; i++) {
128. printStr += ' ' + float32View[i];
129. }
130. hilog.info(0xFF00, TAG, '%{public}s',
131. `MS_LITE_LOG: float32View data: ${printStr}`);

133. // 调用c++的runDemo
134. hilog.info(0xFF00, TAG, '%{public}s',
135. `MS_LITE_LOG: *** Start MSLite Demo ***`);

137. let output: Array<number> = msliteNapi.runDemo(Array.from(float32View), resMgr);
138. hilog.info(0xFF00, TAG, '%{public}s',
139. `MS_LITE_WARN: output length = ${output.length}, value = ${output.slice(0, 20)}`);

141. // 取分类占比的最大值top5
142. this.max = 0;
143. this.maxIndex = 0;
144. this.maxArray = [];
145. this.maxIndexArray = [];
146. let newArray = output.filter(value => value !== this.max);
147. for (let n = 0; n < 5; n++) {
148. this.max = output[0];
149. this.maxIndex = 0;
150. // 取最大值
151. for (let m = 0; m < newArray.length; m++) {
152. if (newArray[m] > this.max) {
153. this.max = newArray[m];
154. this.maxIndex = m;
155. }
156. }
157. this.maxArray.push(Math.round(this.max * 10000));
158. this.maxIndexArray.push(this.maxIndex);
159. // filter数组过滤函数
160. newArray = newArray.filter(value => value !== this.max);
161. }
162. hilog.info(0xFF00, TAG, '%{public}s',
163. `MS_LITE_LOG: max: ${this.maxArray}`);
164. hilog.info(0xFF00, TAG, '%{public}s',
165. `MS_LITE_LOG: maxIndex: ${this.maxIndexArray}`);

167. hilog.info(0xFF00, TAG, '%{public}s',
168. `MS_LITE_LOG: *** Finished MSLite Demo ***`);
169. }).catch((error: BusinessError) => {
170. hilog.error(0xFF00, TAG, '%{public}s',
171. `MS_LITE_ERR: getRawFileContent promise error is: ${error}`);
172. })
173. })
174. // 5.关闭文件
175. fileIo.closeSync(file);
176. })
177. })
178. } catch (err) {
179. hilog.error(0xFF00, TAG, '%{public}s',
180. `MS_LITE_ERR: uri: open file fd failed. ${err}`);
181. }
182. })
183. })
184. }.width('100%')
185. }
186. .height('100%')
187. }
188. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemo/entry/src/main/ets/pages/Index.ets#L16-L338)

### 调测验证

1. 在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：

   ```
   1. Launching com.samples.mindsporelitecdemo
   2. $ hdc shell aa force-stop com.samples.mindsporelitecdemo
   3. $ hdc shell mkdir data/local/tmp/xxx
   4. $ hdc file send C:\Users\xxx\MindSporeLiteCDemo\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
   5. $ hdc shell bm install -p data/local/tmp/xxx
   6. $ hdc shell rm -rf data/local/tmp/xxx
   7. $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemo
   ```
2. 在设备屏幕点击photo按钮，选择图片，点击确定。设备屏幕显示所选图片的分类结果，在日志打印结果中，过滤关键字”MS\_LITE“，可得到如下结果：

   ```
   1. 08-05 17:15:52.001   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: PhotoViewPicker.select successfully, photoSelectResult uri: {"photoUris":["file://media/Photo/13/IMG_1501955351_012/plant.jpg"]}
   2. ...
   3. 08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: crop info.width = 224
   4. 08-05 17:15:52.627   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: crop info.height = 224
   5. 08-05 17:15:52.628   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: Succeeded in reading image pixel data, buffer: 200704
   6. 08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: float32View data: float32View data: 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143 1.4722440242767334 1.2385478019714355 1.308123230934143
   7. 08-05 17:15:52.971   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: *** Start MSLite Demo ***
   8. 08-05 17:15:53.454   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Build MSLite model success.
   9. 08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Run MSLite model Predict success.
   10. 08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: Get model outputs:
   11. 08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: - Tensor 0 name is: Default/head-MobileNetV2Head/Sigmoid-op466.
   12. 08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: - Tensor data is:
   13. 08-05 17:15:53.753   4684-4684    A00000/[MSLiteNapi]            pid-4684              I     MS_LITE_LOG: 3.43385e-06 1.40285e-05 9.11969e-07 4.91007e-05 9.50266e-07 3.94537e-07 0.0434676 3.97196e-05 0.00054832 0.000246202 1.576e-05 3.6494e-06 1.23553e-05 0.196977 5.3028e-05 3.29346e-05 4.90475e-07 1.66109e-06 7.03273e-06 8.83677e-07 3.1365e-06
   14. 08-05 17:15:53.781   4684-4684    A03d00/JSAPP                   pid-4684              W     MS_LITE_WARN: output length =  500 ;value =  0.0000034338463592575863,0.000014028532859811094,9.119685273617506e-7,0.000049100715841632336,9.502661555416125e-7,3.945370394831116e-7,0.04346757382154465,0.00003971960904891603,0.0005483203567564487,0.00024620210751891136,0.000015759984307806008,0.0000036493988773145247,0.00001235533181898063,0.1969769448041916,0.000053027983085485175,0.000032934600312728435,4.904751449430478e-7,0.0000016610861166554969,0.000007032729172351537,8.836767619868624e-7
   15. 08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: max:9497,7756,1970,435,46
   16. 08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: maxIndex:323,46,13,6,349
   17. 08-05 17:15:53.831   4684-4684    A03d00/JSAPP                   pid-4684              I     MS_LITE_LOG: *** Finished MSLite Demo ***
   ```

### 效果示意

在设备上，点击photo按钮，选择相册中的一张图片，点击确定。在图片下方显示此图片占比前4的分类信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/a38sIaDMTzqdiWqYVjDo1Q/zh-cn_image_0000002589245659.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=401ABE3086B868C1B3E1B96FDE77885B58B4734A2EBB817DF6A2AA7691497E89) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/w3OMhuSZTSmcmKY-KvOIHQ/zh-cn_image_0000002558765848.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=7744867D0B0FB7B003412794A025018B4C8CC7C4DB4905D93E3C105A651ED7A3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Wiu_ntaAQPqMvelU0d2cKg/zh-cn_image_0000002558606192.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=6C59F3C27877B14158782F659CCD6F6446289699F381F5653DB4F99C5A231367) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/r_3gFi4OTQytKDQhJszLjw/zh-cn_image_0000002558765850.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=DC39459C758A59341171F5CE3D3D375C84755207955544036766C1517282772B)

## 示例代码

* [基于MindSporeLite接口实现图像分类（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MindSporeLiteKit/MindSporeLiteCDemo)
