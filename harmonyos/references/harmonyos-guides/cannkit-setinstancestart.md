---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstancestart
title: SetInstanceStart
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > SetInstanceStart
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2d93e14ff733edd9dcd0ff5bf759fc774a1bb163dff93aeea5524459be220e1a
---

## 函数功能

设置算子某个IR输入在实际输入中的起始序号（index）。

## 函数原型

```
1. void SetInstanceStart(const uint32_t instance_start)
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

```
1. const auto &ir_inputs = node->GetOpDesc()->GetIrInputs();  // 算子IR定义的所有输入
2. for (size_t i = 0; i < ir_inputs.size(); ++i) {
3. auto ins_info = compute_node_info.MutableInputInstanceInfo(i);  // 获取第i个IR输入对应的AnchorInstanceInfo对象
4. GE_ASSERT_NOTNULL(ins_info);
5. size_t input_index = ir_index_to_instance_index_pair_map[i].first; // 获取统计后的算子IR输入对应的实际输入index
6. ins_info->SetInstanceStart(input_index); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
7. }
```
