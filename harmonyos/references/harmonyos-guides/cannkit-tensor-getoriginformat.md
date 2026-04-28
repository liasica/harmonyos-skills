---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getoriginformat
title: GetOriginFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetOriginFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca32cb2c121c8bdbffda1a1f567ad7a9bf42eeabba83fe146003db462107101b
---

## 函数功能

获取Tensor的原始Format。

该Format是指原始网络模型的Format。

## 函数原型

```
1. ge::Format GetOriginFormat() const;
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
