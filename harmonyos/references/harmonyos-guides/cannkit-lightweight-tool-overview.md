---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-lightweight-tool-overview
title: 概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:059a5939394d790621162513430506f5dcaa68151e06d64878bad27facf02073
---

## 简介

轻量化工具是一款集模型压缩算法和网络结构搜索算法于一体的自动模型轻量化工具，针对NPU架构对深度神经网络模型进行深度的模型优化，可以帮助开发者自动地完成模型轻量化以及网络结构的生成任务。目前支持无训练模式、插件式量化模式、大语言模型低位量化和网络结构搜索训练。

* 无训练量化：开发者可以直接输入模型，无需重训练，快速的完成模型轻量化。适用于快捷方便量化的开发者使用。
* 插件式量化：为开发者提供模型量化API，在开发者训练工程中对浮点模型进行量化模型校准或量化模型重训练，易用性高，插件式重训练量化适用于较高精度要求的开发者。
* 大语言模型低位量化：提供大语言模型的4bit低位量化支持。通过权重量化、激活量化和参数提取三段式执行流程，实现大模型压缩。
* 网络结构搜索训练：支持分类网络、检测网络、分割网络三种网络类型。开发者配置相应的搜索参数和接口函数后，使用网络结构搜索工具进行搜索，在设定的算力约束下，得到优秀的网络模型。适用于需要自动生成网络结构的开发者。

| 模式 | 支持的框架 | 支持的策略 | 支持的设备 |
| --- | --- | --- | --- |
| 无训练量化 | TensorFlow、PyTorch、ONNX | Quant\_INT8-8 | 同时支持CPU和GPU模式，GPU支持单机单卡。 |
| 插件式量化 | TensorFlow、PyTorch | Quant\_INT8-8 | 支持GPU，支持单机单卡。 |
| 网络结构搜索训练 | TensorFlow、PyTorch | NASEA | 支持GPU，支持单机单卡和单机多卡。 |
| 大语言模型低位量化 | PyTorch | Quant\_INT16-4 | 支持GPU，量化蒸馏支持单机多卡。 |

说明

Quant\_INT8-8：数据8bit量化，权重8bit量化。

Quant\_INT16-4：数据16bit量化，权重4bit量化。

通过模型轻量化以及网络结构搜索获得模型在NPU上的收益可以参见[模型收益](cannkit-model-benefits.md)。

