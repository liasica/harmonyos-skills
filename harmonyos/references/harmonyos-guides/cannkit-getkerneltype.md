---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkerneltype
title: GetKernelType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetKernelType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f9828947f5e64d54926d4d5ce1736a41e5557be53d677f033b253e04aa5b7784
---

## 函数功能

获取当前内核的类型。

## 函数原型

```cpp
const char *GetKernelType() const
```

## 参数说明

无

## 返回值

当前内核的类型。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto kernel_type = extend_context->GetKernelType();
```
