---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getlistint
title: GetListInt
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > RuntimeAttrs > GetListInt
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a22466e93f3082bd166447ec1834a31aaae5f9a8a915aa7b7ae09c83a8150aeb
---

## 函数功能

获取list int类型的属性值。

## 函数原型

```cpp
const TypedContinuousVector<int64_t> *GetListInt(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 属性在IR原型定义中以及在OP\_IMPL注册中的索引。 |

## 返回值

指向属性值的指针。

关于TypedContinuousVector类型的定义，请参见[TypedContinuousVector](cannkit-typedcontinuousvector-introduction.md)。

## 约束说明

无

## 调用示例

```cpp
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
const TypedContinuousVector<int64_t> *attr0 = runtime_attrs->GetListInt(0);
```
