---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-architecture
title: 基本架构
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 硬件架构 > 基本架构
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3ca5382977ec7db7c60f292373cc359e6fb0f6d34e4391fdcda221d1cf7b3b6a
---

如下展示了总体的硬件基本架构。其中，AI Core通过数据总线与硬件结构中其它基本单元相连接，基于AscendC开发的算子，通过总线传输并最终运行在AI Core上。下文的编程模型基于硬件架构的抽象进行介绍，了解该内容能够更好的理解编程模型；对于需要完成高性能编程的深度开发者，更需要了解硬件架构相关知识，最佳实践中很多内容都以本章为基础进行介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/CsQnNcVVTci-v1J_HqPHTA/zh-cn_image_0000002558765726.png?HW-CC-KV=V1&HW-CC-Date=20260429T054102Z&HW-CC-Expire=86400&HW-CC-Sign=D726109C1B2B481CC04AF1AB8A3CAB1459AABF7A93F8665571A975FFE126BD9A)

AI Core负责执行标量、向量和张量相关的计算密集型算子，包括三种基础**计算单元**：Cube（矩阵）计算单元、Vector（向量）计算单元和Scalar（标量）计算单元，同时还包含**存储单元**（包括硬件存储和用于数据搬运的搬运单元）和**控制单元**。硬件架构根据Cube计算单元和Vector计算单元是否同核部署分为**耦合架构**和**分离架构**两种。

Kirin9020/KirinX90系列处理器：耦合架构

## 耦合架构

耦合架构是指Cube计算单元和Vector计算单元同核部署，架构图如下图所示。下图中列出了计算架构中的[存储单元](cannkit-storage-unit.md)和[计算单元](cannkit-computing-unit.md)，箭头表示数据处理流向，MTE1/MTE2/MTE3代表[搬运单元](cannkit-storage-unit.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/NjcgdaFqRiiPlEQ4yjrbFQ/zh-cn_image_0000002558606070.png?HW-CC-KV=V1&HW-CC-Date=20260429T054102Z&HW-CC-Expire=86400&HW-CC-Sign=F0335D99F92FDEDE44A359EBC639AAC33ACA8DA23D7FA479FC5B15F1BBC5C38F)

说明

图中的虚线箭头表明Kirin9020/KirinX90系列处理器支持Scalar直接读写GM数据。

## 分离架构

如下图所示，分离架构将AI Core拆成矩阵计算(AI Cube、AIC)和向量计算(AI Vector、AIV)两个独立的核，每个核都有自己的Scalar单元，能独立加载自己的代码段，从而实现矩阵计算与向量计算的解耦，在系统软件的统一调度下互相配合达到计算效率优化的效果。AIV与AIC之间通过Global Memory进行数据传递。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/bUMp5XCqSmeC0qzZ20V5VQ/zh-cn_image_0000002589325597.png?HW-CC-KV=V1&HW-CC-Date=20260429T054102Z&HW-CC-Expire=86400&HW-CC-Sign=03D9B81A8FE2E2069EBDC8B3D9C9783C1E690CE8DB6850F836D81BF8094C8BC3)

* AIC架构

  + 包含4个并行执行单元（搬运单元和计算单元）：MTE1、MTE2、Cube、Scalar。
  + 包含7个内存单元：GM（核外）、L1、L0A、L0B，L0C、BiasTable Buffer、FixPipe Buffer。
* AIV架构

  + 包含4个并行执行单元：MTE2、MTE3、Vector、Scalar。
  + 包含2个内存单元：GM（核外）、UB。
* 典型计算数据流

  + Vector计算：GM-UB- [Vector]-UB-GM。
  + Cube计算：GM-L1-L0A/L0B-Cube-L0C-FixPipe-GM、GM-L1-L0A/L0B-Cube-L0C-FixPipe-L1。
