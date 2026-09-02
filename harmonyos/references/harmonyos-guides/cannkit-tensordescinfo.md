---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordescinfo
title: TensorDescInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDescInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:604002b7a8b2bcc8b12cd8db6939fdc2511fed6f5f4835241e86f612cbd39f09
---

```cpp
struct TensorDescInfo {
    Format format_ = FORMAT_RESERVED;        /* tbe op注册支持的格式 */
    DataType dataType_ = DT_UNDEFINED;       /* tbe op注册支持的数据类型 */
    };
```

Format为枚举类型，定义请参考[Format](cannkit-ge-format.md)。

DataType为枚举类型，定义请参考[DataType](cannkit-ge-datatype.md)。
