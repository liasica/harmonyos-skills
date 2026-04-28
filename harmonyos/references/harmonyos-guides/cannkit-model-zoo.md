---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-zoo
title: Model Zoo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > Model Zoo
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:20951eb45dee09f5144c707ca8f4f6bdc2e2fe6fff8c772988db0c4c01d784da
---

## 概述

Model Zoo提供了可直接调用的硬件最优模型库，集成图片分类、目标检测、语义分割、超分等典型场景的网络模型，包含CANN性能调优使用指导、性能友好模型结构和推荐指数。帮助开发者快速了解算子的参数取值如何在硬件上获得更好的性能和能效收益，以及如何优化模型结构可以实现高性能与低功耗。

## Model Zoo模型下载

在模型下载中，.caffemodel、.pb、.onnx文件是原始浮点模型，基于相关论文实现，并进行了NPU硬件亲和性调整。因此，这些模型的输入尺寸可能与论文中描述的尺寸有所差异。

.om是标准IR算子构建的OM模型文件，其中quant8\_8.om是量化生成的OM模型文件，所有模型可通过[Netron工具](cannkit-visualization-tool-usage.md)可视化。

Model Zoo中模型的名称、性能、模型下载信息如下表所示。

| 场景 | 网络模型（单batch） | 浮点性能[1]（耗时ms） | 量化性能[1]（耗时ms） | 模型下载 | SHA256校验码 | 参考[2] |
| --- | --- | --- | --- | --- | --- | --- |
| 图片分类 | Alexnet | 9.92 | 4.49 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/42/v3/eyPGmahYTnKtskcw6wC7yg/hwhiaimodelzoo-alexnet-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T083009Z&HW-CC-Expire=315360000&HW-CC-Sign=9F85C5C4E2A049C8F6502D37F45E9FF743213331FA837B19F492C961451F5C1E) | 7b01980acf0d16dadc6c9c326cdf757d2166928ae49cfd4091df154a5c512640 | [论文&实现](https://arxiv.org/abs/1404.5997) |
| 图片分类 | Resnet18 | 2.63 | 1.24 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2b/v3/-3ps6ob3QO6CSom10fi0Gw/hwhiaimodelzoo-resnet18-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081504Z&HW-CC-Expire=315360000&HW-CC-Sign=1E7889E8F15927FF8198A949D5D9B42CC3CB81F4CE9A1F341CB4E90B77346E45) | 4aa7caaa112f5280cb5c0ab5eed6edf84a16fe9a0b92b9ee333a808c9f07e886 | [论文&实现](https://arxiv.org/abs/1512.03385) |
| 图片分类 | VGG16 | 16.56 | 8.55 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/d3/v3/iCUHL864TRKbqKINLlFKnQ/hwhiaimodelzoo-vgg16-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081340Z&HW-CC-Expire=315360000&HW-CC-Sign=4F2EA9998432D7CD60710CD7690E3554C71512D6AA74F2E01FAD30A9CD4AC70B) | f9193765889077e5997ddc8c1e75a563c8a1205e613da9634d3d83277962dd42 | [论文&实现](https://arxiv.org/abs/1409.1556) |
| 图片分类 | VGG19 | 18.34 | 8.73 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/21/v3/gd9SP5_hRG2JfFW-8tgC0Q/hwhiaimodelzoo-vgg19-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T080831Z&HW-CC-Expire=315360000&HW-CC-Sign=C156643FD0B8EC4C829972E8C460EA8FF1CB3AEEBCD7DADD5CD031E98FC301A5) | d19f363602740ff5859380c40ca6f0bed0cb3744f469873cdf862c71c7007a94 | [论文&实现](https://arxiv.org/abs/1409.1556) |
| 图片分类 | Resnet50 | 5.15 | 3.54 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/10/v3/Q-dHdmq1TQ6FzYOy60u1VQ/hwhiaimodelzoo-resnet50-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081405Z&HW-CC-Expire=315360000&HW-CC-Sign=BB6F826B1072CDDBA83C6D7351CEF356327EFF7D97EE84C788F9621E1A9A4CE6) | 6dedf4b5c3bfdaf70410236f1f73d942a5231f217e18c51918ba39b3b740b2df | [论文&实现](https://arxiv.org/abs/1512.03385) |
| 图片分类 | Inception\_v3 | 6.56 | 3.76 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/4f/v3/qtjKvj1sSoK8_ySu6xLE2g/hwhiaimodelzoo-inceptionv3-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082107Z&HW-CC-Expire=315360000&HW-CC-Sign=2788E8301870BD3C1AC15B845CF204B27BA412C976A9670B1DDF984A8AAA0026) | d06c88a79acd19b10d5f7eddaae6aba3c02372cfdb036296b845aa3a9ccf46be | [论文&实现](https://arxiv.org/abs/1512.00567) |
| 图片分类 | Inception\_v4 | 11.90 | 7.29 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/5c/v3/HCh4-WFvR6iw4egm2vAvxQ/hwhiaimodelzoo-inceptionv4-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082010Z&HW-CC-Expire=315360000&HW-CC-Sign=194B3E4976AE798E8A887AA69BF9894D30EDA727BF8B9B06428892A2A9BD9918) | e042f489e6915eb6de5daa4b3200462e76f1bedca7147e2a19e8311a4b05afde | [论文&实现](https://arxiv.org/abs/1602.07261) |
| 图片分类 | Inception\_Resnet\_v2 | 15.91 | 5.59 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/70/v3/Hsox_-bbR9a5EDFg8_mn6A/hwhiaimodelzoo-inceptionresnetv2-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081911Z&HW-CC-Expire=315360000&HW-CC-Sign=DB418566ED9B3AA260AAA1D589A13BCC250E2F809BBFD3A67D400DCE1C6DFF16) | 229164e49753126357f4a587694ca925afa60d1bfec184dba00085d69b5fc47b | [论文&实现](https://arxiv.org/abs/1602.07261) |
| 图片分类 | Mobilenet\_v1 | 2.16 | 0.52 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2c/v3/KzMd67g3TSqsCjocI_WCVQ/hwhiaimodelzoo-mobilenetv1-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082701Z&HW-CC-Expire=315360000&HW-CC-Sign=E1B233C47BA93FEE1747A38739840277730B54FC0739D78D79277D72FF5D77BA) | 864ef1d651e7f2cb9de69ce34d81e40783bdac47069b6db22aefb6f4ae17f24b | [论文&实现](https://arxiv.org/abs/1704.04861) |
| 图片分类 | Mobilenet\_v2 | 2.49 | 1.18 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2/v3/ZSK31G6DQQCZdPN46ialkA/hwhiaimodelzoo-mobilenetv2-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082301Z&HW-CC-Expire=315360000&HW-CC-Sign=8C37AE09586B0DD74C079AE4C3E07E376F66015E4DED2CB1367F22869B92623E) | 362c0169917122e45f4c5aed69ad3b9c8509b51a0531e6912360eff6c8b81cbc | [论文&实现](https://arxiv.org/abs/1801.04381) |
| 图片分类 | Mobilenet\_v2\_1.4 | 3.16 | 1.67 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2b/v3/b6CQs3z-TgyxhL2RmM99Gg/hwhiaimodelzoo-mobilenetv2v1p4-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082201Z&HW-CC-Expire=315360000&HW-CC-Sign=638FA2EBD56970A77CEA8ACE1075E6C43AC69890FE7DB3B9FB705E822C10BA15) | 8f1a05a83e813fac16e958ad5436569fe83f75f88137819d52ce2e268ad04126 | [论文&实现](https://arxiv.org/abs/1704.04861) |
| 图片分类 | Mobilenet\_v3\_Large | 3.29 | 2.33 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c1/v3/1tgbS5yhSHCVSrT3EZMk8Q/hwhiaimodelzoo-mobilenetv3-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082402Z&HW-CC-Expire=315360000&HW-CC-Sign=991EF094DEC163F2A7E32FBAB61DC3DF6C1D26932357D76B452B725A73CF0B27) | 086640ff192629b6dba33d905ddb0925d612e395703948c6c7221f2e4126b85d | [论文&实现](https://arxiv.org/abs/1905.02244) |
| 图片分类 | Googlenet | 34.69 | 1.64 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/7e/v3/XwBoZqjZSlGr8Qr90k3acA/hwhiaimodelzoo-googlenet-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082502Z&HW-CC-Expire=315360000&HW-CC-Sign=7F5D53B22154CDE1B350367A5A31EAF81780D49DFF0D6C8E070EAAF973958DAC) | 97ef0325be2c3b8824a903abaeea943260d2f349da63d193168c96eff735ad0e | [论文&实现](https://arxiv.org/abs/1409.4842) |
| 图片分类 | Squeezenet\_v1 | 2.13 | 1.24 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/22/v3/LsUOWWXqS-Cy7BhWCL6k7w/hwhiaimodelzoo-squeezenetv1-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081800Z&HW-CC-Expire=315360000&HW-CC-Sign=7A8C3CE1BDD91367BB92DD6A6DDBC3D2F9CE5E1C2C716E4C5B9D687C96997F42) | e20be44bdaa30b9fa4a22ef876c1e7bd88db49b5d063992ef1595b34d3544997 | [论文&实现](https://arxiv.org/abs/1602.07360) |
| 目标检测 | SSD\_mobilenetv2\_voc | 5.02 | 2.84 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/ee/v3/-DV4ExjOQv6dZPxNyX0UIg/hwhiaimodelzoo-mobilenetv2ssd-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082602Z&HW-CC-Expire=315360000&HW-CC-Sign=9E6FD16BC06F1EE732447C5CA9A0AAC2E559DF42593D22A517CEC6F94D990AB3) | 1d273130a07a6f888f6df1088b478049da9a961a3dbeaca7bfa92e616f0f01e9 | [论文1&实现1](https://arxiv.org/abs/1801.04381)、[论文2&实现2](https://arxiv.org/abs/1512.02325) |
| 目标检测 | Yolo\_v5 | 4.74 | 4.33 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b6/v3/XBnjg_e5TMyG31kCCbdp1Q/hwhiaimodelzoo-yolo-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081602Z&HW-CC-Expire=315360000&HW-CC-Sign=F31AC615FBD3DE8001EB12B9F8D5718EE3BA0BE1DDECF60A51E6901D24EE8E71) | 83a205d70fcd9b31c13530da0b8752a6976b125b02ac07091fd088f58cd5a80f | [论文&实现](https://arxiv.org/abs/1804.02767) |
| 语义分割 | FCN | 131.23 | 62.76 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/d8/v3/ZDtRfBLDR86G-UakQBtEPA/hwhiaimodelzoo-fcn-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082927Z&HW-CC-Expire=315360000&HW-CC-Sign=0974C70798D459DBFD9542D65C72FB8B9BD583C14F52837BFED5DABB405719EA) | 0cd87a51c1ea978a68e9cd4790106e99d910f78d5e68ec06e2bdd637aae5a73c | [论文&实现](https://arxiv.org/abs/1605.06211) |
| 语义分割 | DeepLab\_v3 | 17.40 | 13.87 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/11/v3/qUSCbzzPT82XhxA1bC4HAQ/hwhiaimodelzoo-deeplabv3-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T083100Z&HW-CC-Expire=315360000&HW-CC-Sign=230AD01AEDBE1916683B6BB35BDED9B363EB06276BDF98DA64B2C7EF9B6CC285) | 381f830f6b0154bf086dbc5b15575465a34c1b3d233a6d27bc417077832697c7 | [论文&实现](https://arxiv.org/abs/1706.05587) |
| 超分 | VDSR | 17.71 | 10.67 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c6/v3/u6c2DYcSQQGHp_-K5pLVIg/hwhiaimodelzoo-vdsr-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T081700Z&HW-CC-Expire=315360000&HW-CC-Sign=358520AA2A16D4C2D7CA6703692D2D1209BFDFC38414C55AF442F89F9ACA6896) | bf5a699ea55b2d2e42ac40884f2697d807b5b3f37e655ecb342e873c6ba6b844 | [论文&实现](https://arxiv.org/abs/1511.04587) |
| 超分 | FSRCNN | 17.24 | 17.02 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/3d/v3/K_eT1fFuQM6vi9zsRe2CDQ/hwhiaimodelzoo-fsr-100.520.020.011.zip?HW-CC-KV=V1&HW-CC-Date=20230423T082800Z&HW-CC-Expire=315360000&HW-CC-Sign=794BA667B6CAC909B5E8EBD672D638C4160971C62FAB237535417E0849713A92) | 03775c806d8d166fd29753ea8eaa3db377246fa469487b7e161a9e405a6ffa1c | [论文&实现](https://arxiv.org/abs/1608.00367) |

说明

* [1] 此性能数据测试基于kirin 9000芯片的华为手机。
* [2] 原始模型文件是参考论文和实现中的模型训练而来。

除Model Zoo中推荐的网络模型，还可以构建自定义的网络模型。性能优势的算子和计算结构如下。

## CANN算子性能指导

从易用性角度上来说，提供的算子功能不存在限制，但是从性能的使用角度上来说，是基于算子实现方式给出对应的性能使用指导。

### NN算子

| IR算子 | 性能使用指导 | 推荐使用指数 |
| --- | --- | --- |
| Activation | 当前性能硬件最优。 | ☆☆☆☆☆ |
| HardSwish | 当前性能硬件最优。 | ☆☆☆☆☆ |
| PRelu | 当前性能硬件最优。 | ☆☆☆☆☆ |
| BNInference | 当前性能硬件最优。  Conv(depthwise)+Bn组合使用时，会进行图融合优化抵消。 | ☆☆☆☆☆ |
| Convolution | 当Cin和Cout都是16的倍数时性能最优。 | ☆☆☆☆☆ |
| QuantizedConvolution | 当Cin和Cout都是32的倍数时性能最优。 | ☆☆☆☆☆ |
| ConvTranspose | - 当Cin和Cout都是16的倍数时性能最优。  - 当前针对kernel 1\*1，2\*2，3\*3，8\*8优化性能最优。 | ☆☆☆☆☆ |
| BiasAdd | 当前性能硬件最优。  Conv(depthwise)+BiasAdd组合使用时，会进行图融合优化抵消。 | ☆☆☆☆☆ |
| Eltwise | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LRN | 当前性能硬件较优。  - 计算过程中计算均值方差，计算量较大，性能差于batchNorm。  - 主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。 | ☆☆☆ |
| ConvolutionDepthwise | 当前性能硬件最优。 | ☆☆☆☆☆ |
| QuantizedConvolutionDepthwise | 当前性能硬件最优。 | ☆☆☆☆☆ |
| FullyConnection | 性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。 | ☆☆☆☆☆ |
| QuantizedFullyConnection | 性能受DDR带宽限制，非算力受限算子，算法设计时合理配置权重大小。 | ☆☆☆☆☆ |
| PoolingD | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Scale | 当前性能硬件最优。  Conv(depthwise)+Scale组合使用时，会进行图融合优化抵消。 | ☆☆☆☆☆ |
| ShuffleChannel | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| ShuffleChannelV2 | 为了适配支持ANN场景算子，性能较差，仅支持功能。 | ☆ |
| Softmax | 当前性能硬件最优。  4维输入，axis=1，基于C通道做softmax时性能最优。 | ☆☆☆☆☆ |
| TopK | 为了适配支持ANN场景算子，性能较差，仅支持功能。 | ☆ |
| LogSoftmax | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Rank | shape推导类算子，模型构建时即可抵消。 | ☆☆☆☆☆ |
| ScatterNd | 非规则数据搬移，性能较差，不建议模型过多使用。 | ☆☆☆ |
| LogicalXor | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Threshold | 当前性能硬件最优。 | ☆☆☆☆☆ |
| AxisAlignedBboxTransform | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Normalize | 当前性能硬件最优。 | ☆☆☆☆☆ |
| SVDF | 当前性能硬件最优。 | ☆☆☆☆☆ |
| ReduceMean | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LayerNorm | 当前性能硬件最优。  - 计算过程中计算均值方差，计算量较大，性能差于batchNorm。  - 主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。 | ☆☆☆ |
| InstanceNorm | 当前性能硬件较优。  - 计算过程中计算均值方差，计算量较大，性能差于batchNorm。  - 主要用于图像增强，对精度计算较敏感，NPU使用FP16计算存在精度风险。 | ☆☆☆ |
| PriorBox | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LSTM | 当前性能硬件较优，功能支持较窄。 | ☆☆☆☆ |

### Math算子

| IR算子 | 性能使用指导 | 推荐使用指数 |
| --- | --- | --- |
| Add | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Mul | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Expm1 | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Ceil | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Sin | 性能较差。 | ☆ |
| Cos | 性能较差。 | ☆ |
| Floor | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Log1p | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LogicalAnd | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LogicalNot | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Maximum | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Minimum | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Equal | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Reciprocal | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Sqrt | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Square | 当前性能硬件最优。 | ☆☆☆☆☆ |
| CastT | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Sign | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Exp | 当前性能硬件最优。 | ☆☆☆☆☆ |
| FloorMod | 当前性能硬件最优。 | ☆☆☆☆☆ |
| GreaterEqual | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Greater | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Less | 当前性能硬件最优。 | ☆☆☆☆☆ |
| MatMul | 当前性能硬件最优。 | ☆☆☆☆☆ |
| RealDiv | 性能较差，建议等效成mul或者Reciprocal+mul。 | ☆ |
| Rint | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Round | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Rsqrt | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| Sub | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Range | 模型构建时最优。 | ☆☆☆☆☆ |
| Acos | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Asin | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Log | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LogicalOr | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Neg | 当前性能硬件最优。 | ☆☆☆☆☆ |
| ReduceProdD | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| ReduceSum | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Tan | 性能较差。 | ☆ |
| Power | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Pow | 性能较差。 | ☆ |
| ArgMaxExt2 | 当前性能硬件最优。 | ☆☆☆☆ |
| FloorDiv | 性能较差，不建议使用。 | ☆ |
| NotEqual | 当前性能硬件最优。 | ☆☆☆☆☆ |
| LessEqual | 当前性能硬件最优。 | ☆☆☆☆☆ |
| SquaredDifference | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Atan | 当前性能硬件最优。 | ☆☆☆☆☆ |
| BatchMatMul | 当前性能硬件最优。 | ☆☆☆☆☆ |
| ClipByValue | 当前性能硬件最优。 | ☆☆☆☆☆ |
| L2Normalize | 当前性能硬件最优。 | ☆☆☆☆☆ |
| ReduceMax | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |
| ReduceMin | kirin 9000芯片的手机性能较优，其余芯片的手机无性能优化，仅支持功能。 | ☆ |

### Array算子

| IR算子 | 性能使用指导 | 推荐使用指数 |
| --- | --- | --- |
| ConcatD | 当前性能硬件最优。  当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。 | ☆☆☆☆☆ |
| FakeQuantWithMinMaxVars | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Reshape | 当前性能硬件最优。  有些场景算子会被融合抵消掉。 | ☆☆☆☆☆ |
| SplitD | 当前性能硬件最优。  当Cin是16的倍数且Cout是16的倍数时，做图融合抵消，性能最优。 | ☆☆☆☆☆ |
| SplitV | 由于是乱序的数据重排，性能较差。 | ☆ |
| Unpack | 由于是乱序的数据重排，性能较差。 | ☆ |
| Flatten | 由于是乱序的数据重排，性能较差。 | ☆ |
| Slice | 由于是乱序的数据重排，性能较差。 | ☆ |
| ExpandDims | shape推导类算子，模型构建时即可抵消。 | ☆☆☆☆☆ |
| GatherV2D | 由于是乱序的数据重排，性能较差。 | ☆ |
| GatherNd | 由于是乱序的数据重排，性能较差。 | ☆ |
| Pack | 由于是乱序的数据重排，性能较差。 | ☆ |
| SpaceToDepth | 由于是乱序的数据重排，性能较差。 | ☆ |
| DepthToSpace | 由于是乱序的数据重排，大部分场景性能较差。  针对4宫格场景（Cin=4，block=1）有特殊优化，性能较优。 | ☆☆ |
| StridedSlice | 由于是乱序的数据重排，性能较差。 | ☆ |
| SpaceToBatchND | 由于是乱序的数据重排，性能较差。 | ☆ |
| BatchToSpaceND | 由于是乱序的数据重排，性能较差。 | ☆ |
| Tile | 由于是乱序的数据重排，性能较差。 | ☆ |
| Size | shape推导类算子，模型构建时即可抵消。 | ☆☆☆☆☆ |
| Fill | 由于是乱序的数据重排，性能较差。 | ☆ |
| Select | 仅支持功能。 | ☆☆ |
| PadV2 | 针对HW方向补0的场景性能较优。  其他场景由于乱序的数据重排，性能较差。 | ☆☆☆ |
| Squeeze | shape推导类算子，模型构建时即可抵消。 | ☆☆☆☆☆ |
| Pad | 针对HW方向补0的场景性能较优。  其他场景由于乱序的数据重排，性能较差。 | ☆☆☆ |
| MirrorPad | 其他场景由于乱序的数据重排，性能较差。 | ☆ |
| OneHot | 其他场景由于乱序的数据重排，性能较差。 | ☆ |
| Shape | shape推导类算子，模型构建时即可抵消。 | ☆☆☆☆☆ |
| Dequantize | 当前性能硬件最优。 | ☆☆☆☆☆ |
| Quantize | 当前性能硬件最优。 | ☆☆☆☆☆ |

### Detection算子

| IR算子 | 性能使用指导 | 推荐使用指数 |
| --- | --- | --- |
| Permute | 由于乱序的数据重排，虽然做了相关优化，但是硬件不适合过多此类操作。 | ☆☆☆ |
| SSDDetectionOutput | 当前性能最优。 | ☆☆☆☆☆ |

### Image算子

| IR算子 | 性能使用指导 | 推荐使用指数 |
| --- | --- | --- |
| ImageData  DynamicImageData  ImageCrop  ImageChannelSwap  ImageColorSpaceConvertion  ImageResize  ImageDataTypeConversion  ImagePadding | AIPP相关图形处理算子，性能硬件最优。 | ☆☆☆☆☆ |
| CropAndResize | 仅功能支持，性能较差。 | ☆ |
| ResizeBilinear  ResizeBilinearV2  Interp | 大部分场景性能硬件最优，个别场景待优化。 | ☆☆☆☆☆ |
| ResizeNearestNeighbor  Upsample | 大部分场景性能硬件最优，个别场景待优化。 | ☆☆☆☆☆ |
| Crop | 仅功能支持，性能较差。 | ☆ |
| NonMaxSuppressionV3D | 仅功能支持，性能较差。 | ☆ |

## 性能友好计算结构

| 应用场景 | 网络类型 | 推荐指数 | 推荐说明 |
| --- | --- | --- | --- |
| 分类网络 | AlexNet | ☆☆☆☆ | 全连接层权重较大，推理过程带宽受限，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | VGG16 | ☆☆☆☆ | 全连接层权重较大，推理过程带宽受限，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | VGG19 | ☆☆☆ | 全连接层权重较大，推理过程带宽受限，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | ResNet18/34/50/101/152 | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近100%，ResNet50可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)下载。 |
| 分类网络 | GoogleNet | ☆☆☆☆ | 硬件算力利用率接近75%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | InceptionV3 | ☆☆☆☆ | 硬件算力利用率接近85%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | InceptionV4 | ☆☆☆☆ | 硬件算力利用率接近85%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | Inception\_Resnet\_v2 | ☆☆☆☆ | 硬件算力利用率接近90%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | Xception | ☆☆☆☆ | 硬件算力利用率接近85%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | MobileNet\_v1 | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | MobileNet\_v2 | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | MobileNet\_v3 | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | SqueezeNet | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 分类网络 | DenseNet | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%。 |
| 分类网络 | ShuffleNet\_v1  ShuffleNet\_v2 | ☆ | 存在大量shuffleChannel操作，本身是内存搬移操作，非计算受限。  此网络为带宽受限网络，shuffleChannel仅支持功能，性能不保证较优。 |
| 分类网络 | Resnext | ☆☆☆☆ | 硬件算力利用率接近85%。 |
| 分类网络 | EfficientNet | ☆☆☆☆☆ | 模型权重大小适中，硬件算力利用率接近95%。 |
| 分类网络 | SENet | ☆☆☆☆ | 硬件算力利用率接近75%。 |
| 目标检测 | Faster\_RCNN | ☆☆☆☆☆ | 硬件算力利用率接近85%。 |
| 目标检测 | SSD | ☆☆☆☆ | 硬件算力利用率接近85%，当前仅支持通过omg流程生成。 |
| 目标检测 | FPN | ☆☆☆☆☆ | 硬件算力利用率接近90%，后处理不在模型中，由算法单独完成。 |
| 语义分割 | FCN | ☆☆☆☆☆ | 硬件算力利用率接近85%，由于模型计算量较大，实际部署时要做参数裁剪，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载 。 |
| 语义分割 | DeepLabV3 | ☆☆☆ | 硬件算力利用率接近60%，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 语义分割 | Unet | ☆☆☆ | 硬件算力利用率接近60%。 |
| 语义分割 | MaskRcnn | ☆☆ | 硬件算力利用率接近80%（仅限tf->om版本，IR对接方式不支持）。 |
| 语义分割 | PSPNet | ☆☆☆ | 不支持pyramid pooling算子，可以通过多个pool等效，性能一般。 |
| 超分 | VDSR | ☆☆☆☆☆ | 硬件算力利用率接近85%，可以达到实时超分要求，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 超分 | FSRCNN | ☆☆☆☆ | 硬件算力利用率接近70%，可以达到部分实时超分要求，可从[Model Zoo](cannkit-model-zoo.md#model-zoo模型下载)中下载。 |
| 超分 | SRCNN | ☆☆☆☆ | 硬件算力利用率接近70%，可以达到部分实时超分要求。 |
| 超分 | DnCNN | ☆☆☆☆ | 硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。 |
| 超分 | DRCN | ☆☆☆☆ | 硬件算力利用率接近65%，计算量较大，可以达到部分实时超分要求。 |
| 超分 | DRRN | ☆☆☆ | 硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。 |
| 超分 | EnhanceNet | ☆☆☆ | 硬件算力利用率接近60%，计算量较大，可以达到部分实时超分要求。 |
| 语音语义 | RNN | ☆☆ | 功能支持较为单一。 |
| 语音语义 | LSTM | ☆☆ | 功能支持较为单一。 |
| 语音语义 | Transformer | ☆☆☆☆ | 硬件算力利用率接近70%。 |
| 语音语义 | Bert | ☆☆☆☆ | 硬件算力利用率接近70%。 |
