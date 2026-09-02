---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-listtensortype
title: ListTensorType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ListTensorType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c432bb72fd3aaf51868a0ff48c28044e442a6c95566dd2bfda6b2728a96a915a
---

## 函数功能

ListTensorType类用以定义输入或者输出支持的数据类型，是TensorType的封装，用于标识支持多个数据类型的情况。

## 函数原型

```cpp
explicit ListTensorType(const TensorType &type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| type | 输入 | 数据类型，具体参见[TensorType](cannkit-tensortype.md)。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
