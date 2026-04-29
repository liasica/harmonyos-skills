---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling
title: SetTiling
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAICoreDef > SetTiling
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a6fa0be99808da7254e2aad2384269e17db328750a8b0aaa3f75eb8e7a391175
---

## 函数功能

注册Tiling函数。

## 函数原型

```
1. OpAICoreDef &SetTiling(gert::OpImplRegisterV2::TilingKernelFunc func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Tiling函数。TilingKernelFunc类型定义如下。  using TilingKernelFunc = UINT32 (\*)(TilingContext \*); |

## 返回值

[OpAICoreDef](cannkit-settiling.md)算子定义。

## 约束说明

无
