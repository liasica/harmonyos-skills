---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoptionalinputtensor
title: GetOptionalInputTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetOptionalInputTensor
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:df232ff698e13c27daebe1e89262cb7acfc6e3d7a48ffaabddac9e7ca7255370
---

## 函数功能

根据算子原型定义中的输入索引获取对应的可选输入tensor指针。

## 函数原型

```
1. const Tensor *GetOptionalInputTensor(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |

## 返回值

指定ir\_index的输入tensor指针，当输入ir\_index非法或该INPUT没有实例化时，返回空指针。

关于Tensor类型的定义，请参见[Tensor](cannkit-tensor-constructor.md)。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor时，只能在tensor中获取到正确的shape、format、datatype信息，无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

## 调用示例

```
1. ge::graphStatus Tiling4ReduceCommon(TilingContext* context) {
2. auto in_shape = context->GetInputShape(0);
3. GE_ASSERT_NOTNULL(in_shape);
4. auto axes_tensor = context->GetOptionalInputTensor(1);
5. // ...
6. }
```
