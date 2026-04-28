---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-setdim
title: SetDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Shape > SetDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:86b6c1f0d9d3e5d739d3ccd02ee752b7b6a2dc7799bbd2d6695e521b68e20a4d
---

## 函数功能

将Shape中第idx维度的值设置为value。

## 函数原型

```
1. graphStatus SetDim(size_t idx, int64_t value);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| idx | 输入 | Shape维度的索引，索引从0开始。 |
| value | 输入 | 需设置的值。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

## 异常处理

无

## 约束说明

使用SetDim接口前，只能使用Shape(const std::vector<int64\_t>& dims)构造shape对象。如果使用Shape()构造shape对象，使用SetDim接口将返回失败。
