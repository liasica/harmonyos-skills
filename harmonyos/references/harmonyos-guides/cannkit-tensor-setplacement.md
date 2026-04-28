---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setplacement
title: SetPlacement
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > SetPlacement
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a40869e57d906324c87ff8eabc53cc2626e80968e531383d3b481063c68a098c
---

## 函数功能

设置Tensor的数据存放的位置。

## 函数原型

```
1. graphStatus SetPlacement(const ge::Placement &placement);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| placement | 输入 | 需设置的数据地址的值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

无
