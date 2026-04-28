---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getrequiredinputshape
title: GetRequiredInputShape
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > TilingContext > GetRequiredInputShape
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45488fe81a32c6c3c80fb755b4f9585927bd13de05486fdcc6cde8125d0e8876
---

## 函数功能

根据算子原型定义中的输入索引获取对应的必选输入shape指针。

## 函数原型

```
1. const StorageShape *GetRequiredInputShape(const size_t ir_index) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| ir\_index | 输入 | 必选输入在算子IR原型定义中的索引，从0开始计数。 |

## 返回值

指定的输入shape指针，shape中包含了原始shape与运行时shape。关于StorageShape类型的定义，请参见[StorageShape](cannkit-storageshape-introduction.md)。

当输入ir\_index非法时，返回空指针。

## 约束说明

无

## 调用示例

```
1. ge::graphStatus InferShape4ConcatD(TilingContext* context) {
2. auto in_shape = context->GetRequiredInputShape(0);
3. // ...
4. }
```
