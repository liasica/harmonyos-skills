---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-create
title: Create
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > Create
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:391adde1cd1348c302973ce73e35c6ab9a25b81228f442adea0ebe1b32e1b4b7
---

## 函数功能

创建一个ContinuousVector实例，ContinuousVector不支持动态扩容。

## 函数原型

```cpp
template<typename T>  static std::unique_ptr<uint8_t[]> Create(size_t capacity, size_t &total_size)
template<typename T>  static std::unique_ptr<uint8_t[]> Create(const size_t capacity)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| T | 输入 | 实例中包含的元素类型。 |
| capacity | 输入 | 实例的最大容量。 |
| total\_size | 输出 | 本实例的总长度。 |

## 返回值

指向本实例的指针。

## 约束说明

无

## 调用示例

```cpp
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity); // 创建了一个可以存放100个int64_t数据的内存。
```
