---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cann-kit-2
title: 使用OMG工具将ONNX模型转换为OM离线模型报错
breadcrumb: FAQ > AI功能开发 > 计算平台 > CANN异构计算框架（CANN Kit） > 使用OMG工具将ONNX模型转换为OM离线模型报错
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:a75d4d4aaf3d9b6a80650b198090ab914caee08d351a7c71582a5820f1719550
---

## 问题现象

使用OMG工具将ONNX模型转换为OM离线模型报错，命令执行部分日志如下：

```shell
W/AI_FMK (16075): ops_kernel_ store_manager.cpp DlopenComputeLibrary(41)::"dlopen so failed: libai_npucore_itf.so: cannot open shared object file:No such file or directory"
I/AI_FMK (16075): ops_kernel_store_manager.cpp DlCloseComputeLibrary(83)::"handle is null, not need to close library" 
I/AI_FMK (16075): model_util.cpp BuildOrigin2IRGraph(229)::"Modelutil::BuildOrigin2IRGraph from file" 
I/AI_FMK (16075): proto_util.cpp ReadBytesFromBinaryFile(192)::"Read size:16697653"
W/AI_FMK (16075): parser_factory.cpp LoadcustomOpLib(58)::"dlerror: libcustom_op.so: cannot open shared object file:No such file or directory 
E/AI_FMK(16075): onnx_graph_parser.cpp ParserGraph(875):Pre-check has errors."
E/AI_INFRA (16075): model_util.cpp ParseOriginBuffer2IrGraph(475)::"ret == SUCCESS" "false, return ret." 
E/AI_INFRA (16075): model_util.cpp ParseOriginONNX2IrGraph(541)::"ParseOriginBuffer2IrGraph(inputOptions, srcbuffer, irGraph, hiai::FrameworkType::ONNX) == SUCCESS" "false, return FAIL." 
E/AI_INFRA (16075): model_util.cpp BuildOrigin2IRGraph(233）::"ret == SUCCESS" "false,return ret 
E/AI_FMK (16075): omg.cpp GenerateIRModel(113)::"Failed to generator IR graph!."
E/OMG_TOOL (16075):command_util.cpp ProcessCommand(1226)::"OMG Generate execute failed!!"
E/OMG_TOOL (16075): main.cpp main(21)::"OMG generate offline model failed. Please see the log or pre-checking report for more details."
```

当前目录下check\_result.json文件的部分信息如下：

```json
  {"name": "/quant1/Constant", "result": "success", "type": "Constant" },
  {"name": "/quant1/Constant_1", "result": "success", "type": "Constant" },
  {"cause": [{ "code": 1, "message": "The type: QuantizeLinear is not supported." }], "name": "/quant1/QuantizeLinear", "result": "failed", "type": "QuantizeLinear"},
  {"name": "/backbone/conv1/Cast","result": "success", "type": "Cast" },
  {"name": "/backbone/conv1/Constant", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Constant_1", "result": "success", "type": "Constant" },
  {"cause": [{"code": 1, "message": "The type: DequantizeLinear is not supported." }], "name": "/backbone/conv1/DequantizeLinear", "result": "failed", "type":"DequantizeLinear" },
  {"name": "/backbone/conv1/Constant_2", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Constant_3","result": "success", "type": "Constant"},
  {"name": "/backbone/conv1/Constant_4", "result": "success", "type": "Constant"},
  {"cause": [{ "code": 1, "message": "The type: DequantizeLinear is not supported." }], "name": "/backbone/conv1/DequantizeLinear_1", "result": "failed", "type":"DequantizeLinear"},
  {"name": "/backbone/conv1/Constant_5", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/ConstantOfShape", "result": "success", "type": "ConstantOfShape" },
  {"name": "/backbone/conv1/Constant_6", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Constant_7", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Cast_1", "result": "success", "type": "Cast" },
  {"cause": [{ "code": 1, "message": "The type: DequantizeLinear is not supported." }], "name": "/backbone/conv1/DequantizeLinear_2", "result": "failed", "type":"DequantizeLinear" },
  {"name": "/backbone/conv1/Conv", "result": "success", "type": "Conv" },
  {"name": "/backbone/conv1/Constant_8", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Constant_9", "result": "success", "type": "Constant" },
  {"cause": [{ "code": 1, "message": "The type: QuantizeLinear is not supported." }], "name": "/backbone/conv1/QuantizeLinear", "result": "failed", "type":"QuantizeLinear"},
  {"name": "/backbone/act1/Cast", "result": "success", "type": "Cast" },
  {"name": "/backbone/act1/Constant", "result": "success", "type": "Constant" },
  {"name": "/backbone/act1/Constant_1", "result": "success", "type": "Constant"},
  {"cause": [{ "code": 1, "message": "The type: DequantizeLinear is not supported." }], "name": "/backbone/act1/DequantizeLinear", "result": "failed", "type":"DequantizeLinear" },
  {"name": "/backbone/act1/LeakyRelu", "result": "success", "type": "LeakyRelu" },
  {"name": "/backbone/conv1/Constant_2", "result": "success", "type": "Constant" },
  {"name": "/backbone/conv1/Constant_3","result": "success", "type": "Constant"}
```

