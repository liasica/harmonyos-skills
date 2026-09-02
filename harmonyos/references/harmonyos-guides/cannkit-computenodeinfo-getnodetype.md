---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-getnodetype
title: GetNodeType
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetNodeType
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:906eea046e9f5a0fb212b45714366b38272fb5635eb18960dacadd83205583a0
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
auto node_type = compute_node_info.GetNodeType();
```
