---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-11-14T08:53:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fe8fd469b3da52b1f7adfffa93e835b3e0f4248f7f39b8e2339486a027bbf07c
---

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/CFlsg-BuSsaUvQcphCd8YA/zh-cn_image_0000002817509369.png?HW-CC-KV=V1&HW-CC-Date=20261114T005357Z&HW-CC-Expire=31536000000&HW-CC-Sign=FB2D2B12429740A434B1E397F6BFD099596B4EA4A501B2BFFAF0FF2B7CD44337)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/RVDHmsXASA2UGhkK-deIZg/zh-cn_image_0000002788309938.png?HW-CC-KV=V1&HW-CC-Date=20261114T005357Z&HW-CC-Expire=31536000000&HW-CC-Sign=272729F39B67D054697A511D0D82B3F4963E9194312B0765B7D7EC7F955A6EE1)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/9od5fgxuSpqBi5qdMV2cSA/zh-cn_image_0000002817429301.png?HW-CC-KV=V1&HW-CC-Date=20261114T005357Z&HW-CC-Expire=31536000000&HW-CC-Sign=D67B83F50602C50DB6CC7A830C0F85C0D31EB5A0F9EDFE873D6149D5C651C8E4)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/PKw0_iIkQSOK3IKP_nFA4g/zh-cn_image_0000002788469882.png?HW-CC-KV=V1&HW-CC-Date=20261114T005357Z&HW-CC-Expire=31536000000&HW-CC-Sign=69FBAF54E2C97CB7BE8F46B9044A9CEA98078415C08075380AE36CD0F9A8007E)

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
