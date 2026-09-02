---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getfusionparseparamfn
title: GetFusionParseParamFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetFusionParseParamFn
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8a1c32de0438edf85a4f56cd65de77499ec7049f4381f1250b8589dc63b30645
---

## 函数功能

获取解析融合算子属性的函数。

## 函数原型

```cpp
FusionParseParamFunc GetFusionParseParamFn() const
```

## 参数说明

无

## 约束说明

GetFusionParseParamFn接口后续版本将会废弃，请使用[GetFusionParseParamByOpFn](cannkit-getfusionparseparambyopfn.md)接口获取融合算子的属性。
