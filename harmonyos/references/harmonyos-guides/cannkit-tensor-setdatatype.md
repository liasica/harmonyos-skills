---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdatatype
title: SetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d97f2aae9940fb5f0647f7b14a498c4b0c756f99522ae7b687b3159bb814edb
---

## 函数功能

设置Tensor的Datatype。

## 函数原型

```
1. graphStatus SetDataType(const ge::DataType &dtype);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| dtype | 输入 | 需设置的DataType值。  关于DataType类型，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
