---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputtensorrange
title: GetInputTensorRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeRangeContext > GetInputTensorRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf18ead88668df9111e34a7687538dc2e57cf1c42795d28c5fd204d1cbc84835
---

## 函数功能

根据算子输入索引获取对应的输入tensor range指针。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. using TensorRange = Range<Tensor>
2. const TensorRange *GetInputTensorRange(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

输入tensor range的指针，index非法时，返回空指针。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor range时，只能在tensor中获取到正确的shape、format、datatype信息，无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

## 调用示例

```
1. const auto infer_shape_range_func = [](gert::InferShapeRangeContext *context) -> graphStatus {
2. auto input_shape_range = context->GetInputTensorRange(0U);
3. auto output_shape_range = context->GetOutputShapeRange(0U);
4. *output_shape_range->GetMin() = input_shape_range->GetMin()->GetStorageShape();
5. *output_shape_range->GetMax() = input_shape_range->GetMax()->GetStorageShape();
6. return GRAPH_SUCCESS;
7. };
```
