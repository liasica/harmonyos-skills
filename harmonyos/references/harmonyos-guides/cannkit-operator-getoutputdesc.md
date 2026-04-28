---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-getoutputdesc
title: GetOutputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetOutputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bd4b61b6409febeb933d1e467e3b96acb87dfaa016440fa14721671139f696a6
---

## 函数功能

根据算子Output名称或Output索引获取算子Output的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. TensorDesc GetOutputDesc(const std::string &name) const;
2. TensorDesc GetOutputDescByName(const char_t *name) const;
3. TensorDesc GetOutputDesc(uint32_t index) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子Output名称。  当无此算子Output名称时，返回TensorDesc默认构造的对象，其中，主要设置[DataType](cannkit-ge-datatype.md)为DT\_FLOAT（表示float类型），[Format](cannkit-ge-format.md)为FORMAT\_NCHW（表示NCHW）。 |
| index | 输入 | 算子Output索引。  当无此算子Output索引时，则返回TensorDesc默认构造的对象，其中，主要设置[DataType](cannkit-ge-datatype.md)为DT\_FLOAT（表示float类型），[Format](cannkit-ge-format.md)为FORMAT\_NCHW（表示NCHW）。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| [TensorDesc](cannkit-tensordesc-construction-and-destructor.md) | 算子Output的TensorDesc。 |

## 异常处理

无

## 约束说明

无
