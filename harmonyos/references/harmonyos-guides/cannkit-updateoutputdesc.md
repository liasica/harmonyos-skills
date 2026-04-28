---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updateoutputdesc
title: UpdateOutputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > UpdateOutputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f67b0e7e0e9599300025a0550827950d12226c0f44ca1ca8343bd00d3f4c2f07
---

## 函数功能

根据算子Output名称更新Output的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus UpdateOutputDesc(const std::string &name, const TensorDesc &tensor_desc);
2. graphStatus UpdateOutputDesc(const char_t *name, const TensorDesc &tensor_desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子Output名称。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 更新TensorDesc成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
