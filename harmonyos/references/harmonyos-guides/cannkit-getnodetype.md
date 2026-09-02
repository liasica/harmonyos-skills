---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodetype
title: GetNodeType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetNodeType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e52b8a99d843a722eb7289f8e95374fbfb89b3fb0dbdfda05751565b4e922e33
---

## 函数功能

获取算子的类型。

## 函数原型

```cpp
const char *GetNodeType() const
```

## 参数说明

无

## 返回值

算子的类型。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto node_type = extend_context->GetNodeType();
```
