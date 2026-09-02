---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoptionalinputshape
title: GetOptionalInputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetOptionalInputShape
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3f77ff87fee924f52dac89c30464ee8a4de014795557a97622551c7477de33b
---

## 函数功能

根据算子原型定义中的输入索引获取对应的可选输入shape指针。

## 函数原型

```cpp
const StorageShape *GetOptionalInputShape(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 算子IR原型定义中的输入索引，从0开始计数。 |

## 返回值

指定的输入shape指针，shape中包含了原始shape与运行时shape。关于StorageShape类型的定义，请参见[StorageShape](cannkit-storageshape-introduction.md)。

当输入ir\_index非法，或该INPUT没有实例化时，返回空指针。

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus Tiling4ConcatD(TilingContext* context) {
  const StorageShape *shape_bias = context->GetOptionalInputShape(kBatchMatMulBiasIdx);
  // ...
}
```
