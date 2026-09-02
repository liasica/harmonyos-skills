---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-delinputwithoriginaltype
title: DelInputWithOriginalType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > DelInputWithOriginalType
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4fc0eb723010364c8a32f432a9aed483ba60d53d5a6d0d20c89b89b5aca3407f
---

## 函数功能

根据算子类型，删除算子指定输入边。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const std::string &ori_type)
OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const char_t *ori_type)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| input\_idx | 输入 | 需要删除的输入边编号。 |
| ori\_type | 输入 | 删除节点的原始算子类型。 |

## 约束说明

无
