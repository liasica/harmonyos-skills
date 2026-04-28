---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updateinputdesc
title: UpdateInputDesc
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Operator > UpdateInputDesc
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8649cebc0eee43bcced8d734c8ecb4485753114082a2a189d59d8e89dab8285f
---

## 函数功能

根据算子Input名称更新Input的TensorDesc。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. graphStatus UpdateInputDesc(const std::string &name, const TensorDesc &tensor_desc);
2. graphStatus UpdateInputDesc(const char_t *name, const TensorDesc &tensor_desc);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 算子Input名称。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 更新TensorDesc成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

| 异常场景 | 说明 |
| --- | --- |
| 无对应name输入 | 函数提前结束，返回GRAPH\_FAILED。 |

## 约束说明

无
