---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputtensorrange
title: GetRequiredInputTensorRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeRangeContext > GetRequiredInputTensorRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9747fc70948a14a115d031c279cc592ce17fee10d4becddbee984310b1387923
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入tensor range指针。

## 函数原型

```
1. const TensorRange *GetRequiredInputTensorRange(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

TensorRange类型指针，定义如下。

```
1. using TensorRange = Range<Tensor>;
```

ir\_index非法时，返回空指针。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor range时，只能在tensor中获取到正确的shape、format、datatype信息。无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

## 调用示例

```
1. const auto infer_shape_range_func = [](gert::InferShapeRangeContext *context) -> graphStatus {
2. auto input_shape_range = context->GetRequiredInputTensorRange(0U);
3. auto output_shape_range = context->GetOutputShapeRange(0U);
4. *output_shape_range->GetMin() = input_shape_range->GetMin()->GetStorageShape();
5. *output_shape_range->GetMax() = input_shape_range->GetMax()->GetStorageShape();
6. return GRAPH_SUCCESS;
7. };
```
