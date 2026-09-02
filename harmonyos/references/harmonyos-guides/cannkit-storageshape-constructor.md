---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-constructor
title: 构造函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > StorageShape > 构造函数
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b153d5f4b5dee8f0c071f9d1f18a0891dfc0346c3dfe35c7269b1deac9c01ae
---

## 函数功能

构造一个运行时shape实例。

## 函数原型

```cpp
StorageShape()
StorageShape(const std::initializer_list<int64_t> &origin_shape, const std::initializer_list<int64_t> &storage_shape)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| origin\_shape | 输入 | 原始shape。 |
| storage\_shape | 输入 | 运行时shape。 |

## 返回值

返回一个初始化后StorageShape对象。

## 约束说明

无

## 调用示例

```cpp
StorageShape shape({3, 256, 256}, {3, 256, 256});
```
