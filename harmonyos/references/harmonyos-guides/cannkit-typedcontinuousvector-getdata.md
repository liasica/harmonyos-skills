---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-typedcontinuousvector-getdata
title: GetData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TypedContinuousVector > GetData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:8787f9c032d8388d52f3383bf62e8dbeca8814a9b270e6a3d712b19cfc4bf5be
---

## 函数功能

获取首个元素的指针地址，[GetData(), reinterpret\_cast<T \*>(GetData()) + GetSize()]中的数据即为当前容器中保存的数据。

## 函数原型

```cpp
const T *GetData() const
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
auto cap = cv->GetData<int64_t>();
```
