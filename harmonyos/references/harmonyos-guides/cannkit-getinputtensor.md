---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputtensor
title: GetInputTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetInputTensor
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f5271a58849e69b8a8d9ad1b2e7c2b7e6d5d479fac178904727c71674f061d0
---

## 函数功能

根据算子输入索引获取对应的输入tensor指针。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```cpp
const Tensor *GetInputTensor(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

指定的输入tensor指针，当输入index非法时返回空指针。

关于Tensor类型的定义，请参见[Tensor](cannkit-tensor-constructor.md)。

## 约束说明

如果输入没有被设置为数据依赖，调用此接口获取tensor时，只能在tensor中获取到正确的shape、format、datatype信息，无法获取到真实的tensor数据地址（获取到的地址为nullptr）。

## 调用示例

```cpp
ge::graphStatus Tiling4ReduceCommon(TilingContext* context) {
  auto in_shape = context->GetInputShape(0);
  GE_ASSERT_NOTNULL(in_shape);
  auto axes_tensor = context->GetInputTensor(1);
  // ...
}
```
