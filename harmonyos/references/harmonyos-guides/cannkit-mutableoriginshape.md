---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableoriginshape
title: MutableOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > MutableOriginShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3cb8bcd34c0e0403e6c93dd1b99968b50db9041f7585552866ccd6f891cf0016
---

## 函数功能

获取可写的原始shape。

## 函数原型

```cpp
Shape &MutableOriginShape()
```

## 参数说明

无

## 返回值

可写的原始shape。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto origin_shape = shape.MutableOriginShape(); // 3,256,256
```
