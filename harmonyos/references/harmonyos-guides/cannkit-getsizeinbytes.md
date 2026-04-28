---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsizeinbytes
title: GetSizeInBytes
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetSizeInBytes
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:99b62b826ac552806e9d121cc71bb8151bfde085da4fa74a14294060579b589d
---

## 函数功能

根据传入的element\_count和data\_type，获取element\_count个该data\_type所占用的内存总大小。

## 函数原型

```
1. int64_t GetSizeInBytes(int64_t element_count, DataType data_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| element\_count | 输入 | 用于标识多少个data\_type。 |
| data\_type | 输入 | 数据类型，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

如果传入个数为非法值或传入不支持的数据类型，返回-1。

## 异常处理

无

## 约束说明

无
