---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-architecture
title: 基本架构
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 基本概念 > 硬件架构 > 基本架构
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:18+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:24b86bd790cb7c32f4584ad061ced45b1e489c656c97e2c7234ec1c377c9a3c3
---

如下展示了总体的硬件基本架构。其中，基于AscendC开发的算子经由数据总线传输，最终在AI Core上运行，从而与其他基本单元协同工作。下文的编程模型基于硬件架构的抽象进行介绍，了解该内容能够更好的理解编程模型；对于需要完成高性能编程的深度开发者，更需要了解硬件架构相关知识，最佳实践中很多内容都以本章为基础进行介绍。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/H9l8Zk5FTg-57TEN4sKQBw/zh-cn_image_0000002820526691.png?HW-CC-KV=V1&HW-CC-Date=20261119T014917Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE3C2BB628306B7CE3A253749DC3B95CC50DD360DCDEC832FE5451E990A98FDC)

AI Core负责执行标量、向量和张量相关的计算密集型算子，包括三种基础**计算单元**：Cube（矩阵）计算单元、Vector（向量）计算单元和Scalar（标量）计算单元，同时还包含**存储单元**（包括硬件存储和用于数据搬运的搬运单元）和**控制单元**。硬件架构根据Cube计算单元和Vector计算单元是否同核部署分为**耦合架构**和**分离架构**两种。

Kirin9050/Kirin9020/Kirin9030/KirinX90系列处理器：耦合架构

## 耦合架构

耦合架构是指Cube计算单元和Vector计算单元同核部署，架构图如下图所示。下图中列出了计算架构中的[存储单元](cannkit-storage-unit.md)和[计算单元](cannkit-computing-unit.md)，箭头表示数据处理流向，MTE1/MTE2/MTE3代表[搬运单元](cannkit-storage-unit.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/jLQGN6psT4-zZGCmK33fLA/zh-cn_image_0000002820406691.png?HW-CC-KV=V1&HW-CC-Date=20261119T014917Z&HW-CC-Expire=31536000000&HW-CC-Sign=4890CD9D92737F57E4CF710C834E2E7C5ABD5C77526694BD8B5DBBF08BCC5266)

**说明** 

图中的虚线箭头表明Kirin9050/Kirin9020/Kirin9030/KirinX90系列处理器支持Scalar直接读写GM数据。

## 分离架构

如下图所示，分离架构将AI Core拆成矩阵计算(AI Cube、AIC)和向量计算(AI Vector、AIV)两个独立的核，每个核都有自己的Scalar单元，能独立加载自己的代码段，从而实现矩阵计算与向量计算的解耦，在系统软件的统一调度下互相配合达到计算效率优化的效果。AIV与AIC之间通过Global Memory进行数据传递。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/m9RttUkrSlyfj5k33qhKyg/zh-cn_image_0000002791726712.png?HW-CC-KV=V1&HW-CC-Date=20261119T014917Z&HW-CC-Expire=31536000000&HW-CC-Sign=5931AAFDFABBE52C2151A0AEC16222531FBFCCB82BC7519DC1E9379FF44F8AF5)

* AIC架构

  + 包含4个并行执行单元（搬运单元和计算单元）：MTE1、MTE2、Cube、Scalar。
  + 包含7个内存单元：GM（核外）、L1、L0A、L0B，L0C、BiasTable Buffer、FixPipe Buffer。
* AIV架构

  + 包含4个并行执行单元：MTE2、MTE3、Vector、Scalar。
  + 包含2个内存单元：GM（核外）、UB。
* 典型计算数据流

  + Vector计算：GM-UB- [Vector]-UB-GM。
  + Cube计算：GM-L1-L0A/L0B-Cube-L0C-FixPipe-GM、GM-L1-L0A/L0B-Cube-L0C-FixPipe-L1。
