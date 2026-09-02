---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-getsize
title: GetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVectorVector > GetSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f69d669b412bab153792af5b6b87d1b72e9f909b531f9adc70fe963e9b81a80c
---

## 函数功能

获取当前存放的实际元素数量。

## 函数原型

```cpp
size_t GetSize() const
```

## 参数说明

无

## 返回值

当前存放的实际元素数量。

## 约束说明

无

## 调用示例

```cpp
// 创建ContinuousVectorVector对象cvv
// ...
// 增加元素
// ...
auto cv = cvv->add(inner_vector_capacity);
// ...
// 获取当前存放的实际元素数量
auto size = cvv->GetSize();
```
