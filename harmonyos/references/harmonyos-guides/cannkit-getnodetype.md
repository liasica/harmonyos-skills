---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodetype
title: GetNodeType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ExtendedKernelContext > GetNodeType
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95a76a7c1fd7737b9d0c3e19f1895278860ae8a7ef9c25c6c2d782f3bae90eb8
---

## 函数功能

获取算子的类型。

## 函数原型

```
1. const char *GetNodeType() const
```

## 参数说明

无

## 返回值

算子的类型。

## 约束说明

无

## 调用示例

```
1. // 假设已存在KernelContext *context
2. auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
3. auto node_type = extend_context->GetNodeType();
```
