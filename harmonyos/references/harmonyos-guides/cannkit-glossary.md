---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-glossary
title: CANN Kit术语
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > CANN Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:14+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:79d7a6c4ad2ad0090964306a877e76551295769fbff8daa0b15d2ce79fe9c455
---

## A

### AIPP；人工智能预处理

AIPP（AI Pre-Process）是针对AI推理输入数据进行预处理的模块，实现不同格式图片数据到NPU标准输入格式的转换，可称为“硬件图像预处理”，无需重新训练模型即可完成适配，获得较好的推理性能收益。

### AscendC；CANN算子开发编程语言

华为昇腾、麒麟AI处理器提供的C++算子开发接口，封装了硬件架构抽象、编程范式及基础/高阶API，用于自定义算子开发。

## C

### CPU Twin Debugging；CPU孪生调试

在AsendC算子开发中，CPU孪生调试是一种在CPU上模拟运行算子进行调试的功能，支持自动精度比对、printf打印、DumpTensor、assert断言、gdb单步调试等调测项，可帮助开发者在NPU上板前快速定位代码逻辑和精度问题，提高算子NPU上板成功率。

## G

### GE；图引擎

GE（Graph Engine）是图模式神经网络运行引擎，负责将模型计算过程造成计算图并下发到Kirin硬件执行。相对于单个算子依次下发的方式，图模式下，GE可以通过计算图优化、多流并行、内存复用、模型下沉等技术手段，加速模型执行效率，减少模型内存占用。

## H

### Host侧Tiling；主机侧分块

当本地内存（Local Memory）无法完整容纳算子输入输出时，在主机CPU上进行数据切分、分块计算的过程。将Tiling切分算法参数传递给Kernel侧，用于指导AI Core并行数据的切分，让不擅长标量计算的AI Core专注于计算任务。

## L

### LLM Engine；大语言模型引擎

LLM Engine是基于CANN Kit的大语言模型推理解决方案，为大模型业务提供计算链路加速封装，包括多步骤高效串联、内存复用、数据零拷贝、LoRA拓展、多模态拓展等功能，助力开发者完成模型量化、NPU亲和适配和模型转换，实现高性能、低功耗的大模型部署。

### LoRA；低秩适配

LoRA（Low-Rank Adaptation）是一种大模型轻量化微调技术，通过在预训练量化基模上外挂浮点LoRA分支进行特定场景训练。解决模型量化后精度下降的问题，针对特定场景（如对话、翻译等）进行模型微调，只需训练少量LoRA参数，其他基模参数冻结，大幅降低训练成本。

## M

### Maintenance Testing Debugging and Optimization；维测调优

维测调优是CANN Kit提供的对AI模型进行性能统计，并获取性能数据的能力。开发人员可分析模型和单算子的性能数据，并通过模型的层级输出对比精度来完成问题定位。

## O

### OMG；离线模型转换工具

OMG（Offline Model Generator）是CANN Kit提供的离线模型转换工具，用于将Caffe、TensorFlow、ONNX、MindSpore等框架训练的网络模型转换为达芬奇架构的离线模型（.om格式）。

## Z

### Zero Memory Copy；内存零拷贝

内存零拷贝是将存放在ION内存中的数据（如GPU纹理数据或模型输入数据）直接封装为输入输出张量进行推理的技术，无需数据拷贝，可节省内存和推理时间。
