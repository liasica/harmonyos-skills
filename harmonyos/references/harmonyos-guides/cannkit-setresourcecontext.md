---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setresourcecontext
title: SetResourceContext
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > SetResourceContext
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:251bfc06828c2e251bdc5b19852db234728b2f219b34d23513dec53ef05748a6
---

## 函数功能

为标识为key的资源，设置资源上下文对象，并交由资源上下文管理器管理。

此接口一般由写类型的资源类算子调用，如stack push等。

## 函数原型

```
1. graphStatus SetResourceContext(const ge::AscendString &key, ResourceContext *resource_context)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| key | 输入 | 资源唯一标识。 |
| resource\_context | 输入 | 资源上下文对象指针，可参见[GetResourceContext](cannkit-getresourcecontext.md)接口的[返回值](cannkit-getresourcecontext.md#返回值)。 |

## 返回值

graphStatus：GRAPH\_SUCCESS，代表成功；GRAPH\_FAILED，代表失败。

## 约束说明

若使用[Create](cannkit-create.md)接口创建InferenceContext时未传入resource context管理器指针，则该接口返回失败。
