---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d2db09f9f243df89821dcbeb82f07c454cb79d67e136a6785f36d25da88f4027
---

## 函数功能

获取TensorDesc所描述Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```
1. Format GetOriginFormat() const;
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
