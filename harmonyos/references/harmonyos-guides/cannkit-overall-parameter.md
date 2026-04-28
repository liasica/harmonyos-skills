---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-overall-parameter
title: OMG参数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > 离线模型转换 > OMG参数
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e511d2b221045381722a719f75959e5606e3ad70479b7b1d81924352e93509f5
---

说明

* 路径：支持大小写字母、数字、下划线。
* 文件名：支持大小写字母、数字、下划线和点(.)。

| 参数名称 | 参数描述 | 是否必选 | 默认值 |
| --- | --- | --- | --- |
| --h/help | 显示帮助信息。 | 否 | 不涉及 |
| --mode | 运行模式。  0：生成DaVinci模型。  1：模型转json。json可查看模型结构的文本格式。  3：仅做预检，检查模型文件的内容是否合法。 | 否 | 0 |
| --model | 原始框架模型文件路径。 | 是 | 不涉及 |
| --framework | 原始框架类型。  0：Caffe。  3：TensorFlow。  5：ONNX。  6：MindSpore。  **说明：**  - 当mode为1时，该参数可选，可以指定Caffe、TensorFlow、ONNX、MindSpore，不指定时默认为离线模型转json。  - 当mode为0或3时，该参数必选，可以指定Caffe或TensorFlow或ONNX或MindSpore。  - 当原始模型格式为TensorFlow的CheckPoint、SavedModel、TFLite时，推荐使用[tf2onnx](https://github.com/onnx/tensorflow-onnx)工具转换成ONNX模型后使用。 | 是 | 不涉及 |
| --weight | 权值文件路径。当原始模型是Caffe时需要指定。当原始模型是其他框架时不需要指定。 | 否 | 不涉及 |
| --output | 存放转换后的离线模型文件的路径（包含文件名），例如"out/caffe\_resnet18"。转换后的模型文件，会自动以.om的后缀结尾。 | 是 | 不涉及 |
| --hiai\_version | 指定使用OMG的版本，当前支持：v300|v310|IR。 | 否 | IR |
| --om | 模型文件路径。当mode为1时必填。 | 否 | 不涉及 |
| --json | 模型文件转换为json格式文件的路径。 | 否 | 不涉及 |
| --input\_shape | 输入数据的shape。当input\_shape参数为-1时，必须和--dynamic\_dims参数联合使用。  例如：“input\_name1: n1, c1, h1, w1; input\_name2: n2, c2, h2, w2”。input\_name必须是转换前的网络模型中的节点名称。  当原始模型是ONNX时，input\_name必须是模型转换前的网络模型中input算子的name。  **说明：**  - 当原始模型是ONNX，并且ONNX模型输入维度为动态时，此参数必须指定。  - 当原始模型是TensorFlow，并且TensorFlow模型输入维度为动态时，此参数必须指定。 | 否 | 不涉及 |
| --input\_format | 输入数据格式：NCHW和NHWC。  **说明：**  - 当原始框架是Caffe时或ONNX或MindSpore时，此参数不生效。  - 当原始框架是TensorFlow时，绝大多数场景不需要指定，如果转换时提示需要指定，根据实际情况指定。 | 否 | 不涉及 |
| --input\_type | 支持设定模型输入格式，支持指定为FP32、FP16、 INT32、UINT8等，包括多输入和单输入。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该格式的输入。模型输入支持场景详见非AIPP场景设定输入类型支持情况和AIPP场景设定输入类型支持情况。  例如："input\_name1:FP16;input\_name2:UINT8"。  input\_name必须是转换前的网络模型中的节点名称。  当原始模型是ONNX时，input\_name必须是模型转换前的网络模型中input算子的name。 | 否 | FP32 |
| --input\_fp16\_nodes | 不支持与--input\_type同时设置。  指定数据类型为“fp16nchw”的输入节点名称。  例如：“node\_name1;node\_name2”。  **说明：** 当原始框架是ONNX或MindSpore时，此参数不生效。 | 否 | 不涉及 |
| --out\_nodes | 指定输出节点。  - 如果原始模型是TensorFlow或者Caffe，按照以下格式指定：“node\_name1:0;node\_name1:1;node\_name2:0”。  node\_name必须是模型转换前的网络模型中的节点名称。同一个节点的输出从0开始，如果该节点有多个输出，依次往后累加。  - 如果原始模型是ONNX，按照以下格式指定：“tensor\_name1;tensor\_name2”。  tensor\_name必须是模型转换前的网络模型中的节点输出Tensor名称。 | 否 | 不涉及 |
| --output\_type | 支持设定模型的输出数据类型，支持指定为FP32、FP16、INT32、UINT8等，包括多输出和单输出。具体是否能成功生成离线模型，取决于原始模型是否支持指定为该类型的输出。模型输出支持场景详见非AIPP场景设定输入类型支持情况。  例如："output\_name1:FP16;output\_name2:UINT8"。  output\_name必须是转换前的网络模型中的节点名称。  当原始框架是ONNX时，output\_name可以是模型转换前的网络模型中output算子的name或者是开发者指定out\_nodes中所用到的tensor\_name。 | 否 | FP32 |
| --is\_output\_fp16 | 不支持与--output\_type同时设置。  标注输出的数据类型是否为“fp16 nchw”。  例如：false, true, false, true。  **说明：** 当原始框架是ONNX或MindSpore时，此参数不生效。 | 否 | false |
| --stream\_num | 模型使用的stream数量，当前仅支持1。 | 否 | 1 |
| --check\_report | 预检结果保存文件路径。若不指定该路径，在模型转换失败或mode为3（仅做预检）时，将预检结果保存在当前路径下。 | 否 | 不涉及 |
| --net\_format | 指定网络算子优先选用的数据格式。  **说明：** 该参数现已不推荐使用，可通过网络推导得出。 | 否 | 不涉及 |
| --insert\_op\_conf | AIPP配置文件路径。详情参见[模型转换AIPP配置文件说明](cannkit-aipp-configuration-file.md)。 | 否 | 不涉及 |
| --op\_name\_map | 算子映射配置文件路径。包含DetectionOutput网络时需要指定。  例如：不同的网络中DetectionOutput算子的功能不同，指定DetectionOutput到FSRDetectionOutput或者SSDDetectionOutput的映射。  **说明：** 算子映射配置文件的内容示例如：DetectionOutput:SSDDetectionOutput。 | 否 | 不涉及 |
| --compress\_conf | 轻量化配置文件路径。该参数需与轻量化工具搭配使用，由轻量化工具自动生成。具体参见[模型轻量化](cannkit-lightweight-tool-overview.md)。 | 否 | 不涉及 |
| --weight\_data\_type | 支持设定模型权值数据类型，支持指定为FP32或FP16。  该参数仅针对模型中权值数据类型为FP32时生效，根据设定将权值数据类型由FP32转为FP16存储或维持FP32不变。该参数默认值为FP16。  例如："weight\_data\_type:FP16"。  **说明：** 由于CPUCL不支持FP16的权重进行计算，如果模型需要兼容CPU计算库，需要指定该参数为FP32。 | 否 | FP16 |
| --weight\_merge | 离线模型权值归并开关，支持指定在离线模型生成时权值是否进行归并存储操作；该参数为true时，模型权值归并存储。该参数为false时，权值维持非归并存储方式，对性能无影响。该参数默认为true。 | 否 | true |
| --use\_origin\_format | 支持设定模型的输入输出和原始模型保持一致的format。  **说明：** 本参数仅支持基于yolo、inception的业务网络转换设置为true，其它网络转换使用默认值false。 | 否 | false |
| --dynamic\_dims | 支持同一个原始模型生成能支持不同shape输入档位的Davinci模型，该参数指定可以变化的dim值。和\*\*--input\_shape\*\*参数配合使用，在input\_shape参数中可以变化的dim使用-1代替。  该参数中每一种可以变化的dims值使用分号分隔（也称为一档），如果一档中有多个维度，每个维度之间使用逗号分隔。举例：  - 动态batch  --input\_shape = "input\_name1:-1,c,h,w" --dynamic\_dims = "n1;n2;n3"  - 动态分辨率  --input\_shape = "input\_name1:n,-1,-1,c" --dynamic\_dims = "h1,w1;h2,w2"  **说明：** 使用约束：支持可以变化的shape种类最多16种。 | 否 | 不涉及 |
| --platform | 芯片平台，当--target设置为omc时必须设置。 | 否 | 不涉及 |
| --target | 目标模型类型。  - om  硬件无关Davinci模型。  - omc  硬件强相关Davinci模型，仅可在--platform指定的平台部署 | 否 | om |

说明

当前只支持下表列出的情况。

* 非AIPP场景设定输入类型支持情况

  | **原始模型实际输入** | **离线模型期望输入（开发者设定）** | **针对OMG参数** |
  | --- | --- | --- |
  | FP32 | FP16 | --input\_type |
  | FP32 | FP32 | --input\_type |
  | FP16 | FP16 | --input\_type |
  | UINT8 | UINT8 | --input\_type |
  | INT32 | INT32 | --input\_type |
  | INT8 | INT8 | --input\_type |
* AIPP场景设定输入类型支持情况

  | **原始模型实际输入** | **离线模型期望输入** | **是否有AIPP** | **针对OMG参数** |
  | --- | --- | --- | --- |
  | FP32 | UINT8 | 有 | --input\_type |
  | FP16 | UINT8 | 有 | --input\_type |
  | UINT8 | UINT8 | 有 | --input\_type |
* 设定输出类型支持情况

  | **原始模型** | **离线模型输出** | **针对OMG参数** |
  | --- | --- | --- |
  | FP32 | UINT8 | --output\_type |
  | FP16 | UINT8 | --output\_type |
  | UINT8 | UINT8 | --output\_type |
  | FP16 | FP16 | --output\_type |
  | FP32 | FP32 | --output\_type |
  | FP32 | FP16 | --output\_type |
  | FP16 | FP32 | --output\_type |
  | INT8 | INT8 | --output\_type |
  | INT32 | INT32 | --output\_type |
  | INT64 | INT64 | --output\_type |
