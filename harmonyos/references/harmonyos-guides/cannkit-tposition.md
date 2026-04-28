---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tposition
title: TPosition
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPosition
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30819e30a1db4ba095bf81386a2dcb83ea38466155c20921a14345e24a3bcd53
---

AscendC管理不同层级的物理内存时，用一种抽象的逻辑位置（TPosition）来表达各级别的存储，代替了片上物理存储的概念，达到隐藏硬件架构的目的。主要的TPosition类型包括：VECIN、VECOUT、VECCALC、A1、A2、B1、B2、CO1、CO2，其中VECIN、VECCALC、VECOUT主要用于矢量编程，A1、A2、B1、B2、C1、C2、CO1、CO2用于矩阵编程。开发者可以参考了解TPosition的基础概念，通过[通用约束](cannkit-general-constraints.md)表1了解TPosition和物理存储的映射关系。

TPosition定义如下。

```
1. enum class TPosition : uint8_t {
2. GM,
3. A1,
4. A2,
5. B1,
6. B2,
7. C1,
8. C2,
9. CO1,
10. CO2,
11. VECIN,
12. VECOUT,
13. VECCALC,
14. LCM = VECCALC,
15. SPM,
16. SHM = SPM,
17. TSCM,
18. C2PIPE2GM,
19. C2PIPE2LOCAL,
20. MAX,
21. };
```

TPosition枚举值的具体定义如下。

**表1** TPosition枚举值含义说明

| 枚举值 | 具体含义 |
| --- | --- |
| GM | Global Memory，对应AI Core的外部存储。 |
| VECIN | 用于矢量计算，搬入数据的存放位置，在数据搬入Vector计算单元时使用此位置。 |
| VECOUT | 用于矢量计算，搬出数据的存放位置，在将Vector计算单元结果搬出时使用此位置。 |
| VECCALC | 用于矢量计算/矩阵计算，在计算需要临时变量时使用此位置。 |
| A1 | 用于矩阵计算，存放整块A矩阵，可类比CPU多级缓存中的二级缓存。 |
| B1 | 用于矩阵计算，存放整块B矩阵，可类比CPU多级缓存中的二级缓存。 |
| C1 | 用于矩阵计算，存放整块Bias矩阵，可类比CPU多级缓存中的二级缓存。 |
| A2 | 用于矩阵计算，存放切分后的小块A矩阵，可类比CPU多级缓存中的一级缓存。 |
| B2 | 用于矩阵计算，存放切分后的小块B矩阵，可类比CPU多级缓存中的一级缓存。 |
| C2 | 用于矩阵计算，存放切分后的小块Bias矩阵，可类比CPU多级缓存中的一级缓存。 |
| CO1 | 用于矩阵计算，存放小块结果C矩阵，可理解为Cube Out。 |
| CO2 | 用于矩阵计算，存放整块结果C矩阵，可理解为Cube Out。 |
| SPM | 当Unified Buffer内存有溢出风险时，用于Unified Buffer的数据暂存。 |
| TSCM | Temp Swap Cache Memory, 用于临时把数据交换到额外空间，进行Matmul运算。 |
| C2PIPE2GM | 用于存放FIXPIPE量化参数。 |
| C2PIPE2LOCAL | 预留参数。为后续的功能做保留，开发者暂时无需关注。 |
