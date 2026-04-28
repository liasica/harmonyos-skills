---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getrequiredinputtensor
title: GetRequiredInputTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeContext > GetRequiredInputTensor
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f8c820b806dd149129da8ec3fa37d4fe211e33943d348e891448881a8f912d66
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入tensor指针。

## 函数原型

```
1. const Tensor *GetRequiredInputTensor(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

返回指定输入的tensor指针，若输入的ir\_index非法，返回空指针。

关于Tensor类型的定义，请参见[Tensor](cannkit-tensor-constructor.md)。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor时，只能在tensor中获取到正确的shape、format、datatype信息。无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

## 调用示例

```
1. ge::graphStatus InferShapeForXXX(InferShapeContext *context) {
2. auto in_shape = context->GetRequiredInputTensor(2);
3. // ...
4. }
```
