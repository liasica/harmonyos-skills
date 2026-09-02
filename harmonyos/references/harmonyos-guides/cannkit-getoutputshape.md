---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputshape
title: GetOutputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetOutputShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:96e0ec470a8a951052393d59c9f73fe8b75875fd9ae58961850429405990805a
---

## 函数功能

根据算子输出索引获取对应的输出shape指针。这里的输出索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```cpp
const StorageShape *GetOutputShape(size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输出索引，从0开始计数。 |

## 返回值

指定的输出shape指针，index非法时，返回空指针。

关于StorageShape类型的定义，请参见[StorageShape](cannkit-storageshape-introduction.md)。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4ConcatD(TilingContext* context) {
  auto out_shape = context->GetOutputShape(0);
  // ...
}
```
