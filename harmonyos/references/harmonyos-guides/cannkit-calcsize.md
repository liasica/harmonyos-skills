---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-calcsize
title: CalcSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > CalcSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:f04859a15c9eb5f31f619ebf73298272cdcc989ab767c7a13c22db03a89b0248
---

## 函数功能

用于计算算子对应的ComputeNodeInfo需要预分配的内存空间大小。

ComputeNodeInfo的内存空间是平铺式的，内存依次存放ComputeNodeInfo自身的数据成员、算子IR定义输入个数的Anchor信息、实际输入个数和输出个数的编译阶段的Tensor描述信息以及属性信息。该函数的计算结果不包含属性信息所占的内存空间大小。

## 函数原型

```cpp
static ge::graphStatus CalcSize(const size_t ir_inputs_num, const size_t inputs_num, const size_t outputs_num, size_t &total_size);
static ge::graphStatus CalcSize(const size_t ir_inputs_num, const size_t ir_outputs_num, const size_t inputs_num, const size_t outputs_num, size_t &total_size);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_inputs\_num | 输入 | 算子IR原型定义的输入个数。 |
| ir\_outputs\_num | 输出 | 算子IR原型定义的输出个数。 |
| inputs\_num | 输入 | 算子实际的输入个数。 |
| outputs\_num | 输出 | 算子实际的输出个数。 |
| total\_size | 输出 | 需要预分配的ComputeNodeInfo和相关信息的内存总大小，不包含RuntimeAttrs的内存大小。 |

## 返回值

返回值为graphStatus类型（uint32\_t），其不同的状态取值说明如下。

| 状态 | 值 | 说明 |
| --- | --- | --- |
| ge::GRAPH\_SUCCESS | 0 | 执行成功。 |
| ge::GRAPH\_PARAM\_INVALID | 50331649 | 执行失败，参数无效，校验未通过。 |

## 约束说明

无

## 调用示例

```cpp
auto ir_input_num = node->GetOpDesc()->GetIrInputs().size();
auto input_num = node->GetInDataNodesAndAnchors().size();
auto output_num = node->GetAllOutDataAnchorsSize();
GE_ASSERT_SUCCESS(ComputeNodeInfo::CalcSize(ir_input_num, input_num, output_num, total_size));
```
