---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getoutputshape
title: GetOutputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeContext > GetOutputShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:345290e6735a679305f9fe8f6a1f5044f9bb7cbff4cd2d4847b57b547bd5496e
---

## 函数功能

根据算子输出索引获取对应的输出shape指针。这里的输出索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. Shape *GetOutputShape(const size_t index);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输出索引，从0开始计数。 |

## 返回值

返回指定的输出shape指针，输入index非法时，返回空指针。

关于Shape类型的定义，请参见[Shape](cannkit-shape-introduction.md)。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus InferShapeForReshape(InferShapeContext *context) {
2. const gert::Shape *x_shape = context->GetInputShape(0);        // 获取第0个输入的shape
3. const gert::Tensor *shape_tensor = context->GetInputTensor(1); // 获取第1个输入的tensor  数据依赖
4. gert::Shape *output_shape = context->GetOutputShape(0);
5. if (x_shape == nullptr || shape_tensor == nullptr || output_shape == nullptr) {
6. // 防御式编程，不应该出现的场景，打印错误并返回失败
7. return ge::GRAPH_FAILED;
8. }
9. // ...
10. }
```
