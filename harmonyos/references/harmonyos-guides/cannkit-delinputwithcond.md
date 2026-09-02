---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-delinputwithcond
title: DelInputWithCond
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > DelInputWithCond
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dc076496136639ba1221dbcb55bea9be0e8354d75cf54413bd93f9d08381ad42
---

## 函数功能

根据算子属性，删除算子指定输入边。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &DelInputWithCond(int32_t inputIdx, const std::string &attrName, bool attrValue);
OpRegistrationData &DelInputWithCond(int32_t input_idx, const char_t *attr_name, bool attr_value);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| inputIdx | 输入 | 需要删除的输入边编号。 |
| attrName | 输入 | 属性名字。 |
| attrValue | 输入 | 属性的值。 |

## 约束说明

无
