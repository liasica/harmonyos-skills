---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-mindspore-lite-1
title: MindSpore Lite Kit使用三方框架模型的方法
breadcrumb: FAQ > AI功能开发 > 计算平台 > 昇思推理框架（MindSpore Lite） > MindSpore Lite Kit使用三方框架模型的方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4db6f9d8687d512ffb5b693869f184e11185b8bea893859b24d13c9370d350ba
---

## 问题现象

MindSpore Lite使用.ms格式模型进行推理。当前大部分开发者使用了不同的第三方框架,比如TensorFlow、TensorFlow Lite、Caffe、ONNX等。为了保持开发者的模型一致性，MindSpore Lite如何使用这些三方框架的模型？

## 背景知识

[MindSpore Lite](../harmonyos-guides/mindspore-lite-kit-introduction.md)是HarmonyOS内置的轻量化AI引擎，目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用。[开发流程](../harmonyos-guides/mindspore-lite-kit-introduction.md#开发流程)：MindSpore Lite分为两个阶段：

1. 模型转换：

   MindSpore Lite使用.ms格式模型进行推理。

   对于第三方框架模型，比如TensorFlow、TensorFlow Lite、Caffe、ONNX等，可以使用MindSpore Lite提供的模型转换工具转换为.ms模型，使用方法可参考[使用MindSpore Lite进行模型转换](../harmonyos-guides/mindspore-lite-converter-guidelines.md)。

   更多关于MindSpore Lite模型转换的使用，可参考其官网介绍[推理模型离线转换](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html)，其中有[Linux环境准备](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#linux环境使用说明)和[Windows环境准备](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#windows环境使用说明)的详细说明。
2. [模型部署](../harmonyos-guides/deployment.md)：
   * [使用MindSpore Lite进行模型推理 (C/C++)](../harmonyos-guides/mindspore-lite-guidelines.md)
   * [使用MindSpore Lite进行端侧训练 (C/C++)](../harmonyos-guides/mindspore-lite-train-guidelines.md)
3. [开发方式](../harmonyos-guides/mindspore-lite-kit-introduction.md#开发方式)：

   MindSpore Lite已作为系统部件在HarmonyOS标准系统内置，基于MindSpore Lite开发AI应用的开发方式有：
   * 方式一：[使用MindSpore Lite实现图像分类（ArkTS）](../harmonyos-guides/mindspore-guidelines-based-js.md)。开发者直接在UI代码中调用MindSpore Lite ArkTS API加载模型并进行AI模型推理，此方式可快速验证效果。
   * 方式二：[使用MindSpore Lite实现图像分类（C/C++）](../harmonyos-guides/mindspore-guidelines-based-native.md)。开发者将算法模型和调用MindSpore Lite Native API的代码封装成动态库，并通过N-API封装成ArkTS接口，供UI调用。

## 解决方案

1. 构建模型：建立用于特定目标识别的推理模型，此步骤可以根据实际的业务场景需要由开发者自行构建。

   场景1：目标识别，识别摄像头中人物的手势，如✌或者✋。

   过程：可以使用YOLOv5实现针对特定目标，如手部关键点（即手势）的检测。构建相应的数据集和训练代码，训练并生成相应的推理模型。

   特定目标的检测方法可以通过建立推理模型并使用大量数据进行训练来提高识别准确度。

   MindSpore Lite的模型转换工具目前支持使用的第三方框架有MINDIR、CAFFE、TFLITE、TF、ONNX、PYTORCH、MSLITE。
2. 模型转换，通过MindSporeLite的converter工具进行模型转换：
   1. 工具的下载和环境准备，请根据不同的操作系统进行设置：[Linux环境准备](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#环境准备)，[Windows环境准备](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#环境准备-1)。
   2. 通过命令进行模型转换，MindSpore Lite模型转换工具提供了多种参数设置，用户可根据需要来选择使用，详细参见[参数说明](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#参数说明)。
   3. 使用示例说明，以Caffe模型LeNet为例，执行转换命令（Linux）./converter\_lite --fmk=CAFFE --modelFile=lenet.prototxt --weightFile=lenet.caffemodel --outputFile=lenet更多[示例参考](https://www.mindspore.cn/lite/docs/zh-CN/r2.0/use/converter_tool.html#使用示例)。
3. 模型选择：将需要使用的模型.ms文件放置在entry/src/main/resources/rawfile工程目录下。
4. 在[Index](https://gitee.com/harmonyos_samples/MindSporeLiteArkTS/blob/master/entry/src/main/ets/pages/Index.ets)页面的Process方法中进行模型调用，过程如下：
   1. 输入数据的处理：此处以获取相册图片为例，调用@ohos.file.picker实现相册图片文件的选择。
   2. 根据模型的输入尺寸，调用@ohos.multimedia.image （实现图片处理）、@ohos.file.fs（实现基础文件操作）API对选择图片进行裁剪、获取图片buffer数据，并进行标准化处理。
   3. 引入MindSporeLite能力：工程默认设备定义的能力集可能不包含MindSporeLite，需在DevEco Studio工程的entry/src/main目录下，手动创建[syscap.json](https://gitee.com/harmonyos_samples/MindSporeLiteArkTS/blob/master/entry/src/main/syscap.json)文件。
5. 通过[modelPredict](https://gitee.com/harmonyos_samples/MindSporeLiteArkTS/blob/master/entry/src/main/ets/model/Model.ets)函数调用@ohos.ai.mindSporeLite实现端侧推理的过程如下：
   1. 创建上下文，设置线程数、设备类型等参数。
   2. 从内存加载模型。
   3. 设置输入数据。
   4. 执行推理。

完整示例代码参考：[基于MindSporeLite接口实现图像分类](https://gitee.com/harmonyos_samples/MindSporeLiteArkTS/tree/master)。

## 常见FAQ

Q：主要应用场景有哪些？

A：图像分类，如给定一张图像（猫、狗、飞机、汽车等），判断图像所属的类别。目标检测，使用预置目标检测模型，检测标识摄像头输入帧中的对象（手势、燃气表等）并添加标签。图像分割，可用于检测目标在图片中的位置。

Q：MindSpore Lite推理框架使用NNRT设备进行推理时，为什么出现Build失败？

A：在使用NNRT推理时，由于设置parallelEnable=true导致Build失败。

Q：官方样例库里的模型mobilenetv2.ms跑NNRT失败？如果将三方框架的模型转成ms模型，能跑NNRT吗？

A：官方样例库里的模型mobilenetv2.ms不支持跑NNRT。三方框架的模型包转成ms模型之后是否支持NNRT与模型里实际用到的算子有关。

Q：实时识别手势（如✌或✋）？

A：可以参考解决方案，先构建推理模型，再通过模型转换，模型部署，模型调用来实现。

Q：means和stds代表什么？

A：means和stds是用于图像预处理中的归一化（Normalization）参数，means：图像每个通道的均值（Mean），stds：图像每个通道的标准差（Standard Deviation），数值是在ImageNet数据集上计算出的统计平均值和标准差。

Q：目前有ONNX库可以直接使用吗？

A：目前三方中心仓已有一个ONNX可以使用：[sherpa\_onnx](https://ohpm.openharmony.cn/#/cn/detail/sherpa_onnx)。

Q：MindSpore Lite使用的模型中是否支持控制流算子？

A：目前MindSpore Lite并不支持控制流算子，建议开发者修改成无控制流算子的模型。

## 总结

* MindSpore Lite提供离线转换模型功能的工具，支持多种类型的模型转换，转换后的模型可用于推理。目前支持的输入模型类型有：MindSpore、TensorFlow Lite、Caffe、TensorFlow、ONNX和PyTorch。
* 可根据业务场景实现推理模型，并部署到端侧调用。如，针对特定目标的检测（手势、燃气表设备等）。
* 需要自己开发并使用数据集进行模型的开发和训练。
