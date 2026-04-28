---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorcreatorregister
title: OperatorCreatorRegister
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OperatorCreatorRegister
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4886ec216dd6dd76ad5683a3d1e6ba90ac09546536a6cc21c452eb26ebb68274
---

## 函数功能

OperatorCreatorRegister构造函数和析构函数。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. OperatorCreatorRegister(const std::string &operator_type, OpCreator const &op_creator);
2. OperatorCreatorRegister(const char_t *const operator_type, OpCreatorV2 const &op_creator);
3. ~OperatorCreatorRegister() = default;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| operator\_type | 输入 | 算子类型。 |
| op\_creator | 输入 | 算子构造函数。 |

## 返回值

OperatorCreatorRegister构造函数返回OperatorCreatorRegister类型的对象。

## 约束说明

算子注册接口，注册一个算子原型，此接口被其他头文件引用，一般不用由算子开发者直接调用。
