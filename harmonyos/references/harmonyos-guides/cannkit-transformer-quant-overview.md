---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-transformer-quant-overview
title: Transformer结构量化概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > Transformer结构量化概述
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:986bc251f7d68dc48626628b310448feb95907912341a701cf14506c987eed82
---

## 简介

轻量化工具针对Transformer结构模型提供量化与微调能力，目前支持大语言模型低比特量化、插件式量化以及量化基模外挂LoRA微调。量化完成后，可通过量化模型导出完成量化参数提取与ONNX导出，供OMC/OMG离线模型编译使用。

* 大语言模型低比特量化：提供大语言模型的4bit低位量化支持。对于激活张量支持静态s16量化以及动态s8量化，静态量化采用标准的两段式执行流程：权重量化、激活量化，动态量化在权重量化完成后即可完成，推荐使用动态量化。适用于快捷完成大模型压缩的开发者。
* 插件式量化：为开发者提供模型量化API，在开发者训练工程中对浮点模型进行量化模型校准或量化模型重训练，易用性高，插件式重训练量化适用于较高精度要求的开发者。
* 量化基模外挂LoRA微调：在量化基模上外挂LoRA分支进行特定场景训练，即量化基模+LoRA的结构微调，作用于量化损失修复和下游场景任务续训。
* 量化模型导出：支持量化基模与外挂LoRA两类量化权重，基于量化策略文件与量化权重完成量化参数提取与ONNX导出。

| 模式 | 支持的框架 | 支持的策略 | 支持的设备 |
| --- | --- | --- | --- |
| 大语言模型低比特量化 | PyTorch | Quant\_INT8-4\_ECO | 支持GPU/NPU，支持单机单卡。 |
| 插件式量化 | PyTorch | Quant\_aigc\_ptq、Quant\_aigc\_qat、  Quant\_INT8-4\_ECO | 支持GPU/NPU，支持单机单卡。 |
| 量化基模外挂LoRA微调 | PyTorch | LoRA分支Quant\_INT16-8 | 支持GPU/NPU，支持单机单卡。 |

**说明** 

Quant\_aigc\_ptq：数据8bit量化，权重8bit量化。量化参数基于校准。

Quant\_aigc\_qat：数据8bit量化（默认，可配置为16bit），权重8bit量化。量化参数支持训练微调。

Quant\_INT8-4\_ECO：数据动态8bit量化，权重4bit量化。量化参数支持训练微调。

## 支持范围

* 插件式量化支持GPU/NPU训练，单机单卡训练。
* 大语言模型低比特量化支持GPU/NPU量化。
* 量化基模外挂LoRA微调支持GPU/NPU训练，单机单卡训练。

## 系统要求

PyTorch开发者使用本工具需同时满足下列环境要求：

* Python >= 3.10
* Ubuntu 22.04
* PyTorch 2.7.1
* opencv-python
* GPU需要使用支持CUDA的显卡，NPU需要昇腾计算卡。

## 开发者指引

开发者可以根据下表中列举的不同场景选择适宜的优化方式。

| 开发者场景 | 工具链提供功能 | 建议使用工具 | 优势 |
| --- | --- | --- | --- |
| - 缺少足量数据集和训练资源  - 追求高易用性  - 需要对大语言模型进行4bit低bit量化 | Quant\_INT8-4\_ECO | [LLM模型一站式量化](cannkit-large-language-one-stop.md) | 推荐动态量化，无需模型改造，新手开发者友好 |
| - 有一定编程能力  - 持有模型训练工程  - transformers结构 | Quant\_aigc\_ptq、Quant\_aigc\_qat、  Quant\_INT8-4\_ECO | [插件式量化](cannkit-plug-in-quantification.md) | 接口开放，用户可自主结合模型优化工程进行量化 |
| - 量化模型需特定场景续训  - 修复量化精度损失 | LoRA分支Quant\_INT16-8 | [量化基模外挂LoRA微调](cannkit-external-lora-fine-tuning.md) | 仅训练LoRA参数，训练成本低 |
| - 完成量化后需部署 | 量化参数文件、ONNX模型 | [量化模型导出](cannkit-quant-model-export.md) | 支持量化基模与外挂LoRA权重 |

该轻量化工具位于"tools\_dopt"目录下。

| 目录文件 | 描述说明 |
| --- | --- |
| tools\_dopt/dopt\_pytorch\_py3 | PyTorch框架插件式量化、大语言模型低bit量化以及量化基模外挂LoRA微调的工具入口以及demo。 |
