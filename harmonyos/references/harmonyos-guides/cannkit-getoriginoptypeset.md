---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginoptypeset
title: GetOriginOpTypeSet
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetOriginOpTypeSet
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55cacf4c346c7d1060cff3454ab272a346f6d92caa57b2ff5b08887b155e6ec8
---

## 函数功能

获取原始模型的算子类型集合。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. std::set<std::string> GetOriginOpTypeSet () const;
2. Status GetOriginOpTypeSet(std::set<ge::AscendString> &ori_op_type) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ori\_op\_type | 输出 | 原始模型的算子类型集合。 |

## 约束说明

无
