---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputshape
title: GetInputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetInputShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8e35708d8673c934a50c566814b7433725f101931721742ff5a0e65a01d3e373
---

## 函数功能

根据算子输入索引获取对应的输入shape指针。这里的输入索引是指算子实例化后实际的索引，不是原型定义中的索引。

## 函数原型

```
1. const StorageShape *GetInputShape(const size_t index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| index | 输入 | 算子输入索引，从0开始计数。 |

## 返回值

指定的输入shape指针，输入shape中包含了原始shape与运行时shape信息。关于StorageShape类型的定义，请参见[StorageShape](cannkit-storageshape-introduction.md)。

当输入index非法时返回空指针。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus TilingForMul(TilingContext *context) {
2. auto input_shape_0 = *context->GetInputShape(0);
3. auto input_shape_1 = *context->GetInputShape(1);
4. auto output_shape = context->GetOutputShape(0);
5. // ...
6. }
```
