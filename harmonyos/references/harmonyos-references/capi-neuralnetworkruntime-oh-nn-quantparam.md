---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-04-28T08:19:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9f59ee6ac308cd8827dcd859124f7d1be3765d07cc1388b51d3483e4873da3c4
---

```
1. typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

PhonePC/2in1TabletTV

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/MiTBAyfRRnK08Vcc3DKoQg/zh-cn_image_0000002552801262.png?HW-CC-KV=V1&HW-CC-Date=20260428T001908Z&HW-CC-Expire=86400&HW-CC-Sign=9894A056D83E4C8D22186287757D10BF3A44ED9789AE7EA1BA37BC376C0F767E)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/Gku-THfMSYCcD7RwP3nsXQ/zh-cn_image_0000002583440957.png?HW-CC-KV=V1&HW-CC-Date=20260428T001908Z&HW-CC-Expire=86400&HW-CC-Sign=A07103F0545A73D19CC47EB2F387085055CBD73B232AFCCA07EE17FF531D3CF7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/4d-kFgG0TzS49cjgyvih3w/zh-cn_image_0000002552960912.png?HW-CC-KV=V1&HW-CC-Date=20260428T001908Z&HW-CC-Expire=86400&HW-CC-Sign=B03FD507E053CD68F2A7EE2CC377626D480D63177E5C52322A5C337C67381738)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/1SBjUotYQimHQgB-rPYHzQ/zh-cn_image_0000002583480913.png?HW-CC-KV=V1&HW-CC-Date=20260428T001908Z&HW-CC-Expire=86400&HW-CC-Sign=481D6C2BAEC171ECDE4E2E535B1B2D973630E928CF54EC85532339225BFD3704)

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
