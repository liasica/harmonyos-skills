---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-plugin-based-quantization
title: 插件式量化
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 插件式量化
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e3d573bd55c94eea5931c5c9bc8158c663a4ac8381531bfbd11c19c2e6e1ca9d
---

## 依赖环境准备

插件式量化运行环境依赖开发者本身的训练工程环境，目前轻量化工具支持TensorFlow和PyTorch两种框架的插件式量化。

说明

插件式量化环境配置完成后，可同时支持无训练和重训练量化。

## TensorFlow插件式量化

TensorFlow模型优化训练如下步骤：

前提条件：准备模型训练数据集、全精度的基线ckpt文件。

1. 准备TensorFlow环境（[准备TensorFlow环境](cannkit-plugin-based-quantization.md#准备tensorflow环境)）。
2. 调用API生成模型优化策略模板（[获取量化配置模板](cannkit-plugin-based-quantization.md#获取量化配置模板)）。
3. 优化策略文件配置（[优化策略配置](cannkit-plugin-based-quantization.md#优化策略配置)）。
4. 训练模型（[训练或校准模型](cannkit-plugin-based-quantization.md#训练模型)）。（重训练模式对量化模型训练，无训练模式对量化模型进行校准）
5. 提取模型及量化参数（[转换模型](cannkit-plugin-based-quantization.md#转换模型)）。

### 准备TensorFlow环境

准备Linux环境，使用轻量化工具插件式量化功能，开发者需要准备如下依赖。

* python 3.10版本
* 依赖python库说明：

  ```
  1. pip3 install ruamel_yaml
  2. pip3 install pathlib
  3. pip3 install protobuf==3.20.0
  4. pip3 install opencv-python
  ```
* 轻量化工具当前支持tensorflow-gpu 2.8.0版本，使用如下的命令安装：

  ```
  1. pip3 install tensorflow-gpu==2.8.0
  ```

### 获取量化配置模板

将解压出的DDK中的dopt\_tf\_py3添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_tf_py3") ## 其中路径为绝对路径
```

对需要进行量化的TensorFlow模型，调用API生成量化配置json文件。

```
1. from dopt.dopt_tf.opt_main import generate_config_file
2. generate_config_file(sess, dst_path="./config_gen.json")
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| sess | 是 | sess中加载原始的TensorFlow浮点模型。 |
| dst\_path | 是 | dst\_path为生成配置json文件路径。 |

生成的配置样式如下。

```
1. {
2. "quant_strategy_for op 'Conv2D'": [
3. "Quant_INT8-8"
4. ],
5. "quant_strategy_for op 'MatMul'": [
6. "Quant_INT8-8"
7. ],
8. "layer_strategy": {
9. "model/resnet_model/conv2d/Conv2D": {
10. "op_type": "Conv2D",
11. "quant_strategy": "float"
12. },
13. "model/resnet_model/conv2d_1/Conv2D": {
14. "op_type": "Conv2D",
15. "quant_strategy": "float"
16. },

18. }
19. }
```

### 优化策略配置

基于上述生成的配置文件，确定要量化的层，并将对应的quant\_strategy由float调整为对应的量化策略，例如Quant\_INT8-8。

```
1. {
2. "quant_strategy_for op 'Conv2D'": [
3. "Quant_INT8-8"
4. ],
5. "quant_strategy_for op 'MatMul'": [
6. "Quant_INT8-8"
7. ],
8. "layer_strategy": {
9. "model/resnet_model/conv2d/Conv2D": {
10. "op_type": "Conv2D",
11. "quant_strategy": "Quant_INT8-8"
12. },
13. "model/resnet_model/conv2d_1/Conv2D": {
14. "op_type": "Conv2D",
15. "quant_strategy": "Quant_INT8-8"
16. },

18. }
19. }
```

说明

* layer\_strategy中包含的为当前版本所支持的所有可量化层，开发者不应额外添加层。
* 开发者需要根据op\_type选择支持的量化策略，若配置op\_type为不支持的量化策略，那么在后续量化环节会报错。

### 训练模型

开发者需要进行插件式量化时，将解压出的DDK中的dopt\_tf\_py3文件路径添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_tf_py3") ## 其中路径为绝对路径

4. from dopt.dopt_tf.opt_main import optimize_model
```

optimize\_model接口在session中构造模型，并根据配置的量化策略json文件将模型进行量化。

* 配置标志位is\_train\_flag，表示模型当前的量化参数是否随训练更新。
* 配置标志位quant\_flag，表示模型是否走量化通路。

  ```
  1. with tf.Session(config=config) as sess:
  2. ## 待量化的tf模型graph，仅构建拓扑图，不可加载权重
  3. build_tf_model()
  4. quant_flag = tf.placeholder(tf.int32)
  5. is_train_flag = tf.placeholder(tf.bool, name='is_train')
  6. ## 模型量化，自动在 tf.get_default_graph()上进行改图操作
  7. optimize_model(
  8. sess,
  9. config_file,
  10. is_train_flag,
  11. quant_flag
  12. )

  14. ## 调用完optimize_model之后，加载模型权重
  15. saver = tf.Saver()
  16. saver.restore(ckpt)
  17. tf.global_variables_initializer().run()
  ```
* build\_tf\_model：由开发者定义，在session中创建要量化的模型图。
* quant\_flag：tf.int32类型，其中为0表示走浮点通路（不做量化），为1（或其他正值）表示走量化通路，与is\_train\_flag共同作用。
* is\_train\_flag：在quant\_flag > 0时，表示量化参数是否随训练更新。

  | **参数名称** | **是否必填** | **参数描述** |
  | --- | --- | --- |
  | sess | 是 | sess中加载原始的TensorFlow浮点模型。 |
  | config\_file | 是 | 开发者手动配置完成量化层的json文件路径。 |
  | is\_train\_flag | 是 | 模型当前的量化参数是否随训练更新。 |
  | quant\_flag | 是 | 模型是否走量化通路。 |

正常训练模型，检查损失函数loss，效果达标后，可停止训练，需保存对应的ckpt数据。

```
1. ## ckpt save
2. saver = tf.train.Saver()
3. saver.save(sess, train_ckpt_path)
```

开发者需要进行无训练量化时，可以使用set\_calibrate\_state API设置为无训练模式。

```
1. from dopt.dopt_tf.opt_main import set_calibrate_state

3. calibration_mode = True
4. set_calibrate_state(sess, calibration_mode )
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| sess | 是 | 量化后的TensorFlow Session。 |
| calibration\_mode | 是 | bool变量，开发者是否开启无训练（校准）模式。  - True：开启无训练（校准）模式  - False：关闭无训练（校准）模式 |

完成无训练模式的设置之后，使用量化后的"sess"对校准集进行前向推理就可进行无训练量化。

### 转换模型

完成模型量化以及重训练或者校准集前向推理后即可对量化参数进行收集，将session中的量化参数提取至量化文件中并生成对应的PB文件。

将解压出的DDK中的dopt\_tf\_py3文件路径添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_tf_py3") ## 其中路径为绝对路径

4. from dopt.dopt_tf.opt_main import generate_final_model
```

初始化原始浮点模型，加载量化训练的ckpt，利用提供的接口提取参数。

```
1. with tf.Session(config=config) as sess:
2. build_tf_model()
3. generate_final_model(
4. sess,
5. config_file         = FLAGS.config_file,
6. output_name_list    = output_name_list,
7. ckpt_file           = train_ckpt_path,
8. output_dir          = output_dir
9. )
```

build\_tf\_model：由开发者定义，在session中创建要量化的模型图。

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| sess | 是 | sess中加载原始的TensorFlow浮点模型。 |
| config\_file | 是 | 开发者手动配置完成量化层的json文件路径与optimize\_model处理时的配置保持一致。 |
| output\_name\_list | 是 | pb模型的最后一层输出节点名，数据类型为list。 |
| ckpt\_file | 是 | 量化重训练或校准保存的ckpt数据。 |
| output\_dir | 否 | 提取的pb和量化参数保存路径，需确保该路径存在，如果不填写模型在当前路径下保存。 |

## PyTorch插件式量化

PyTorch模型优化训练如下步骤：

前提条件：准备模型训练数据集、全精度的基线参数pth文件。

1. 准备PyTorch环境（[准备PyTorch环境](cannkit-plugin-based-quantization.md#准备pytorch环境)）。
2. 调用API生成量化配置json文件（[生成量化配置json文件](cannkit-plugin-based-quantization.md#生成量化配置json文件)）。
3. 修改策略文件配置（[优化策略配置](cannkit-plugin-based-quantization.md#优化策略配置-1)）。
4. 调用API训练量化模型（[训练或校准模型](cannkit-plugin-based-quantization.md#训练模型-1)）。
5. 调用API生成量化ONNX模型及量化参数文件（[生成量化模型](cannkit-plugin-based-quantization.md#生成量化模型)）。

### 准备PyTorch环境

使用轻量化工具插件式量化功能，开发者需要准备如下依赖。

* python 3.10版本
* 依赖python库说明：

  ```
  1. pip3 install ruamel_yaml
  2. pip3 install pathlib
  3. pip3 install protobuf>=3.20.0
  4. pip3 install onnx==1.14.0
  ```
* 轻量化工具当前仅支持PyTorch 1.11版本。使用如下的命令安装：

  ```
  1. pip3 install torch==1.11.0
  ```

说明

* 路径：支持大小写字母、数字、下划线。
* 文件名：支持大小写字母、数字、下划线和点(.)。

### 生成量化配置json文件

将解压出的DDK中的dopt\_pytorch\_py3文件路径添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_pytorch_py3") ## 其中路径为绝对路径

4. from dopt.dopt_torch.opt_main import generate_config_file
```

对需要进行量化的PyTorch模型，调用API生成量化配置json文件。

```
1. generate_config_file(model, input_shape, dst_path="./config_gen.json") # model：torch.nn.Module， input_shape : "input1:input1.shape;input2:input2.shape"
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| model | 是 | torch.nn.Module，未经过torch.nn.parallel.DistributedDataParallel等分布式API封装的模型。 |
| input\_shape | 是 | 最终部署模型的shape，而非训练阶段的训练数据shape。 |
| dst\_path | 是 | 生成配置json文件路径。 |

### 优化策略配置

生成的配置文件如下：

```
1. {
2. "quant_strategy_for op '<class 'torch.nn.modules.conv.Conv2d'>'": [
3. "Quant_INT8-8"
4. ],
5. "quant_strategy_for op '<class 'torch.nn.modules.linear.Linear'>'": [
6. "Quant_INT8-8"
7. ],
8. "input_shape": "x:1,3,224,224",
9. "params_version": "v1",
10. "layer_strategy": {
11. "conv1/Conv2D": {
12. "op_type": "<class 'torch.nn.modules.conv.Conv2d'>",
13. "quant_strategy": "float"
14. },
15. "conv2/Conv2D": {
16. "op_type": "<class 'torch.nn.modules.conv.Conv2d'>",
17. "quant_strategy": "float"
18. },

20. }
21. }
```

开发者可根据需要的量化修改配置。

* 支持逐层配置量化策略，默认为"float"。
* 支持的量化策略Quant\_INT8-8为8a8w。

以上述json为例，开发者可修改成：

```
1. {
2. "quant_strategy_for op '<class 'torch.nn.modules.conv.Conv2d'>'": [
3. "Quant_INT8-8"
4. ],
5. "quant_strategy_for op '<class 'torch.nn.modules.linear.Linear'>'": [
6. "Quant_INT8-8"
7. ],
8. "input_shape": "x:1,3,224,224",
9. "params_version": "v1",
10. "layer_strategy": {
11. "conv1/Conv2D": {
12. "op_type": "<class 'torch.nn.modules.conv.Conv2d'>",
13. "quant_strategy": "Quant_INT8-8"
14. },
15. "conv2/Conv2D": {
16. "op_type": "<class 'torch.nn.modules.conv.Conv2d'>",
17. "//": "可以逐层配置量化，不量化的层保持浮点",
18. "quant_strategy": "float"
19. },

21. }
22. }
```

* layer\_strategy中包含的为当前版本所支持的所有可量化层，开发者不应额外添加层。
* 开发者需要根据op\_type选择支持的量化策略，若配置op\_type为不支持的量化策略，那么在后续量化环节会报错。
* json文件中，除了input\_shape和layer\_strategy两个key之外，其余内容为提示作用，不会进行解析。
* 参数格式升级，为适应新平台，在 input\_shape 同级key下添加"params\_version": "v2"。

### 训练模型

将解压出的DDK中的dopt\_pytorch\_py3文件路径添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_pytorch_py3") ## 其中路径为绝对路径
3. from dopt.dopt_torch.opt_main import optimize_model
```

开发者需在PyTorch模型定义阶段调用API进行模型的量化操作。

```
1. quant_model = optimize_model(model, config_path) ## config_path为上一步中修改后的json文件绝对路径
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| model | 是 | torch.nn.Module，未经过torch.nn.parallel.DistributedDataParallel等分布式API封装的模型。 |
| config\_path | 是 | 最终部署模型的shape，而非训练阶段的训练数据shape。 |

开发者可根据需要调用API，获取量化相关的损失函数，加入到优化训练中（可选项，简单任务不推荐使用）。

```
1. from dopt.dopt_torch.opt_main import get_quant_loss
2. quant_loss = get_quant_loss(quant_model)
3. total_loss = loss + quant_weight * quant_loss ## quant_weight为量化损失的超参数
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| quant\_model | 是 | 经过optimize\_model API处理后量化模型。 |

对量化训练完成的模型需要保存其对应的checkpoint。

```
1. torch.save(quant_model.state_dict(),"quant.pth")
```

如果开发者无需进行重训练量化可以只进行无训练量化，开启无训练只需调用set\_calibrate\_state API

```
1. from dopt.dopt_torch.opt_main import set_calibrate_state
2. calibrate_mode = True
3. set_calibrate_state(quant_model, calibrate_mode)
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| quant\_model | 是 | 量化后的PyTorch模型。 |
| calibration\_mode | 是 | bool变量，开发者是否开启无训练（校准）模式。  - True：开启无训练（校准）模式  - False：关闭无训练（校准）模式 |

完成无训练模式的设置之后，使用量化后的quant\_model对校准集进行前向推理就可进行无训练量化。

说明

* 调用optimize\_model函数的入参model需要是未经过torch.nn.parallel.DistributedDataParallel等分布式API封装的模型，且优化器optimizer需要针对quant\_model而非原始浮点模型。
* 量化损失非必须添加，quant\_loss需要根据实际量化损失的大小和原始损失的大小进行超参数的调节，一般量化损失函数与原始损失函数比例为1:20，如对优化方向产生较大影响，建议减少量化损失的占比。

### 生成量化模型

将解压出的DDK中的dopt\_pytorch\_py3文件路径添加到python环境变量中：

```
1. import sys
2. sys.path.append(".../dopt_pytorch_py3") ## 其中路径为绝对路径

4. from dopt.dopt_torch.opt_main import generate_final_model
```

训练完成后，使用对应API生成最终模型：

```
1. generate_final_model(
2. model,              ## 浮点模型
3. config_file,         ## 量化配置json文件
4. pth_file = "quant.pth",    ## 量化后 pth 文件
5. output_dir = "./"   ## 量化para与PyTorch的生成文件夹
6. )
```

| **参数名称** | **是否必填** | **参数描述** |
| --- | --- | --- |
| model | 是 | 浮点模型。 |
| config\_file | 是 | 量化配置json文件路径，与optimize\_model api的处理的config\_path保持一致。 |
| pth\_file | 是 | 量化训练的权重文件。 |
| output\_dir | 是 | PyTorch和量化参数保存路径。请确保该路径存在，如果不填写，模型将默认保存到当前路径下。 |

说明

* 调用generate\_final\_model函数的入参model须为重新构建的浮点模型。
* 生成的PyTorch模型中不带有量化参数，但是会做部分图融合以及伪量化处理。
