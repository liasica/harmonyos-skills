---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cann-kit-3
title: 使用CANN Kit加载ONNX模型转换后的OM模型报错
breadcrumb: FAQ > AI功能开发 > 计算平台 > CANN异构计算框架（CANN Kit） > 使用CANN Kit加载ONNX模型转换后的OM模型报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e837f0eade2412cc3a997de484f6b009b0c3d29dbc063a433c2135aad38531fc
---

## 问题现象

执行OMG命令，将ONNX模型转换为OM模型后，在HarmonyOS 5.0上使用CANN Kit加载该OM模型后报错。

部分报错信息如下：

```log
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     reshape_check_support.cc ReshapeCheckFunc(41)::check reshape dimInfo fail
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Reshape_4] type [Reshape] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     permute_check_support.cc IsSupport(21)::realdimCnt > 4
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Transpose_2] type [Permute] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     vector_op_checker.cc IsSupport(87)::input dimCnt 5 > 4
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Sigmoid_2] type [Activation] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     split_desc.cc InitAttr(38)::too much dim count = 5
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     split_check_support.cc IsSupport(35)::init desc fail
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Split_2] type [SplitV] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetInputOriginalDims(69)::binary op get original input dimCnt error, dimCnt is 5.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetNCHWDims(218)::get input original dims error.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     vector_op_checker.cc IsSupport(164)::init desc fail
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     mul_check_support.cc IsSupport(39)::wrong params
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Mul_10] type [Mul] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetInputOriginalDims(69)::binary op get original input dimCnt error, dimCnt is 5.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetNCHWDims(218)::get input original dims error.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     vector_op_checker.cc IsSupport(164)::init desc fail
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     pow_check_support.cc IsSupport(27)::wrong params
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Pow_2] type [Pow] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetInputOriginalDims(69)::binary op get original input dimCnt error, dimCnt is 5.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetNCHWDims(218)::get input original dims error.
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     vector_op_checker.cc IsSupport(164)::init desc fail
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     mul_check_support.cc IsSupport(39)::wrong params
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   W     fe_sub_stores_manager.cc CheckSupported(302)::"CheckSupported: the op name [/model.24/Mul_11] type [Mul] is not supported in npucl store [elementary_lib]"
08-04 16:19:13.996   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     binary_desc.cc GetInputOriginalDims(69)::binary op get original input dimCnt error, dimCnt is 5.
```

```log
08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     op_strategy.cc GetCompileInfo(39)::ConcatD SelectKernel failed!
08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     compile_task.cc GetStrategy(300)::GetCompileInfo failed!
08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     compile_task.cc Compile(175)::ConcatD /model.24/Concat_2 compileInfo is null.
08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     npu_graph_compiler.cc GenModelTaskDef(422)::"Call FusionTaskBuild failed."
08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     npu_graph_compiler.cc Compile(184)::"GenModelTaskDef failed"
08-04 16:19:13.940   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   E     model_compiler_util.cpp operator()(110)::"ModelCompiler::CompileGraph: subGraph SubGraph_2 compiled failed in cl NPUCL!"
08-04 16:19:13.940   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   E     general_model_compiler.cpp DoCompile(242)::"CompileGraph ge_default failed!"
08-04 16:19:13.943   58217-58217   C02150/com.hm.example/AI_INFRA  com.hm.example   E     general_model_compiler.cpp Compile(351)::"DoCompile(optimizerOptions, options, weightInfo, computeGraph, compiledModel) == SUCCESS" "false, return FAIL."
08-04 16:19:13.946   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   E     hcl_model_builder_impl.cpp BuildModel(568)::"BuildModelByHcl failed"
08-04 16:19:13.947   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   E     hcl_built_model_impl.cpp RestoreFromBuffer(259)::"restore model failed."
08-04 16:19:13.947   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   I     ai_timer_manager.cpp Initiate(114)::"create epollfd [82]"
08-04 16:19:13.947   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   I     ai_timer_manager.cpp Initiate(123)::"add pipe read end to epoll: success!"
08-04 16:19:13.947   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   I     ai_timer_manager.cpp CreateTimer(219)::"add timerfd [85] to epoll [82]"
08-04 16:19:13.947   58217-58217   C02150/com.hm.example/AI_INFRA  com.hm.example   E     hcl_built_model_itf.cpp CreateItfBuiltModel(50)::"clBuitModelImpl" "null, return FAIL."
08-04 16:19:13.947   58217-58217   C02154/com.hm.example/AI_FMK    com.hm.example   E     hiai_hdi_built_model.c HiaiHclBuiltModelRestore(83)::"HIAI_HCL_BuiltModel_Restore failed."
08-04 16:19:13.947   58217-58217   C02108/com.hm.example/HIAI      com.hm.example   E     [nodict] [invalidDomain]BuiltModelRestore failed
08-04 16:19:13.947   58217-58217   C02108/com.hm.example/HIAI      com.hm.example   E     [nodict] [invalidDomain]ret == OH_NN_SUCCESSfalse, return HIAI_COMPATIBILITY_INCOMPATIBLE.
```

## 背景知识

* ONNX（开放神经网络交换格式，Open Neural Network Exchange）是一种用于表示深度学习和机器学习模型的标准。ONNX提供标准的算子、方法和数据类型，用于表示计算图模型。算法模型可以表示为有向无环图，其中节点（Node）代表算子，边代表数据的流向。同时，ONNX也支持算子扩展，以支持自定义的计算方法。
* [CANN](../harmonyos-guides/cannkit-introduction.md)（Compute Architecture for Neural Networks）是华为面向AI推出的端云一致的异构计算架构。在HarmonyOS设备上，CANN Kit面向Kirin芯片平台为各种人工智能模型和算法提供统一的接入和运行环境。开发者的应用程序使用CANN Kit的API和开发者数据，在设备端实现智能推理、模型训练以及模型优化等操作，充分发挥设备的本地智能处理能力。
* [离线模型转换](../harmonyos-guides/cannkit-offline-model-conversion.md)：使用CANN Kit SDK时，可以预先使用OMG工具将Caffe、TensorFlow、ONNX、MindSpore模型转换为OM离线模型，移动端AI程序直接读取离线模型进行推理。模型转换成功后会在当前目录下生成对应的OM文件，转换失败则会在当前目录下生成check\_result.json文件。

## 问题定位

1. 第1段日志中的关键字“CheckSupported”表明当前是在检查模型中各算子在当前设备NPU上的支持情况，从日志以下关键信息可知：当前设备NPU不支持当前5维的算子。

   ```log
   permute_check_support.cc IsSupport(21)::realdimCnt > 4
   vector_op_checker.cc IsSupport(87)::input dimCnt 5 > 4
   split_desc.cc InitAttr(38)::too much dim count = 5
   ```
2. 第2段日志中的以下信息，表明NPU在进行分片时，ConcatD算子分片失败，最终不兼容报错。

   ```screen
   08-04 16:19:13.940   58217-58217   C02151/com.hm.example/AI_NPUCL  com.hm.example   E     op_strategy.cc GetCompileInfo(39)::ConcatD SelectKernel failed!
   ...
   08-04 16:19:13.947   58217-58217   C02108/com.hm.example/HIAI      com.hm.example   E     [nodict] [invalidDomain]ret == OH_NN_SUCCESSfalse, return HIAI_COMPATIBILITY_INCOMPATIBLE.
   ```

## 分析结论

当前模型中包含部分5维算子，在当前设备上不支持运行。

## 修改建议

将当前模型中的5维算子替换为4维及4维以下的模型算子。
