---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershape
title: InferShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > InferShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e36f53ae1a486bf9172f50878a8fbda38583d6c9fe74e2f569bbd0fcd86313dc
---

## 函数功能

注册算子的InferShape函数。

开发者需要为算子编写一个InferShapeKernelFunc类型的函数，并使用该接口进行注册。

InferShapeKernelFunc 类型定义如下。

```cpp
using InferShapeKernelFunc = UINT32 (*)(InferShapeContext *);
```

InferShape函数的原型是确定的，其接受一个InferShapeContext类型作为输入，在此context上，可以获取到输入、输出的shape指针等内容（算子原型定义上的输入、输出、属性信息）。InferShape成功后，返回ge::GRAPH\_SUCCESS，其他返回值被认为推导失败。推导失败后，执行过程结束退出。

## 函数原型

```cpp
OpImplRegisterV2 &InferShape(InferShapeKernelFunc infer_shape_func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| infer\_shape\_func | 输入 | 要注册的自定义InferShape函数，类型为InferShapeKernelFunc。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了InferShape函数infer\_shape\_func。

## 约束说明

无
