---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-memory
title: OH_NN_Memory
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_Memory
category: harmonyos-references
scraped_at: 2026-04-28T08:19:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0c5808a08f1e79f0867a7c4a49bb27f6e9d919fb9d00e4d3d073a7956955d0cf
---

```
1. typedef struct OH_NN_Memory {...} OH_NN_Memory
```

## 概述

PhonePC/2in1TabletTV

内存结构体。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_Tensor](capi-neuralnetworkruntime-nn-tensor.md)

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| void \* const data | 指向共享内存的指针，该共享内存通常由底层硬件驱动申请。 |
| const size\_t length | 记录共享内存的字节长度。 |
