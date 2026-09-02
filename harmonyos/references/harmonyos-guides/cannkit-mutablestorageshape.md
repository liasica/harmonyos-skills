---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutablestorageshape
title: MutableStorageShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > MutableStorageShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:218216913d753fb2614882a5d15d09960b65949f8e4c5aae4807be5694560932
---

## 函数功能

获取可写的运行时shape。

## 函数原型

```cpp
Shape &MutableStorageShape()
```

## 参数说明

无

## 返回值

可写的运行时shape。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto storage_shape = shape.MutableStorageShape(); // 256,256,3
```
