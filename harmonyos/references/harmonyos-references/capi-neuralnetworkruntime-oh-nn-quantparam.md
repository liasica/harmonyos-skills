---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam
title: OH_NN_QuantParam
breadcrumb: API参考 > AI > Neural Network Runtime Kit（Neural Network运行时服务） > C API > 结构体 > OH_NN_QuantParam
category: harmonyos-references
scraped_at: 2026-11-19T09:55:04+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b3fc0245ee36a5027f3ef77dca5473438c5d5b15482a39da39c75cb7477cadc9
---

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

## 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/6KTjGpUbS_CyQOzxL3vgRA/zh-cn_image_0000002820408221.png?HW-CC-KV=V1&HW-CC-Date=20261119T015408Z&HW-CC-Expire=31536000000&HW-CC-Sign=24141E6FCA9635C4BD938F2D792DB5FC4BD1B6BD88BAF19B7295E53448A89BC5)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/XIWwd4wFR9-9iaWVO23NEQ/zh-cn_image_0000002791728240.png?HW-CC-KV=V1&HW-CC-Date=20261119T015408Z&HW-CC-Expire=31536000000&HW-CC-Sign=BF9F5C9846535CDEE151571AF65F39B2193695D52B5666F1DDD99AA430E23043)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/lFadatDMS7KUCkYNarQYqA/zh-cn_image_0000002791568268.png?HW-CC-KV=V1&HW-CC-Date=20261119T015408Z&HW-CC-Expire=31536000000&HW-CC-Sign=106501BAB4C83EE5BB9647F90F1AF4F4A140F513EE58EB847075C1A92983A7CE)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/tEEzrtxLQIuVwCGcXJ7sLA/zh-cn_image_0000002820528221.png?HW-CC-KV=V1&HW-CC-Date=20261119T015408Z&HW-CC-Expire=31536000000&HW-CC-Sign=04EF56823DDA69201E7A690B027224B53B5F1FD2926582B143114FCD213202B2)

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
