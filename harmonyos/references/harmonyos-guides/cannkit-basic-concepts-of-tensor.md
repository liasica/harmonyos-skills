---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-concepts-of-tensor
title: Tensor基本概念
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 附录 > Tensor基础知识参考 > Tensor基本概念
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d02cb30795d15b381b46803b113fa4c112aa9c3479b452ac08e405ef33cf61bc
---

Tensor是算子计算数据的容器，TensorDesc（Tensor描述符）是对Tensor中数据的描述。TensorDesc数据结构包含如下属性如表1所示。

**表1** TensorDesc属性解释

| 属性 | 定义 |
| --- | --- |
| 名称(name) | 用于对Tensor进行索引，不同Tensor的name需要保持唯一。 |
| 形状(shape) | Tensor的形状，比如(10, )或者(1024, 1024)或者(2, 3, 4)等。如形状(3, 4)表示第一维有3个元素，第二维有4个元素，(3, 4)表示一个3行4列的矩阵数组。  形式：(i1, i2, …, in)，其中i1到in均为正整数。  **说明：** 由于AI Core算子编译器限制，不支持传入shape中含0的tensor(空tensor)，开发者在构造输入时需要避免传入空tensor。 |
| 数据类型(dtype) | 指定Tensor对象的数据类型。  取值范围：float16, float32, int8, int16, int32, uint8, uint16, bfloat16, bool等。 |
| 数据排布格式(format) | 数据的物理排布格式，定义了解读数据的维度。  详细请参见[数据排布格式](cannkit-data-layout-format.md)。 |
