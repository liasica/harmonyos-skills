---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-constraints
title: 通用约束
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 通用约束
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8120c303e545cd6b53a3581a934e808ef5ba9e787ce663533fc4ef4593a93772
---

AscendC管理不同层级的物理内存时，用一种抽象的逻辑位置（TPosition）来表达各级别的存储，代替了片上物理存储的概念，达到隐藏硬件架构的目的。TPosition类型包括：VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2，具体介绍请参考[TPosition](cannkit-tposition.md)。TPosition与物理内存的映射关系如表1所示。

**表1** TPosition与物理内存映射关系

| TPosition | 物理内存 |
| --- | --- |
| GM | Global Memory |
| VECIN | Unified Buffer |
| VECCALC | Unified Buffer |
| VECOUT | Unified Buffer |
| A1 | L1 Buffer |
| A2 | L0A Buffer |
| B1 | L1 Buffer |
| B2 | L0B Buffer |
| C1 | Kirin9020系列处理器，L1 Buffer |
| C1 | KirinX90系列处理器，L1Buffer |
| C2 | Kirin9020系列处理器，BT Buffer |
| C2 | KirinX90系列处理器，BT Buffer |
| CO1 | L0C Buffer |
| CO2 | Kirin9020系列处理器，Global Memory |
| CO2 | KirinX90系列处理器，Global Memory |
| TSCM | L1 Buffer |
| SPM | Kirin9020系列处理器，Global Memory |
| SPM | KirinX90系列处理器，Global Memory |

AscendC内存管理模块在进行内存分配时会对起始地址进行对齐。各类存储单元的对齐要求如表2所示。

使用AscendC数据计算和数据搬运接口时，目的操作数和源操作数地址偏移对齐要求和表2保持一致，**如果AscendC指令接口中已说明操作数起始地址对齐要求，则以具体指令中的说明为准。**

**表2** 不同存储单元的对齐要求

| 存储单元 | 对齐要求 |
| --- | --- |
| Global Memory | 暂无对齐要求。 |
| Unified Buffer | 32Byte对齐。 |
| L1 Buffer | 32Byte对齐。 |
| L0A Buffer/L0B Buffer | 512Byte对齐。 |
| L0C Buffer | 64Byte对齐。 |
| BT Buffer | 64Byte对齐。 |
