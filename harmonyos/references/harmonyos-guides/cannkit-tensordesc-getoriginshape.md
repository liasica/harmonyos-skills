---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getoriginshape
title: GetOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetOriginShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1f857a92c8138894de99f3cc68c6b7a6b39e758ea0bd55a8c622a05f8b31cd57
---

## 函数功能

获取TensorDesc所描述Tensor的原始Shape。

## 函数原型

```
1. Shape GetOriginShape() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Shape](cannkit-shape-construction-and-destructor.md) | TensorDesc描述的originShape。 |

## 异常处理

无

## 约束说明

无
