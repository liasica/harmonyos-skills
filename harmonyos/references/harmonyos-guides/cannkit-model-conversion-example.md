---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-conversion-example
title: 模型转换示例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > 离线模型转换 > 模型转换示例
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac3a6ae5630b15ff384f7095d609c7353b0f3bb7ae1cd5d7e915dcc0432998b6
---

使用CANN Kit SDK时，可以预先使用OMG工具将Caffe、TensorFlow、ONNX、MindSpore模型转换为OM离线模型，移动端AI程序直接读取离线模型进行推理。OMG工具位于[Tools下载](cannkit-preparations.md#tools下载)的tools/tools\_omg下，可运行在64位Linux平台上。

## Caffe模型转换

当前支持[Caffe](https://gitee.com/mirrors/caffe) 1.0版本。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)，转换命令：

```
1. ./omg --model xxx.prototxt --weight yyy.caffemodel --framework 0 --output ./modelname
```

转换示例：

```
1. ./omg --model deploy.prototxt --weight squeezenet_v1.1.caffemodel --framework 0 --output ./squeezenet
```

当看到OMG generate offline model success时，则说明转换成功，会在当前目录下生成squeezenet.om。

## TensorFlow模型转换

当前支持[TensorFlow](https://www.tensorflow.org/?hl=zh-cn) 2.x版本。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)，转换命令：

```
1. ./omg --model xxx.pb --framework 3 --output ./modelname --input_shape "xxx:n,h,w,c" --out_nodes "node_name1:0"
```

转换示例：

```
1. ./omg --model mobilenet_v2_1.0_224_frozen.pb --framework 3 --output ./mobilenet_v2 --input_shape "input:1,224,224,3" --out_nodes "MobilenetV2/Predictions/Reshape_1:0"
```

当看到OMG generate offline model success时，则说明转换成功，会在当前目录下生成mobilenet\_v2.om。

## ONNX模型转换

当前支持[ONNX](https://github.com/onnx/onnx) opset版本7~18（最高支持到V1.13.1）。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)，转换命令：

```
1. ./omg --model xxx.onnx --framework 5 --output ./modelname
```

转换示例:

```
1. ./omg --model resnet18.onnx --framework 5 --output ./resnet18
```

当看到如下log时，则说明转换成功，会在当前目录下生成resnet18.om。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/vSgQqzL1R1euhBKKQYRmrA/zh-cn_image_0000002552959216.png?HW-CC-KV=V1&HW-CC-Date=20260427T235118Z&HW-CC-Expire=86400&HW-CC-Sign=5657A07E6DEFC57A259B6F390B9F6F1CD54903C2FABBEE25E1B7968CEA402301)

## 量化模型转换（以Caffe模型为例）

目前大部分模型在NPU上都是使用16bit float类型进行计算的，使用量化既可以减少模型的体积，也可以加快模型推理速度。

量化模型转换依赖轻量化工具，利用轻量化工具生成模型及轻量化配置，通过"compress\_conf"参数传递给OMG并生成量化模型，更多说明请参见[模型轻量化](cannkit-lightweight-tool-overview.md)。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)，转换命令：

```
1. ./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --output ./modelname  --compress_conf=param
```

转换示例：

```
1. ./omg --model deploy.prototxt --weight squeezenet_v1.1.caffemodel --framework 0 --output ./squeezenet --compress_conf=param
```

当看到OMG generate offline model success时，说明模型量化成功，会在当前目录下生成量化模型squeezenet.om。

## 推理前可变Shape模型转换（以ONNX模型为例）

如果一个模型需要支持一次加载，然后不同次的推理会遇到不同的batch，或者不同的分辨率，那么可以使用推理前可变Shape的模型转换。

在模型转换时，将推理过程可能遇到的所有Shape种类预先通过dynamic\_dims和input\_shape指定出来，生成一个标准IR模型，其携带多种shape输入。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)。

转换示例：

```
1. ./omg --model=./1batch.onnx --input_shape="inputName:-1,3,128,128" --dynamic_dims="1;2;5" --framework=5 --output=./FlexibleShapeModelName
```

说明

不同shape输入对应的不同输出shape，可在模型转换日志中，通过 "Graph:" 关键字查找对应的shape信息，方便在模型推理时指定对应的输出描述。

## MindSpore模型转换

MindSpore支持的算子数量有限，建议通过[TensorFlow模型转换](cannkit-model-conversion-example.md#tensorflow模型转换)或者[ONNX模型转换](cannkit-model-conversion-example.md#onnx模型转换)。

## AIPP模型转换（以Caffe模型为例）

如果模型推理需要对图像或其他输入数据进行变换（如图像尺寸变换、色域转换、减均值/乘系数等），可使用AIPP模型转换功能。转换后的模型增加算子替换此类操作，可提升效率。

命令行中的参数说明请参见[OMG参数](cannkit-overall-parameter.md)，转换命令：

```
1. ./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --insert_op_conf aipp_conf_static.cfg --output ./modelname
```

转换示例：

```
1. ./omg --model deploy.prototxt --weight squeezenet_v1.1.caffemodel --framework 0 --insert_op_conf aipp_conf_static.cfg --output ./squeezenet
```

当出现OMG generate offline model success时，说明AIPP模型转换成功，会在当前目录下生成AIPP squeezenet.om模型。

说明

aipp\_conf\_static.cfg是AIPP的配置文件，位置存放在"tools/tools\_omg/sample"文件夹中，具体说明参见[AIPP配置文件说明](cannkit-aipp-configuration-file.md)。
