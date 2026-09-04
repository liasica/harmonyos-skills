---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginoptypeset
title: GetOriginOpTypeSet
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetOriginOpTypeSet
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4865185c99b6bef6076984eef421fc7979cb2caac1c53b3e1d40d47499f21c24
---

## 函数功能

获取原始模型的算子类型集合。

## 函数原型

![](https://media:401788444113475924) 

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
