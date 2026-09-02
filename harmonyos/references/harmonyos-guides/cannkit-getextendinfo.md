---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getextendinfo
title: GetExtendInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetExtendInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe0b91df5a0aba3e6f572304edb1470d8c8bcbb96801c4563f894bc9fb7970c4
---

## 函数功能

获取本kernel的扩展信息。

## 函数原型

```cpp
const KernelExtendInfo *GetExtendInfo() const
```

## 参数说明

无

## 返回值

本kernel的扩展信息。

关于KernelExtendInfo类型的定义，请参见[内部关联接口](cannkit-internal-associated-apis.md)KernelExtendInfo类。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto extend_info = extend_context->GetExtendInfo();
```
