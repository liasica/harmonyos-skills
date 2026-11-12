---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:943ec181e7d387f5e5a48ad162818ef9ea5783ed495416678a10e09886bd97d4
---

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/2wSzOx6GRomNwCmqUfpGCQ/zh-cn_image_0000002786362204.png?HW-CC-KV=V1&HW-CC-Date=20261112T233238Z&HW-CC-Expire=31536000000&HW-CC-Sign=BCDE52D42F5BD00B7642710E464D7CDA06867C6EB38496C5707BC5D3FB989722)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Q2D9V_HKQMKsdzJ00CKm-A/zh-cn_image_0000002815561625.png?HW-CC-KV=V1&HW-CC-Date=20261112T233238Z&HW-CC-Expire=31536000000&HW-CC-Sign=A10035C7821E7B08979A81F884889F11A5C7CB5FBDDDBF0971D2CBAC6A74318E)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/hqs9MGsFRmOCqILZqRdtdA/zh-cn_image_0000002815401709.png?HW-CC-KV=V1&HW-CC-Date=20261112T233238Z&HW-CC-Expire=31536000000&HW-CC-Sign=2D5C465EFACB8592D525383A2ED5C684CC32B55C05111942824DA47A46F02435)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/z1CjW4t6SK2eKPC54Z3v8Q/zh-cn_image_0000002786522134.png?HW-CC-KV=V1&HW-CC-Date=20261112T233238Z&HW-CC-Expire=31536000000&HW-CC-Sign=C2376C799FA182B09CA1A7965D3B9EB1D051F619C7741A77F5BAE2D47C517D08)

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_QuantParam](capi-neuralnetworkruntime-nn-quantparam.md)

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32\_t \*numBits | 量化位数。 |
| const double \*scale | 指向量化公式中scale数据的指针。 |
| const int32\_t \*zeroPoint | 指向量化公式中zero point数据的指针。 |
