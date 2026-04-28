---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setunknowndimnumshape
title: SetUnknownDimNumShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > SetUnknownDimNumShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f818bb9435ff74c86a32f5091805d0ecc8077b5992b2d0c7ca7d8fe65566b961
---

## 函数功能

设置tensor的shape为{-2}，用来表示tensor是完全未知的。

## 函数原型

```
1. graphStatus SetUnknownDimNumShape();
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
