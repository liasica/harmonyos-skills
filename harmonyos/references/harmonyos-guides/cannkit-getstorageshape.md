---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getstorageshape
title: GetStorageShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > GetStorageShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3bb8e901e22e709e0bd28cc7d9810a8b5f3edc55e8c828b9c0ead4f441c38a67
---

## 函数功能

获取运行时shape。

## 函数原型

```cpp
const Shape &GetStorageShape() const
```

## 参数说明

无

## 返回值

运行时shape。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto storage_shape = shape.GetStorageShape(); // 256,256,3
```
