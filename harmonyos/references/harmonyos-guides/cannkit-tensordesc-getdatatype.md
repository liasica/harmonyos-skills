---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getdatatype
title: GetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a2f4aedf9b2506a6dd30e996d877ae766281dbf7c0cf0a953335cb59011c3ef
---

## 函数功能

获取TensorDesc所描述Tensor的数据类型。

## 函数原型

```
1. DataType GetDataType() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [DataType](cannkit-ge-datatype.md) | TensorDesc所描述的Tensor的数据类型。 |

## 异常处理

无

## 约束说明

由于返回的DataType信息为值拷贝，因此修改返回的DataType信息，不影响TensorDesc中已有的DataType信息。
