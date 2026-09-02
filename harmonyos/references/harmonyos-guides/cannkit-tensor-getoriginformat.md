---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c746badcd773e9bc773c99ff60d9aa0e40053116ec73c59d8b9cafebe097935e
---

## 函数功能

获取Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```cpp
ge::Format GetOriginFormat() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| ge::Format | 返回tensor的原始Format值，默认值为FORMAT\_RESERVED。 |

## 异常处理

无

## 约束说明

无
