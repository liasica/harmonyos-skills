---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeinfo
title: GetComputeNodeInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetComputeNodeInfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:725a384ab6227f70bab90d8deee35fa6b81195d572a2406c87267cef39f30ace
---

## 函数功能

获取本kernel对应的计算节点的信息。

图执行时本质上是执行图上的一个个结点的kernel在执行。本方法能够从KernelContext中获取保存的ComputeNodeInfo，而ComputeNodeInfo中包含InputDesc等信息。

## 函数原型

```
1. const ComputeNodeInfo *GetComputeNodeInfo() const
```

## 参数说明

无

## 返回值

计算节点的信息。

关于ComputeNodeInfo的定义，请参见[ComputeNodeInfo](cannkit-computenodeinfo-introduction.md)。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto compute_node_info = extend_context->GetComputeNodeInfo();
```
