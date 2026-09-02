---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getshape
title: GetShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TensorDesc > GetShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b6a5142e13b04f905ec29d955e0eea35df252d418752eddab799de0e81c2514a
---

## 函数功能

获取TensorDesc所描述Tensor的Shape。

## 函数原型

```cpp
Shape GetShape() const;
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| [Shape](cannkit-shape-construction-and-destructor.md) | TensorDesc描述的shape。 |

## 异常处理

无

## 约束说明

由于返回的Shape信息为值拷贝，因此修改返回的Shape信息，不影响TensorDesc中已有的Shape信息。
