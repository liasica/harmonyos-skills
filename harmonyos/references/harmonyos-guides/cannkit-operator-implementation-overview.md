---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-implementation-overview
title: 算子实现概述
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 算子实现 > 算子实现概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef527c224113a0e7cac1696a2da68f18bbb00b01eda6c9d08347aec85589f68c
---

AscendC的算子实现主要包含两个部分：

* Host侧Tiling实现

  由于NPU中AI Core内部存储无法完全容纳算子输入输出的所有数据，需要每次搬运一部分输入数据进行计算然后搬出，再搬运下一部分输入数据进行计算，这个过程就称之为Tiling。切分数据的算法称为Tiling算法或者Tiling策略。根据算子的shape等信息来确定数据切分算法相关参数（比如每次搬运的块大小，以及总共循环多少次）的计算程序，称之为Tiling实现，也叫Tiling函数(Tiling Function)。由于Tiling实现中完成的均为标量计算，AI Core并不擅长，所以我们将其独立出来放在Host侧CPU上执行。
* Device侧Kernel实现

  Kernel实现即算子核函数实现，在Kernel函数内部通过解析Host侧传入的Tiling结构体获取Tiling信息，根据Tiling信息控制数据搬入搬出Local Memory的流程；通过调用计算、数据搬运、内存管理、任务同步API，实现算子逻辑。其核心逻辑基本上都为计算密集型任务，需要在NPU上执行。

本章介绍了矢量编程、矩阵编程两种典型场景下的算子Tiling、Kernel实现，是对上文中两种典型编程范式的具体应用，同时也介绍了编程的更多细节、API的使用方法等。然后介绍[工程化算子开发](cannkit-overview-of-engineering-operator.md)这种算子开发方式。
