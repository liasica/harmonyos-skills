---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapedim
title: GetShapeDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetShapeDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9fe7f9d37c73a711d6efd65847ab31699e97ad99f499fb7dbd0b9e71c1dbfe9d
---

## 函数功能

获取shape第idx维度。

## 函数原型

```
1. int64_t GetShapeDim(const size_t idx) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| idx | 输入 | 维度的索引，索引从0开始。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int64\_t | 返回shape第idx位置的值，默认值为0。 |

## 异常处理

无

## 约束说明

无
