---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-mutableoriginshape
title: MutableOriginShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Tensor > MutableOriginShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b31f6730b2c8f5a75b6e857ce9ae9f87d9db03deeea600a3987fc84feacc94f
---

## 函数功能

获取Tensor的原始shape。

## 函数原型

```cpp
Shape &MutableOriginShape()
```

## 参数说明

无

## 返回值

原始shape引用。

关于Shape类型的定义，请参见[Shape](cannkit-shape-construction-and-destructor.md)。

## 约束说明

无

## 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableOriginShape(); // 1,2,3
```
