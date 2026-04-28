---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginshapedim
title: GetOriginShapeDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetOriginShapeDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:717d47f2c1542ab8efd6b20316a7004b31e099fea736ee280dfa0241db8b5bf1
---

## 函数功能

获取原始shape第idx维度。

## 函数原型

```
1. int64_t GetOriginShapeDim(const size_t idx) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| idx | 输入 | 维度的索引，索引从0开始。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int64\_t | 返回原始shape第idx位置的值。 |

## 异常处理

无

## 约束说明

无
