---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsizebydatatype
title: GetSizeByDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > GetSizeByDataType
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b63aa706d30001c96178777adeeba1131eed423355a1ecfcbac262c9c1f195e
---

## 函数功能

根据传入的data\_type，获取该data\_type所占用的内存大小。

## 函数原型

```
1. inline int GetSizeByDataType(DataType data_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| data\_type | 输入 | 数据类型，请参见[DataType](cannkit-ge-datatype.md)。 |

## 返回值

该data\_type所占用的内存大小（单位为bytes），如果传入非法值或不支持的数据类型，返回-1。

## 异常处理

无

## 约束说明

无
