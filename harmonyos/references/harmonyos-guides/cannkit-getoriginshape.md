---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginshape
title: GetOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > GetOriginShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8fd8f5a5c1ae3613a09b3c83c914a24f9464cffa7be66c881e72356ce9c2d17
---

## 函数功能

获取原始shape。

## 函数原型

```cpp
const Shape &GetOriginShape() const
```

## 参数说明

无

## 返回值

原始shape

## 约束说明

无

## 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto origin_shape = shape.GetOriginShape(); // 3,256,256
```
