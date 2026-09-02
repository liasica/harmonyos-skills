---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-inferdatatype
title: InferDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > OpImplRegisterV2 > InferDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:713f050ce514bfb7ed4b48500945b5222648a0cf0e3c076a2f933c833c6d90d7
---

## 函数功能

注册算子的InferDataType函数。

开发者需要为算子编写一个InferDataTypeKernelFunc类型的函数，并使用该接口进行注册。

InferDataTypeKernelFunc类型定义如下。

```cpp
using InferDataTypeKernelFunc = UINT32 (*)(InferDataTypeContext *);
```

## 函数原型

```cpp
OpImplRegisterV2 &InferDataType(InferDataTypeKernelFunc infer_datatype_func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| infer\_datatype\_func | 输入 | 要注册的自定义InferDataType函数，类型为InferDataTypeKernelFunc。 |

## 返回值

返回算子的OpImplRegisterV2对象，该对象新增注册了InferDataType函数infer\_datatype\_func。

## 约束说明

无
