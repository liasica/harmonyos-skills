---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-no-training-and-quantization
title: 无训练量化
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 无训练量化
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ecef552e3f2afb6e653436ded5acfcf47aa81530c9486e7b7190c5fd8d010af
---

## 输入准备

### 准备模型

* TensorFlow开发者

  开发者需提供需要量化的pb模型。
* PyTorch开发者

  开发者需提供需要量化的模型定义py文件以及模型参数pth文件。
* ONNX开发者

  开发者需提供需要量化的ONNX模型。

### 准备校准集

开发者需提供bin格式或图片格式的校准集。bin格式的输入数据需按照以下方式存储，如表1。图片格式的数据为存放测试图片的文件夹，图片格式的输入默认以BGR的三通道彩图读取，读出的数据格式为NCHW，其中N为提供图片的数量。

说明

轻量化工具支持的图片格式包括 ".bmp"，".dib"，".jpeg"，".jpg"，".jpe"，".png"，".webp"，".pbm"，".pgm"，".ppm"，".tiff"，".tif"，".BMP"，".DIB"，".JPEG"，".JPG"，".JPE"，".PNG"，".WEBP"，".PBM"，".PGM"，".PPM"，".TIFF"，".TIF"。

bin格式的输入数据支持两种定义方式，分别适用于任意维度（除4维之外）的输入数据和4维的输入数据（推荐开发者使用任意维度的定义方式）。

对于任意维度（除4维之外）的输入数据，bin文件需按照以下方式定义，以维度（50, 100, 300）的3维数据为例，读出的数据形状为（50, 100, 300）。

**表1** 任意维度（除4维之外）二进制校准集说明

| **文件头/数据** | **地址偏移** | **Type** | **Value** | **Description** |
| --- | --- | --- | --- | --- |
| 文件头（共20字节） | 0000 | 32bit int | 610 | Magic number  当magic number = 610，用来校验文件的合法性。 |
| 文件头（共20字节） | 0004 | 32bit int | 3 | Input data rank |
| 文件头（共20字节） | 0008 | 32bit int | 50 | Input dimension 1 |
| 文件头（共20字节） | 0012 | 32bit int | 100 | Input dimension 2 |
| 文件头（共20字节） | 0016 | 32bit int | 300 | Input dimension 3 |
| 数据 | N/A | Float32 | N/A | 数据数量等于50\*100\*300 |

对于4维的输入数据，bin文件可以按照表1定义，也可以按照表2定义， 以维度（50, 3, 28, 28）的4维数据为例，读出的数据形状为（50, 3, 28, 28）。

**表2** 4维二进制校准集说明

| **文件头/数据** | **地址偏移** | **Type** | **Value** | **Description** |
| --- | --- | --- | --- | --- |
| 文件头（共20字节） | 0000 | 32bit int | 510 | Magic number  当magic number = 510，用来校验文件的合法性 |
| 文件头（共20字节） | 0004 | 32bit int | 50 | Input num |
| 文件头（共20字节） | 0008 | 32bit int | 3 | Input channels |
| 文件头（共20字节） | 0012 | 32bit int | 28 | Input height |
| 文件头（共20字节） | 0016 | 32bit int | 28 | Input width |
| 数据 | N/A | Float32 | N/A | 数据数量等于50\*3\*28\*28 |

说明

