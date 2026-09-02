---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputtdinfo
title: GetInputTdInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetInputTdInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7e0505b41c00c7eb8ffb96e79ecee950f6b30e309c5be305a24a69057f012c7
---

## 函数功能

根据输入索引信息，获取算子的对应输入Tensor描述，注意，编译时无法确定的shape信息不在Tensor描述中（由于编译时无法确定shape，因此该Tensor描述里不包含shape信息）。

## 函数原型

```cpp
const CompileTimeTensorDesc *GetInputTdInfo(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子的输入索引，从0开始计数。 |

## 返回值

返回const类型的Tensor描述信息。

## 约束说明

无

## 调用示例

```cpp
auto compute_node_info = extend_kernel_context->GetComputeNodeInfo();
auto input_td = compute_node_info->GetInputTdInfo(input_index);
```
