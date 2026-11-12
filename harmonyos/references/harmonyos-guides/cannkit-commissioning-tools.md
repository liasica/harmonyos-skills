---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-commissioning-tools
title: AscendC算子调试调优概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > AscendC算子调试调优 > AscendC算子调试调优概述
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:9c716a5f9ee1d32f475dfdee5192f654a03ca22793a1fc86c8ea7fbebd67659b
---

## 工具介绍

### 使用说明

介绍AscendC算子调测工具的调测流程和调测功能等，开发者可通过**算子直调工程**和**mskl调测工具**两种方式，在不同场景下对AscendC算子发起Tiling、精度、性能调测。

**表1** 工具指引

| 使用场景 | 操作指引 | 说明 |
| --- | --- | --- |
| 算子如何进行仿真调测 | [Simulator性能仿真功能](cannkit-simulator-performance-simulation.md) | 通过算子直调工程和mskl调测工具，验证实际算子精度是否正常，性能是否达标。 |
| 算子如何进行Tiling调测 | [Tiling调测功能](cannkit-tiling-tuning.md) | 通过mskl调测工具的mskl.tiling\_func接口调用Tiling函数，并介绍了Tiling的结果说明。 |

### 使用约束

仅支持对静态Shape算子调测，暂不支持动态Shape算子调测。

## 基本概念

**表2** 基本概念

| 概念 | 描述 |
| --- | --- |
| 标准自定义算子工程场景(customize) | 该场景下，开发者需按照“工程创建->算子实现->编译部署>算子调用”的流程完成算子开发和调用。基于工程代码框架完成算子核函数的开发和Tiling实现，通过工程编译脚本完成算子编译部署。Tiling开发基于CANN提供的编程框架进行，后续更易于借助框架功能实现单算子API调用、图模式算子调用等。 |
| 输入数据和标杆数据 | 使用AscendC调测工具时，需要提供算子输入数据及标杆数据（Golden数据）。  - 输入数据：固定shape算子运行时的输入数据，bin格式。  - 标杆数据：根据输入数据计算出来的真值数据，用于与输出数据进行精度比对，bin格式。 |
| Tiling | 描述Kirin AI处理器上算子的输入/输出数据切分、分块计算、多核并行等策略，主要是为了满足片上存储限制和计算pipeline的需求，最大化计算并行性和数据局部性（data locality），从而发挥硬件的极致性能。 |
| CAModel | CAModel(Cycle Accurate Model)仿真器主要用于生成算子性能仿真流水数据。 |
| CCEC | CCEC(Cube-based Computing Engine Compiler)工具基于毕昇编译器，通过自动拼接编译选项构建的一种编译方式。其中，毕昇编译器是一款专为达芬奇SoC设计的编译器，支持异构编程扩展，可将开发者编写的昇腾算子代码编译成二进制可执行文件和动态库等形式，详细介绍请参考《[毕昇编译器使用指南](https://www.hiascend.com/document/detail/zh/canncommercial/82RC1/index/index.html)》。 |
| CCEprint/Intrilog | Intrilog：落盘算子运行中的CCE指令流。 |
| 原地算子(in-place op) | 一般指原地更新操作类算子，即算子的输入和输出为同一地址，算子在计算完成后，把原有的输出结果直接覆盖在输入的地址上，以减少不必要的内存占用。 |

输入数据和标杆数据可通过numpy生成，样例如下。

```python
import numpy as np
def gen_data_simple():
    input_x = np.random.uniform(-100, 100, [8, 2048]).astype(np.float16)
    input_y = np.random.uniform(-100, 100, [8, 2048]).astype(np.float16)
    golden = (input_x + input_y).astype(np.float16)
    input_x.tofile("./input/input_x.bin")     # 通过numpy生成的随机输入数据x
    input_y.tofile("./input/input_y.bin")     # 通过numpy生成的随机输入数据y
    golden.tofile("./output/golden.bin")      # 根据输入计算出来的真值数据，即标杆数据
```

## 运行流程

对单算子进行调测的关键步骤如下。

1. 环境准备：使用本工具进行算子调测前，请先完成基础环境搭建，详细操作参见[环境准备](cannkit-environment-preparation.md)。
2. 算子工程准备与部署：完成算子开发，并通过build\_and\_install.sh将算子部署到CANN环境。
3. 发起算子调测，目前支持以下方式，请按需选择：

   * 算子直调工程：通过CMake编译生成可执行程序，在仿真模式下链接CAModel仿真器的动态共享库，在Host侧完成算子的功能验证与性能仿真，详细操作参见[Simulator性能仿真功能](cannkit-simulator-performance-simulation.md)。
   * mskl调测工具：在Python脚本中调用mskl接口，快速实现Kernel的下发、编译与运行，适用于算子的Tiling逻辑验证与功能验证，详细操作参见[Tiling调测功能](cannkit-tiling-tuning.md)和[Simulator性能仿真功能](cannkit-simulator-performance-simulation.md)。

   调测过程中支持的调测能力如下：

   * Tiling调测：对Tiling函数调测，生成Tiling结果，验证Tiling函数功能。
   * 精度调试：通过simulator仿真进行核函数精度调试，支持自动精度比对。
   * 性能调优：通过simulator仿真获取算子执行circle数，评估算子性能。
