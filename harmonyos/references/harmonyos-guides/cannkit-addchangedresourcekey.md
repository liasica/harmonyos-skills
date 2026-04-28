---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-addchangedresourcekey
title: AddChangedResourceKey
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > AddChangedResourceKey
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8bdeca06bcf3e56ad0de37c71e7aa5b99a6f6ee7218ad433cd082b30b2b4f62b
---

## 函数功能

在写类型的资源算子（如stack push）推导过程中，若资源shape变化了，调用该接口通知框架。

框架依据变化的资源key，触发对应读算子（如stack pop）的重新推导。

## 函数原型

```
1. graphStatus AddChangedResourceKey(const ge::AscendString &key)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| key | 输入 | 资源唯一标识。 |

## 返回值

graphStatus：GRAPH\_SUCCESS，代表成功；GRAPH\_FAILED，代表失败。

## 约束说明

无
