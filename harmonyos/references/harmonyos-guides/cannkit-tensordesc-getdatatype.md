---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getdatatype
title: GetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:39524505b0d5bdd92486d38ee0a4538a61d39063093cce3d9646360c89f0c1bd
---

## 函数功能

获取TensorDesc所描述Tensor的数据类型。

## 函数原型

```cpp
DataType GetDataType() const;
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

无
