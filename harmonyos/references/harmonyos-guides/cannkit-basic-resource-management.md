---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-resource-management
title: 资源管理
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 资源管理
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0cb2171228af65258cc9a8aea0e50f011d0956c061d5d501fc7247e1b48129ca
---

KirinX90/Kirin9030 AI处理器为单核耦合架构，不支持资源管理类接口，具体如下。

**表1** 资源管理兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| CubeResGroupHandle、GroupBarrier、KfcWorkspace | 不支持。该API用于在分离模式下对AI Core计算资源分组管理，KirinX90/Kirin9030 AI处理器为单核耦合架构，不需要。 |
