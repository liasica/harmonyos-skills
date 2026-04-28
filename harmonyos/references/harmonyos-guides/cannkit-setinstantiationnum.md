---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinstantiationnum
title: SetInstantiationNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > AnchorInstanceInfo > SetInstantiationNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:62a62618f57c342c025a2c0156d244819a20a665c50a760dc6daeb2871781f60
---

## 函数功能

设置IR定义某个输入对应的实际输入个数。

## 函数原型

```
1. void SetInstantiationNum(const uint32_t instantiation_num)
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

```
1. const auto &ir_inputs = node->GetOpDesc()->GetIrInputs();  // 算子IR定义的所有输入
2. for (size_t i = 0; i < ir_inputs.size(); ++i) {
3. auto ins_info = compute_node_info.MutableInputInstanceInfo(i);  // 获取第i个IR输入对应的AnchorInstanceInfo对象
4. GE_ASSERT_NOTNULL(ins_info);
5. size_t instance_num = ir_index_to_instance_index_pair_map[i].second; // 获取统计后的算子IR输入对应的实际输入个数
6. ins_info->SetInstantiationNum(instance_num); // 将该信息保存到IR输入对应的AnchorInstanceInfo对象中
7. }
```
