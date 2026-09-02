---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getiroutputsnum
title: GetIrOutputsNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetIrOutputsNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:82812a6a6c7921d23fc7e1b7a1f8f0d7f72257f40b48c00cdec191afc14ee9dc
---

## 函数功能

获取算子IR原型定义中的输出个数。

## 函数原型

```cpp
size_t GetIrOutputsNum() const
```

## 参数说明

无

## 返回值

IR原型中定义的输出个数，size\_t类型。

## 约束说明

无

## 调用示例

```cpp
size_t index = compute_node_info->GetIrOutputsNum();
```
