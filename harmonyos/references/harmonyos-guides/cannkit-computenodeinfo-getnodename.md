---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-getnodename
title: GetNodeName
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetNodeName
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:03c40f5d883189d51be4ae59eb6f280bed854124d05f6d5388b70f6e70d5dd99
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

返回算子的名称。

## 约束说明

无

## 调用示例

```cpp
auto node_name = compute_node_info.GetNodeName();
```
