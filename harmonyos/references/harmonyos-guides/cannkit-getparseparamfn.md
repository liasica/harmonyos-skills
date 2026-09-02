---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getparseparamfn
title: GetParseParamFn
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > OpRegistrationData > GetParseParamFn
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:721fc93676a8e884dc89ddff7777118c098699a9ec0780fb8d900ec21f8e5dc1
---

## 函数功能

获取解析算子属性的函数。

## 函数原型

```cpp
ParseParamFunc GetParseParamFn() const
```

## 参数说明

无

## 约束说明

GetParseParamFn接口后续版本将会废弃，请使用[ParseParamsByOperatorFn](cannkit-parseparamsbyoperatorfn.md)接口获取算子属性。
