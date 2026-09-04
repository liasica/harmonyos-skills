---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-zoo
title: Model Zoo
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > Model Zoo
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:24+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:8daef54b0bf412fa599dec8efe480f4d99ad9599819b3e6bdf9788d0c2896e41
---

## 概述

Model Zoo提供了可直接调用的硬件最优模型库，集成图片分类、目标检测、语义分割、超分等典型场景的网络模型，包含CANN性能调优使用指导、性能友好模型结构和推荐指数。帮助开发者快速了解算子的参数取值如何在硬件上获得更好的性能和能效收益，以及如何优化模型结构可以实现高性能与低功耗。

## Model Zoo模型下载

在模型下载中，.caffemodel、.pb、.onnx文件是原始浮点模型，基于相关论文实现，并进行了NPU硬件亲和性调整。因此，这些模型的输入尺寸可能与论文中描述的尺寸有所差异。

.om是标准IR算子构建的OM模型文件，其中quant8\_8.om是量化生成的OM模型文件，所有模型可通过[Netron工具](cannkit-visualization-tool-usage.md)可视化。

Model Zoo中模型的名称、性能、模型下载信息如下表所示。

| 场景 | 网络模型（单batch） | 浮点性能[1]（耗时ms） | 量化性能[1]（耗时ms） | 模型下载 | SHA256校验码 | 参考[2] |
| --- | --- | --- | --- | --- | --- | --- |
| 图片分类 | Alexnet | 9.92 | 4.49 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/ff/v3/WgKijE0NS1qcJIJL5rCDHQ/hwhiaimodelzoo-alexnet-100.520.020.011.zip) | 36307375e641bd7d4a334f2c4cf0eafdea498e9f152ea3c1c51a704677ec3835 | [论文&实现](https://arxiv.org/abs/1404.5997) |
| 图片分类 | Resnet18 | 2.63 | 1.24 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/03/v3/vTERUl8GTluL09tUnJ7Jmw/hwhiaimodelzoo-resnet18-100.520.020.011.zip) | 46a553aa7f871bd7f20432e05b45e8dd29c353baba1d378ff46b97bf713aa691 | [论文&实现](https://arxiv.org/abs/1512.03385) |
| 图片分类 | VGG16 | 16.56 | 8.55 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/7d/v3/eZPETpR5R4Si0TOrRWLw2w/hwhiaimodelzoo-vgg16-100.520.020.011.zip) | 2d13fb620ffac15a45966a62128d659257b0872824a8de319fc1e86049643fa4 | [论文&实现](https://arxiv.org/abs/1409.1556) |
| 图片分类 | VGG19 | 18.34 | 8.73 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/56/v3/2WnJO0m7QVma59q77O5Tgw/hwhiaimodelzoo-vgg19-100.520.020.011.zip) | 4306f34da7d12e4347037b9cf303ff9b6b73a5981bd11a0e9e389393e2f9c0b2 | [论文&实现](https://arxiv.org/abs/1409.1556) |
| 图片分类 | Resnet50 | 5.15 | 3.54 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/21/v3/qy49dCmnScexkAVOm__KCg/hwhiaimodelzoo-resnet50-100.520.020.011.zip) | a099a6fbfb961f895ee20a33ba15331687c9c56c4ca9dc4e7edd186d288f0e1f | [论文&实现](https://arxiv.org/abs/1512.03385) |
| 图片分类 | Inception\_v3 | 6.56 | 3.76 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/cb/v3/8JaIaepzSX6R18exmIFWvQ/hwhiaimodelzoo-inceptionv3-100.520.020.011.zip) | c87b0af87eb890b3dc88bf3100911f205ef0f4a89444f76828f0f26ff3fe4c74 | [论文&实现](https://arxiv.org/abs/1512.00567) |
| 图片分类 | Inception\_v4 | 11.90 | 7.29 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b3/v3/Vjc-YJpSRwec6ZuFcVk5kw/hwhiaimodelzoo-inceptionv4-100.520.020.011.zip) | 7e07ac3d437a4b77f6126edce8aaad9161f4966b8a7ccf4ab45c201c7822f103 | [论文&实现](https://arxiv.org/abs/1602.07261) |
| 图片分类 | Inception\_Resnet\_v2 | 15.91 | 5.59 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/76/v3/gW-gLgQORFCqM8jtSSCbtQ/hwhiaimodelzoo-inceptionresnetv2-100.520.020.011.zip) | 7aa61159af9d249a1005bd90ac9b73d12e783d2d1f47d2e04e3ec4d769bf2946 | [论文&实现](https://arxiv.org/abs/1602.07261) |
| 图片分类 | Mobilenet\_v1 | 2.16 | 0.52 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/39/v3/YkAePn2HSgmW8U72yxB9dg/hwhiaimodelzoo-mobilenetv1-100.520.020.011.zip) | 28c5f9eb98a4d73a7f84dd6e1bef0509fa69cc604da0957d802e6f88bc146379 | [论文&实现](https://arxiv.org/abs/1704.04861) |
| 图片分类 | Mobilenet\_v2 | 2.49 | 1.18 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/a8/v3/DQrCYEWFRaO5bHS3nwZFRQ/hwhiaimodelzoo-mobilenetv2-100.520.020.011.zip) | b1bca0efb898c1d3d1afda50803f172724c7b02e1b7abb07581656cf7401d622 | [论文&实现](https://arxiv.org/abs/1801.04381) |
| 图片分类 | Mobilenet\_v2\_1.4 | 3.16 | 1.67 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/79/v3/NfX95ubPQGeiB0LsdJSRyw/hwhiaimodelzoo-mobilenetv2v1p4-100.520.020.011.zip) | d78e276b5cec8c311ac4ac582a11efcaa7704fba798b0639809bdd7f6944256b | [论文&实现](https://arxiv.org/abs/1704.04861) |
| 图片分类 | Mobilenet\_v3\_Large | 3.29 | 2.33 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/7c/v3/IykFBaHlQKqZDbm8U_zTIg/hwhiaimodelzoo-mobilenetv3-100.520.020.011.zip) | b6a6ef84e2002e751a953de619a0442dd36d473612cee55362761ef14583d591 | [论文&实现](https://arxiv.org/abs/1905.02244) |
| 图片分类 | Googlenet | 34.69 | 1.64 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/9b/v3/u6ZoAIfDQLSAeVKWD50Xgg/hwhiaimodelzoo-googlenet-100.520.020.011.zip) | b080ac170fd7a70d511c54864f4e4d4740c1cbd015cbdd7849732ff3da9109a2 | [论文&实现](https://arxiv.org/abs/1409.4842) |
| 图片分类 | Squeezenet\_v1 | 2.13 | 1.24 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c3/v3/aC83DdmoTnqUfRdIWCw3Jw/hwhiaimodelzoo-squeezenetv1-100.520.020.011.zip) | 0af69192a0139a82e7ab534a5331e03bfd6375e7bf4ed3432dfc292303004fb3 | [论文&实现](https://arxiv.org/abs/1602.07360) |
| 目标检测 | SSD\_mobilenetv2\_voc | 5.02 | 2.84 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/1f/v3/p97a_G8OSDinS9Hv3nLrEg/hwhiaimodelzoo-mobilenetv2ssd-100.520.020.011.zip) | 18623a50030858340b23a204b8c65a3fe713f6591c205e6880ff6fa7b3ef1e05 | [论文1&实现1](https://arxiv.org/abs/1801.04381)、[论文2&实现2](https://arxiv.org/abs/1512.02325) |
| 目标检测 | Yolo\_v5 | 4.74 | 4.33 | [ONNX&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b4/v3/gP0tjMfUQQab0ygbagoowA/hwhiaimodelzoo-yolo-100.520.020.011.zip) | 498efe2105fa2ee3f67d3eba270869d51ff667e149bbe4c86927be0bb635a4e3 | [论文&实现](https://arxiv.org/abs/1804.02767) |
| 语义分割 | FCN | 131.23 | 62.76 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c6/v3/3FbS7dMZRJaxIeFgbr4YjQ/hwhiaimodelzoo-fcn-100.520.020.011.zip) | ee77a2e8cd4ba37de6c0587c4c814d4fe5ec1326ae5f6e248ea5e3fdccc0d8e2 | [论文&实现](https://arxiv.org/abs/1605.06211) |
| 语义分割 | DeepLab\_v3 | 17.40 | 13.87 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2d/v3/RtruZ--kSjGi0qJ0WYVzvg/hwhiaimodelzoo-deeplabv3-100.520.020.011.zip) | 979eab9c9416f034ba2592dfa47f8b0aaa4a7aa9ea9c9e0cc1ad87e68ebb0885 | [论文&实现](https://arxiv.org/abs/1706.05587) |
| 超分 | VDSR | 17.71 | 10.67 | [CAFFE&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/a1/v3/ftoOofw5SJ-jyVV3BcpiQg/hwhiaimodelzoo-vdsr-100.520.020.011.zip) | a1063d88e341d6abcf293eb1ba7aee10b5856abd8cd6b8c51594b4375933dc7a | [论文&实现](https://arxiv.org/abs/1511.04587) |
| 超分 | FSRCNN | 17.24 | 17.02 | [TF&OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/ec/v3/K4RspWrzQs-v5rrBUXijpg/hwhiaimodelzoo-fsr-100.520.020.011.zip) | 55c7206c1851ef9b187790a7f8dbba4b58dc4808a1df9798cc0053059b81644c | [论文&实现](https://arxiv.org/abs/1608.00367) |

![](https://media:401788444061485574) 

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
