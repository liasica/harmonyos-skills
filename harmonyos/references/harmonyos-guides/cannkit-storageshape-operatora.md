---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-operatora
title: operator==
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > operator==
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d332949ce8c1acdce3ea393d4efd489949c33195cb2ecb6e649a6672d0696d86
---

## 函数功能

判断shape是否相等。

## 函数原型

```cpp
bool operator==(const StorageShape &other) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| other | 输入 | 另一个shape。 |

## 返回值

true：相等。

false：不相等。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape0({3, 256, 256}, {256, 256, 3});
StorageShape shape1({3, 256, 256}, {3, 256, 256});
bool is_same_shape = shape0 == shape1; // false
```
