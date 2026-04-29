---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-datacopy
title: 数据搬运
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 数据搬运
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a3a24850a8f4b0043ad487612ea80ac8068720c17ea2760def934bdd0e45a08
---

KirinX90/Kirin9030处理器部分数据通路特性存在差异，具体如下。

**表1** 数据搬运兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| DataCopy: L1 Buffer->Bias Table Buffer | - KirinX90 AI处理器：浮点下只支持fp16数据类型，在L1 Buffer要求非紧凑排布（占32bit空间，其中高16bit为dummy数据）; 做 L1 Buffer->Bias Table Buffer数据搬运后，fp16数据和dummy数据会一起搬运到Bias Table Buffer里。Mmad基础API计算时会自动获取有效的低16bit数据参与计算。  - Kirin9030 AI处理器：L1 Buffer到Bias Table Buffer搬运的每块数据块长度从64B变更为32B，目的操作数上数据两块之间间隔的单位从64B变更为32B；浮点下只支持fp16数据类型，在L1 Buffer要求紧凑排布。 |
| LoadDataWithSparse | 不支持。不支持结构化稀疏功能，因此算子需要采用正常稠密的矩阵计算。 |
| SetLoadDataBoundary | 不支持。该接口用于设置Load3D时L1 Buffer的边界值。如果指令在处理源操作数时，源操作数在L1 Buffer上的地址超出设置的边界，则会从L1 Buffer的起始地址开始读取数据。设置为0表示无边界，可以使用整个L1 Buffer。  如果需要在L1 Buffer上循环读取操作数，需要将对应的Load3D接口手动拆分成多条指令，手动绕回。 |
| LoadDataWithTranspose | Kirin9030 AI处理器：要求dstFracGap = 0。 |
| LoadData | 不支持，B1->B2的Load3Dv2接口。 |
