---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computing-unit
title: 计算单元
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 自定义算子开发 > AscendC算子开发 > 基本概念 > 硬件架构 > 计算单元
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:93707c4bf2648fc810cd10a40099393f828878b3a965682401df255127764ca1
---

计算单元是AI Core中提供强大算力的核心单元，包括三种基础**计算单元**：Cube（矩阵）计算单元、Vector（向量）计算单元和Scalar（标量）计算单元，完成AI Core中不同类型的数据计算。

## Scalar

Scalar负责各类型的标量数据运算和程序的流程控制。功能上可以看做一个小CPU，完成整个程序的循环控制、分支判断、Cube/Vector等指令的地址和参数计算以及基本的算术运算，并且可以通过在事件同步模块中插入同步符的方式来控制AI Core中其他功能性单元的执行流水。相对于Host CPU，Scalar的计算能力较弱，重点用于发射指令，性能调优时尽量减少if/else及变量运算。

如下图所示：Scalar通过标准的ALU(Arithmetic Logic Unit)执行标量运算指令。

**图1** Scalar对指令和数据的访问

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/V64pDPZSTP-C3MsjtSnLCg/zh-cn_image_0000002786520606.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=C84DD43464D76220266F82C6BD522BF03CD3B8586951C6ED3B6108CFF002275A)

ALU需要的代码段和数据段（栈空间）都来自于GM。ICache用于缓存代码段，缓存大小与硬件规格相关，比如为16K或32K，以2K为单位加载；DCache用于缓存数据段，大小也与硬件规格相关，比如为16K，以cacheline(64Byte)为单位加载。

考虑到核内访问效率最高，应尽量保证代码段和数据段被缓存在ICache和DCache，避免核外访问； 同时根据数据加载单位不同，编程时可以考虑单次加载数据大小，来提升加载效率。例如在DCache加载数据时，当数据内存首地址与cacheline(64Byte)对齐时，加载效率最高。

## Vector

Vector负责执行向量运算。向量计算单元执行向量指令，类似于传统的单指令多数据(SIMD, Single Instruction Multiple Data)指令，每个向量指令可以完成多个操作数的同一类型运算。如下图所示，向量计算单元可以快速完成两个FP16类型的向量相加或者相乘。向量指令支持多次迭代执行，也支持对带有间隔的向量直接进行运算。

**图2** 向量运算

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/vJgod-M7TDmEJiwZ58CH_w/zh-cn_image_0000002786360678.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=C3333E415CD84E0258C9A1626E797BCE43A97172119060D8C6837E369FB5E073)

Vector所有计算的源数据以及目标数据都要求存储在Unified Buffer中，Vector指令的首地址和操作长度有对齐要求，通常要求32字节对齐，具体对齐要求参考[API的约束描述](https://www.hiascend.com/document/detail/zh/CANNCommunityEdition/latest/API/ascendcopapi/docs/zh/api/SIMD-API/basic_api/memory_vector_compute/data_move/DataCopy_GMAndUB_continuous.md)。

## Cube

Cube计算单元负责执行矩阵运算。Cube一次执行可以完成A矩阵(M\*K)与B矩阵(K\*N)的矩阵乘。如下图所示红色虚线框划出了Cube计算单元及其访问的存储单元，其中左矩阵A来源于L0A，右矩阵B来源于L0B，L0C存储矩阵乘的结果和中间结果。

**图3** 矩阵运算

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/rDUfceQFQTmU-EKHaYVrNA/zh-cn_image_0000002815560099.png?HW-CC-KV=V1&HW-CC-Date=20261112T233223Z&HW-CC-Expire=31536000000&HW-CC-Sign=9EBD8AA30211459F016E3C6345AF2135148D8CB9C9A46A0CE190790583EF561C)
