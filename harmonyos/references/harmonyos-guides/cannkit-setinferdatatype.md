---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinferdatatype
title: SetInferDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > SetInferDataType
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b44acd94c9f039342d0856a5d5dfc0f8507e2bdcbe760e0c7c7870017ca7a40
---

## 函数功能

注册DataType推导函数。

## 函数原型

```
1. OpDef &SetInferDataType(gert::OpImplRegisterV2::InferDataTypeKernelFunc func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | DataType推导函数。**InferDataTypeKernelFunc**类型定义如下。  using InferDataTypeKernelFunc = UINT32 (\*)(InferDataTypeContext \*); |

## 返回值

[OpDef](cannkit-input.md)算子定义。

## 约束说明

无
