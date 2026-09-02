---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ComputeNodeInfo > Init
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c10923dd272595e89871fd64e8810ca5e89cc975ea2c3e5326fae47cf0100434
---

## 函数功能

初始化ComputeNodeInfo类。

## 函数原型

```cpp
void Init(const size_t ir_inputs_num, const size_t inputs_num, const size_t outputs_num, const ge::char_t *node_name, const ge::char_t *node_type);
void Init(const size_t ir_inputs_num, const size_t ir_outputs_num, const size_t inputs_num, const size_t outputs_num, const size_t attr_size, const ge::char_t *node_name, const ge::char_t *node_type);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_inputs\_num | 输入 | 算子原型输入的个数。 |
| inputs\_num | 输入 | 算子实际输入个数。 |
| outputs\_num | 输入 | 算子实际输出个数。 |
| node\_name | 输入 | 节点名称。 |
| node\_type | 输入 | 节点类型（算子原型名称）。 |
| ir\_outputs\_num | 输入 | 算子原型输出的个数。 |
| attr\_size | 输入 | 属性个数。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
auto ir_input_num = node->GetOpDesc()->GetIrInputs().size();
auto ir_output_num = node->GetOpDesc()->GetIrOutputs().size();
auto inputs_num = node->GetInDataNodesAndAnchors().size();
auto outputs_num = node->GetOutDataNodesAndAnchors().size();
GE_ASSERT_SUCCESS(ComputeNodeInfo::Init(ir_input_num, inputs_num,outputs_num, node_name, node_type));
```
