---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginoptypeset
title: GetOriginOpTypeSet
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetOriginOpTypeSet
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:141dc165e5c56b75c51e34a49d56c832258d733e670d2169b7892e66a0a28704
---

## 函数功能

获取原始模型的算子类型集合。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::set<std::string> GetOriginOpTypeSet () const;
Status GetOriginOpTypeSet(std::set<ge::AscendString> &ori_op_type) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ori\_op\_type | 输出 | 原始模型的算子类型集合。 |

## 约束说明

无
