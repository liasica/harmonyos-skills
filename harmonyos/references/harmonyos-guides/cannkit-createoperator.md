---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createoperator
title: CreateOperator
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OperatorFactory > CreateOperator
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbce2e3cc346d65d2e8ed085cc84dea8a24c170aaf79e20240b7ec19c0751876
---

## 函数功能

基于算子名称和算子类型获取算子对象实例。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. static Operator CreateOperator(const std::string &operator_name, const std::string &operator_type)
2. static Operator CreateOperator(const char_t *const operator_name, const char_t *const operator_type)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_name | 输入 | 算子名称。 |
| operator\_type | 输入 | 算子类型。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| string | 算子对象实例。 |

## 约束说明

无
