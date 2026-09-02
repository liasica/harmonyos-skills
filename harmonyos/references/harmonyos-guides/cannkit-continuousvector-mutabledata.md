---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-mutabledata
title: MutableData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > MutableData
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aef8f0f82ec81fc505ccbbd4f67fe12f0a96e5ee191dff811ccd1388dab31e89
---

## 函数功能

获取首个元素的指针地址，[GetData(), reinterpret\_cast<T \*>(GetData()) + GetSize()]中的数据即为当前容器中保存的数据。

## 函数原型

```cpp
void *MutableData()
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
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto cap = cv->MutableData();
```
