---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isexistop
title: IsExistOp
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OperatorFactory > IsExistOp
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f7121f56213dceea8f2453a03cdea74207956b0d7a25d58d229df16c0bc1e8d2
---

## 函数功能

查询指定的算子类型是否支持。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. static bool IsExistOp(const std::string &operator_type)
2. static bool IsExistOp(const char_t *const operator_type)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| bool | - true：支持此算子。  - false：不支持此算子。 |

## 约束说明

无
