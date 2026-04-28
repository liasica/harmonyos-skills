---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-graph-compilation-and-execution
title: 图编译和图执行
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子部署 > 算子入图（GE图）开发 > 图编译和图执行
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c10c70fb750c6476e51c545f380047ecfda283d7e1b957c7f4fd143dfa6b544e
---

单算子模型执行是指基于图IR执行算子，先编译算子（例如，使用OMG工具将Ascend IR定义的单算子描述文件编译成算子omc模型文件），再调用模型加载推理接口执行单算子网络。下文仅提供单算子模型执行的样例和基础内容讲解，详细内容请参考[端侧部署](cannkit-whole-deployment-process.md)章节。

说明

HarmonyOS Next暂不支持图编译与图执行，仅支持通过[AI框架算子适配](cannkit-overview-of-ai-framework-operator.md)方式集成自定义算子，以下步骤仅供参考。

## 环境要求

* 已参考[环境准备](cannkit-environment-preparation.md)，完成DDK驱动和软件的安装，配置DDK软件所需基本环境变量。

  安装DDK软件后，使用DDK运行开发者进行编译、运行时，需要以DDK运行开发者登录环境，执行**source ${install\_path}/ddk/tools/tools\_ascendc/set\_ascendc\_env.sh**命令设置环境变量。其中${install\_path}为DDK软件的安装目录，例如：/home。
* 已参考完成算子的开发和部署。

## 准备验证代码工程

在执行NPU调试命令时，例如：

```
1. ascendebug kernel --backend npu  --chip-version kirin9020 --repo-type customize --json-file ./temp.json --core-type AiCore
```

命令行参数详见[NPU调测参数](cannkit-cli-parameters.md#npu调测参数)，会在${debug\_workspace} /${op\_type} /npu/src下生成验证样例工程，代码工程目录结构如下。

```
1. src
2. ├── BuildIRGraph.cpp  // 生成单算子图源文件
3. ├── BuildIRGraph.h    // 单算子图入口：CreateCustomIRGraph
4. ├── build.sh            // omc 模型编译脚本
5. ├── CMakeLists.txt
6. ├── custom_graph.omc // 编译后得到的omc模型
7. └── op_proto.h         // 算子编译输出的算子原型定义头文件
```

## 生成单算子离线模型文件

执行验证样例工程下的build.sh。

```
1. ./build.sh
```

以上命令执行后，会在当前路径下生成custom\_graph.omc的离线模型文件。

## 生成输入数据

在样例工程目录下，执行如下命令：

```
1. python3 scripts/gen_data.py
```

会在input目录下生成两个shape为(8,2048)，数据类型为float16的数据文件input\_0.bin与input\_1.bin，用于进行AddCustom算子的验证。

代码样例如下。

```
1. import numpy as np
2. a = np.random.randint(100, size=(8, 2048,)).astype(np.float16)
3. b = np.random.randint(100, size=(8, 2048,)).astype(np.float16)
4. a.tofile('input_0.bin')
5. b.tofile('input_1.bin')
```

## APP集成代码

开发者可以参考如下样例编写模型加载、执行的代码逻辑。完整集成流程请参考[应用开发](../hiai-Guides/app-dev-0000001052605540.md)。

以下是关键步骤的代码示例，不可以直接拷贝编译运行，仅供参考，调用接口后，需增加异常处理的分支，并记录报错日志、提示日志，此处不一一列举。

```
1. int RunModel(void* modelData, size_t modelSize)
2. {
3. // 1.加载omc模型
4. auto modelDescV1 = std::make_shared<hiai::AiModelDescription>("model", 3, 0, 0, 0);
5. modelDescV1->SetModelBuffer(modelData, modelSize);

7. std::vector<std::shared_ptr<hiai::AiModelDescription>> modelDescVec;
8. modelDescVec.push_back(modelDescV1);
9. auto clientV1 = std::make_shared<hiai::AiModelMngerClient>();
10. if (clientV1->Init(nullptr) != hiai::SUCCESS) {
11. LOGE("client Init() failed.");
12. return FAILURE;
13. }

15. if (clientV1->Load(modelDescVec) != hiai::SUCCESS) {
16. LOGE("client Load() failed.");
17. return FAILURE;
18. }
19. LOGI("load model success");
20. std::vector<hiai::TensorDimension> inDimVecV1;
21. std::vector<hiai::TensorDimension> outDimVecV1;
22. std::vector<std::shared_ptr<hiai::AiTensor>> inTensorVecV1;
23. std::vector<std::shared_ptr<hiai::AiTensor>> outTensorVecV1;

25. if (clientV1->GetModelIOTensorDim(modelDescV1->GetName(), inDimVecV1, outDimVecV1) != hiai::SUCCESS) {
26. LOGE("client GetModelIOTensorDim() failed.");
27. clientV1->UnLoadModel();
28. return FAILURE;
29. }
30. // 2、设置模型输入、输出
31. for (size_t i = 0; i < INPUT_NUM &&  i < inDimVecV1.size(); ++i) {
32. void *data = nullptr;
33. size_t size = 0;
34. LOGI("open input file  inputFile: %s ", INPUT_LIST[i].c_str());
35. if (!ReadData(INPUT_LIST[i], &data, size)) {
36. LOGE("open input file failed! inputFile: %s ", INPUT_LIST[i].c_str());
37. clientV1->UnLoadModel();
38. return FAILURE;
39. }

41. auto inputV1 = std::make_shared<hiai::AiTensor>();

43. inputV1->Init(&inDimVecV1[i], INPUT_TYPE);
44. if (inputV1->GetSize() != size) {
45. LOGE("inputSize: %d != fileSize: %zu ", inputV1->GetSize(), size);
46. clientV1->UnLoadModel();
47. free(data);
48. data = nullptr;
49. return FAILURE;
50. }
51. memcpy(inputV1->GetBuffer(), data, size);
52. inTensorVecV1.push_back(inputV1);
53. free(data);
54. data = nullptr;
55. }
56. LOGI("load input success");

58. for (size_t i = 0; i < outDimVecV1.size(); i++) {
59. auto outputV1 = std::make_shared<hiai::AiTensor>();
60. outputV1->Init(&outDimVecV1[i], OUTPUT_TYPE);
61. outTensorVecV1.push_back(outputV1);
62. }
63. LOGI("init output success");

65. // 3、进行模型推理
66. hiai::AiContext context;
67. context.AddPara("model_name", "model");
68. int32_t istamp = 0;

70. auto retCode = clientV1->Process(context, inTensorVecV1, outTensorVecV1, 1000, istamp);
71. if (retCode != hiai::SUCCESS) {
72. LOGE("process failed.");
73. clientV1->UnLoadModel();
74. return retCode;
75. }
76. LOGI("process success");

78. for (size_t i = 0; i < outTensorVecV1.size(); i++) {
79. char* data = reinterpret_cast<char*>(outTensorVecV1[i]->GetBuffer());
80. DumpBufferToFile(data, outTensorVecV1[i]->GetSize(), OUTPUT_PATH);
81. }
82. LOGI("dump output success");

84. // 4、模型卸载
85. clientV1->UnLoadModel();
86. return retCode;
87. }
```
