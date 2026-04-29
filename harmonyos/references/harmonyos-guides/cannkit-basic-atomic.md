---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-atomic
title: 原子操作
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 原子操作
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5128e4f7cdc214442e2a0b6a5ea4ec1a9ad84f5760cf3f7063b22448de27395f
---

KirinX90/Kirin9030处理器不支持Atomic特性，具体包含如下接口。

**表1** 原子操作兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| SetAtomicAdd、SetAtomicType、SetAtomicNone、SetAtomicMax、SetAtomicMin、SetStoreAtomicConfig、GetStoreAtomicConfig | 不支持。  KirinX90/Kirin9030处理器不支持开发者在GM完成Atomic操作。开发者需要在NPU片上的Buffer完成计算后，再使用基础API DataCopy将计算结果从NPU片上的Buffer搬到GM。 |
