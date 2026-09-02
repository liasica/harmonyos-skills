---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinferdatatype
title: SetInferDataType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > SetInferDataType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bc6f0cf8d0f8a8abf06433d24790d466754f6e6a3c3bb86ad5794ff10d8fe6ee
---

## 函数功能

注册DataType推导函数。

## 函数原型

```cpp
OpDef &SetInferDataType(gert::OpImplRegisterV2::InferDataTypeKernelFunc func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | DataType推导函数。**InferDataTypeKernelFunc**类型定义如下。  using InferDataTypeKernelFunc = UINT32 (\*)(InferDataTypeContext \*); |

## 返回值

[OpDef](cannkit-input.md)算子定义。

## 约束说明

无
