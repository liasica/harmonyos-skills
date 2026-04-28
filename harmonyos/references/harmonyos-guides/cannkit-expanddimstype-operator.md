---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-expanddimstype-operator
title: operator==
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExpandDimsType > operator==
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9881e0716cfb6b6c7bca4276a57f81418c2af5509e06bcdf1a1c74112cbf9dcc
---

## 函数功能

判断本补维规则对象与另一个对象是否一致。

## 函数原型

```
1. bool operator==(const ExpandDimsType &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个补维规则对象。 |

## 返回值

true表示一致，false表示不一致。

## 约束说明

无

## 调用示例

```
1. ExpandDimsType type1("1001");
2. ExpandDimsType type2("1001");
3. bool is_same_type = type1 == type2; // true
```
