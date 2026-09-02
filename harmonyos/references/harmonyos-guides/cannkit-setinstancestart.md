---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstancestart
title: SetInstanceStart
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > SetInstanceStart
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:1e6897dbd66bbfd4598b5ffb8a31a71972f8b1c45d3359f6c6412162b5b8d90a
---

## 函数功能

设置算子某个IR输入在实际输入中的起始序号（index）。

## 函数原型

```cpp
void SetInstanceStart(const uint32_t instance_start)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| instance\_start | 输入 | 首个实例化Anchor的index。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
const auto &ir_inputs = node->GetOpDesc()->GetIrInputs(); // 算子IR定义的所有输入
for (size_t i = 0; i < ir_inputs.size(); ++i) {
  auto ins_info = compute_node_info.MutableInputInstanceInfo(i); // 获取第i个IR输入对应的AnchorInstanceInfo对象
  GE_ASSERT_NOTNULL(ins_info);
  size_t input_index = ir_index_to_instance_index_pair_map[i].first; // 获取统计后的算子IR输入对应的实际输入index
  ins_info->SetInstanceStart(input_index); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
}
```
