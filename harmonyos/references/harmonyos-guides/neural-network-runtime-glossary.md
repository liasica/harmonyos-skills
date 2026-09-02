---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/neural-network-runtime-glossary
title: Neural Network Runtime Kit术语表
breadcrumb: 指南 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > Neural Network Runtime Kit术语表
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:fbfa61eda906495e24c31b12bf0d0c2de990aef7f986478ccb84cba0ed1fcadb
---

## A

### Acceleration Chip; 加速芯片

专门用于加速AI神经网络运行计算任务的硬件芯片，作为NNRt的底层计算资源，提供比通用CPU更高效的矩阵计算能力。

### Asynchronous Inference; 异步推理

一种推理执行方式，推理请求提交后立即返回，推理完成通过回调通知调用方。与同步推理相比，可以提高系统吞吐量。

## C

### Compilation Cache; 编译缓存

将模型编译结果保存为缓存文件或内存数据的机制。再次编译相同模型时可直接加载缓存，大幅缩短编译时间。

### Custom Extension Property; 自定义扩展属性

针对特定AI硬件的专有配置项，通过NNRt提供的扩展配置接口设置。具体属性名称和取值需参考硬件厂商。

## D

### Device Management; 设备管理

NNRt的功能模块之一，负责展示已对接的AI硬件信息，并提供选择AI硬件的接口。

## F

### FP16 Mode; FP16模式

一种半精度浮点计算模式，通过降低数值精度换取更高的计算性能和更低的内存占用，适用于对精度要求不高的推理场景。

## H

### Hardware Driver; 硬件驱动

位于NNRt底层的AI加速芯片驱动程序，负责将NNRt的模型表达转换为硬件可执行的计算格式。

### Heterogeneous Inference; 异构推理

模型在不同类型硬件（如CPU、GPU与AI加速芯片）之间协同执行模型推理的能力。

## I

### In-memory Model Cache; 内存模型缓存

将编译后的模型对象保存在内存中，便于快速加载和复用，避免重复编译开销。

### Inference Framework; 推理框架

运行在AI加速芯片之上、提供模型推理能力的软件框架，如MindSpore Lite。推理框架通过调用NNRt接口实现跨芯片推理。

### In-series Operator Fusion; 算子融合

将多个相邻的算子合并为一个算子执行的优化技术，可以减少数据搬运和内核启动开销，提升推理性能。

## L

### Low-level Device Abstraction Layer (HDI); 硬件设备抽象层

定义硬件设备标准化接口的层，使得上层软件（如NNRt）可以通过统一接口访问不同厂商的AI加速芯片。

## M

### Memory Management; 内存管理

NNRt的功能模块之一，负责在AI硬件驱动上申请共享内存并分配给推理输入输出张量，在张量销毁时释放对应共享内存。

### MindIR; MindSpore中间表示

MindSpore Lite推理框架使用的模型图格式，与NNRt内部模型图格式兼容，因此MindSpore Lite无需调用NNRt构图接口即可直接对接。

### MindSpore Lite

华为自研的AI推理框架，内置支持NNRt，可通过MindIR模型图直接对接NNRt，实现无感知的跨AI硬件推理。

### Model Cache; 模型缓存

NNRt的功能模块之一，将已编译的模型对象保存为缓存格式(文件或内存)，下次编译时可直接加载，大幅提升编译速度。

### Model Compilation; 模型编译

NNRt的处理阶段，将内部模型图或离线模型文件通过编译接口在底层AI硬件驱动上转化为硬件相关的模型对象。

### Model Construction; 模型构造

NNRt的处理阶段，通过调用构图接口将推理框架的模型图转换为NNRt内部模型图的过程。

### Model Graph; 模型图

表示神经网络拓扑结构的图结构，包含算子节点和张量连接关系，用于描述模型的计算流程。

### Model Inference; 模型推理

NNRt的处理阶段，基于已编译的模型对象创建执行器，设置推理输入输出张量，然后在AI硬件上执行模型计算。

## N

### Neural Network Runtime (NNRt); 神经网络运行时

面向AI领域的跨芯片推理计算运行时，作为中间桥梁连通上层AI推理框架和底层加速芯片，实现AI模型的跨芯片推理计算。

### NN\_Tensor; 张量句柄

NNRt的张量句柄，用于设置执行器的推理输入和输出张量，包含数据布局、数据类型、形状等。

### NPU; 神经网络处理器

专门用于加速神经网络计算的专用芯片，是NNRt对接的AI加速硬件类型之一。

## O

### OH\_NNCompilation; 编译器句柄

NNRt的编译器句柄类型，用于配置和执行模型编译，包括指定设备、设备缓存、设备性能参数等。

### OH\_NNExecutor; 执行器句柄

NNRt的执行器句柄类型，用于构造模型图，包括添加张量、添加算子、指定输入输出等。

### Offline Model; 离线模型

与特定AI硬件直接相关的模型文件格式，由硬件厂商提供的模型转换器将原始训练模型转换而来。离线模型编译速度快，但无法跨硬件兼容。

### Online Graph Construction; 在线构图

AI推理框架调用NNRt构图接口，将框架内部模型图转换为NNRt内部模型图的过程。

### Operator; 算子

神经网络模型中的基本计算单元，如卷积、池化、激活函数等。NNRt目前支持大部分常用算子，具体实现位于AI硬件驱动中。

### Operator Type; 算子类型

标识算子功能的枚举值，如OH\_NN\_OPS\_ADD表示加法算子，用于在添加算子时指定算子种类。

## P

### Performance Mode; 性能模式

NNRt提供的硬件配置选项，包括极致性能、高性能、中等功耗、低功耗等模式，用于调整推理时的性能与功耗平衡。

### Priority; 优先级

模型计算的执行优先级配置，决定推理任务在硬件上的调度顺序。

## Q

### Quantization Parameter; 量化参数

用于指定张量量化信息的参数，包括缩放因子、零点等，在构造模型时指定张量的量化配置。

## R

### Runtime; 运行时

程序运行时的执行环境，提供程序加载、内存管理、任务调度等基础服务。

## S

### Shared Memory; 共享内存

可被不同进程或设备访问的内存区域。NNRt通过在AI硬件驱动上申请共享内存来实现输入输出数据的“零拷贝”。

### Synchronous Inference; 同步推理

一种推理执行方式，推理请求提交后阻塞等待推理完成并返回结果。与异步推理相比，实现更简单，但可能降低系统吞吐量。

## T

### Tensor; 张量

多维数组，是神经网络模型中数据的基本表示形式，包括输入数据、输出数据、权重参数等。张量是算子计算的基本载体。

### Tensor Data Buffer; 张量数据缓冲区

存储张量实际数据的内存区域，通过OH\_NNTensor\_GetDataBuffer接口获取指针后可进行读写操作。

## Z

## Zero-copy; 零拷贝

数据从一个内存区域传递到另一个内存区域时，无需CPU介入复制操作的技术。NNRt通过AI硬件驱动上的共享内存实现输入输出数据的零拷贝，提升推理性能。
