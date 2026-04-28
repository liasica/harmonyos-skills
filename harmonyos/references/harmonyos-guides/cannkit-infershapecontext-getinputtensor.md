---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getinputtensor
title: GetInputTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeContext > GetInputTensor
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9ef28225ea27067587361303a3fd8b08ca192d00c607e68e446c0a8830dbef40
---

## 函数功能

根据算子输入索引获取对应的输入tensor指针。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. const Tensor *GetInputTensor(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

返回指向输入Tensor指针，当输入index非法时，返回空指针。

关于Tensor类型的定义，请参见[Tensor](cannkit-tensor-constructor.md)。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor时，只能在tensor中获取到正确的shape、format、datatype信息。无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

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