## 背景知识

* ONNX（开放神经网络交换格式，Open Neural Network Exchange）是一种用于表示深度学习和机器学习模型的标准。ONNX提供标准的算子、方法和数据类型，用于表示计算图模型。算法模型可以表示为有向无环图，其中节点（Node）代表算子，边代表数据的流向。同时，ONNX也支持算子扩展，以支持自定义的计算方法。
* [CANN](../harmonyos-guides/cannkit-introduction.md)（Compute Architecture for Neural Networks）是华为面向AI推出的端云一致的异构计算架构。在HarmonyOS设备上，CANN Kit面向Kirin芯片平台为各种人工智能模型和算法提供统一的接入和运行环境。开发者的应用程序使用CANN Kit的API和开发者数据，在设备端实现智能推理、模型训练以及模型优化等操作，充分发挥设备的本地智能处理能力。
* [模型轻量化](../harmonyos-guides/cannkit-lightweight-tool-instructions.md)：HarmonyOS 5.0提供一款集模型压缩算法和网络结构搜索算法于一体的自动模型轻量化工具，针对NPU架构对深度神经网络模型进行深度的模型优化，可以帮助开发者自动地完成模型轻量化以及网络结构的生成任务。目前支持无训练模式、插件式量化模式、大语言模型低位量化和网络结构搜索。
* [离线模型转换](../harmonyos-guides/cannkit-offline-model-conversion.md)：使用CANN Kit SDK时，可以预先使用OMG工具将Caffe、TensorFlow、ONNX、MindSpore模型转换为OM离线模型，移动端AI程序直接读取离线模型进行推理。模型转换成功后会在当前目录下生成对应的OM文件，转换失败则会在当前目录下生成check\_result.json文件。

## 问题定位

1. 根据以下执行日志，可得知OMG命令转换离线模型失败，更多的信息需要查看预检查报告，即check\_result.json文件信息。

   ```shell
   E/OMG_TOOL (16075): main.cpp main(21)::"OMG generate offline model failed. Please see the log or pre-checking report for more details."
   ```
2. 根据当前转换目录下生成的check\_result.json文件内的以下报错信息可知，该ONNX模型使用了QuantizeLinear和DequantizeLinear这2个ONNX的量化算子，当前HarmonyOS 5.0的CANN Kit仅支持官网提供的量化方案：[模型轻量化](../harmonyos-guides/cannkit-lightweight-tool-instructions.md)。

   ```json
   {"cause":[{"code":1,"message":"The type: QuantizeLinear is not supported."}],"name":"/quant1/QuantizeLinear","result":"failed","type":"QuantizeLinear"}
   ···
   {"cause":[{"code":1,"message":"The type: DequantizeLinear is not supported."}],"name":"/backbone/conv1/DequantizeLinear_1","result":"failed","type":"DequantizeLinear"}
   ```

## 分析结论

该模型使用了HarmonyOS 5.0当前不支持的ONNX量化算子，导致模型转换时报错。

## 修改建议

使用HarmonyOS 5.0提供的[轻量化工具](../harmonyos-guides/cannkit-lightweight-tool-instructions.md)对该ONNX模型进行模型轻量化优化之后，再根据官方文档进行[模型转换](../harmonyos-guides/cannkit-model-conversion.md)。

目前支持ONNX的轻量化方式为[无训练量化](../harmonyos-guides/cannkit-no-training-and-quantization.md#onnx模型无训练量化)。可以参考[模型轻量化示例](../harmonyos-guides/cannkit-examples.md)。
