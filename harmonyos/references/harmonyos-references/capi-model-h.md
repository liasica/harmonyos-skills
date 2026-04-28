---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h
title: model.h
breadcrumb: API参考 > AI > MindSpore Lite Kit（昇思推理框架服务） > C API > 头文件 > model.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bb27eaafab95b6c84bb768264c3d6b20b476671f7ce517fb16db1f3b210b2b03
---

## 概述

PhonePC/2in1TabletTVWearable

提供了模型相关接口，可以用于模型创建、模型推理等，该接口是非线程安全的。

**引用文件：** <mindspore/model.h>

**库：** libmindspore\_lite\_ndk.so

**系统能力：** SystemCapability.Ai.MindSpore

**起始版本：** 9

**相关模块：** [MindSpore](capi-mindspore.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| OH\_AI\_TensorHandleArray | [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) | 张量数组结构体，用于存储张量数组指针和张量数组长度。 |
| OH\_AI\_ShapeInfo | [OH\_AI\_ShapeInfo](capi-mindspore-oh-ai-shapeinfo.md) | 形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。 |
| OH\_AI\_CallBackParam | [OH\_AI\_CallBackParam](capi-mindspore-oh-ai-callbackparam.md) | 回调函数中传入的算子信息。 |
| void \* | [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) | 指向模型对象的指针。 |
| void \* | [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) | 指向训练配置对象的指针。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef bool (\*OH\_AI\_KernelCallBack)(const OH\_AI\_TensorHandleArray inputs, const OH\_AI\_TensorHandleArray outputs,const OH\_AI\_CallBackParam kernel\_Info)](capi-model-h.md#oh_ai_kernelcallback) | OH\_AI\_KernelCallBack | 回调函数指针。  该函数指针是用于设置[OH\_AI\_ModelPredict](capi-model-h.md#oh_ai_modelpredict)函数参数中的两个回调函数。  该指针指向的函数需要包含三个参数，其中inputs和outputs对应了算子的输入和输出张量，kernel\_Info表示当前算子的信息。  可以通过回调函数监控算子执行的情况，例如统计算子的执行时间，校验算子的正确性等等。 |
| [OH\_AI\_API OH\_AI\_ModelHandle OH\_AI\_ModelCreate(void)](capi-model-h.md#oh_ai_modelcreate) | - | 创建一个模型对象。 |
| [OH\_AI\_API void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model)](capi-model-h.md#oh_ai_modeldestroy) | - | 释放一个模型对象。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)](capi-model-h.md#oh_ai_modelbuild) | - | 从内存缓冲区加载并编译MindSpore Lite模型。  注意，同一个[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)对象仅能传递给[OH\_AI\_ModelBuild](capi-model-h.md#oh_ai_modelbuild)或者[OH\_AI\_ModelBuildFromFile](capi-model-h.md#oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)](capi-model-h.md#oh_ai_modelbuildfromfile) | - | 通过模型文件加载并编译MindSpore Lite模型。  注意，同一个[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)对象仅能传递给[OH\_AI\_ModelBuild](capi-model-h.md#oh_ai_modelbuild)或者[OH\_AI\_ModelBuildFromFile](capi-model-h.md#oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelResize(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_ShapeInfo \*shape\_infos, size\_t shape\_info\_num)](capi-model-h.md#oh_ai_modelresize) | - | 调整已编译模型的输入形状。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelPredict(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_TensorHandleArray \*outputs, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)](capi-model-h.md#oh_ai_modelpredict) | - | 执行模型推理。 |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetInputs(const OH\_AI\_ModelHandle model)](capi-model-h.md#oh_ai_modelgetinputs) | - | 获取模型的输入张量数组结构体。 |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetOutputs(const OH\_AI\_ModelHandle model)](capi-model-h.md#oh_ai_modelgetoutputs) | - | 获取模型的输出张量数组结构体。 |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetInputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)](capi-model-h.md#oh_ai_modelgetinputbytensorname) | - | 通过张量名获取模型的输入张量。 |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetOutputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)](capi-model-h.md#oh_ai_modelgetoutputbytensorname) | - | 通过张量名获取模型的输出张量。 |
| [OH\_AI\_API OH\_AI\_TrainCfgHandle OH\_AI\_TrainCfgCreate()](capi-model-h.md#oh_ai_traincfgcreate) | - | 创建训练配置对象指针，仅用于端侧训练。 |
| [OH\_AI\_API void OH\_AI\_TrainCfgDestroy(OH\_AI\_TrainCfgHandle \*train\_cfg)](capi-model-h.md#oh_ai_traincfgdestroy) | - | 销毁训练配置对象指针，仅用于端侧训练。 |
| [OH\_AI\_API char \*\*OH\_AI\_TrainCfgGetLossName(OH\_AI\_TrainCfgHandle train\_cfg, size\_t \*num)](capi-model-h.md#oh_ai_traincfggetlossname) | - | 获取损失函数的名称列表，仅用于端侧训练。 |
| [OH\_AI\_API void OH\_AI\_TrainCfgSetLossName(OH\_AI\_TrainCfgHandle train\_cfg, const char \*\*loss\_name, size\_t num)](capi-model-h.md#oh_ai_traincfgsetlossname) | - | 设置损失函数的名称列表，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_OptimizationLevel OH\_AI\_TrainCfgGetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg)](capi-model-h.md#oh_ai_traincfggetoptimizationlevel) | - | 获取训练配置的优化等级，仅用于端侧训练。 |
| [OH\_AI\_API void OH\_AI\_TrainCfgSetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg, OH\_AI\_OptimizationLevel level)](capi-model-h.md#oh_ai_traincfgsetoptimizationlevel) | - | 设置训练配置的优化等级，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)](capi-model-h.md#oh_ai_trainmodelbuild) | - | 从内存缓冲区加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type,const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)](capi-model-h.md#oh_ai_trainmodelbuildfromfile) | - | 根据路径读取加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_RunStep(OH\_AI\_ModelHandle model, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)](capi-model-h.md#oh_ai_runstep) | - | 单步训练模型，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetLearningRate(OH\_AI\_ModelHandle model, float learning\_rate)](capi-model-h.md#oh_ai_modelsetlearningrate) | - | 设置训练的学习率，仅用于端侧训练。 |
| [OH\_AI\_API float OH\_AI\_ModelGetLearningRate(OH\_AI\_ModelHandle model)](capi-model-h.md#oh_ai_modelgetlearningrate) | - | 获取训练的学习率，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetWeights(OH\_AI\_ModelHandle model)](capi-model-h.md#oh_ai_modelgetweights) | - | 获取模型的所有权重Tensors，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelUpdateWeights(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray new\_weights)](capi-model-h.md#oh_ai_modelupdateweights) | - | 更新模型的权重Tensor内容，仅用于端侧训练。 |
| [OH\_AI\_API bool OH\_AI\_ModelGetTrainMode(OH\_AI\_ModelHandle model)](capi-model-h.md#oh_ai_modelgettrainmode) | - | 获取训练模式。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetTrainMode(OH\_AI\_ModelHandle model, bool train)](capi-model-h.md#oh_ai_modelsettrainmode) | - | 设置训练模式，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetupVirtualBatch(OH\_AI\_ModelHandle model, int virtual\_batch\_multiplier, float lr,float momentum)](capi-model-h.md#oh_ai_modelsetupvirtualbatch) | - | 设置虚拟batch用于训练，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModel(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, const char \*model\_file,OH\_AI\_QuantizationType quantization\_type, bool export\_inference\_only,char \*\*output\_tensor\_name, size\_t num)](capi-model-h.md#oh_ai_exportmodel) | - | 导出训练模型，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModelBuffer(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, void \*model\_data,size\_t \*data\_size, OH\_AI\_QuantizationType quantization\_type,bool export\_inference\_only, char \*\*output\_tensor\_name, size\_t num)](capi-model-h.md#oh_ai_exportmodelbuffer) | - | 导出训练模型内存缓存，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportWeightsCollaborateWithMicro(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type,const char \*weight\_file, bool is\_inference,bool enable\_fp16, char \*\*changeable\_weights\_name,size\_t num)](capi-model-h.md#oh_ai_exportweightscollaboratewithmicro) | - | 导出模型权重，只能用于micro推理，仅用于端侧训练。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelLoadConfig(OH\_AI\_ModelHandle model, const char \*config\_path)](capi-model-h.md#oh_ai_modelloadconfig) | - | 加载模型配置文件。 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelPredictWithConfig(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs, OH\_AI\_TensorHandleArray \*outputs, const char \*config, const OH\_AI\_KernelCallBack before, const OH\_AI\_KernelCallBack after)](capi-model-h.md#oh_ai_modelpredictwithconfig) | - | 执行模型推理，支持每次推理设置不同推理参数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AI\_KernelCallBack()

PhonePC/2in1TabletTVWearable

```
1. typedef bool (*OH_AI_KernelCallBack)(const OH_AI_TensorHandleArray inputs, const OH_AI_TensorHandleArray outputs,const OH_AI_CallBackParam kernel_Info)
```

**描述**

回调函数指针。

该函数指针是用于设置[OH\_AI\_ModelPredict](capi-model-h.md#oh_ai_modelpredict)函数参数中的两个回调函数。

该指针指向的函数需要包含三个参数，其中inputs和outputs对应了算子的输入和输出张量，kernel\_Info表示当前算子的信息。

可以通过回调函数监控算子执行的情况，例如统计算子的执行时间，校验算子的正确性等等。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) inputs | 模型输入对应的张量数组结构体。 |
| const [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) outputs | 模型输出对应的张量数组结构体。 |
| const [OH\_AI\_CallBackParam](capi-mindspore-oh-ai-callbackparam.md) kernel\_Info | 当前算子的信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 回调执行是否成功，若成功返回true，失败则返回false。 |

### OH\_AI\_ModelCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_ModelHandle OH_AI_ModelCreate(void)
```

**描述**

创建一个模型对象。

**起始版本：** 9

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) | 模型对象指针。 |

### OH\_AI\_ModelDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_ModelDestroy(OH_AI_ModelHandle *model)
```

**描述**

释放一个模型对象。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) \*model | 模型对象指针。 |

### OH\_AI\_ModelBuild()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context)
```

**描述**

从内存缓冲区加载并编译MindSpore Lite模型。

注意，同一个[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)对象仅能传递给[OH\_AI\_ModelBuild](capi-model-h.md#oh_ai_modelbuild)或者[OH\_AI\_ModelBuildFromFile](capi-model-h.md#oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const void \*model\_data | 内存中已经加载的模型数据地址。 |
| size\_t data\_size | 模型数据的长度。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) model\_context | 模型运行时的上下文环境，具体见 [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelBuildFromFile()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context)
```

**描述**

通过模型文件加载并编译MindSpore Lite模型。

注意，同一个[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)对象仅能传递给[OH\_AI\_ModelBuild](capi-model-h.md#oh_ai_modelbuild)或者[OH\_AI\_ModelBuildFromFile](capi-model-h.md#oh_ai_modelbuildfromfile)一次，如果多次调用该函数需要创建多个不同的[OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const char \*model\_path | 模型文件路径。字符串长度限制跟随文件系统。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) model\_context | 模型运行时的上下文环境，具体见 [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelResize()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelResize(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_ShapeInfo *shape_infos, size_t shape_info_num)
```

**描述**

调整已编译模型的输入形状。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [const OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) inputs | 模型输入对应的张量数组结构体。 |
| [OH\_AI\_ShapeInfo](capi-mindspore-oh-ai-shapeinfo.md) \*shape\_infos | 输入形状信息数组，按模型输入顺序排列的由形状信息组成的数组，模型会按顺序依次调整张量形状。 |
| size\_t shape\_info\_num | 形状信息数组的长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelPredict()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelPredict(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs,OH_AI_TensorHandleArray *outputs, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after)
```

**描述**

执行模型推理。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [const OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) inputs | 模型输入对应的张量数组结构体。 |
| [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) \*outputs | 模型输出对应的张量数组结构体的指针。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) before | 模型推理前执行的回调函数。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) after | 模型推理后执行的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelGetInputs()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetInputs(const OH_AI_ModelHandle model)
```

**描述**

获取模型的输入张量数组结构体。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) | 模型输入对应的张量数组结构体。 |

### OH\_AI\_ModelGetOutputs()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetOutputs(const OH_AI_ModelHandle model)
```

**描述**

获取模型的输出张量数组结构体。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) | 模型输出对应的张量数组结构体。 |

### OH\_AI\_ModelGetInputByTensorName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetInputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name)
```

**描述**

通过张量名获取模型的输入张量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const char \*tensor\_name | 张量名称。字符串长度跟随系统限制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) | tensor\_name所对应的输入张量的张量指针，如果输入中没有该张量则返回空。 |

### OH\_AI\_ModelGetOutputByTensorName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandle OH_AI_ModelGetOutputByTensorName(const OH_AI_ModelHandle model, const char *tensor_name)
```

**描述**

通过张量名获取模型的输出张量。

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const char \*tensor\_name | 张量名称。字符串长度跟随系统限制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandle](capi-mindspore-oh-ai-tensorhandle.md) | tensor\_name所对应的输出张量的张量指针，如果输出中没有该张量则返回空。 |

### OH\_AI\_TrainCfgCreate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TrainCfgHandle OH_AI_TrainCfgCreate()
```

**描述**

创建训练配置对象指针，仅用于端侧训练。

**起始版本：** 11

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) | 训练配置对象指针。 |

### OH\_AI\_TrainCfgDestroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TrainCfgDestroy(OH_AI_TrainCfgHandle *train_cfg)
```

**描述**

销毁训练配置对象指针，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) \*train\_cfg | 训练配置对象指针。 |

### OH\_AI\_TrainCfgGetLossName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API char **OH_AI_TrainCfgGetLossName(OH_AI_TrainCfgHandle train_cfg, size_t *num)
```

**描述**

获取损失函数的名称列表，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |
| size\_t \*num | 损失函数数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API char \*\* | 损失函数的名称列表。 |

### OH\_AI\_TrainCfgSetLossName()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TrainCfgSetLossName(OH_AI_TrainCfgHandle train_cfg, const char **loss_name, size_t num)
```

**描述**

设置损失函数的名称列表，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |
| const char \*\*loss\_name | 损失函数的名称列表。 |
| size\_t num | 损失函数数量。 |

### OH\_AI\_TrainCfgGetOptimizationLevel()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_OptimizationLevel OH_AI_TrainCfgGetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg)
```

**描述**

获取训练配置的优化等级，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_OptimizationLevel](capi-types-h.md#oh_ai_optimizationlevel) | 优化等级。 |

### OH\_AI\_TrainCfgSetOptimizationLevel()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API void OH_AI_TrainCfgSetOptimizationLevel(OH_AI_TrainCfgHandle train_cfg, OH_AI_OptimizationLevel level)
```

**描述**

设置训练配置的优化等级，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |
| [OH\_AI\_OptimizationLevel](capi-types-h.md#oh_ai_optimizationlevel) level | 优化等级。 |

### OH\_AI\_TrainModelBuild()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_TrainModelBuild(OH_AI_ModelHandle model, const void *model_data, size_t data_size,OH_AI_ModelType model_type, const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg)
```

**描述**

从内存缓冲区加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const void \*model\_data | 指向存储读入模型文件缓冲区的指针。 |
| size\_t data\_size | 缓冲区大小。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) model\_context | 模型运行时的上下文环境，具体见 [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| const [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_TrainModelBuildFromFile()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_TrainModelBuildFromFile(OH_AI_ModelHandle model, const char *model_path,OH_AI_ModelType model_type,const OH_AI_ContextHandle model_context,const OH_AI_TrainCfgHandle train_cfg)
```

**描述**

根据路径读取加载训练模型，并将模型编译至可在Device上运行的状态，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const char \*model\_path | 模型文件路径。字符串长度限制跟随文件系统。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md) model\_context | 模型运行时的上下文环境，具体见 [OH\_AI\_ContextHandle](capi-mindspore-oh-ai-contexthandle.md)。 |
| const [OH\_AI\_TrainCfgHandle](capi-mindspore-oh-ai-traincfghandle.md) train\_cfg | 训练配置对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_RunStep()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_RunStep(OH_AI_ModelHandle model, const OH_AI_KernelCallBack before,const OH_AI_KernelCallBack after)
```

**描述**

单步训练模型，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) before | 模型推理前执行的回调函数。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) after | 模型推理后执行的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelSetLearningRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelSetLearningRate(OH_AI_ModelHandle model, float learning_rate)
```

**描述**

设置训练的学习率，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| float learning\_rate | 学习率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelGetLearningRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API float OH_AI_ModelGetLearningRate(OH_AI_ModelHandle model)
```

**描述**

获取训练的学习率，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API float | 学习率，没有设置优化器时为0.0。 |

### OH\_AI\_ModelGetWeights()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_TensorHandleArray OH_AI_ModelGetWeights(OH_AI_ModelHandle model)
```

**描述**

获取模型的所有权重Tensors，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) | 模型的所有权重Tensor。 |

### OH\_AI\_ModelUpdateWeights()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelUpdateWeights(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray new_weights)
```

**描述**

更新模型的权重Tensor内容，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [const OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) new\_weights | 要更新的权重Tensor。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelGetTrainMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API bool OH_AI_ModelGetTrainMode(OH_AI_ModelHandle model)
```

**描述**

获取训练模式。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API bool | 表示是否是训练模式。true表示是训练模式，false表示不是训练模式。 |

### OH\_AI\_ModelSetTrainMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelSetTrainMode(OH_AI_ModelHandle model, bool train)
```

**描述**

设置训练模式，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| bool train | 是否为训练模式。true表示是训练模式，false表示不是训练模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelSetupVirtualBatch()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelSetupVirtualBatch(OH_AI_ModelHandle model, int virtual_batch_multiplier, float lr,float momentum)
```

**描述**

设置虚拟batch用于训练，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| int virtual\_batch\_multiplier | 虚拟batch乘法器，当设置值小于1时，表示禁用虚拟batch。长度跟随系统限制。 |
| float lr | 学习率，默认为-1.0f。 |
| float momentum | 动量，默认为-1.0f。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ExportModel()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ExportModel(OH_AI_ModelHandle model, OH_AI_ModelType model_type, const char *model_file,OH_AI_QuantizationType quantization_type, bool export_inference_only,char **output_tensor_name, size_t num)
```

**描述**

导出训练模型，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const char \*model\_file | 导出的模型文件路径。字符串长度限制跟随文件系统。 |
| [OH\_AI\_QuantizationType](capi-types-h.md#oh_ai_quantizationtype) quantization\_type | 量化类型。 |
| bool export\_inference\_only | 是否导出推理模型。true表示导出推理模型，false表示不导出推理模型。 |
| char \*\*output\_tensor\_name | 设置导出模型的输出Tensor，默认为空表示全量导出。 |
| size\_t num | 输出Tensor的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ExportModelBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ExportModelBuffer(OH_AI_ModelHandle model, OH_AI_ModelType model_type, void *model_data,size_t *data_size, OH_AI_QuantizationType quantization_type,bool export_inference_only, char **output_tensor_name, size_t num)
```

**描述**

导出训练模型内存缓存，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| void \*model\_data | 指向导出模型文件缓冲区的指针。 |
| size\_t \*data\_size | 缓冲区大小。 |
| [OH\_AI\_QuantizationType](capi-types-h.md#oh_ai_quantizationtype) quantization\_type | 量化类型。 |
| bool export\_inference\_only | 是否导出推理模型。true表示导出推理模型，false表示不导出推理模型。 |
| char \*\*output\_tensor\_name | 设置导出模型的输出Tensor，默认为空表示全量导出。 |
| size\_t num | 输出Tensor的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ExportWeightsCollaborateWithMicro()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ExportWeightsCollaborateWithMicro(OH_AI_ModelHandle model, OH_AI_ModelType model_type,const char *weight_file, bool is_inference,bool enable_fp16, char **changeable_weights_name,size_t num)
```

**描述**

导出模型权重，只能用于micro推理，仅用于端侧训练。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype) model\_type | 模型文件类型，具体见[OH\_AI\_ModelType](capi-types-h.md#oh_ai_modeltype)。 |
| const char \*weight\_file | 导出的权重文件路径。字符串长度限制跟随文件系统。 |
| bool is\_inference | 是否导出推理模型，当前只支持设置为true。 |
| bool enable\_fp16 | 浮点权重是否保存为float16格式。true表示保存为float16格式，false表示不保存为float16格式。 |
| char \*\*changeable\_weights\_name | shape可变的权重Tensor名称。 |
| size\_t num | shape可变的权重Tensor名称的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelLoadConfig()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelLoadConfig(OH_AI_ModelHandle model, const char *config_path);
```

**描述**

加载模型配置文件。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| const char \*config\_path | 配置文件路径。字符串长度限制跟随文件系统。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |

### OH\_AI\_ModelPredictWithConfig()

PhonePC/2in1TabletTVWearable

```
1. OH_AI_API OH_AI_Status OH_AI_ModelPredictWithConfig(OH_AI_ModelHandle model, const OH_AI_TensorHandleArray inputs, OH_AI_TensorHandleArray *outputs, const char *config, const OH_AI_KernelCallBack before, const OH_AI_KernelCallBack after)
```

**描述**

执行模型推理，支持每次推理设置不同推理参数。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AI\_ModelHandle](capi-mindspore-oh-ai-modelhandle.md) model | 模型对象指针。 |
| [const OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) inputs | 模型输入对应的张量数组结构体。 |
| [OH\_AI\_TensorHandleArray](capi-mindspore-oh-ai-tensorhandlearray.md) \*outputs | 模型输出对应的张量数组结构体的指针。 |
| const char \*config | 模型配置文件。字符串长度限制跟随文件系统。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) before | 模型推理前执行的回调函数。 |
| [const OH\_AI\_KernelCallBack](capi-model-h.md#oh_ai_kernelcallback) after | 模型推理后执行的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AI\_API [OH\_AI\_Status](capi-status-h.md#oh_ai_status) | 枚举类型的状态码[OH\_AI\_Status](capi-status-h.md#oh_ai_status)，若成功返回OH\_AI\_STATUS\_SUCCESS，失败则返回具体错误码。 |
