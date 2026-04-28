---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-adv-api
title: 高阶API迁移指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:938eea2a6f6f7bad34995d3e39a59928620f24a9262510d5cc5b946800870a16
---

高阶API，数据类型支持范围存在差异，详见[《Ascend C算子接口》](cannkit-ascend-c-apis.md)。数据类型差异兼容策略，参考[数据类型](cannkit-basic-datatype.md)。下面重点描述接口功能差异的兼容说明。

## HCCL通信类

不支持HCCL通信类高阶API。

## 矩阵计算

KirinX90/Kirin9030支持Matmul高阶API，但在涉及领域特性的部分存在不兼容情况。

**表1** Matmul高阶API

| 接口名称 | 兼容说明 |
| --- | --- |
| SetHF32 | 不支持。 |
| SetSparseIndex | 不支持。 |
| MatmulConfig | 不支持IBShare模板。 |
