---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-mutablestorageshape
title: MutableStorageShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > MutableStorageShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49cfeb5cb20a85bb5d69aaaebeca6d96d022f9ad8936a1aa62a3ec79e6f1d1e6
---

## 函数功能

获取运行时Tensor的shape，此shape对象是可变的。

## 函数原型

```cpp
Shape &MutableStorageShape()
```

## 参数说明

无

## 返回值

运行时shape的引用。

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableStorageShape(); // 2,1,3
```
