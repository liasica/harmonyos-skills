---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-train-guidelines
title: 使用MindSpore Lite进行端侧训练 (C/C++)
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > 模型部署 > 使用MindSpore Lite进行端侧训练 (C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:67246d6ae43d7825ee4b3f2e0672d62fd331c07fca6fea237f8f8b31d0522758
---

## 场景介绍

MindSpore Lite是一款AI引擎，它提供了面向不同硬件设备AI模型推理的功能，目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用，同时支持在端侧设备上进行部署训练，让模型在实际业务场景中自适应用户的行为。

本文介绍使用MindSpore Lite端侧AI引擎进行模型训练的通用开发流程。

## 接口说明

此处给出使用MindSpore Lite进行模型训练相关的部分接口，具体请见下方表格。更多接口及详细内容，请见[MindSpore](../harmonyos-references/capi-mindspore.md)。

| 接口名称 | 描述 |
| --- | --- |
| OH\_AI\_ContextHandle OH\_AI\_ContextCreate() | 创建一个上下文的对象。注意：此接口需跟OH\_AI\_ContextDestroy配套使用。 |
| OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type) | 创建一个运行时设备信息对象。 |
| void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context) | 释放上下文对象。 |
| void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info) | 添加运行时设备信息。 |
| OH\_AI\_TrainCfgHandle OH\_AI\_TrainCfgCreate() | 创建训练配置对象指针。 |
| void OH\_AI\_TrainCfgDestroy(OH\_AI\_TrainCfgHandle \*train\_cfg) | 销毁训练配置对象指针。 |
| OH\_AI\_ModelHandle OH\_AI\_ModelCreate() | 创建一个模型对象。 |
| OH\_AI\_Status OH\_AI\_TrainModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path, OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context, const OH\_AI\_TrainCfgHandle train\_cfg) | 通过模型文件加载并编译MindSpore Lite训练模型。 |
| OH\_AI\_Status OH\_AI\_RunStep(OH\_AI\_ModelHandle model, const OH\_AI\_KernelCallBack before, const OH\_AI\_KernelCallBack after) | 单步训练模型。 |
| OH\_AI\_Status OH\_AI\_ModelSetTrainMode(OH\_AI\_ModelHandle model, bool train) | 设置训练模式。 |
| OH\_AI\_Status OH\_AI\_ExportModel(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, const char \*model\_file, OH\_AI\_QuantizationType quantization\_type, bool export\_inference\_only, char \*\*output\_tensor\_name, size\_t num) | 导出训练后的ms模型。 |
| void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model) | 释放一个模型对象。 |

## 开发步骤

使用MindSpore Lite进行模型训练的开发流程如下图所示。

**图 1** 使用MindSpore Lite进行模型训练的开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/VldiDHXHR7C_HQYlBN6fyA/zh-cn_image_0000002589325717.png?HW-CC-KV=V1&HW-CC-Date=20260429T054345Z&HW-CC-Expire=86400&HW-CC-Sign=EEFCE062B42A1542C13BB765BD0B25B6ED794141123270C11216D1CC2DD83636)

进入主要流程之前需要先引用相关的头文件，并编写函数生成随机的输入，具体如下：

```
1. #include <stdlib.h>
2. #include <stdio.h>
3. #include <string.h>
4. #include "mindspore/model.h"

6. int GenerateInputDataWithRandom(OH_AI_TensorHandleArray inputs) {
7. for (size_t i = 0; i < inputs.handle_num; ++i) {
8. float *input_data = (float *)OH_AI_TensorGetMutableData(inputs.handle_list[i]);
9. if (input_data == NULL) {
10. printf("OH_AI_TensorGetMutableData failed.\n");
11. return  OH_AI_STATUS_LITE_ERROR;
12. }
13. int64_t num = OH_AI_TensorGetElementNum(inputs.handle_list[i]);
14. const int divisor = 10;
15. for (size_t j = 0; j < num; j++) {
16. input_data[j] = (float)(rand() % divisor) / divisor;  // 0--0.9f
17. }
18. }
19. return OH_AI_STATUS_SUCCESS;
20. }
```

然后进入主要的开发步骤，包括模型的准备、读取、编译、训练、模型导出和释放，具体开发过程及细节请见下文的开发步骤及示例。

