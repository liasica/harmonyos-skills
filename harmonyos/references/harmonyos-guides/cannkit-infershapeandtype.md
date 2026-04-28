---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapeandtype
title: InferShapeAndType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > InferShapeAndType
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed885e96657b0d0afa2edae9fd2797324406af00ed97f5e62d09bb7ac7d92f8a
---

## 函数功能

推导Operator输出的shape和DataType。

关于DataType数据类型的定义，请参见[DataType](cannkit-ge-datatype.md)。

## 函数原型

```
1. graphStatus InferShapeAndType();
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 推导成功，返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
