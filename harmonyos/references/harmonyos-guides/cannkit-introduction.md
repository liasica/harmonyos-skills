---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-introduction
title: CANN Kit简介
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f763b712df2a57e1df133ae7f5ea693d230bc72956a115149acaa88ff5e2a6b7
---

CANN（Compute Architecture for Neural Networks）是华为面向AI推出的端云一致的异构计算架构。在HarmonyOS设备上，CANN Kit面向Kirin芯片平台为各种人工智能模型和算法提供统一的接入和运行环境。开发者的应用程序使用CANN Kit的API和开发者数据，在设备端实现智能推理、模型训练以及模型优化等操作，充分发挥设备的本地智能处理能力。

模型是将人工智能算法应用于大量训练数据后得到的结果。开发者可以使用模型依据新的输入数据进行智能推理和预测。模型能够完成许多用常规代码实现起来难度较大或效率较低的复杂任务。例如，你可以训练模型对图像进行语义分割，识别图像中的不同物体类别并精确划分其区域或者对语音数据进行处理，实现语音唤醒、语音识别以及语音合成等功能。

开发者可以使用华为昇腾提供的[CANN](https://www.hiascend.com/software/cann)开发平台进行模型的构建和训练。将训练好的模型转换为适合CANN Kit的模型格式，以便集成到开发者的应用中。此外，开发者也可以基于其他开源或自研的机器学习框架进行模型开发，然后借助CANN Kit提供的工具链将模型适配到HarmonyOS生态中。

CANN Kit通过协同调度设备的NPU（神经网络处理单元）、CPU等硬件资源，实现高效的设备端智能计算性能优化。在提升计算效率的同时，尽可能降低对内存和电量的消耗。在设备端直接运行模型，减少了对网络的依赖，不仅保障了开发者数据的隐私安全，还使应用程序在各种网络环境下都能保持快速响应，为开发者提供流畅的智能交互体验。

CANN Kit构建在底层的硬件驱动和优化的计算库之上，面向华为自研的达芬奇架构NPU的计算核心，与云侧昇腾芯片统一支持AscendC自定义算子编程语言和相关工具链，确保开发者面向NPU的开发优化可以一次开发、多端运行。

CANN Kit是HarmonyOS智能生态的重要基石，为众多领域的智能应用提供核心支撑。例如：支持图像视觉相关的Core Vision Kit、用于自然语言处理的Natural Language Kit等AI计算加速能力，同时支持HarmonyOS的MindSpore Lite Kit、Neural Network Runtime Kit，三方的MNN、PaddleLite等推理框架能力，共同打造丰富的智能应用场景。

## 场景

### 模型优化

* Model Zoo：模型库和工具包，为开发者提供海量模型结构及算子，助力开发者选择硬件能效更优的模型结构。
* 模型轻量化：优化模型大小，降低计算量，降低空间占用与算力需求。

### 模型转换

* 离线模型转换：CANN Kit通过OMG工具可以把神经网络各种算子，比如卷积、池化、激活、全连接等离线编译成硬件专用的AI指令序列，同时将数据和权重重新排布，指令与数据融合在一起生成离线模型。
* AIPP（AI Pre-Process）：AI预处理，支持输入数据硬件预处理，包括图像裁剪、通道交换、色域转换、图片缩放、数据类型转换、旋转和图片补边。由于AIPP硬件专用，可以获得更好的推理性能收益。通过模型转化配置文件生成动静态AIPP模型，及完成AIPP功能参数设置。
* 可变data\_type：用于模型输入输出数据类型多样性的场景，无需修改训练好的模型，在使用OMG工具进行[模型转换](cannkit-overall-parameter.md)时，通过指定输入、输出数据类型使得同一个模型适用于不同输入输出的场景。

### 端侧部署

* 模型推理：主要包含模型编译和推理，是其它端侧部署的基础场景。
* AIPP部署：端侧AIPP部署主要为动态AIPP功能提供支持，即同一动态AIPP模型可以支持不同输入且使能不同AIPP功能的推理场景。
* 异构：CANN Kit能够自动识别运行环境上的计算能力，对神经网络进行自适应的子图拆分和设备协同调度能力。能够支持NPU、CPU的计算加速，在没有NPU的情况下，也能通过CPU提供更广泛的硬件适应能力。
* 内存零拷贝：将存放数据的ION内存封装为输入输出张量，直接进行推理，不需要进行输入张量和输出张量的数据拷贝，以便节省内存以及推理时间。
* 深度融合：模型推理时结合硬件深度融合，减少对DDR的访问，提升能效比。

### 单算子

在三方应用框架加载其原始模型阶段，根据算子的输入、输出、权重信息等参数创建相应的单算子执行器对象并完成加载。三方应用框架执行模型推理时，在其中算子计算过程中调用单算子推理接口，完成算子计算。

### AscendC自定义算子开发

AscendC 是CANN Kit针对算子开发场景推出的编程语言，支持C和C++标准规范，最大化匹配开发者开发习惯；通过多层接口抽象、自动并行计算、孪生调试等关键技术，提高算子开发效率，助力AI开发者低成本完成算子开发和模型调优部署。

## 基本概念

在进行CANN Kit开发前，开发者应了解以下基本概念：

* NPU

  NPU（Neural-network Processing Unit，神经网络处理器）是一种专门用于进行深度学习计算的芯片。
* 算子

  深度学习算法由一个个计算单元组成，我们称这些计算单元为算子（Operator，简称OP）。
* 异构计算

  异构计算（Heterogeneous Computing），又译异质运算，主要是指使用不同类型指令集或体系架构的计算单元组成系统的计算方式。CANN Kit使用到的计算单元类别包括CPU、NPU等。
* AIPP

  AIPP是针对AI推理的输入数据进行预处理的模块。CANN Kit模型推理一般需要标准化输入数据格式，而一般模型推理场景数据是一张图片，在格式上存在多样性，AIPP可实现不同格式图片数据到NPU标准输入数据格式的转换。对已训练好的模型，不用重新训练匹配推理计算平台需要的数据格式，而只通过AIPP参数配置或者在软件上调用AIPP接口即可完成适配。由于AIPP硬件专用，可以获得较好的推理性能收益，又可以称为“硬件图像预处理”。
* 量化蒸馏

  是一种结合模型压缩技术的方法，旨在通过在量化过程中引入教师模型的知识来指导学生模型的学习，从而减少量化带来的精度损失。这种方法的核心目标是在降低模型大小和计算复杂度的同时，尽可能保留模型的性能。

## 约束与限制

本Kit仅适用于带有Kirin NPU的Phone、Tablet、PC/2in1、TV设备。从5.1.0(18)版本开始，新增支持TV设备。

## 模拟器支持情况

本kit暂不支持模拟器。

## 与相关Kit的关系

HarmonyOS AI开放层次由上层到底层分别为：

* MindSpore Lite Kit：HarmonyOS内置的轻量化AI引擎，提供统一推理接口和多后端硬件加速能力，使能手机、PC/2in1、TV等全场景智能应用。
* Neural Network Runtime Kit：面向AI领域的跨芯片推理计算运行时，作为中间桥梁连通上层AI推理框架和底层加速芯片，实现AI模型的跨芯片推理计算。
* CANN Kit：海思AI硬件统一开放计算架构，支持AscendC NPU自定义编程、端云协同复用，擅长偏重载AI计算、需深度优化性能功耗场景。

Neural Network Runtime Kit可支持系统内置的MindSpore Lite推理框架（MindSpore Lite Kit），MindSpore Lite Kit已开放了配置NNRt的Native接口。

MindSpore Lite Kit对接NNRt可无需构图，两者共享同一份模型图格式（MindIR），因此使用MindSpore Lite在NNRt上加载模型将快于其他AI推理框架。此外，MindSpore Lite也支持通用硬件CPU/GPU与NNRt AI加速硬件之间的模型异构推理功能。

CANN Kit作为麒麟平台的后端接入Neural Network Runtime Kit，支撑Neural Network Runtime Kit于麒麟平台的AI计算能力。CANN Kit构建在底层的硬件驱动和优化的计算库之上，与云侧昇腾芯片统一支持AscendC自定义算子编程语言和相关工具链，是HarmonyOS智能生态的重要基石，为众多领域的智能应用提供核心支撑。
