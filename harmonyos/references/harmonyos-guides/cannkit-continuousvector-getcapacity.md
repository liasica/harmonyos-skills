---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-getcapacity
title: GetCapacity
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > GetCapacity
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc85128fcb2f505d0b3c3bac2bcb24dfbbe21a88b0568d534bea3ad312016939
---

## 函数功能

获取最大可保存的元素个数。

## 函数原型

```
1. size_t GetCapacity() const
```

## 参数说明

无

## 返回值

最大可保存的元素个数。

## 约束说明

无

## 调用示例

```
1. size_t capacity = 100U;
2. auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
3. auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
4. auto cap = cv->GetCapacity(); // 100U
```
