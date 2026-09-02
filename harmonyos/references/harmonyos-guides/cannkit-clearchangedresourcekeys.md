---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-clearchangedresourcekeys
title: ClearChangedResourceKeys
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > ClearChangedResourceKeys
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:dcc1ea0d4f88206fa3ef4b427a06efa4cb0370786e68e29964c78bfbe7a7f985
---

## 函数功能

一般由框架调用。

当变化了的资源触发重新推导之后，需要调用该接口清除inference\_context中保存的变化了的资源标识。

## 函数原型

```cpp
void ClearChangedResourceKeys()
```

## 参数说明

无

## 返回值

无

## 约束说明

无
