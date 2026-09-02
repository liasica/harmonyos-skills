---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodename
title: GetNodeName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetNodeName
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4778765a99581177a0e77132319e22e063dc0293573680a9f1244183b0ea38a7
---

## 函数功能

获取算子的名称。

## 函数原型

```cpp
const char *GetNodeName() const
```

## 参数说明

无

## 返回值

算子的名称。

## 约束说明

无

## 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto node_name = extend_context->GetNodeName();
```
