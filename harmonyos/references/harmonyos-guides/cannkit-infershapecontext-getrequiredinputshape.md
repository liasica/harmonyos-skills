---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapecontext-getrequiredinputshape
title: GetRequiredInputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > InferShapeContext > GetRequiredInputShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:09fc8818661c55ef7fd5358c66073c9bf9997bbf8312b7c08986a36cf7157b89
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入shape指针。

## 函数原型

```
1. const Shape *GetRequiredInputShape(const size_t ir_index) const;
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

```
1. ge::graphStatus InferShapeForXXX(InferShapeContext *context) {
2. auto in_shape = context->GetRequiredInputShape(2);
3. // ...
4. }
```