轻量化工具已提供脚本支撑bin格式文件的转换，详见[Tools下载](cannkit-preparations.md#tools下载)的tools\_dopt/dopt\_tf\_py3/demo/quant8-8/notrain/bin\_data\_preprocessing.py。

### 填写config.prototxt文件

config.prototxt参数说明如下表所示。其中BINARY模式不进行预处理，IMAGE模式根据开发者给出的均值方差进行预处理。

| 参数名称 | 参数描述 | 是否必填 |
| --- | --- | --- |
| strategy | 优化策略，当前对所有框架都只支持Quant\_INT8-8。 | 否，默认策略为Quant\_INT8-8 |
| device | 使用GPU还是CPU进行量化。  - USE\_GPU：GPU模式  - USE\_CPU：CPU模式 | 否，默认CPU模式 |
| exclude\_op | 量化算子黑名单，配置该参数，算子不进行量化。  支持两种方式，开发者可任选一种方式或两种方式混合使用。  - 使用一个exclude\_op，exclude\_op包含多个op\_name，用分号隔开。  - 使用多个exclude\_op，每个exclude\_op包含一个op\_name 。  当所给op\_name不在模型内时，会报错。  **说明：** ONNX的exclude\_op应该为weight name。 | 否 |
| preprocess\_parameter | 校准数据配置文件路径。 | 是 |

preprocess\_parameter包含的子参数说明如下表所示，对于模型有多输入的情况，每一个输入都需要配置一份preprocess\_parameter。

| 参数名称 | 参数描述 | 是否必填 |
| --- | --- | --- |
| input\_type | 使用二进制文件输入还是图片格式输入。  - BINARY：使用二进制输入  - IMAGE：使用图片格式输入 | 否，默认IMAGE格式 |
| image\_format | 图片格式，仅在IMAGE模式下生效。  - BGR：使用BGR图片格式输入  - RGB：使用RGB图片格式输入 | 否，默认采用BGR |
| mean\_value | 图片预处理的均值参数，仅"IMAGE"模式下生效。  类型为float的数值，范围为0.0-255.0。  mean\_value个数必须和输入的C维度相等。 | 否，默认输入C维度为0.0 |
| standard\_deviation | 图片预处理使用的标准差，仅"IMAGE"模式下生效。  类型为float的数值，需要>=0.0。 | 否，默认为0.0 |
| input\_file\_path | 输入校准集的绝对路径，bin文件路径或存有图片的文件夹。  例如："/path/to/user/data"。 | 是 |

说明

* 当使用"IMAGE"模式输入时，工具链会对图片做如下处理：image = (image - mean\_value) / standard\_deviation。
* 当使用"BINARY"模式时，工具链不会对输入数据做任何处理，即image\_format、mean\_value、standard\_deviation三个参数无效。

配置文件的配置示例如下所示。

* BINARY模式输入

  ```
  1. strategy: "Quant_INT8-8"
  2. device: USE_GPU
  3. // 多输入场景提供不同的bin文件
  4. preprocess_parameter:
  5. {
  6. input_type: BINARY
  7. input_file_path: "path/to/user/bin/caffe_inception_calibrationset1.bin"
  8. }
  9. preprocess_parameter:
  10. {
  11. input_type: BINARY
  12. input_file_path: "path/to/user/bin/caffe_inception_calibrationset2.bin"
  13. }
  14. // ...
  15. exclude_op:  "conv1"
  16. exclude_op:  "conv2;conv3"
  ```
* IMAGE模式输入

  ```
  1. strategy: "Quant_INT8-8"
  2. device: USE_GPU
  3. // 多输入场景提供不同的图片路径
  4. preprocess_parameter:
  5. {
  6. input_type: IMAGE
  7. image_format: BGR
  8. mean_value: 104.0
  9. mean_value: 113.0
  10. mean_value: 123.0
  11. standard_deviation: 0.5
  12. input_file_path: "path/to/user/images1/"
  13. }
  14. preprocess_parameter:
  15. {
  16. input_type: IMAGE
  17. image_format: BGR
  18. mean_value: 104.0
  19. mean_value: 113.0
  20. mean_value: 123.0
  21. standard_deviation: 0.5
  22. input_file_path: "path/to/user/images2/"
  23. }
  24. // ...
  25. exclude_op:  "conv1"
  26. exclude_op:  "conv2;conv3"
  ```

## TensorFlow模型无训练量化

### 环境准备

该功能支持TensorFlow 2.8 CPU或GPU版本。如没有该版本环境，需要自行安装；如已有，则不需要配置环境。

TensorFlow2.8安装方法如下:

```
1. pip3 install tensorflow-gpu==2.8
```

### 模型量化

运行"python3 tools\_dopt/dopt\_tf\_py3/dopt\_so.py"。请在python3环境下运行该命令。

运行该脚本对TensorFlow模型进行无训练量化的参数如下所示。

说明

* 路径：支持大小写字母、数字、下划线。
* 文件名：支持大小写字母、数字、下划线和点(.)。

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| -m, --mode | 是 | 运行模式。  0：无训练模式。（当前只支持0） |
| --framework | 是 | 深度学习框架类型。  3：TensorFlow  5：PyTorch或ONNX |
| --model | 是 | 原始模型文件路径，支持pb模型。 |
| --cal\_conf | 是 | 校准方式量化配置文件路径。  量化配置文件说明请参见[填写config.prototxt文件](cannkit-no-training-and-quantization.md#填写configprototxt文件)。 |
| --output | 是 | 存放量化完成后的模型文件绝对路径，例如"/path/to/out/resnet18.pb"。 |
| --input\_format | 是 | 输入格式数据， NHWC或NCHW。  当开发者选择IMAGE格式或文件头为510的bin文件作为输入数据，并选择输入格式数据为NHWC时，工具会自动调整通道顺序；当选择文件头为610的bin文件作为输入数据时不会调整通道顺序。 |
| --input\_shape | 是 | 输入数据的shape。  例如：“input\_name1: n1, c1，h1, w1; input\_name2: n2, c2, h2,w2”。input\_name必须是转换前的网络模型中的节点名称。多输入input\_shape之间由';'进行分割。input\_shape中指定各维度输入数据值需与网络模型中指定的输入节点所需形状保持一致。例如：假设转换前网络模型指定输入节点为input\_shape\_network: none, 224, 224, 3; input\_shape第2、3、4维度输入数值必须为224,224,3，否则尺寸不匹配。假设转换前网络模型指定输入节点为input\_shape\_network: 1, 224, 224, 3；则input\_shape各维度输入数据均不可变。 |
| --out\_nodes | 是 | 指定输出节点。  例如：“node\_name1; node\_name2; node\_name3”。node\_name必须是模型转换前的网络模型中的节点名称。 |
| --compress\_conf | 是 | 模型文件转为二进制格式文件的路径。  例如：“param\_file”。该文件为轻量化配置，在使用OMG离线模型转换时将被作为参数compress\_conf的输入。 |
| --device\_idx | 否 | GPU或CPU的设备号，默认为0。 |

运行量化脚本后，会输出开发者--output传入同名的pb，以及--compress\_conf传入同名的量化配置文件。例如：开发者--output输入quantmodel.pb，--compress\_conf输入param，最终会输出quantmodel.pb和param。

## PyTorch模型无训练量化

### 环境准备

该功能现仅支持PyTorch1.11版本。使用如下命令安装依赖：

```
1. pip3 install torch==1.11
```

### 模型量化

运行"python3 tools\_dopt/dopt\_pytorch\_py3/dopt\_so.py"。运行该脚本对PyTorch模型进行无训练量化的参数如下所示。

说明

路径：支持大小写字母、数字、下划线。

文件名：支持大小写字母、数字、下划线和点(.)。

| 参数名称 | 是否必填 | 参数描述 |
| --- | --- | --- |
| -m, --mode | 是 | 运行模式。  0：无训练模式。（当前只支持0） |
| --framework | 是 | 深度学习框架类型。  3：TensorFlow  5：PyTorch或ONNX |
| --model | 是 | PyTorch模型定义文件路径。 |
| --weight | 是 | PyTorch模型参数pth文件路径。 |
| --cal\_conf | 是 | 校准方式量化配置文件路径。  量化配置文件说明请参见[填写config.prototxt文件](cannkit-no-training-and-quantization.md#填写configprototxt文件)。 |
| --output | 是 | 存放量化完成后的模型文件绝对路径，例如"/path\_to\_out/resnet.pt"。 |
| --input\_shape | 是 | 输入数据的shape。例如：“input\_name1: n1, c1, h1, w1; input\_name2: n2, c2, h2, w2”。input\_name是模型定义中，forward()函数的入参名称。input\_shape中指定的各输入数据的维度信息，用于转换PyTorch模型，需与实际模型的输入节点形状保持一致。 |
| --compress\_conf | 是 | 模型文件转为二进制格式文件的路径。  例如：“param\_file”。该文件为轻量化配置，在使用OMG离线模型转换时将被作为参数compress\_conf的输入。 |
| --device\_idx | 否 | GPU或CPU的设备号，默认为0。 |
| --input\_format | PyTorch框架无需配置该参数 | 输入格式数据，NHWC或NCHW。  当开发者选择IMAGE格式或文件头为510的bin文件作为输入数据，并选择输入格式数据为NHWC时，工具会自动调整通道顺序；当选择文件头为610的bin文件作为输入数据时不会调整通道顺序。 |
| --out\_nodes | PyTorch框架无需配置该参数 | 指定输出节点。  例如：“node\_name1; node\_name2; node\_name3”。node\_name必须是模型转换前的网络模型中的节点名称。 |

运行量化脚本后，会输出开发者--output传入同名的pt，以及--compress\_conf传入同名的量化配置文件。例如：开发者--output输入quantmodel.pt，--compress\_conf输入param，最终会输出quantmodel.pt和param。

## ONNX模型无训练量化

### 环境准备

该功能支持ONNX Runtime 1.15 CPU版本和ONNX环境。如没有该版本环境，需要自行安装；如已有，则不需要配置环境。

ONNX安装方法如下:

```
1. pip3 install onnx==1.14
```

其他依赖：

```
1. pip3 install protobuf==3.20.0
```

ONNX Runtime CPU版本安装方法如下:

```
1. pip3 install onnxruntime==1.15
```

### 模型量化

运行"python3 tools\_dopt/dopt\_onnx\_py3/dopt\_so.py"。请在python3环境下运行该命令。

运行该脚本对ONNX模型进行无训练量化的参数如下所示。

说明

* 路径：支持大小写字母、数字、下划线。
* 文件名：支持大小写字母、数字、下划线和点(.)。

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| -m, --mode | 是 | 运行模式。  0：无训练模式。（当前只支持0） |
| --framework | 是 | 深度学习框架类型。  3：TensorFlow  5：PyTorch或ONNX |
| --weight | ONNX框架无需配置该参数 | 权值文件路径。 |
| --model | 是 | 原始模型文件路径，支持ONNX模型。 |
| --cal\_conf | 是 | 校准方式量化配置文件路径。  量化配置文件说明请参见[填写config.prototxt文件](cannkit-no-training-and-quantization.md#填写configprototxt文件)。 |
| --output | 是 | 存放量化完成后的模型文件绝对路径，例如"/path\_to\_out/resnet.onnx"。 |
| --input\_format | 是 | 输入格式数据， NHWC或NCHW。  当开发者选择IMAGE格式或文件头为510的bin文件作为输入数据，并选择输入格式数据为NHWC时，工具会自动调整通道顺序；当选择文件头为610的bin文件作为输入数据时不会调整通道顺序。 |
| --input\_shape | 是 | 输入数据的shape。  例如：“input\_name1: n1, c1，h1, w1; input\_name2: n2, c2, h2,w2”。input\_name必须是转换前的网络模型中的节点名称。多输入input\_shape之间由';'进行分割。input\_shape中指定各维度输入数据值需与网络模型中指定的输入节点所需形状保持一致。例如：假设转换前网络模型指定输入节点为input\_shape\_network: none, 224, 224, 3; input\_shape第2、3、4维度输入数值必须为224,224,3，否则尺寸不匹配。假设转换前网络模型指定输入节点为input\_shape\_network: 1, 224, 224, 3；则input\_shape各维度输入数据均不可变。 |
| --out\_nodes | 是 | 指定输出节点。  例如：“node\_name1; node\_name2; node\_name3”。node\_name必须是模型转换前的网络模型中的节点名称。 |
| --compress\_conf | 是 | 模型文件转为二进制格式文件的路径。  例如：“param\_file”。该文件为轻量化配置，在使用OMG离线模型转换时将被作为参数compress\_conf的输入。 |
| --device\_idx | ONNX框架无需配置该参数 | GPU或CPU的设备号，默认为0。 |

运行量化脚本后，会输出开发者--output传入同名的ONNX，以及--compress\_conf传入同名的量化配置文件。例如：开发者--output输入quantmodel.onnx，--compress\_conf输入param，最终会输出quantmodel.onnx和param。
