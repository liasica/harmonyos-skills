---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordescinfo
title: TensorDescInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDescInfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7f2d2b22c328e8f631a112de1abe0feda9370c375167a3ddafd7ea5a17f2f389
---

```
1. struct TensorDescInfo {
2. Format format_ = FORMAT_RESERVED;        /* tbe op register support format */
3. DataType dataType_ = DT_UNDEFINED;       /* tbe op register support datatype */
4. };
```

Format为枚举类型，定义请参考[Format](cannkit-ge-format.md)。

DataType为枚举类型，定义请参考[DataType](cannkit-ge-datatype.md)。
