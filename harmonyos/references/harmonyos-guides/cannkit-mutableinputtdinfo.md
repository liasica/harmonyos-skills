---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableinputtdinfo
title: MutableInputTdInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > MutableInputTdInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bf001e9cba1f322a13882d97c5faf2dd9758dcfc7d612f9eca814f8889cea721
---

## 函数功能

根据输入索引信息，获取算子的对应输入Tensor描述，注意，编译时无法确定的shape信息不在Tensor描述中（由于编译时无法确定shape，因此该Tensor描述里不包含shape信息）。

## 函数原型

```cpp
CompileTimeTensorDesc *MutableInputTdInfo(const size_t index)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入对应的索引，从0开始计数。 |

## 返回值

返回Tensor描述。返回对象为非const。

## 约束说明

无

## 调用示例

```cpp
  for (size_t i = 0; i < compute_node_info.GetInputsNum(); ++i) {
    auto td = compute_node_info.MutableInputTdInfo(i);
    // ...
  }
```
