---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-getdim
title: GetDim
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Shape > GetDim
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4be040fc7cc1bd9c2568b7a9da9697996014198c11e83e4e9c96a0d83c76f03c
---

## 函数功能

获取Shape第idx维的长度。

## 函数原型

```
1. int64_t GetDim(size_t idx) const;
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| idx | 输入 | 维度索引，索引从0开始。 |

## 返回值

| 类型 | 描述 |
| --- | --- |
| int64\_t | 第idx维的长度。 |

## 异常处理

无

## 约束说明

无
