---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype
title: DataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > DataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-07-17
content_hash: sha256:5ad761a026600e671335582cef0f224792264eba939a959092f205f87c4121a9
---

DataType枚举值定义如下。

```cpp
enum DataType {
  DT_FLOAT = 0, // float type
  DT_FLOAT16 = 1, // fp16 type
  DT_INT8 = 2, // int8 type
  DT_INT32 = 3, // int32 type
  DT_UINT8 = 4, // uint8 type
                           // reserved
  DT_INT16 = 6, // int16 type
  DT_UINT16 = 7, // uint16 type
  DT_UINT32 = 8, // unsigned int32
  DT_INT64 = 9, // int64 type
  DT_UINT64 = 10, // unsigned int64
  DT_DOUBLE = 11, // double type
  DT_BOOL = 12, // bool type
  DT_STRING = 13, // string type
  DT_DUAL_SUB_INT8 = 14, // dual output int8 type
  DT_DUAL_SUB_UINT8 = 15, // dual output uint8 type
  DT_COMPLEX64 = 16, // complex64 type
  DT_COMPLEX128 = 17, // complex128 type
  DT_QINT8 = 18, // qint8 type
  DT_QINT16 = 19, // qint16 type
  DT_QINT32 = 20, // qint32 type
  DT_QUINT8 = 21, // quint8 type
  DT_QUINT16 = 22, // quint16 type
  DT_RESOURCE = 23, // resource type
  DT_STRING_REF = 24, // string ref type
  DT_DUAL = 25, // dual output type
  DT_VARIANT = 26, // dt_variant type
  DT_BF16 = 27, // bf16 type
  DT_UNDEFINED = 28, // 用于表示DataType字段尚未设置。
  DT_INT4 = 29, // int4 type
  DT_UINT1 = 30, // uint1 type
  DT_INT2 = 31, // int2 type
  DT_UINT2 = 32, // uint2 type
  DT_COMPLEX32 = 33, // complex32 type
  DT_MAX // 标记数据类型的边界。
};
```
