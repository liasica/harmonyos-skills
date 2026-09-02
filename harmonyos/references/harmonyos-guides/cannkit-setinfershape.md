---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinfershape
title: SetInferShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpDef > SetInferShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:351285de3f80ede7716e43b4a75c92c968a461e09ef0489e7342d9847c372cac
---

## 函数功能

注册Shape推导函数。

## 函数原型

```cpp
OpDef &SetInferShape(gert::OpImplRegisterV2::InferShapeKernelFunc func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Shape推导函数。InferShapeKernelFunc类型定义如下。  using InferShapeKernelFunc = UINT32 (\*)(InferShapeContext \*); |

## 返回值

[OpDef](cannkit-input.md)算子定义。

## 约束说明

无
