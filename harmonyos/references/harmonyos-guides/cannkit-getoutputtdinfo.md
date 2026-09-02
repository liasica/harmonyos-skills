---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputtdinfo
title: GetOutputTdInfo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > GetOutputTdInfo
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3b6a5f3a48d5dc810d448ce336d1ac3f537ee0175c0901c6b71a59b22919127
---

## 函数功能

获取算子指定输出的Tensor描述，注意，编译时无法确定的shape信息不在Tensor描述中（由于编译时无法确定shape，因此该Tensor描述里不包含shape信息）

## 函数原型

```cpp
const CompileTimeTensorDesc *GetOutputTdInfo(const size_t index) const
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子的输出索引，从0开始计数。 |

## 返回值

返回const类型的Tensor描述信息。

## 约束说明

无

## 调用示例

```cpp
auto compute_node_info = extend_kernel_context->GetComputeNodeInfo();
auto output_td = compute_node_info->GetOutputTdInfo(output_index);
```
