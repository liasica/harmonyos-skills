---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-mutabledata
title: MutableData
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > MutableData
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b85165df25da59dfddffd4bbdd9944c2736d1736067fe3acb72047e7697536f
---

## 函数功能

获取首个元素的指针地址，[GetData(), reinterpret\_cast<T \*>(GetData()) + GetSize()]中的数据即为当前容器中保存的数据。

## 函数原型

```
1. void *MutableData()
```

## 参数说明

无

## 返回值

首个元素的指针地址。

## 约束说明

无

## 调用示例

```
1. size_t capacity = 100U;
2. auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
3. auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
4. auto cap = cv->MutableData();
```
