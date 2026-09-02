---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-sync
title: 同步控制
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 同步控制
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-08-14
content_hash: sha256:1578be6df9db2828b15c90b34fe786ef1c4dae304bec761793542a417b3f71f1
---

KirinX90/Kirin9030处理器不支持多个NPU核之间硬同步能力（硬件同步是利用硬件自带的全核同步指令由硬件保证多核同步）。但由于KirinX90/Kirin9030处理器的NPU是单核耦合架构(AICORE: 1\*AIC +1\*AIV)，所以针对如下涉及多核的同步API进行软件兼容，开发者无需感知细节。

**表1** 多核同步兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| SyncAll（硬同步）、CrossCoreSetFlag、CrossCoreWaitFlag | 软件兼容。 |
