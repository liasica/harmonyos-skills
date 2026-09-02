---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getomoptype
title: GetOmOptype
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetOmOptype
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:73baf19a9baab833d15148671567d6fa5f868b6fd781068cca3f86727e76daf5
---

## 函数功能

获取模型的算子类型。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetOmOptype () const;
Status GetOmOptype(ge::AscendString &om_op_type) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| om\_op\_type | 输出 | 模型的算子类型。 |

## 约束说明

无
