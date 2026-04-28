---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getvalue
title: GetValue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AttrValue > GetValue
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf75040873e923348b98ecfd241839c0d847ccce526d86e16612f0223bedb2d0
---

## 函数功能

获取属性key-value键值对中的value值，并将value值从T类型转换为DT类型。

* 支持将INT类型转换为int64\_t类型。
* 支持将FLOAT类型转换为float类型。
* 支持将STR类型转换为std::string类型。

## 函数原型

说明

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```
1. template<typename T, typename DT>
2. graphStatus GetValue(DT &val) const
3. graphStatus GetValue(AscendString &val);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| val | 输出 | DT类型的参数。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 数据类型转换成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
