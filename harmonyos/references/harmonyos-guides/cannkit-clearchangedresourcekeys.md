---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-clearchangedresourcekeys
title: ClearChangedResourceKeys
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > InferenceContext > ClearChangedResourceKeys
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c92fbe9df6116de667d5b8287dba713243aec0c94849270a6e7f8d7a9d06dd19
---

## 函数功能

一般由框架调用。

当变化了的资源触发重新推导之后，需要调用该接口清除inference\_context中保存的变化了的资源标识。

## 函数原型

```
1. void ClearChangedResourceKeys()
```

## 参数说明

无

## 返回值

无

## 约束说明

无
