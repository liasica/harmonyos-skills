---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getoriginshape
title: GetOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetOriginShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8aab6aefa638e1f32e894ddbb1726d3b0643e212338ef16f20a37d83eb06c40d
---

## 函数功能

获取TensorDesc所描述Tensor的原始Shape。

## 函数原型

```cpp
Shape GetOriginShape() const;
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
