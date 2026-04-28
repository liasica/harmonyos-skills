---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getformat
title: GetFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:31eb01afdf0d1946aeb257c812fda2ea0641a21ede724e0d5d08e02f3924c4e9
---

## 函数功能

获取Tensor的Format。

## 函数原型

```
1. ge::Format GetFormat() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| ge::Format | 返回tensor的Format值，默认值为FORMAT\_RESERVED。 |

## 异常处理

无

## 约束说明

无
