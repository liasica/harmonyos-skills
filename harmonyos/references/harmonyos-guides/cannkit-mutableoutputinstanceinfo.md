---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableoutputinstanceinfo
title: MutableOutputInstanceInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > MutableOutputInstanceInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:de6be431cd24d7d69a842aa4a4433117e76d2b2a54a0a7e2f14c798e759e6b4c
---

## 函数功能

根据算子IR原型中的输出索引，获取对应的实例化对象。

## 函数原型

```cpp
AnchorInstanceInfo *MutableOutputInstanceInfo(const size_t ir_index)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输出 | 算子IR原型定义中的输出索引，从0开始计数。 |

## 返回值

返回的实例化对象的地址。返回对象为非const。

## 约束说明

无

## 调用示例

```cpp
for (size_t i = 0; i < ir_outputs.size(); ++i) {
  auto ins_info = compute_node_info.MutableOutputInstanceInfo(i);
  // ...
}
```
