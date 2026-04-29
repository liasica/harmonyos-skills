---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-system-var
title: 系统变量
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 系统变量
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9bf68aaa284aa32ddbd98d4e1d65a58d7b5b4bf6f35d452ea805755962479151
---

KirinX90/Kirin9030处理器不支持如下系统变量访问接口。

**表1** 系统变量兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| CheckLocalMemoryIA | 不支持。  CheckLocalMemoryIA监视设定范围内的UB读写行为，如果监视到有设定范围的读写行为则会出现EXCEPTION报错，未监视到设定范围的读写行为则不会报错。  该接口为调测接口，对功能无影响。 |
