---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputshaperange
title: GetInputShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeRangeContext > GetInputShapeRange
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b7db447edf24b53ce281caad7e0452765d78a5d05a21209dd35979261ee2d7da
---

## 函数功能

根据算子输入索引获取对应的输入shape range指针。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. const Range<Shape> *GetInputShapeRange(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

输入shape range指针，index非法时，返回空指针。

## 约束说明

无

## 调用示例

```
1. const auto infer_shape_range_func = [](gert::InferShapeRangeContext *context) -> graphStatus {
2. auto input_shape_range = context->GetInputShapeRange(0U);
3. auto output_shape_range = context->GetOutputShapeRange(0U);
4. output_shape_range->SetMin(const_cast<gert::Shape *>(input_shape_range->GetMin()));
5. output_shape_range->SetMax(const_cast<gert::Shape *>(input_shape_range->GetMax()));
6. return GRAPH_SUCCESS;
7. };
```
