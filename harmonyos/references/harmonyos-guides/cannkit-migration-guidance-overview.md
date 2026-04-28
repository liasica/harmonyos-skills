---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-migration-guidance-overview
title: 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:94bc19386a0f6c3f75ae9988ae9e191895b60851b8bde1c39d3f5c6416afc21b
---

Ascend910B/Ascend910C和KirinX90/Kirin9030之间的ASC API详细能力差异，见[《Ascend C算子接口》](cannkit-ascend-c-apis.md)。本节当前重点描述主要的差异和兼容适配方案，其它情况可类比参考。

架构版本代表了AI处理器的能力，Ascend910B/Ascend910C和KirinX90/Kirin9030的AI处理器架构版本请参见表1。

**表1** 处理器型号和NPU\_ARCH的对应关系

| 处理器型号 | NPU\_ARCH |
| --- | --- |
| Ascend910B/Ascend910C | 2201 |
| KirinX90 | 3003 |
| Kirin9030 | 3113 |

由于AI处理器架构版本区别，Ascend910B/Ascend910C和KirinX90/Kirin9030 主要差异请参见下表。具体影响的API，详见[基础API迁移指导](cannkit-basic-l2cache.md)和[高阶API迁移指导](cannkit-adv-api.md)。

**表2** KirinX90/Kirin9030相对Ascend910B/Ascend910C的主要差异说明

| 差异点 | 影响和应对策略 |
| --- | --- |
| 不支持GM操作使能L2 Cache | 只影响性能、不影响功能。 |
| 不支持原子操作 | 详见不支持开发者在GM完成Atomic操作。开发者需要在NPU片上的Buffer完成计算后，再使用基础API DataCopy将计算结果从NPU片上的Buffer搬到GM。 |
| 数据类型差异（不支持bfloat16\_t、Cube计算不支持float、Mmad数据格式差异等） | 建议替换成其它数据类型（如half），并根据本指南指导做数据转换。 |
| 不支持AI Core核间同步特性 | KirinX90/Kirin9030 AI处理器为单核耦合架构，软件兼容，等效为单核内部同步。开发者编程时，要避免对核数进行硬编码。 |
| 不支持通信特性 | 不支持。 |
| 不支持训练特性，包括右矩阵Load 3D功能、LoadDataTranspose部分特性 | 不支持。 |
| KirinX90/Kirin9030 AI处理器为耦合架构，而Ascend910B/Ascend910C AI处理器为分离架构 | 开发者编程时，不可以利用ASCENDC\_IS\_AIV/ASCENDC\_IS\_AIC宏进行AIV/AIC区分编程。 |
| 硬件规格 | 开发者编程时，开发者应避免对硬件规格进行硬编码，而应通过从Platform中获取硬件规范，实现参数化编程。 |
