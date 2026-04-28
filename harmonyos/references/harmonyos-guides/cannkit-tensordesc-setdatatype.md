---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setdatatype
title: SetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3aa0dc966058379d7a509b719b28a14803787913a62dbf7098cf7e6798a921d0
---

## 函数功能

向TensorDesc中设置Tensor的数据类型。

## 函数原型

```
1. void SetDataType(DataType dt);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dt | 输入 | 需设置的TensorDesc所描述的Tensor的数据类型信息。  关于DataType类型，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
