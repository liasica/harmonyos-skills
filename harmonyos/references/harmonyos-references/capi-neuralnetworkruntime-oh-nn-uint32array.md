---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-uint32array
title: OH_NN_UInt32Array
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_UInt32Array
category: harmonyos-references
scraped_at: 2026-09-02T15:03:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e78418bc50945fd98460d865ee6b3a230086ac83cbaaf475ba8f7c53f2f6a10
---

```c
typedef struct OH_NN_UInt32Array {...} OH_NN_UInt32Array
```

## 概述

该结构体用于存储32位无符号整型数组。

**起始版本：** 9

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t \*data | 无符号整型数组的指针。 |
| uint32\_t size | 数组长度。 |
