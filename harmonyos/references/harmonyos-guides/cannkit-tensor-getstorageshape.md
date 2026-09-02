---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getstorageshape
title: GetStorageShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > GetStorageShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28a08ad639fec82da140caf664c8fbfa2e14bb7b3ec5c255064565bb54fc3755
---

## 函数功能

获取运行时Tensor的StorageShape，此shape对象为只读。StorageShape和[GetOriginShape](cannkit-tensor-getoriginshape.md)的区别如下。OriginShape是Tensor最初创建时的形状，StorageShape是保存Tensor数据的底层存储的形状。运行时为了适配底层硬件，Tensor的StorageShape和其OriginShape可能会有所不同。

## 函数原型

```cpp
const Shape &GetStorageShape() const
```

## 参数说明

无

## 返回值

只读的运行时shape引用。

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.GetStorageShape(); // 2,1,3
```
