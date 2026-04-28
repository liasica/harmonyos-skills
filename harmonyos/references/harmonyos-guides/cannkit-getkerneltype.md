---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkerneltype
title: GetKernelType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetKernelType
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4adddbc510fac5d9bc2855afc03b21e00a01b11d09822d15920c1ba4ba5bb8e2
---

## 函数功能

获取当前内核的类型。

## 函数原型

```
1. const char *GetKernelType() const
```

## 参数说明

无

## 返回值

当前内核的类型。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto kernel_type = extend_context->GetKernelType();
```
