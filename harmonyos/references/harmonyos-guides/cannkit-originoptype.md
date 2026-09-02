---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-originoptype
title: OriginOpType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > OriginOpType
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8682d649ebb05f857498a64d89c6a79f30827109775386de2b8b7537fa297ffa
---

## 函数功能

设置原始模型的算子类型或算子类型列表。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &OriginOpType(const std::vector<ge::AscendString> &ori_op_type_list);
OpRegistrationData &OriginOpType(const char_t *ori_op_type);
OpRegistrationData &OriginOpType(const std::initializer_list<std::string> &ori_optype_list);
OpRegistrationData &OriginOpType(const std::string &ori_optype);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ori\_op\_type\_list/ori\_optype\_list | 输入 | 原始模型算子类型列表 |
| ori\_op\_type/ori\_optype | 输入 | 原始模型算子类型 |
