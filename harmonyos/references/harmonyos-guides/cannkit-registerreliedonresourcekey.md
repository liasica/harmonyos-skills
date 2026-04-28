---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-registerreliedonresourcekey
title: RegisterReliedOnResourceKey
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > RegisterReliedOnResourceKey
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cd62468c0bf4cd9ba56089b285b8a99e709c3e0354362d1b1a79791ea818aafb
---

## 函数功能

注册依赖的资源。

一般由读类型的算子调用，如stack pop。因读类型算子的shape依赖资源算子，调用该接口注册依赖的资源标识。

若资源算子shape变化可触发读类型算子的重新推导。

## 函数原型

```
1. graphStatus RegisterReliedOnResourceKey(const ge::AscendString &key)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| key | 输入 | 资源的唯一标识。 |

## 返回值

graphStatus：GRAPH\_SUCCESS，代表成功；GRAPH\_FAILED，代表失败。

## 约束说明

无
