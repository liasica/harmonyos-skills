---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getdatatype
title: GetDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:447e49f969fc2bb4c39bbe5bb32afcf0ce55a30a084a73faf49959ec22ec84ff
---

## 函数功能

获取Tensor的DataType。

## 函数原型

```
1. ge::DataType GetDataType() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| ge:: [DataType](cannkit-ge-datatype.md) | 返回tensor的DataType值，默认值为DT\_UNDEFINED。 |

## 异常处理

无

## 约束说明

无
