---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-delinputwithoriginaltype
title: DelInputWithOriginalType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > DelInputWithOriginalType
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:757d7c2790807664b556d08db4daf819281e4a931098c782894a5b2c7537c82f
---

## 函数功能

根据算子类型，删除算子指定输入边。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const std::string &ori_type)
2. OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const char_t *ori_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| input\_idx | 输入 | 需要删除的输入边编号。 |
| ori\_type | 输入 | 删除节点的原始算子类型。 |

## 约束说明

无
