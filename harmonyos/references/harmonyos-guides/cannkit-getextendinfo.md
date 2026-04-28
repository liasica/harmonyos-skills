---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getextendinfo
title: GetExtendInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetExtendInfo
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d5e03dffa4233e57b95abd05901a92d273b58322cc77b92d209a65ce6ca35979
---

## 函数功能

获取本kernel的扩展信息。

## 函数原型

```
1. const KernelExtendInfo *GetExtendInfo() const
```

## 参数说明

无

## 返回值

本kernel的扩展信息。

关于KernelExtendInfo类型的定义，请参见[内部关联接口](cannkit-internal-associated-apis.md)KernelExtendInfo类。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto extend_info = extend_context->GetExtendInfo();
```
