---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-11-21T09:17:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7563a6c9a49ad4bf167974909f162c4fddd66cd05eb454f3ca84a1b5ef54467c
---

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/kh7IZHO9TvaPN08tKTjxmw/zh-cn_image_0000002821759861.png?HW-CC-KV=V1&HW-CC-Date=20261121T011703Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F55C4EA40DBF06974418A4EF34AE3419035E44C3F616029191136F0824B0319)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/qmC7RgtpR3ekyoMIV4Gqsg/zh-cn_image_0000002793039932.png?HW-CC-KV=V1&HW-CC-Date=20261121T011703Z&HW-CC-Expire=31536000000&HW-CC-Sign=94F683664FF62D80B7EB861E0EB9A5D34F523EB3A2E8D4C02D148CDC687D269F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/w_e0rc3uS92UVaGkknnUTg/zh-cn_image_0000002792879958.png?HW-CC-KV=V1&HW-CC-Date=20261121T011703Z&HW-CC-Expire=31536000000&HW-CC-Sign=9933AC8C72A1C7EA2EE6BD795D7633FEDC025BDDEB11C0AD760F04F9F90BED7E)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/9ay3OMD9Qs-JE64377mINQ/zh-cn_image_0000002821839861.png?HW-CC-KV=V1&HW-CC-Date=20261121T011703Z&HW-CC-Expire=31536000000&HW-CC-Sign=A5E5C07E9D1BE8F2587387E53F6C5971B134EF472C73AD7FD86A52162AF3901B)

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
