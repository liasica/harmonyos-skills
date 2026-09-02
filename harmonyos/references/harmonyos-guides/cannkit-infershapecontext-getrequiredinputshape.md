---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getrequiredinputshape
title: GetRequiredInputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeContext > GetRequiredInputShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:015bb127aae4ad1a04053e9992cc8720454eba0d10506f762c127c7d7d83e90d
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入shape指针。

## 函数原型

```cpp
const Shape *GetRequiredInputShape(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

返回指定输入的shape指针，若输入的ir\_index非法，返回空指针。

关于Shape类型的定义，请参见[Shape](cannkit-shape-introduction.md)。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus InferShapeForXXX(InferShapeContext *context) {
  auto in_shape = context->GetRequiredInputShape(2);
  // ...
}
```
