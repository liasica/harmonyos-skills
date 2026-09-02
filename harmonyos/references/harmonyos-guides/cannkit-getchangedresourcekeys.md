---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getchangedresourcekeys
title: GetChangedResourceKeys
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > GetChangedResourceKeys
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a539ba68086abc008c93b44848d5a00b7f8aa60cf5921198cc3e41f81cbb08c5
---

## 函数功能

一般由框架调用。

在结束写类型算子的推导后，可以调用该接口获取变化的资源标识。

## 函数原型

```cpp
const std::set<ge::AscendString>& GetChangedResourceKeys() const
```

## 参数说明

无

## 返回值

| 类型 | 描述 |
| --- | --- |
| std::set<ge::AscendString> | 已变化的资源标识集合。 |

## 约束说明

无
