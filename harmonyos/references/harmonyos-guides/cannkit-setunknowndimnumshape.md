---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setunknowndimnumshape
title: SetUnknownDimNumShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetUnknownDimNumShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e502e15986d1a5e50f74f66d69db075b2d7e2868196d1546e77b856ccaf27964
---

## 函数功能

设置tensor的shape为{-2}，用来表示tensor是完全未知的。

## 函数原型

```cpp
graphStatus SetUnknownDimNumShape();
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 函数执行结果。执行成功，则该值为GRAPH\_SUCCESS(即0)，其他值则为执行失败。 |

## 异常处理

无

## 约束说明

无
