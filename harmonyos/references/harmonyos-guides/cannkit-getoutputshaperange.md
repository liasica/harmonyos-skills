---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputshaperange
title: GetOutputShapeRange
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeRangeContext > GetOutputShapeRange
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8eeb49cba326b1d2a842b10eab71631f73c59f09308651e0af0f0c56bf202334
---

## 函数功能

根据算子输出索引获取对应的输出shape range指针。这里的输出索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```cpp
Range<Shape> *GetOutputShapeRange(const size_t index);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输出索引，从0开始计数。 |

## 返回值

输出shape range指针，index非法时，返回空指针。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferShapeRangeForXXX(gert::InferShapeRangeContext *context) {
  const auto x_shape_range = context->GetInputShapeRange(0);
  if (x_shape_range == nullptr) {
    // 防御式编程 ....
  }
  const auto min_shape = x_shape_range->GetMin();
  const auto max_shape = x_shape_range->GetMax();
 
  auto y_shape_range = context->GetOutputShapeRange(0);
  if (y_shape_range == nullptr) {
    // 防御式编程 ....
  }
  if (y_shape_range->GetMin() == nullptr || y_shape_range->GetMax() == nullptr) {
    // 防御式编程 ....
  }
  // shape range推导逻辑 .....
}
```