1. 模型准备。

   准备的模型格式为.ms，本文以lenet\_train.ms为例（此模型是提前准备的ms模型，本文相关效果仅以此模型文件为例）。开发者请自行准备所需的模型，可以按如下步骤操作：

   * 首先基于MindSpore架构使用Python创建网络模型，并导出为.mindir文件，详细指南参考[这里](https://www.mindspore.cn/tutorials/zh-CN/r2.1/beginner/quick_start.html)。
   * 然后将.mindir模型文件转换成.ms文件，转换操作步骤可以参考[训练模型转换](https://www.mindspore.cn/lite/docs/zh-CN/r2.1/use/converter_train.html)，.ms文件可以导入端侧设备并基于MindSpore Lite端侧框架进行训练。
2. 创建上下文，设置设备类型、训练配置等参数。

   ```
   1. // Create and init context, add CPU device info
   2. OH_AI_ContextHandle context = OH_AI_ContextCreate();
   3. if (context == NULL) {
   4. printf("OH_AI_ContextCreate failed.\n");
   5. return OH_AI_STATUS_LITE_ERROR;
   6. }

   8. OH_AI_DeviceInfoHandle cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
   9. if (cpu_device_info == NULL) {
   10. printf("OH_AI_DeviceInfoCreate failed.\n");
   11. OH_AI_ContextDestroy(&context);
   12. return OH_AI_STATUS_LITE_ERROR;
   13. }
   14. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);

   16. // Create trainCfg
   17. OH_AI_TrainCfgHandle trainCfg = OH_AI_TrainCfgCreate();
   18. if (trainCfg == NULL) {
   19. printf("OH_AI_TrainCfgCreate failed.\n");
   20. OH_AI_ContextDestroy(&context);
   21. return OH_AI_STATUS_LITE_ERROR;
   22. }
   ```
3. 创建、加载与编译模型。

   调用OH\_AI\_TrainModelBuildFromFile加载并编译模型。

   ```
   1. // Create model
   2. OH_AI_ModelHandle model = OH_AI_ModelCreate();
   3. if (model == NULL) {
   4. printf("OH_AI_ModelCreate failed.\n");
   5. OH_AI_TrainCfgDestroy(&trainCfg);
   6. OH_AI_ContextDestroy(&context);
   7. return OH_AI_STATUS_LITE_ERROR;
   8. }

   10. // Build model
   11. int ret = OH_AI_TrainModelBuildFromFile(model, model_file, OH_AI_MODELTYPE_MINDIR, context, trainCfg);
   12. if (ret != OH_AI_STATUS_SUCCESS) {
   13. printf("OH_AI_TrainModelBuildFromFile failed, ret: %d.\n", ret);
   14. OH_AI_ModelDestroy(&model);
   15. OH_AI_ContextDestroy(&context);
   16. return ret;
   17. }
   ```
4. 输入数据。

   模型执行之前需要向输入的张量中填充数据。本例使用随机的数据对模型进行填充。

   ```
   1. // Get Inputs
   2. OH_AI_TensorHandleArray inputs = OH_AI_ModelGetInputs(model);
   3. if (inputs.handle_list == NULL) {
   4. printf("OH_AI_ModelGetInputs failed, ret: %d.\n", ret);
   5. OH_AI_ModelDestroy(&model);
   6. OH_AI_ContextDestroy(&context);
   7. return ret;
   8. }

   10. // Generate random data as input data.
   11. ret = GenerateInputDataWithRandom(inputs);
   12. if (ret != OH_AI_STATUS_SUCCESS) {
   13. printf("GenerateInputDataWithRandom failed, ret: %d.\n", ret);
   14. OH_AI_ModelDestroy(&model);
   15. OH_AI_ContextDestroy(&context);
   16. return ret;
   17. }
   ```
5. 执行训练。

   使用OH\_AI\_ModelSetTrainMode接口设置训练模式，使用OH\_AI\_RunStep接口进行模型训练。

   ```
   1. // Set Train Mode
   2. ret = OH_AI_ModelSetTrainMode(model, true);
   3. if (ret != OH_AI_STATUS_SUCCESS) {
   4. printf("OH_AI_ModelSetTrainMode failed, ret: %d.\n", ret);
   5. OH_AI_ModelDestroy(&model);
   6. OH_AI_ContextDestroy(&context);
   7. return ret;
   8. }

   10. // Model Train Step
   11. ret = OH_AI_RunStep(model, NULL, NULL);
   12. if (ret != OH_AI_STATUS_SUCCESS) {
   13. printf("OH_AI_RunStep failed, ret: %d.\n", ret);
   14. OH_AI_ModelDestroy(&model);
   15. OH_AI_ContextDestroy(&context);
   16. return ret;
   17. }
   18. printf("Train Step Success.\n");
   ```
6. 导出训练后模型。

   使用OH\_AI\_ExportModel接口导出训练后模型。

   ```
   1. // Export Train Model
   2. ret = OH_AI_ExportModel(model, OH_AI_MODELTYPE_MINDIR, export_train_model, OH_AI_NO_QUANT, false, NULL, 0);
   3. if (ret != OH_AI_STATUS_SUCCESS) {
   4. printf("OH_AI_ExportModel train failed, ret: %d.\n", ret);
   5. OH_AI_ModelDestroy(&model);
   6. OH_AI_ContextDestroy(&context);
   7. return ret;
   8. }
   9. printf("Export Train Model Success.\n");

   11. // Export Inference Model
   12. ret = OH_AI_ExportModel(model, OH_AI_MODELTYPE_MINDIR, export_infer_model, OH_AI_NO_QUANT, true, NULL, 0);
   13. if (ret != OH_AI_STATUS_SUCCESS) {
   14. printf("OH_AI_ExportModel inference failed, ret: %d.\n", ret);
   15. OH_AI_ModelDestroy(&model);
   16. OH_AI_ContextDestroy(&context);
   17. return ret;
   18. }
   19. printf("Export Inference Model Success.\n");
   ```
7. 释放模型。

   不再使用MindSpore Lite推理框架时，需要释放已经创建的模型。

   ```
   1. // Delete model and context.
   2. OH_AI_ModelDestroy(&model);
   3. OH_AI_ContextDestroy(&context);
   ```

## 调测验证

1. 编写CMakeLists.txt。

   ```
   1. cmake_minimum_required(VERSION 3.14)
   2. project(TrainDemo)

   4. add_executable(train_demo main.c)

   6. target_link_libraries(
   7. train_demo
   8. mindspore_lite_ndk
   9. )
   ```

   * 使用ohos-sdk交叉编译，需要对CMake设置native工具链路径，即：-DCMAKE\_TOOLCHAIN\_FILE="/xxx/native/build/cmake/ohos.toolchain.cmake"。
   * 编译命令如下，其中OHOS\_NDK需要设置为native工具链路径：

     ```
     1. mkdir -p build

     3. cd ./build || exit
     4. OHOS_NDK=""
     5. cmake -G "Unix Makefiles" \
     6. -S ../ \
     7. -DCMAKE_TOOLCHAIN_FILE="$OHOS_NDK/build/cmake/ohos.toolchain.cmake" \
     8. -DOHOS_ARCH=arm64-v8a \
     9. -DCMAKE_BUILD_TYPE=Release

     11. make
     ```
2. 运行编译的可执行程序。

   * 使用hdc连接设备，并将train\_demo和lenet\_train.ms推送到设备中的相同目录。
   * 使用hdc shell进入设备，并进入train\_demo所在的目录执行如下命令，即可得到结果。

   ```
   1. ./train_demo ./lenet_train.ms export_train_model export_infer_model
   ```

   得到如下输出：

   ```
   1. Train Step Success.
   2. Export Train Model Success.
   3. Export Inference Model Success.
   4. Tensor name: Default/network-WithLossCell/_backbone-LeNet5/fc3-Dense/BiasAdd-op121, tensor size is 80, elements num: 20.
   5. output data is:
   6. 0.000265 0.000231 0.000254 0.000269 0.000238 0.000228
   ```

   在train\_demo所在目录可以看到导出的两个模型文件：export\_train\_model.ms和export\_infer\_model.ms。

## 完整示例

```
1. #include <stdlib.h>
2. #include <stdio.h>
3. #include <string>
4. #include "mindspore/model.h"

6. int GenerateInputDataWithRandom(OH_AI_TensorHandleArray inputs) {
7. for (size_t i = 0; i < inputs.handle_num; ++i) {
8. float *input_data = (float *)OH_AI_TensorGetMutableData(inputs.handle_list[i]);
9. if (input_data == NULL) {
10. printf("OH_AI_TensorGetMutableData failed.\n");
11. return  OH_AI_STATUS_LITE_ERROR;
12. }
13. int64_t num = OH_AI_TensorGetElementNum(inputs.handle_list[i]);
14. const int divisor = 10;
15. for (size_t j = 0; j < num; j++) {
16. input_data[j] = (float)(rand() % divisor) / divisor;  // 0--0.9f
17. }
18. }
19. return OH_AI_STATUS_SUCCESS;
20. }

22. int ModelPredict(char* model_file) {
23. // Create and init context, add CPU device info
24. OH_AI_ContextHandle context = OH_AI_ContextCreate();
25. if (context == NULL) {
26. printf("OH_AI_ContextCreate failed.\n");
27. return OH_AI_STATUS_LITE_ERROR;
28. }

30. OH_AI_DeviceInfoHandle cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
31. if (cpu_device_info == NULL) {
32. printf("OH_AI_DeviceInfoCreate failed.\n");
33. OH_AI_ContextDestroy(&context);
34. return OH_AI_STATUS_LITE_ERROR;
35. }
36. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);

38. // Create model
39. OH_AI_ModelHandle model = OH_AI_ModelCreate();
40. if (model == NULL) {
41. printf("OH_AI_ModelCreate failed.\n");
42. OH_AI_ContextDestroy(&context);
43. return OH_AI_STATUS_LITE_ERROR;
44. }

46. // Build model
47. int ret = OH_AI_ModelBuildFromFile(model, model_file, OH_AI_MODELTYPE_MINDIR, context);
48. if (ret != OH_AI_STATUS_SUCCESS) {
49. printf("OH_AI_ModelBuildFromFile failed, ret: %d.\n", ret);
50. OH_AI_ModelDestroy(&model);
51. OH_AI_ContextDestroy(&context);
52. return ret;
53. }

55. // Get Inputs
56. OH_AI_TensorHandleArray inputs = OH_AI_ModelGetInputs(model);
57. if (inputs.handle_list == NULL) {
58. printf("OH_AI_ModelGetInputs failed, ret: %d.\n", ret);
59. OH_AI_ModelDestroy(&model);
60. OH_AI_ContextDestroy(&context);
61. return ret;
62. }

64. // Generate random data as input data.
65. ret = GenerateInputDataWithRandom(inputs);
66. if (ret != OH_AI_STATUS_SUCCESS) {
67. printf("GenerateInputDataWithRandom failed, ret: %d.\n", ret);
68. OH_AI_ModelDestroy(&model);
69. OH_AI_ContextDestroy(&context);
70. return ret;
71. }

73. // Model Predict
74. OH_AI_TensorHandleArray outputs;
75. ret = OH_AI_ModelPredict(model, inputs, &outputs, NULL, NULL);
76. if (ret != OH_AI_STATUS_SUCCESS) {
77. printf("MSModelPredict failed, ret: %d.\n", ret);
78. OH_AI_ModelDestroy(&model);
79. OH_AI_ContextDestroy(&context);
80. return ret;
81. }

83. // Print Output Tensor Data.
84. for (size_t i = 0; i < outputs.handle_num; ++i) {
85. OH_AI_TensorHandle tensor = outputs.handle_list[i];
86. int64_t element_num = OH_AI_TensorGetElementNum(tensor);
87. printf("Tensor name: %s, tensor size is %ld ,elements num: %ld.\n", OH_AI_TensorGetName(tensor),
88. OH_AI_TensorGetDataSize(tensor), element_num);
89. const float *data = (const float *)OH_AI_TensorGetData(tensor);
90. printf("output data is:\n");
91. const int max_print_num = 50;
92. for (int j = 0; j < element_num && j <= max_print_num; ++j) {
93. printf("%f ", data[j]);
94. }
95. printf("\n");
96. }

98. OH_AI_ModelDestroy(&model);
99. OH_AI_ContextDestroy(&context);
100. return OH_AI_STATUS_SUCCESS;
101. }

103. int TrainDemo(int argc, const char **argv) {
104. if (argc < 4) {
105. printf("Model file must be provided.\n");
106. printf("Export Train Model path must be provided.\n");
107. printf("Export Inference Model path must be provided.\n");
108. return OH_AI_STATUS_LITE_ERROR;
109. }
110. const char *model_file = argv[1];
111. const char *export_train_model = argv[2];
112. const char *export_infer_model = argv[3];

114. // Create and init context, add CPU device info
115. OH_AI_ContextHandle context = OH_AI_ContextCreate();
116. if (context == NULL) {
117. printf("OH_AI_ContextCreate failed.\n");
118. return OH_AI_STATUS_LITE_ERROR;
119. }

121. OH_AI_DeviceInfoHandle cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
122. if (cpu_device_info == NULL) {
123. printf("OH_AI_DeviceInfoCreate failed.\n");
124. OH_AI_ContextDestroy(&context);
125. return OH_AI_STATUS_LITE_ERROR;
126. }
127. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);

129. // Create trainCfg
130. OH_AI_TrainCfgHandle trainCfg = OH_AI_TrainCfgCreate();
131. if (trainCfg == NULL) {
132. printf("OH_AI_TrainCfgCreate failed.\n");
133. OH_AI_ContextDestroy(&context);
134. return OH_AI_STATUS_LITE_ERROR;
135. }

137. // Create model
138. OH_AI_ModelHandle model = OH_AI_ModelCreate();
139. if (model == NULL) {
140. printf("OH_AI_ModelCreate failed.\n");
141. OH_AI_TrainCfgDestroy(&trainCfg);
142. OH_AI_ContextDestroy(&context);
143. return OH_AI_STATUS_LITE_ERROR;
144. }

146. // Build model
147. int ret = OH_AI_TrainModelBuildFromFile(model, model_file, OH_AI_MODELTYPE_MINDIR, context, trainCfg);
148. if (ret != OH_AI_STATUS_SUCCESS) {
149. printf("OH_AI_TrainModelBuildFromFile failed, ret: %d.\n", ret);
150. OH_AI_ModelDestroy(&model);
151. OH_AI_ContextDestroy(&context);
152. return ret;
153. }

155. // Get Inputs
156. OH_AI_TensorHandleArray inputs = OH_AI_ModelGetInputs(model);
157. if (inputs.handle_list == NULL) {
158. printf("OH_AI_ModelGetInputs failed, ret: %d.\n", ret);
159. OH_AI_ModelDestroy(&model);
160. OH_AI_ContextDestroy(&context);
161. return ret;
162. }

164. // Generate random data as input data.
165. ret = GenerateInputDataWithRandom(inputs);
166. if (ret != OH_AI_STATUS_SUCCESS) {
167. printf("GenerateInputDataWithRandom failed, ret: %d.\n", ret);
168. OH_AI_ModelDestroy(&model);
169. OH_AI_ContextDestroy(&context);
170. return ret;
171. }

173. // Set Train Mode
174. ret = OH_AI_ModelSetTrainMode(model, true);
175. if (ret != OH_AI_STATUS_SUCCESS) {
176. printf("OH_AI_ModelSetTrainMode failed, ret: %d.\n", ret);
177. OH_AI_ModelDestroy(&model);
178. OH_AI_ContextDestroy(&context);
179. return ret;
180. }

182. // Model Train Step
183. ret = OH_AI_RunStep(model, NULL, NULL);
184. if (ret != OH_AI_STATUS_SUCCESS) {
185. printf("OH_AI_RunStep failed, ret: %d.\n", ret);
186. OH_AI_ModelDestroy(&model);
187. OH_AI_ContextDestroy(&context);
188. return ret;
189. }
190. printf("Train Step Success.\n");

192. // Export Train Model
193. ret = OH_AI_ExportModel(model, OH_AI_MODELTYPE_MINDIR, export_train_model, OH_AI_NO_QUANT, false, NULL, 0);
194. if (ret != OH_AI_STATUS_SUCCESS) {
195. printf("OH_AI_ExportModel train failed, ret: %d.\n", ret);
196. OH_AI_ModelDestroy(&model);
197. OH_AI_ContextDestroy(&context);
198. return ret;
199. }
200. printf("Export Train Model Success.\n");

202. // Export Inference Model
203. ret = OH_AI_ExportModel(model, OH_AI_MODELTYPE_MINDIR, export_infer_model, OH_AI_NO_QUANT, true, NULL, 0);
204. if (ret != OH_AI_STATUS_SUCCESS) {
205. printf("OH_AI_ExportModel inference failed, ret: %d.\n", ret);
206. OH_AI_ModelDestroy(&model);
207. OH_AI_ContextDestroy(&context);
208. return ret;
209. }
210. printf("Export Inference Model Success.\n");

212. // Delete model and context.
213. OH_AI_ModelDestroy(&model);
214. OH_AI_ContextDestroy(&context);

216. // Use The Exported Model to predict
217. std::string temp_path = std::string(export_infer_model) + ".ms";
218. const char *exported_model = temp_path.c_str();
219. ret = ModelPredict(exported_model);
220. if (ret != OH_AI_STATUS_SUCCESS) {
221. printf("Exported Model to predict failed, ret: %d.\n", ret);
222. return ret;
223. }
224. return OH_AI_STATUS_SUCCESS;
225. }

227. int main(int argc, const char **argv) { return TrainDemo(argc, argv); }
```
