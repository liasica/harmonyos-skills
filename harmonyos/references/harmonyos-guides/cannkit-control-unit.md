---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-control-unit
title: 控制单元
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 基本概念 > 硬件架构 > 控制单元
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:95b6c564bc8b231d025551f31913f2494d5ee4695771fbcba02e65b58572ae5c
---

控制单元为整个计算过程提供了指令控制，负责整个AI Core的运行。AI Core包含的控制单元如图1所示，每个模块的具体介绍请参考表1。

**图1** 控制单元

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/ruVIEukmRd6qRDu_WTKtWw/zh-cn_image_0000002815400183.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=052E4C1190AA015E00396D6812458C4109CAE01DE01EA7B9F8243D54236869BF)

**表1** 控制单元及相关的指令队列介绍

| 控制单元/指令队列 | 描述 |
| --- | --- |
| 标量计算单元(Scalar) | Scalar计算单元。 |
| 矩阵运算队列(Cube Queue) | Cube指令队列。同一个队列里的指令顺序执行，不同队列之间可以并行执行。 |
| 向量运算队列(Vector Queue) | Vector指令队列。同一个队列里的指令顺序执行，不同队列之间可以并行执行。 |
| 存储转换队列(MTE Queue) | MTE指令队列。同一个队列里的指令顺序执行，不同队列之间可以并行执行。 |
| 事件同步模块(Event Sync) | 用于控制不同队列指令（也叫做不同指令流水）之间的依赖和同步的模块。 |

多条指令从系统内存通过总线接口进入到AI Core的指令缓存模块(Instruction Cache)中，后续的指令执行过程，根据指令的类型，有两种可能：

* 如果指令是Scalar指令，指令会被Scalar单元直接执行。
* 其他指令，指令会被调度到5个独立的分类队列（Vector指令队列、Cube指令队列、MTE1/MTE2/MTE3指令队列），然后再分配到某个执行单元执行。

同一个指令执行队列中的指令是按照进入队列的顺序进行执行的，不同指令执行队列之间可以并行执行，通过多个指令执行队列的并行执行可以提升整体执行效率。对于并行执行过程中可能出现的数据依赖，通过事件同步模块插入同步指令来控制流水线的同步，提供PipeBarrier、SetFlag/WaitFlag两种指令，保证队列内部以及队列之间按照逻辑关系执行。

* PipeBarrier本身是一条指令，用于在队列内部约束执行顺序。其作用是，保证前序队列中所有数据的读写工作全部完成，后序指令才能执行。
* SetFlag/WaitFlag为两条指令，在SetFlag/WaitFlag的指令中，可以指定一对指令队列的关系，表示两个队列之间完成一组“锁”机制，其作用方式为：

  + SetFlag：当前序指令的所有读写操作都完成之后，当前指令开始执行，并将硬件中的对应标志位设置为1。
  + WaitFlag：当执行到该指令时，如果发现对应标志位为0，该队列的后续指令将一直被阻塞；如果发现对应标志位为1，则将对应标志位设置为0，同时后续指令开始执行。

AscendC提供同步控制API，开发者可自行控制同步。但更推荐使用[编程模型](cannkit-spmd-model.md)中介绍的编程模型和范式进行开发，其已自动完成同步控制，通常无需再关注同步；自行同步控制可能会带来一定的编程复杂度。

希望开发者可以理解同步的基本原理，便于后续更好地理解、设计并行计算程序；同时少数情况需要开发者手动插入同步，您可以通过[什么时候需要开发者手动插入同步](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/ascendcopapi/docs/zh/api/SIMD-API/basic_api/sync_control/intra_core_sync/intra_core_sync_overview.md)章节来了解具体内容。
