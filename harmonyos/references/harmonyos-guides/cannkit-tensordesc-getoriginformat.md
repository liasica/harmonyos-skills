---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48fe1a840616a32f6bca47535d8241d4b2391483e2f050d6f5a7a9d1cacdb458
---

## 函数功能

获取TensorDesc所描述Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```cpp
Format GetOriginFormat() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Format](cannkit-ge-format.md) | TensorDesc所描述的Tensor的originFormat信息。  关于Format数据类型的定义，请参见[Format](cannkit-ge-format.md)。 |

## 异常处理

无

## 约束说明

无
