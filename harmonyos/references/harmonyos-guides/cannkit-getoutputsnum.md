---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputsnum
title: GetOutputsNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetOutputsNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:901e825738dda7cd302825ba09c5603337712d23a119de1d3125c05104aa5c17
---

## 函数功能

获取算子在网络中的实际输出个数。

## 函数原型

```cpp
size_t GetOutputsNum() const
```

## 参数说明

无

## 返回值

算子的实际输出个数。

## 约束说明

无

## 调用示例

```cpp
size_t index = compute_node_info->GetOutputsNum();
```
