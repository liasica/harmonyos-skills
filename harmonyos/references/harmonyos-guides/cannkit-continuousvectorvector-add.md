---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-add
title: Add
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVectorVector > Add
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f1063d2c09c19d6bfc4e59ac913b7eeaaacf395cfbe09ed89d4aaeaeca6fc0e5
---

## 函数功能

新增一个ContinuousVector元素，其中新增ContinuousVector元素的容量为inner\_vector\_capacity。

## 函数原型

```cpp
template<typename T> ContinuousVector *Add(size_t inner_vector_capacity)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| inner\_vector\_capacity | 输入 | 新增ContinuousVector元素的容量。 |

## 返回值

新增ContinuousVector元素的首地址。

## 约束说明

无

## 调用示例

```cpp
// 创建ContinuousVectorVector对象cvv
// ...
// 增加元素
size_t inner_vector_capacity = 2;
auto cv = cvv->Add(inner_vector_capacity);
```
