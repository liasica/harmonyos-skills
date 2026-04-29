---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-kernel-tiling
title: Kernel Tiling
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > Kernel Tiling
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be40eb2b532886d74d4fcc77170d80c665dbf0cf8339b7c81c2db5bf3b5e6d44
---

KirinX90/Kirin9030处理器不支持如下Kernel Tiling接口。

**表1** Kernel Tiling兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| KERNEL\_TASK\_TYPE\_DEFAULT、KERNEL\_TASK\_TYPE | 不支持。  KirinX90/Kirin9030 AI处理器为耦合架构(AI Core: 1 \* AIC + 1 \* AIV)，下发Task执行时，会将整个AI Core启动。当算子配置MIX\_AIC\_1\_2时，需要关注AIV核个数的差异对算子功能的影响。 |
