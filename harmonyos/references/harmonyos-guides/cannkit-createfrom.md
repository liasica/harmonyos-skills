---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createfrom
title: CreateFrom
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AttrValue > CreateFrom
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e60537a8a0795a42ca892184df349f0de928efd7ea303f6d3e4713e444e9a1f4
---

## 函数功能

将传入的DT类型（支持int64\_t、float、std::string类型）的参数转换为对应T类型（支持INT、FLOAT、STR类型）的参数。

* 支持将int64\_t类型转换为INT类型。
* 支持将float类型转换为FLOAT类型。
* 支持将std::string类型转换为STR类型。

## 函数原型

```cpp
template<typename T, typename DT>
static T CreateFrom(DT &&val)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| val | 输入 | DT类型的参数。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| - INT  - FLOAT  - STR | T类型的参数。 |

## 异常处理

无

## 约束说明

无
