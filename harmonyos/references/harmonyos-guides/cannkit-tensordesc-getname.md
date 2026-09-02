---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getname
title: GetName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetName
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe5aeae22d687552d16c33c025d379003513be47cf9ca5c0b8c2d58f4e3332d1
---

## 函数功能

获取TensorDesc所描述Tensor的名称。

## 函数原型

**说明** 

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetName() const;
graphStatus GetName(AscendString &name);
graphStatus GetName(AscendString &name) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输出 | 算子名称。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 获取name成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
