---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-l2cache
title: L2 Cache
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > L2 Cache
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f0853ac891c8407948e05681b61a0f517b80266f4e44a9ae982c5f383df9c56e
---

KirinX90/Kirin9030处理器不支持L2 Cache，GlobalTensor::SetL2CacheHint接口不生效。算子代码无需进行修改。只影响性能，不影响功能。
