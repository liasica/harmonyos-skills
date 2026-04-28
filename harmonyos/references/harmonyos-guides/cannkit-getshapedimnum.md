---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapedimnum
title: GetShapeDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Tensor > GetShapeDimNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:106ba910ce7824b586009edc2eaf1603152d6833aeb6d45b9c07dbf7a5f6ae1b
---

## 函数功能

获取shape的维度大小，即rank大小。

## 函数原型

```
1. size_t GetShapeDimNum() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| size\_t | 返回shape的维度大小，即shape的rank，如果是unknown的rank，返回0。 |

## 异常处理

无

## 约束说明

无
