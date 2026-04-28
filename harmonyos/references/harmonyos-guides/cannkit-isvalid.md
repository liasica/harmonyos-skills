---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isvalid
title: IsValid
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > IsValid
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cff487c08c5de68e25507e4fce268b5ebf2318df0813e8ad55472dd0fc4469a
---

## 函数功能

判断Tensor对象是否有效。

若实际Tensor数据的大小与TensorDesc所描述的Tensor数据大小一致，则有效。

## 函数原型

```
1. graphStatus IsValid()
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 如果Tensor对象有效，则返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
