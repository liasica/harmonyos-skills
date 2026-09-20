---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-09-21T06:25:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b7b5b175f2e1b99f37b4e18669b740ba54f6ffc2160fbab7269227f52fe6eb33
---

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/qm9Y_ER9QQeF6nV52mdKAg/zh-cn_image_0000002733437424.png)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/18_ks5FBRdqTUgbvNVDDxA/zh-cn_image_0000002762996947.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/wMIiaI8NQPGiP4IUjlGa2g/zh-cn_image_0000002762837065.png)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/NuPY8XBKQN2WNkyA_xo5BQ/zh-cn_image_0000002733277554.png)

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
