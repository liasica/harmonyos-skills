---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getreliedonresourcekeys
title: GetReliedOnResourceKeys
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetReliedOnResourceKeys
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0518c25242e2961b830f51df4c0a899213f4c73cf09bb152025c742243d49673
---

## 函数功能

一般由框架调用。

在结束读类型算子的推导后，可以调用该接口获取依赖的资源标识。

## 函数原型

```
1. const std::set<ge::AscendString>& GetReliedOnResourceKeys() const
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| std::set<ge::AscendString> | 依赖的资源标识集合。 |

## 约束说明

无
