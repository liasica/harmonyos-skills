---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cann-kit-1
title: CANN Kit离线模型转换工具使用报错
breadcrumb: FAQ > AI功能开发 > 计算平台 > CANN异构计算框架（CANN Kit） > CANN Kit离线模型转换工具使用报错
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:39+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:53733eae691da8513d90b24eb5573dcf9b9a7e93e02c52464d4e61ccd03753cb
---

## 问题现象

使用CANN Kit提供的OMG模型转换工具进行转换时，执行如下命令会产生报错。

```shell
omg --model XXX.tflite --framework 3 --output ./mobilenet_v2 --input_shape input_1:-1,224.1,224,0 --out_nodes predictions/Softmax
```

## 背景知识

CANN Kit人工智能框架将人工智能能力集成到HarmonyOS应用中。为了使移动端AI程序，能够直接使用PC端训练好的AI模型进行推理，可以使用CANN Kit的OMG离线转换工具将**Caffe、TensorFlow、ONNX、MindSpore**模型转换为OM离线模型，以供移动端AI程序使用。下面给出TensorFlow的[模型转换示例](../harmonyos-guides/cannkit-model-conversion-example.md)：

```shell
./omg --model mobilenet_v2_1.0_224_frozen.pb --framework 3 --output ./mobilenet_v2 --input_shape "input:1,224,224,3" --out_nodes "MobilenetV2/Predictions/Reshape_1:0"
```

当看到OMG generate offline model success时，则说明转换成功，会在当前目录下生成mobilenet\_v2.om文件。点击[OMG参数](../harmonyos-guides/cannkit-overall-parameter.md)可查阅上述命令中的参数详情。

## 问题定位

问题描述中的转换命令有三点错误，给出的解决方案如下：

1. XXX.tflite模型虽然是TensorFlow框架的模型，但是官方目前只支持TensorFlow2.0的XXX.pb格式的模型。如果一定要将XXX.tflite转为XXX.om模型，可以先将XXX.tflite模型转为官方支持的框架模型，再转为XXX.om模型。
2. 模型的输入shape:"-1,224.1,224,0"只能是正整数，-1，224.1和0是不符合要求的，并且还要保证--input\_shape的输入参数与模型输入的shape一致兼容。
3. 单输出节点的参数格式，应为--out\_nodes predictions/Softmax:0。

更多OMG参数说明，请参考[OMG参数](../harmonyos-guides/cannkit-overall-parameter.md)。

## 分析结论

在使用OMG离线模型转换工具时，需确认原AI模型官方是否支持，如果官方不支持，可以先将模型转换为官方支持的模型，再使用OMG离线模型转换工具。此外，还需要注意转换命令其它参数是否合理。

## 修改建议

针对当前无法直接转换的模型（如TensorFlow Lite），可以先将模型转换为官方支持的框架模型，再转换为OM模型部署到端侧应用中。

## 常见FAQ

Q：Mindspore lite推理框架使用CPU进行推理，一会十几毫秒一会三十几毫秒，为什么耗时不稳定？

A：CPU推理耗时不稳定，建议设置绑核，OH\_AI\_ContextSetThreadAffinityMode(context\_handler, 1)，有效值为0-2，0为默认不绑核，1为绑大核，2为绑中核。

Q：Mindspore lite推理框架除了使用CPU推理，能不能用GPU或者NPU或者NNRT进行推理？

A：当前HarmonyOSNext支持CPU和NNRT进行推理。

Q：使用OMG转换工具提示没有OMG权限。

A：OMG工具位于Tools下载的tools/tools\_omg下，使用管理员权限运行，sudo ./omg。

Q：执行命令：./omg --model=./add\_custom.onnx --framework=5 --output=./AddCustom --target=omc报错：dlopen so failed: libai\_npucore\_itf.so: cannot open shared object file: No such file or directory，如何修改？

A：此问题有多种原因：

1. 由于DDK\_tools安装包更新了后Demo没更新，所以可以使用如下命令执行：./omg --model=./add\_custom.onnx --framework=5 --output=./AddCustom --target=omc --platform=kirin9020。
2. libai\_npucore\_itf.so虽然已经编译成功，但是未部署到正确的路径，需要确保.so文件位于系统动态库搜索路径（如/usr/lib）或自定义路径。

Q：离线模型转换是否对环境有要求，比如系统版本和python版本是否有限制？

A：有要求，请按照[系统要求](../harmonyos-guides/cannkit-lightweight-tool-overview.md#系统要求)搭建环境。

Q：模型转换工具tools\_omg报错：E/AI\_FMK (2834577): onnx\_graph\_parser.cpp ParserGraph(785)::"Pre-check has errors."。

A：报错显示找不到部分so文件，包括librl\_search.so和libcustom\_op.so，初步分析是由于部分算子不在预设支持列表中导致，请排查目录下的check\_result.json文件，这个文件里有报错算子。

**说明** 

STFT算子当前需要通过[自定义算子开发](../harmonyos-guides/cannkit-custom-operator-development.md)进行调优和部署。

Q：纯CNN模型（去掉STFT层）转换显示最终成功，但是实际上推理时无法加载，而且netron也打不开，显示错误：Duplicate value 'stft\_features:0'。

A：原始ONNX模型有冗余小算子，通过onnxsim简化后消除来解决。

Q：调用OH\_AI\_ContextSetThreadNum设置线程数为2，同时调用OH\_AI\_ContextSetThreadAffinityMode设置绑大核（值为1）后，在某些设备（如畅享70x、畅享90标准版）上模型推理耗时从几十毫秒增加到好几秒，如何解决？

A：出现该问题时，可以先验证仅调用OH\_AI\_ContextSetThreadNum设置线程数2，不调用OH\_AI\_ContextSetThreadAffinityMode时的耗时波动情况。如果耗时仍然异常，可以尝试将线程数修改为1，或者将亲核性设置为0（默认不绑核），耗时即可恢复正常的几十毫秒。
