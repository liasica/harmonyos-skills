---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-tensor
title: OH_NN_Tensor
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_Tensor
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f877b84d255131dd217fde3acba5ead0d43b3f749c44b06dc0d0b118082bd77d
---

```c
typedef struct OH_NN_Tensor {...} OH_NN_Tensor
```

## 概述

张量结构体。

通常用于构造模型图中的数据节点和算子参数，在构造张量时需要明确数据类型、维数、维度信息和量化信息。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_TensorDesc](capi-neuralnetworkruntime-nn-tensordesc.md)

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_NN\_DataType](capi-neural-network-runtime-type-h.md#oh_nn_datatype) dataType | 指定张量的数据类型，要求从[OH\_NN\_DataType](capi-neural-network-runtime-type-h.md#oh_nn_datatype)枚举类型中取值。 |
| uint32\_t dimensionCount | 指定张量的维数。 |
| const int32\_t \*dimensions | 指定张量的维度信息（形状）。 |
| const [OH\_NN\_QuantParam](capi-neuralnetworkruntime-oh-nn-quantparam.md) \*quantParam | 指定张量的量化信息，数据类型要求为[OH\_NN\_QuantParam](capi-neuralnetworkruntime-oh-nn-quantparam.md)。 |
| [OH\_NN\_TensorType](capi-neural-network-runtime-type-h.md#oh_nn_tensortype) type | 指定张量的类型。type的取值和张量的用途相关，当张量用作模型的输入或输出，则要求将type设置为[OH\_NN\_TENSOR](capi-neural-network-runtime-type-h.md#oh_nn_tensortype)；当张量用作算子参数，则要求从[OH\_NN\_TensorType](capi-neural-network-runtime-type-h.md#oh_nn_tensortype)中选择除[OH\_NN\_TENSOR](capi-neural-network-runtime-type-h.md#oh_nn_tensortype)以外的枚举值。 |
