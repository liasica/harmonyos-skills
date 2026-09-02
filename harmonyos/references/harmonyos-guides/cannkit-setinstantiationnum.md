---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstantiationnum
title: SetInstantiationNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > SetInstantiationNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:ee4c013fbfa0db43cfd888442d29f59d010c0e41d274217f03d13e55d616f05c
---

## 函数功能

设置IR定义某个输入对应的实际输入个数。

## 函数原型

```cpp
void SetInstantiationNum(const uint32_t instantiation_num)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| instantiation\_num | 输入 | 实例化的个数。 |

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
  size_t instance_num = ir_index_to_instance_index_pair_map[i].second; // 获取统计后的算子IR输入对应的实际输入个数
  ins_info->SetInstantiationNum(instance_num); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
}
```
