---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-elmtwise-infer-shapeandtype
title: ELMTWISE_INFER_SHAPEANDTYPE
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ELMTWISE_INFER_SHAPEANDTYPE
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cebf6861fd33308005ccc897014c5740d1b19b161f2c5e47e6bb07033f4105d1
---

## 函数功能

提供公共函数宏封装，供算子开发者开发InferShape函数。该函数基于输入的shape和dtype，设置输出的shape和dtype。

例如，输入shape为（1,2,3,4），dtype为float，则该宏会设置算子的输出shape为（1,2,3,4），输出dtype为float。

## 函数原型

```
1. ELMTWISE_INFER_SHAPEANDTYPE(in_name, out_name)
```

## 约束说明

无

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| in\_name | 输入 | 算子输入。 |
| out\_name | 输入 | 算子输出。 |

## 返回值

执行成功或失败。

## 调用示例

```
1. COMMON_INFER_FUNC_REG(DiagD, ELMTWISE_INFER_SHAPEANDTYPE("assist", "y"));
```
