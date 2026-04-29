---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-tools
title: 算子调试概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子调试调优 > 算子调试概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f96e0cee465ca867842901bb29e5cf17a2b13846d51201693508c430c9e7ce4
---

## 工具介绍

### 使用说明

介绍AscendC算子调测工具的调测流程和调测功能等，并提供命令行方式，以指导开发者在不同场景下对AscendC算子发起Tiling、精度、性能调测。

**表1** 工具指引

| 使用场景 | 操作指引 | 说明 |
| --- | --- | --- |
| AscendC算子调测工具是什么 | [调测工具简介](cannkit-tiling-tuning.md) | 阐述了工具的基本概念、关键调测功能、调测方式和流程等，帮助开发者快速了解和使用工具。 |
| 算子调测过程中涉及哪些配置和调测功能 | [数据准备与配置说明](cannkit-preparing-input-data-and-benchmark.md) | 阐述命令行方式下算子调测需要的**输入/标杆数据**、**算子信息json文件配置**等。 |
| 算子调测过程中涉及哪些配置和调测功能 | [Tiling调测功能](cannkit-tiling-tuning.md) | 阐述了命令行方式下算子如何进行Tiling计算，并介绍相应产物说明。 |
| 算子调测过程中涉及哪些配置和调测功能 | [CPU孪生调试功能](cannkit-cpu-twin-debugging.md) | 阐述了命令行方式下算子如何在CPU侧编译运行，并介绍精度比对结果，帮助开发者快速定位代码问题。 |
| 算子调测过程中涉及哪些配置和调测功能 | [Simulator性能仿真功能](cannkit-simulator-performance-simulation.md) | 阐述了命令行方式下算子如何在CPU侧通过仿真器进行编译运行，并介绍精度比对结果和性能仿真数据，帮助验证实际算子精度是否正常，性能是否达标。 |
| 算子调测过程中涉及哪些配置和调测功能 | [更多功能](cannkit-commissioning-function-printf.md) | 阐述了命令行方式下算子调测过程中支持的调试功能，包括printf/PRINTF、DumpTensor、assert等打印功能与gdb功能。 |
| 想了解更多调测相关的命令行参数 | [ascendebug调测工具参数说明](cannkit-cli-parameters.md) | 针对命令行方式，本章根据调测功能提供了对应的全量参数说明，帮助开发者快速掌握命令行参数含义和功能。 |
| 使用工具调试调优算子时，遇到问题怎么办 | [算子开发常见问题](cannkit-faqs-operator-development.md) | 工具调测过程中难免会出现异常或报错场景。本章罗列了一些高频问题，给出了具体的原因分析和处理措施。 |

### 使用约束

仅支持对静态Shape算子调测，暂不支持动态Shape算子调测。

## 基本概念

**表2** 基本概念

| 概念 | 描述 |
| --- | --- |
| 标准自定义算子工程场景(customize) | 该场景下，开发者需按照“工程创建->算子实现->编译部署>算子调用”的流程完成算子开发和调用。基于工程代码框架完成算子核函数的开发和Tiling实现，通过工程编译脚本完成算子编译部署。Tiling开发基于CANN提供的编程框架进行，后续更易于借助框架功能实现单算子API调用、图模式算子调用等。 |
| 输入数据和标杆数据 | 使用AscendC调测工具时，需要提供算子输入数据及标杆数据（Golden数据）。  - 输入数据：固定shape算子运行时的输入数据，bin格式。  - 标杆数据：根据输入数据计算出来的真值数据，用于与输出数据进行精度比对，bin格式。 |
| 算子json配置文件 | 用于描述算子的输入、输出及属性信息，以json格式存储。该文件中的参数个数、顺序、数据类型等信息，必须与算子原型相匹配。  工具支持以下配置格式：  [固定输入/输出顺序的算子json配置](cannkit-json-configuration.md)：其输入/输出参数信息单独在inputs、outputs、attrs配置项中设置，不支持输入/输出参数交叉设置。 |
| Tiling | 描述Kirin AI处理器上算子的输入/输出数据切分、分块计算、多核并行等策略，主要是为了满足片上存储限制和计算pipeline的需求，最大化计算并行性和数据局部性（data locality 或 data reuse），从而发挥硬件的极致性能。 |
| CAModel | CAModel(Cycle Accurate Model)仿真器主要用于生成算子性能仿真流水数据。 |
| CCEC | CCEC(Cube-based Computing Engine Compiler)工具基于毕昇编译器，通过自动拼接编译选项构建的一种编译方式。其中，毕昇编译器是一款专为达芬奇SOC设计的编译器，支持异构编程扩展，可将开发者编写的昇腾算子代码编译成二进制可执行文件和动态库等形式，详细介绍请参考《[毕昇编译器使用指南](https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/index/index.html)》。 |
| CCEprint/Intrilog | intrilog：落盘算子运行中的CCE指令流。 |
| 原地算子(in-place op) | 一般指原地更新操作类算子，即算子的输入和输出为同一地址，算子在计算完成后，把原有的输出结果直接覆盖在输入的地址上，以减少不必要的内存占用。 |

输入数据和标杆数据可通过numpy生成，样例如下。

```
1. import numpy as np
2. def gen_data_simple():
3. input_x = np.random.uniform(-100, 100, [8, 2048]).astype(np.float16)
4. input_y = np.random.uniform(-100, 100, [8, 2048]).astype(np.float16)
5. golden = (input_x + input_y).astype(np.float16)
6. input_x.tofile("./input/input_x.bin")     # 通过numpy生成的随机输入数据x
7. input_y.tofile("./input/input_y.bin")     # 通过numpy生成的随机输入数据y
8. golden.tofile("./output/golden.bin")      # 根据输入计算出来的真值数据，即标杆数据
```

## 运行流程

若采用工具命令行方式对单算子调测，其运行流程如图1所示。

**图1** 基于命令行的工具运行流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/VGOT9PGkQwiJ0wLfnnSz6A/zh-cn_image_0000002558606094.png?HW-CC-KV=V1&HW-CC-Date=20260429T054110Z&HW-CC-Expire=86400&HW-CC-Sign=1AF145FDED1F9425D60543B66031F1B932B747A5D0F1F061A6832223D6C9F6A7)

1. 准备环境：使用本工具进行算子调测前，请先完成基础环境搭建，详细操作参见[环境准备](cannkit-environment-preparation.md)。
2. 准备数据：准备好bin格式的输入数据和标杆数据文件，该数据是调测工具的必要输入。
3. 配置json文件：根据工具提供的算子信息json配置样例配置待测算子信息，该文件是调测工具的必要输入。
4. 通过命令行方式发起算子调测。

   目前工具支持的算子调测能力如下，请按需选择：

   * Tiling调测：对Tiling函数调测，生成Tiling结果，验证Tiling函数功能。
   * 精度调试：通过CPU仿真或者simulator仿真进行核函数精度调试，支持自动精度比对、printf/PRINTF/DumpTensor/assert打印等功能。
   * 性能调优：通过simulator仿真获取算子执行circle数，评估算子性能。
