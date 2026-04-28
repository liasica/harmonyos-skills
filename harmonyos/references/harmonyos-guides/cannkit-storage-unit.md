---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storage-unit
title: 存储单元
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 硬件架构 > 存储单元
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6e82c406888085deb5874d5c0bd5aed8b2a45e0d092a454cffd499ef52b321bf
---

AI处理器中的计算资源要想发挥强劲算力，必要条件是保证输入数据能够及时准确地出现在计算单元中，需要精心设计存储系统，保证计算单元所需的数据供应。

AI Core中包含多级**内部存储**，AI Core需要把**外部存储**中的数据加载到内部存储中，才能完成相应的计算。AI Core的主要内部存储包括：L1 Buffer（L1缓冲区）、L0 Buffer（L0缓冲区）、Unified Buffer（统一缓冲区）等。为了配合AI Core中的数据传输和搬运，AI Core中还包含MTE（Memory Transfer Engine，存储转换引擎）搬运单元，在搬运过程中可执行[随路数据格式类型转换](cannkit-channel-associated-format-conversion.md)。

AI Core的内部存储列表如表1所示。

**表1** 存储单元介绍

| 存储单元 | 描述 |
| --- | --- |
| L1 Buffer | L1缓冲区，通用内部存储，是AI Core内比较大的一块数据中转区，可暂存AI Core中需要反复使用的一些数据从而减少从总线读写的次数。 |
| L0A Buffer / L0B Buffer | Cube指令的输入。 |
| L0C Buffer | Cube指令的输出，但进行累加计算的时候，也是输入的一部分。 |
| Unified Buffer | 统一缓冲区，向量和标量计算的输入和输出。 |
| BT Buffer | BiasTable Buffer，存放Bias。 |
| FP Buffer | Fixpipe Buffer，存放量化参数、Relu参数等。 |

**表2** 搬运单元介绍

| 搬运单元 | 描述 |
| --- | --- |
| MTE1 | 负责如下通路的数据搬运：  - L1->L0A/L0B  - L1->UB（只有耦合架构支持）  - L1->BT Buffer |
| MTE2 | 负责如下通路的数据搬运：  - GM->{L1, L0A/B}，在该通路下，基于分形大小搬运，搬运时满足cacheline(512Byte)对齐，性能更优。  - GM->UB，基于cacheline大小搬运性能更优。 |
| MTE3 | 负责如下通路的数据搬运：UB -> GM |
| FixPipe | 只有分离架构支持，负责如下通路的数据搬运，搬运过程中可以完成随路数据格式/类型转换：  - L0C->{GM/L1}  - L1->FP Buffer |

说明

* 不同类型的AI处理器，存储单元大小不同，开发者可通过[GetCoreMemSize](cannkit-getcorememsize.md)接口获取。
* 所有通过搬运单元读写GM的数据都缺省被缓存在L2Cache，以此加快访问速度，提高访问效率。核外L2Cache以cacheline为单位加载数据，根据硬件规格不同，cacheline大小不同（128/256/512Byte等）。
