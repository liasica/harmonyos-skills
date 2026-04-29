---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-lite-kit-introduction
title: MindSpore Lite Kit简介
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > MindSpore Lite Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:44+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6715ac5f024503e9fe39c31348b2770393ae9f38a9c277cd922df7945f006aec
---

## 使用场景

MindSpore Lite是HarmonyOS内置的轻量化AI引擎，面向全场景构建支持多处理器架构的开放AI架构，使能全场景智能应用，为开发者提供端到端的解决方案，为算法工程师和数据科学家提供开发友好、运行高效、部署灵活的体验，帮助人工智能软硬件应用生态繁荣发展。

目前已经在图像分类、目标识别、人脸识别、文字识别等应用中广泛使用。常用场景如：

* 图像分类：最基础的计算机视觉应用，属于有监督学习类别，如给定一张图像（猫、狗、飞机、汽车等等），判断图像所属的类别。
* 目标检测：您可以使用预置目标检测模型，检测标识摄像头输入帧中的对象并添加标签，并用边框标识出来。
* 图像分割：图像分割可用于检测目标在图片中的位置或者图片中某一像素是属于何种对象的。

## 约束与限制

* 本Kit适用于Phone、Tablet、PC/2in1、TV设备，支持使用模拟器运行调试。

## 亮点/优势

MindSpore Lite提供面向不同硬件设备的AI模型推理能力，使用MindSpore Lite的优势如下：

* 更优性能：高效的内核算法和汇编级优化，支持CPU、NNRt专用芯片高性能推理，最大化发挥硬件算力，最小化推理时延和功耗。
* 轻量化：提供超轻量的解决方案，支持模型量化压缩，模型更小跑得更快，使能AI模型极限环境下的部署执行。
* 全场景支持：支持多种操作系统以及嵌入式系统，适配多种软硬件智能设备上的AI应用。
* 高效部署：支持MindSpore/TensorFlow Lite/Caffe/Onnx模型，提供模型压缩、数据处理等能力，统一训练和推理IR，方便用户快速部署。

## 开发流程

**图 1** 使用MindSpore Lite进行模型推理的开发流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/9-LfiwEmTBeUcffIKy4www/zh-cn_image_0000002558765846.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T054343Z&HW-CC-Expire=86400&HW-CC-Sign=E3F0CFF504D37164D908A876B7ACE1D32EE71EE78B789A792B4FFDC145303CEF)

MindSpore Lite开发流程分为两个阶段：

* 模型转换

  MindSpore Lite使用.ms格式模型进行推理。对于第三方框架模型，比如 TensorFlow、TensorFlow Lite、Caffe、ONNX等，可以使用MindSpore Lite提供的模型转换工具转换为.ms模型，使用方法可参考[推理模型转换](mindspore-lite-converter-guidelines.md)。
* 模型部署

  调用MindSpore Lite运行时接口，实现模型推理/训练，大致步骤如下：

  1. 创建推理/训练上下文，包括指定推理/训练硬件、设置线程数等。
  2. 加载.ms模型文件。
  3. 设置模型输入数据。
  4. 执行推理/训练，读取输出。

## 开发方式

MindSpore Lite已作为系统部件在HarmonyOS标准系统内置，基于MindSpore Lite开发AI应用的开发方式有：

* 方式一：[使用MindSpore Lite ArkTS API开发AI应用](mindspore-guidelines-based-js.md)。开发者直接在UI代码中调用 MindSpore Lite ArkTS API 加载模型并进行AI模型推理，此方式可快速验证效果。
* 方式二：[使用MindSpore Lite Native API开发AI应用](mindspore-guidelines-based-native.md)。开发者将算法模型和调用 MindSpore Lite Native API 的代码封装成动态库，并通过N-API封装成ArkTS接口，供UI调用。

## 与其他Kit的关系

HarmonyOS AI开放层次由上层到底层分别为：

* MindSpore Lite Kit：HarmonyOS内置的轻量化AI引擎，提供统一推理接口和多后端硬件加速能力，使能手机、PC/2in1、TV等全场景智能应用。
* [Neural Network Runtime Kit](neural-network-runtime-kit-introduction.md)：面向AI领域的跨芯片推理计算运行时，作为中间桥梁连通上层AI推理框架和底层加速芯片，实现AI模型的跨芯片推理计算。
* [CANN Kit](cannkit-introduction.md)：海思AI硬件统一开放计算架构，支持 Ascend C NPU自定义编程、端云协同复用。擅长偏重载AI计算、需深度优化性能功耗场景。

Neural Network Runtime Kit可支持系统内置的MindSpore Lite推理框架（MindSpore Lite Kit），MindSpore Lite Kit作为已开放了配置NNRt的Native接口。

MindSpore Lite Kit与NNRt接口对接时无需构图，两者共享同一份模型图格式（MindIR），因此使用MindSpore Lite Kit在NNRt上加载模型比其他AI推理框架更高效。此外，MindSpore Lite还支持通用硬件CPU/GPU与NNRt AI加速硬件之间的模型异构推理功能。

CANN Kit作为麒麟平台的后端接入Neural Network Runtime Kit，支撑Neural Network Runtime Kit于麒麟平台的AI计算能力。CANN Kit构建在底层的硬件驱动和优化的计算库之上，与云侧昇腾芯片统一支持AscendC自定义算子编程语言和相关工具链，是HarmonyOS智能生态的重要基石，为众多领域的智能应用提供核心支撑。
