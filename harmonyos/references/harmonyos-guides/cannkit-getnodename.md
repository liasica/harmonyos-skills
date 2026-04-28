---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodename
title: GetNodeName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetNodeName
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ec8a637116654e7caab0f1e14a392c13977ba59d15b82e7194a9eedbcee31c7
---

## 函数功能

获取算子的名称。

## 函数原型

```
1. const char *GetNodeName() const
```

## 参数说明

无

## 返回值

算子的名称。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto node_name = extend_context->GetNodeName();
```
