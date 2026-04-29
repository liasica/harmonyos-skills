---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getomoptype
title: GetOmOptype
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetOmOptype
category: harmonyos-guides
scraped_at: 2026-04-29T13:42:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aaf6fe0a7c5946ef7fd9f4684baed73ba1e78b5de4a7461214c596544d0983ae
---

## 函数功能

获取模型的算子类型。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. std::string GetOmOptype () const;
2. Status GetOmOptype(ge::AscendString &om_op_type) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| om\_op\_type | 输出 | 模型的算子类型。 |

## 约束说明

无
