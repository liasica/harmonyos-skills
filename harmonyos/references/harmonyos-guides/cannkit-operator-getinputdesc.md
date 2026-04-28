---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-getinputdesc
title: GetInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > GetInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0d52b457b058827eb94c91db6b608dfddb59bafab415bbf22d011be4640b64b4
---

## 函数功能

根据算子Input名称或Input索引获取算子Input的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. TensorDesc GetInputDesc(const std::string &name) const;
2. TensorDesc GetInputDescByName(const char_t *name) const;
3. TensorDesc GetInputDesc(uint32_t index) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子Input名称。  当无此算子Input名称时，则返回TensorDesc默认构造的对象，其中，主要设置[DataType](cannkit-ge-datatype.md)为DT\_FLOAT（表示float类型），[Format](cannkit-ge-format.md)为FORMAT\_NCHW（表示NCHW）。 |
| index | 输入 | 算子Input索引。  当无此算子Input索引时，则返回TensorDesc默认构造的对象，其中，主要设置[DataType](cannkit-ge-datatype.md)为DT\_FLOAT（表示float类型），[Format](cannkit-ge-format.md)为FORMAT\_NCHW（表示NCHW）。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| [TensorDesc](cannkit-tensordesc-construction-and-destructor.md) | 算子Input的TensorDesc。 |

## 异常处理

无

## 约束说明

无
