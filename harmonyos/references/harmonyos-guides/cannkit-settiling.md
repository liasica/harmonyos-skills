---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling
title: SetTiling
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 原型注册与管理 > OpAICoreDef > SetTiling
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7438506a0adc63d13e74df4e38f0c5c7ec8ae1d89c4e12d603bf112fed57e162
---

## 函数功能

注册Tiling函数。

## 函数原型

```cpp
OpAICoreDef &SetTiling(gert::OpImplRegisterV2::TilingKernelFunc func);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| func | 输入 | Tiling函数。TilingKernelFunc类型定义如下。  using TilingKernelFunc = UINT32 (\*)(TilingContext \*); |

## 返回值

[OpAICoreDef](cannkit-settiling.md)算子定义。

## 约束说明

无
