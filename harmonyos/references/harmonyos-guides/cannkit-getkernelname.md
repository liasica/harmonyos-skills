---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getkernelname
title: GetKernelName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetKernelName
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ab9f24cb25d3c7d08df9402face1d6ea9b79202797d38bb99908c9b0ad10a1bd
---

## 函数功能

获取当前内核的名称。

## 函数原型

```
1. const char *GetKernelName() const
```

## 参数说明

无

## 返回值

当前内核的名称。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto kernel_name = extend_context->GetKernelName();
```
