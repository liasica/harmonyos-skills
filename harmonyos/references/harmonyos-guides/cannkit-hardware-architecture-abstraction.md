---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hardware-architecture-abstraction
title: 硬件架构抽象
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程模型 > 硬件架构抽象
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b519fe1c3f6539add88e4d8c47178222b41e8ffc41a500c4da63e1160bdfba5
---

AscendC基于硬件抽象架构进行编程， 屏蔽不同硬件之间的差异。

**图1** 硬件架构抽象

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/bQqlbIYpRSuRQtXw_sjN5w/zh-cn_image_0000002589325601.png?HW-CC-KV=V1&HW-CC-Date=20260429T054104Z&HW-CC-Expire=86400&HW-CC-Sign=0EEBB8597D580E9EA7F26BFF0D7FF75F1B51BD82799448241C8A76DE190A9C7A)

AI Core中包含**计算单元、存储单元、搬运单元**等核心组件。

* 计算单元包括了三种基础计算资源：Cube计算单元、Vector计算单元和Scalar计算单元。
* 存储单元包括内部存储和外部存储：

  + AI Core的内部存储，统称为Local Memory，对应的数据类型为LocalTensor。由于不同芯片间硬件资源不固定，可以为UB、L1、L0A、L0B等。
  + AI Core能够访问的外部存储称之为Global Memory，对应的数据类型为GlobalTensor。
* DMA(Direct Memory Access)搬运单元：负责在Global Memory和Local Memory之间搬运数据。

AI Core内部核心组件及组件功能详细说明如下表。

**表1** AI Core内部核心组件

| 组件分类 | 组件名称 | 组件功能 |
| --- | --- | --- |
| 计算单元 | Scalar | 执行地址计算、循环控制等标量计算工作，并把向量计算、矩阵计算、数据搬运、同步指令发射给对应单元执行。 |
| 计算单元 | Vector | 负责执行向量运算。 |
| 计算单元 | Cube | 负责执行矩阵运算。 |
| 存储单元 | Local Memory | AI Core的内部存储。 |
| 搬运单元 | DMA(Direct Memory Access) | 负责在Global Memory和Local Memory之间搬运数据，包含搬运单元MTE2（Memory Transfer Engine，数据搬入单元），MTE3（数据搬出单元）等。 |

开发者在理解硬件架构的抽象时，需要重点关注如下**异步指令流、同步信号流**、**计算数据流**三个过程：

* AI Core内部的异步并行计算过程：Scalar计算单元读取指令序列，并把向量计算、矩阵计算、数据搬运指令发射给对应单元的指令队列，向量计算单元、矩阵计算单元、数据搬运单元异步的并行执行接收到的指令。该过程可以参考图1中蓝色箭头所示的指令流。
* 不同的指令间有可能存在依赖关系，为了保证不同指令队列间的指令按照正确的逻辑关系执行，Scalar计算单元也会给对应单元下发同步指令。各单元之间的同步过程可以参考图1中的绿色箭头所示的同步信号流。
* AI Core内部数据处理的基本过程：DMA搬入单元把数据搬运到Local Memory，Vector/Cube计算单元完成数据计算，并把计算结果写回Local Memory，DMA搬出单元把处理好的数据搬运回Global Memory。该过程可以参考图1中的红色箭头所示的数据流。
