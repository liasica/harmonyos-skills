---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-04-29T14:09:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be43a8c04af0d77aebd0aede1a0033ac0cf451cd9701016be1f41dfd635a51ae
---

```
1. typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

PhonePC/2in1TabletTV

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/nOjUryZ8QNS1u9zw1fIy8A/zh-cn_image_0000002589247245.png?HW-CC-KV=V1&HW-CC-Date=20260429T060945Z&HW-CC-Expire=86400&HW-CC-Sign=86D616F24CE3F335B09D295B1835A82CF33332D52C0996394F534C0BE7A7EA91)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/givau3ZCQpyEGl-Ia6E8cQ/zh-cn_image_0000002558767438.png?HW-CC-KV=V1&HW-CC-Date=20260429T060945Z&HW-CC-Expire=86400&HW-CC-Sign=9FA436DBC46710F449772A430F45F97002BAEB568F25C24471088091C902F4D3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/pQt9yAuLThGPcAiUhp2XRw/zh-cn_image_0000002558607780.png?HW-CC-KV=V1&HW-CC-Date=20260429T060945Z&HW-CC-Expire=86400&HW-CC-Sign=2FF32C311FFC697E9E1A06F0B51658EF216858E3747E19BD7D0C7FBAF134E5B1)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/rmSXjBL4TySiDX6T5Q81Cw/zh-cn_image_0000002589327307.png?HW-CC-KV=V1&HW-CC-Date=20260429T060945Z&HW-CC-Expire=86400&HW-CC-Sign=CCFF10E2DF3300A7D1070733795CDB448428F26C34C07D341736A9EB6B419077)

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_QuantParam](capi-neuralnetworkruntime-nn-quantparam.md)

**相关模块：** [NeuralNetworkRuntime](capi-neuralnetworkruntime.md)

**所在头文件：** [neural\_network\_runtime\_type.h](capi-neural-network-runtime-type-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| uint32\_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32\_t \*numBits | 量化位数。 |
| const double \*scale | 指向量化公式中scale数据的指针。 |
| const int32\_t \*zeroPoint | 指向量化公式中zero point数据的指针。 |