经过轻量化工具小型化后的模型，可以使用OMG转换工具转为OM离线模型，使用方式可参见[量化模型转换](cannkit-model-conversion-example.md#量化模型转换以caffe模型为例)。

该轻量化工具位于"tools\_dopt"目录下。

| 目录文件 | 描述说明 |
| --- | --- |
| tools\_dopt/dopt\_tf\_py3 | TensorFlow框架无训练，插件式量化，网络结构搜索的工具入口以及demo。 |
| tools\_dopt/dopt\_pytorch\_py3 | PyTorch框架无训练，插件式，大语言模型量化，网络结构搜索的工具入口以及demo。 |
| tools\_dopt/dopt\_onnx\_py3 | ONNX框架无训练工具入口。 |

## 支持范围

* 插件式支持GPU训练，单机单卡训练。
* 无训练支持CPU和GPU量化。
* 大语言模型低位量化支持GPU量化。
* 网络结构搜索工具支持单机单卡和单机多卡，进行分类、检测、分割场景的骨架搜索，依赖运行环境参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。

## 系统要求

* TensorFlow开发者使用本工具需同时满足下列环境要求：

  + Python 3.10
  + Ubuntu 22.04
  + Tensorflow 2.8.0
  + GPU需要使用支持CUDA的显卡（无训练量化可不配置）
* PyTorch开发者使用本工具需同时满足下列环境要求：

  + Python 3.10
  + Ubuntu 22.04
  + PyTorch 1.11
  + opencv-python
  + GPU需要使用支持CUDA的显卡（无训练量化可不配置）
* ONNX开发者使用本工具需同时满足下列环境要求：

  + Python 3.10
  + Ubuntu 22.04
  + ONNX Runtime 1.15
  + ONNX 1.14

## 开发者指引

下面列举了不同开发者场景对应的步骤和工具链功能。开发者可以根据下表中列举的不同场景选择适宜的优化方式。

### TensorFlow开发者

| **开发者场景** | **使用依赖** | **工具链提供功能** | **建议使用工具** | 优势 |
| --- | --- | --- | --- | --- |
| - 缺少足量数据集和训练资源  - 追求高易用性 | - 可运行TensorFlow环境  - 模型pb文件（需要开发者自行转换）  - 校准集 | Quant\_INT8-8 | [TensorFlow无训练量化](cannkit-no-training-and-quantization.md#tensorflow模型无训练量化) | 无需TensorFlow编写代码，新手开发者友好 |
| - 对精度要求较高  - 有足够数据集和训练资源  - 有一定编程能力  - 持有模型训练工程 | - 可运行TensorFlow环境  - 模型的ckpt文件  - 训练集  - 测试集  - 开发者需要在训练工程中调用轻量化工具API量化模型并进行重训练 | Quant\_INT8-8 | [TensorFlow插件式量化](cannkit-plugin-based-quantization.md#tensorflow插件式量化) | 模型精度可保障 |
| - 需要自动生成符合需求的网络结构 | - [环境准备](cannkit-network-structure-search-training.md#环境准备)  - 训练集  - 测试集  - 开发者需要根据说明书编写模型接口代码 | 搜索生成网络结构 | [网络结构搜索训练](cannkit-network-structure-search-training.md) | 可根据开发者提供的配置信息自动搜索到在特定场景上表现优秀的网络结构 |

### PyTorch开发者

| **开发者场景** | **使用依赖** | **工具链提供功能** | **建议使用工具** | **优势** |
| --- | --- | --- | --- | --- |
| - 缺少足量数据集和训练资源  - 追求高易用性 | - 可运行PyTorch环境  - 模型参数文件pth  - python模型定义  - 校准集 | Quant\_INT8-8 | [PyTorch无训练量化](cannkit-no-training-and-quantization.md#pytorch模型无训练量化) | 无需PyTorch编写代码，新手开发者友好 |
| - 对精度要求较高  - 有足够数据集和训练资源  - 有一定编程能力 | - 可运行PyTorch环境  - 模型参数文件pth  - 训练集  - 测试集  - 开发者需要调用轻量化工具API量化模型并进行重训练 | Quant\_INT8-8 | [PyTorch插件式量化](cannkit-plugin-based-quantization.md#pytorch插件式量化) | 模型精度可保障 |
| - 需要自动生成符合需求的网络结构 | - [环境准备](cannkit-network-structure-search-training.md#环境准备)  - 训练集  - 测试集  - 开发者需要根据说明书编写模型接口代码 | 搜索生成网络结构 | [网络结构搜索训练](cannkit-network-structure-search-training.md) | 可根据开发者提供的配置信息自动搜索到在特定场景上表现优秀的网络结构 |
| - 需要对大语言模型进行4bit权重量化 | - 训练集  - 开发者根据说明书生成配置文件和执行脚本  - 脚本执行量化 | Quant\_INT16-4 | [大语言模型低位量化](cannkit-large-language-one-stop.md) | 超大规模模型，权重压缩至4bit |

### ONNX开发者

| **开发者场景** | **开发者需要准备** | **工具链提供功能** | **建议使用工具** | 优势 |
| --- | --- | --- | --- | --- |
| - 缺少足量数据集和训练资源  - 追求高易用性 | - 可运行ONNX Runtime环境  - ONNX model  - 校准集 | Quant\_INT8-8 | [ONNX模型无训练量化](cannkit-no-training-and-quantization.md#onnx模型无训练量化) | 无需编写代码，新手开发者友好 |
