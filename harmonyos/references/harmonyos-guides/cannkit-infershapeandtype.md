---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapeandtype
title: InferShapeAndType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > InferShapeAndType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1c3663820655804e52a4e3d3e81b8919b8d5a1adeec6b4d12d806b327a5e9f4
---

## 函数功能

推导Operator输出的shape和DataType。

关于DataType数据类型的定义，请参见[DataType](cannkit-ge-datatype.md)。

## 函数原型

```cpp
graphStatus InferShapeAndType();
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
