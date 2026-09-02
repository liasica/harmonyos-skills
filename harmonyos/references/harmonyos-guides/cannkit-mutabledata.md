---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutabledata
title: MutableData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TypedContinuousVector > MutableData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:b1c4d39cc9f58eb4aba521e239efe460993c7c9657fc1012d6399be433f278fa
---

## 函数功能

获取首个元素的指针地址，[GetData(), reinterpret\_cast<T \*>(GetData()) + GetSize()]中的数据即为当前容器中保存的数据。

## 函数原型

```cpp
T *MutableData()
```

## 参数说明

无

## 返回值

首个元素的指针地址。

## 约束说明

无

## 调用示例

```cpp
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<TypedContinuousVector *>(cv_holder.get());
auto cap = cv->MutableData();
```
