---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-memory
title: OH_NN_Memory
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_Memory
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ac7f2a3c15f501e91d69421687e073fcb6f912aef367a97fdc300623039b0f6d
---

```c
typedef struct OH_NN_Memory {...} OH_NN_Memory
```

## 概述

内存结构体。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_Tensor](capi-neuralnetworkruntime-nn-tensor.md)

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| void \* const data | 指向共享内存的指针，该共享内存通常由底层硬件驱动申请。 |
| const size\_t length | 记录共享内存的字节长度。 |
