---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkernelname
title: GetKernelName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetKernelName
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ef9ccacebaedf68f17f3a148da5b88cf3ab0e6fe4ff49d4659c976425ad9147a
---

## 函数功能

获取当前内核的名称。

## 函数原型

```cpp
const char *GetKernelName() const
```

## 参数说明

无

## 返回值

当前内核的名称。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto kernel_name = extend_context->GetKernelName();
```
