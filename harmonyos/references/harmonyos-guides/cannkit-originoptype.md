---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-originoptype
title: OriginOpType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > OriginOpType
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b9eb0bb5eff5d8608a5c3fac4b5fc84b85f079af151750d882cbc176e95b37ac
---

## 函数功能

设置原始模型的算子类型或算子类型列表。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. OpRegistrationData &OriginOpType(const std::vector<ge::AscendString> &ori_op_type_list);
2. OpRegistrationData &OriginOpType(const char_t *ori_op_type);
3. OpRegistrationData &OriginOpType(const std::initializer_list<std::string> &ori_optype_list);
4. OpRegistrationData &OriginOpType(const std::string &ori_optype);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ori\_op\_type\_list/ori\_optype\_list | 输入 | 原始模型算子类型列表 |
| ori\_op\_type/ori\_optype | 输入 | 原始模型算子类型 |
