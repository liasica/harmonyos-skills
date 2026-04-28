---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputshaperange
title: GetRequiredInputShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeRangeContext > GetRequiredInputShapeRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e85509254d31ac3004888a728e61a293430e8a0bbd50d8161e41fc0473737d3b
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入shape range指针。

## 函数原型

```
1. const Range<Shape> *GetRequiredInputShapeRange(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

shape range指针，ir\_index非法时，返回空指针。

## 约束说明

无

## 调用示例

```
1. const auto infer_shape_range_func = [](gert::InferShapeRangeContext *context) -> graphStatus {
2. auto input_shape_range = context->GetRequiredInputShapeRange(0U);
3. auto output_shape_range = context->GetOutputShapeRange(0U);
4. output_shape_range->SetMin(const_cast<gert::Shape *>(input_shape_range->GetMin()));
5. output_shape_range->SetMax(const_cast<gert::Shape *>(input_shape_range->GetMax()));
6. return GRAPH_SUCCESS;
7. };
```
