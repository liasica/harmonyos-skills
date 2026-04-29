---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-examples
title: 模型轻量化示例
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 模型轻量化示例
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:334a61a717422f57f5c2356ef158e946d0cdb89b25cecdebcaa2dc6ea3a0bea3
---

## TensorFlow Quant\_INT8-8无训练量化Demo

### 环境准备

请参见[环境准备](cannkit-no-training-and-quantization.md#环境准备)，安装TensorFlow及依赖。

### 模型配置

* 准备量化模型

  将基线模型的pb文件放入"dopt\_tf\_py3/demo/quant8-8/notrain/tensorflow\_mnist/basemodel/"中。该路径下已经放入了mnist基线模型mnist.pb。
* 准备量化输入数据

  参见[模型量化](cannkit-no-training-and-quantization.md#模型量化)，将图片或二进制形式的校准集放入"dopt\_tf\_py3/demo/quant8-8/notrain/tensorflow\_mnist/mnist\_test/"中。该路径下已经放入了图片校准集。

### 模型量化

执行"dopt\_tf\_py3/demo/quant8-8/notrain/tensorflow\_mnist/"下run\_release.sh即可。

"dopt\_tf\_py3/demo/quant8-8/notrain/tensorflow\_mnist"中存有量化后的pb模型和量化配置文件，运行demo后生成的文件如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/usdb_P3sQ1KBh6-YTGIJ4g/zh-cn_image_0000002558765714.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=06845A60B3DDCB0D10AD5521489AB8BD11D03033AFA65B08DA2F893C032726DB)

## PyTorch Quant\_INT8-8无训练量化Demo

### 环境准备

请参见[环境准备](cannkit-no-training-and-quantization.md#环境准备-1)，安装PyTorch及依赖。

### 模型配置

* 准备量化模型

  将基线模型的模型定义文件(.py)以及模型参数文件放入"dopt\_pytorch\_py3/demo/quant8-8/notrain/pytorch\_mnist/"。

  该路径下已经放入了mnist基线模型定义文件mnist.py以及模型参数文件mnist.pth。
* 准备量化输入数据

  参见[模型量化](cannkit-no-training-and-quantization.md#模型量化-1)，将图片或二进制形式的校准集放入"dopt\_pytorch\_py3/demo/quant8-8/notrain/pytorch\_mnist/"中。

### 模型量化

执行"dopt\_pytorch\_py3/demo/quant8-8/notrain/pytorch\_mnist/"下run\_release.sh即可。

"dopt\_pytorch\_py3/demo/quant8-8/notrain/pytorch\_mnist/"中存有PyTorch无训练量化示例文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/8tSXFzkbS1KCD7n8ALFX-w/zh-cn_image_0000002558606058.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=F7C4858860B05B61A43A5DFB9F9C0812F26AD5AD073C8C327CC174A3171D97A8)

## ONNX Quant\_INT8-8无训练量化Demo

### 环境准备

环境准备请参见[环境准备](cannkit-no-training-and-quantization.md#环境准备-2)，安装ONNX及依赖。

### 示例代码

将dopt\_onnx\_py3 目录添加到系统环境中，在终端环境执行

```
1. python3 ./dopt_so.py \
2. --framework 5 \
3. --mode   0 \
4. --model "./resnet18_matmul.onnx" \          ## 待量化的ONNX模型
5. --cal_conf "./config.prototxt" \            ## 校准集配置文件
6. --output  "./resnet18_matmul_quant.onnx" \  ## 量化后的ONNX文件
7. --input_shape   input:1,3,128,128 \         ## 浮点模型输入shape
8. --compress_conf  ./mnist_param              ## dopt 工具生成的量化文件
```

其中，./config.prototxt配置内容为（[配置文件使用方法](cannkit-no-training-and-quantization.md#onnx模型无训练量化)）：

```
1. strategy: 'Quant_INT8-8'
2. device: USE_CPU
3. preprocess_parameter:
4. {
5. input_type: BINARY
6. input_file_path: './input1.bin'
7. }
```

## TensorFlow Quant\_INT8-8插件式量化Demo

### 环境准备

请参见[准备TensorFlow环境](cannkit-plugin-based-quantization.md#准备tensorflow环境)。安装TensorFlow-gpu 2.8.0版本以及其必要的依赖。

### 示例代码

```
1. import sys
2. sys.path.append(".../dopt_tf_py3") ## 其中路径为绝对路径

4. def generate_config():
5. with tf.Session(config=config) as sess:
6. build_tf_model() ## 自定义tf模型graph，仅构建拓扑图，不可加载权重
7. from dopt.dopt_tf.opt_main import generate_config_file
8. generate_config_file(sess, dst_path="./config_gen.json")

10. def train_model():
11. with tf.Session(config=config) as sess:
12. build_tf_model() ## 自定义tf模型graph，仅构建拓扑图，不可加载权重
13. from dopt.dopt_tf.opt_main import optimize_model
14. quant_flag = tf.placeholder(tf.int32)
15. is_train_flag = tf.placeholder(tf.bool, name='is_train')
16. ## 模型量化，自动在 tf.get_default_graph()上进行改图操作
17. optimize_model(
18. sess,
19. "./config_gen.json",
20. is_train_flag,
21. quant_flag
22. )
23. ## 调用完optimize_model之后，加载模型权重
24. saver = tf.Saver()
25. saver.restore(ckpt)
26. tf.global_variables_initializer().run()
27. ## train model
28. for i in range(...):
29. optimizer = ...
30. feed_dict[is_train_flag] = True
31. feed_dict[quant_flag] = 1
32. sess.run(train_op, feed_dict)
33. ## eval model
34. feed_dict[is_train_flag] = False
35. feed_dict[quant_flag] = 1
36. sess.run(output, feed_dict)
37. evaluate_output(output)

39. def calibrate_model():
40. with tf.Session(config=config) as sess:
41. build_tf_model() ## 自定义tf模型graph，仅构建拓扑图，不可加载权重
42. from dopt.dopt_tf.opt_main import optimize_model, set_calibrate_state
43. quant_flag = tf.placeholder(tf.int32)
44. is_train_flag = tf.placeholder(tf.bool, name='is_train')
45. ## 模型量化，自动在 tf.get_default_graph()上进行改图操作
46. optimize_model(
47. sess,
48. "./config_gen.json",
49. is_train_flag,
50. quant_flag
51. )
52. ## 调用完optimize_model之后，加载模型权重
53. saver = tf.Saver()
54. saver.restore(ckpt)

56. calibration_mode = True
57. set_calibrate_state(sess, calibration_mode )
58. ## eval model
59. feed_dict[is_train_flag] = False
60. feed_dict[quant_flag] = 1
61. sess.run(output, feed_dict)
62. evaluate_output(output)

64. def generate_params():
65. with tf.Session(config=config) as sess:
66. build_tf_model()
67. from dopt.dopt_tf.opt_main import generate_final_model
68. generate_final_model(
69. sess,
70. config_file         = "./config_gen.json",
71. output_name_list    = ["output"],
72. ckpt_file           = "train_ckpt_path",
73. output_dir          = "./output_dir"
74. )
75. if __name__ == "__main__":
76. ## step 1
77. ## 开发者接入，配置修改
78. generate_config()

80. ## step 2
81. ## 训练模型，直至达标
82. train_model() ## 重训练量化模型
83. ## calibrate_model()  ## 校准量化模型

85. ## step 3
86. ## 提取参数，用于后续模型部署
87. generate_params()
```

## PyTorch Quant\_INT8-8插件式量化Demo

### 环境准备

请参见[准备PyTorch环境](cannkit-plugin-based-quantization.md#准备pytorch环境)。安装PyTorch-gpu 1.11版本以及其必要的依赖。

### 示例代码

```
1. import sys
2. sys.path.append(".../dopt_tf_py3") ## 其中路径为绝对路径

4. def generate_config():
5. model = build_torch_model()  ## 开发者待量化的浮点模型
6. generate_config_file(model, input_shape, dst_path="./config_gen.json") # model：torch.nn.Module， input_shape : "input1:input1.shape;input2:input2.shape"
7. return model

9. def train_model():
10. model = build_torch_model() ## 开发者待量化的浮点模型
11. from dopt.dopt_torch.opt_main import optimize_model
12. model.load_state_dict(state)  ## load 浮点模型参数

14. ## 调用optimize model 量化模型
15. quanted_model = optimize_model(model, config_path)

17. ## train model
18. quant_loss = get_quant_loss(quant_model)
19. optimizer = torch.optim.SGD(quanted_model.parameters(), lr=0.001, momentum=0.9) ## 假设使用SGD优化器

21. for input_data, label in range(...):
22. optimizer.zero_grad()
23. outputs = model(input_data)
24. loss = loss_fn(outputs, label) ## loss_fn 为原始浮点网络训练loss

26. total_loss = loss + quant_weight * quant_loss ## quant_weight是指量化损失所占比例
27. loss.backward()

29. optimizer.step()

31. def calibrate_model():
32. model = build_torch_model() ## 开发者待量化的浮点模型
33. from dopt.dopt_torch.opt_main import optimize_model, set_calibrate_state
34. model.load_state_dict(state)  ## load 浮点模型参数

36. ## 调用optimize model 量化模型
37. quanted_model = optimize_model(model, config_path)

39. calibrate_mode = True
40. set_calibrate_state(model, calibrate_mode)

42. for input_data, label in range(...):
43. outputs = model(input_data)

45. def generate_params():
46. model = build_torch_model()
47. from dopt.dopt_torch.opt_main import generate_final_model
48. generate_final_model(model,
49. config_file,
50. pth_file="quant.pth",
51. output_dir="./results_dir")

53. if __name__ == "__main__":
54. ## step 1
55. ## 开发者接入，配置修改
56. generate_config()

58. ## step 2
59. ## 训练模型，直至达标
60. train_model()
61. ## 无训练模式
62. ## calibrate_model()

64. ## step 3
65. ## 提取参数，用于后续模型部署
66. generate_params()
```

## TensorFlow NASEA网络结构搜索Demo

### NASEA分类网络

分类网络Demo位于tools\_dopt/dopt\_tf\_py3/demo/nas\_ea/ea\_cls\_imagenet，包含5个文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Ev4JaMwQSTWXowe2A_zYjA/zh-cn_image_0000002589325585.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=7FBF0E2A76D4DE11055D760C995EDF4A8F8C0707615F64286F1A6468751851AC)

* blocks.so：搜索空间文件
* readme.md：搜索训练指导文件
* run\_release.sh：开始搜索的执行脚本
* scen.yaml：配置项
* user\_module.py：工具的自定义接口

执行步骤：

1. 准备ImageNet数据集（tfrecord格式），并修改scen.yaml文件中的数据集路径。
2. 环境准备请参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。
3. 加载依赖的开源代码：

   1. 进入分类网络demo目录：

      ```
      1. cd tools_dopt/dopt_tf_py3/demo/nas_ea/ea_cls_imagenet
      ```
   2. 下载开源代码：

      ```
      1. git clone https://github.com/Tensorflow/models.git
      ```
   3. 进入开源代码目录：

      ```
      1. cd models
      ```
   4. 切换到指定版本：

      * 如果TensorFlow版本为1.12.0，执行如下命令：

        ```
        1. git checkout v1.12.0
        ```
      * 如果TensorFlow版本为2.1.0，执行如下命令：

        ```
        1. git checkout v2.1.0
        ```
   5. 返回分类网络demo目录：

      ```
      1. cd ..
      ```
   6. 设置PYTHONPATH默认路径：

      ```
      1. export PYTHONPATH=$PYTHONPATH:`pwd`/models/
      ```

   说明

   每次打开终端需要重新执行一次上述命令，或添加到“~/.bashrc”文件，并执行“source ~/.bashrc”。
4. 配置demo下的scen.yaml文件，请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)。scen.yaml中提供了建议参数，开发者可根据实际需求修改。
5. 修改demo下的user\_module.py文件，模型接口定义请参见[TensorFlow用户自定义接口](cannkit-network-structure-search-training.md#tensorflow开发者自定义接口)。user\_module.py中提供了建议配置，开发者可根据实际需求进行修改。
6. 执行脚本run\_release.sh，在results下，生成多个model\_arch\_result\_\*.py文件。开发者可根据log\_classification中提供的信息选择合适的网络结构进行训练。后续训练可参考readme.md中的指导。

### NASEA检测网络

检测网络Demo位于"tools\_dopt/dopt\_tf\_py3/demo/nas\_ea/ea\_det\_coco"，包含6个文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/faUyUzHFRHmZbGEA3rBi4A/zh-cn_image_0000002589245523.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=89B057AC9310CAEB919C768029B9F054B107727FFD4A075AE5E57832DC7FA32A)

* blocks.so：搜索空间文件。
* pre\_train.yaml：预训练的配置项。
* readme.md：搜索训练指导文件。
* run\_release.sh：开始搜索的执行脚本。
* scen.yaml：配置项。
* user\_module.py：工具的自定义接口。

执行步骤：

1. 准备数据集，包括用于预训的ImageNet数据集（tfrecord格式）和用于训练的COCO数据集（原始格式）。若有完成预训练的ckpt文件，则不需再准备ImageNet数据集。请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)，修改scen.yaml文件中的数据集路径。
2. 环境准备请参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。
3. 加载依赖的开源代码。

   1. 进入检测网络demo目录。

      ```
      1. cd tools_dopt/dopt_tf_py3/demo/nas_ea/ea_det_coco
      ```
   2. 下载开源代码。

      ```
      1. git clone https://github.com/pierluigiferrari/ssd_keras.git
      2. git clone https://github.com/Tensorflow/models.git
      ```
   3. 进入开源代码目录。

      ```
      1. cd ssd_keras
      ```
   4. 切换到指定版本。

      ```
      1. git checkout -b v0.9.0
      ```
   5. 返回检测网络demo目录。

      ```
      1. cd ..
      ```
   6. 进入models开源代码目录。

      ```
      1. cd models
      ```
   7. 切换models到指定版本。

      如果TensorFlow版本为1.12.0，执行如下命令：

      ```
      1. git checkout v1.12.0
      ```

      如果TensorFlow版本为2.1.0，则执行如下命令：

      ```
      1. git checkout v2.1.0
      ```
   8. 进入models开源代码目录

      ```
      1. cd models
      ```
   9. 设置PYTHONPATH默认路径

      ```
      1. export PYTHONPATH=$PYTHONPATH:`pwd`/models/
      ```
   10. 按照readme.md中的step1~step4步骤，修改相关开源文件。
4. 配置demo的scen.yaml文件和pre\_train.yaml，请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)。scen.yaml中提供了建议参数，开发者可根据实际需求修改。
5. 修改demo的user\_module.py文件，模型接口定义请参见[TensorFlow用户自定义接口](cannkit-network-structure-search-training.md#tensorflow开发者自定义接口)。user\_module.py中提供了建议配置，开发者可根据实际需求进行修改。
6. 执行脚本run\_release.sh，在results下，生成多个model\_arch\_result\_\*.py文件。开发者可根据log\_detection中提供的信息选择合适的网络结构进行训练。后续训练可参考readme.md中的指导。

### NASEA分割网络

分割网络Demo位于tools\_dopt/dopt\_tf\_py3/demo/nas\_ea/ea\_seg\_voc，包含 6个文件，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/JOehe6pFQfyAfur0xj2ICw/zh-cn_image_0000002558765716.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=F9B6118056C7728EAE8D4689150D6840BC7E57BD0F41FE23CFAFDAC6A6DC0AAF)

* blocks.so：搜索空间文件。
* pre\_train.yaml：预训练的配置项
* readme.md：搜索训练指导文件。
* run\_release.sh：开始搜索的执行脚本。
* scen.yaml：配置项。
* user\_module.py：工具的自定义接口。

执行步骤：

1. 准备数据集，包括用于预训练的ImageNet数据集（tfrecord格式）和用于训练的VOC数据集（tfrecord格式）。若有完成预训练的ckpt文件，则不需再准备ImageNet数据集。请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)，修改scen.yaml文件中的数据集路径。
2. 环境准备请参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。
3. 加载依赖的开源代码。

   1. 进入分割网络demo目录。

      ```
      1. cd tools_dopt/dopt_tf_py3/demo/nas_ea/ea_seg_voc
      ```
   2. 下载开源代码：

      ```
      1. git clone https://github.com/Tensorflow/models.git
      ```
   3. 进入开源代码目录。

      ```
      1. cd models
      ```
   4. 切换到指定版本。

      ```
      1. git checkout v1.13.0
      ```
   5. 返回分割网络demo目录。

      ```
      1. cd ..
      ```
   6. 设置PYTHONPATH默认路径：

      ```
      1. export PYTHONPATH=$PYTHONPATH:`pwd`/models/research:`pwd`/models/research/slim
      ```
   7. 如果TensorFlow版本为2.1.0，需要执行如下命令：
      1. 创建models\_tf2.1，并进入文件夹

         ```
         1. mkdir models_tf2.1
         2. cd models_tf2.1
         ```
      2. 下载开源实现

         ```
         1. git clone https://github.com/Tensorflow/models.git
         ```
      3. 进入开源代码路径

         ```
         1. cd models
         ```
      4. 切换到指定版本

         ```
         1. git checkout v2.1.0
         ```
      5. 返回models\_tf2.1目录

         ```
         1. cd ..
         ```
      6. 设置PYTHONPATH默认路径

         ```
         1. export PYTHONPATH=$PYTHONPATH:`pwd`/models/
         ```

         说明

         每次打开终端需要重新执行一次上述命令，或添加到"~/.bashrc"文件，并执行"source ~/.bashrc"。
   8. 修改开源实现，按照readme.md中修改开源实现的步骤，修改相关开源文件。
4. 配置demo的scen.yaml文件和pre\_train.yaml，请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)。scen.yaml中提供了建议参数，开发者可根据实际需求修改。
5. 修改demo的user\_module.py文件，模型接口定义请参见[TensorFlow用户自定义接口](cannkit-network-structure-search-training.md#tensorflow开发者自定义接口)。user\_module.py中提供了建议配置，开发者可根据实际需求进行修改。
6. 执行脚本run\_release.sh，在results下，生成多个model\_arch\_result\_\*.py文件。开发者可根据log\_segmentation中提供的信息选择合适的网络结构进行训练。后续训练可参考readme.md中的指导。

## PyTorch NASEA网络结构搜索Demo

### NASEA分类网络

分类网络Demo位于tools\_dopt/dopt\_pytorch\_py3/demo/nas\_ea/ea\_cls\_imagenet\_pytorch，包含5个文件，如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/GK7P3ciQRWq8gfGPxUYzQw/zh-cn_image_0000002558606060.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=C5CAC9F73D8008067348598AF65D8F30BBD4F4C3AB44572EE51C2759447E5173)

* blocks.so：搜索空间文件
* readme.md：搜索训练指导文件
* run\_release.sh：开始搜索的执行脚本
* scen.yaml：配置项
* user\_module.py：工具的自定义接口

执行步骤：

1. 准备ImageNet数据集（原始格式），并修改scen.yaml文件中的数据集路径。
2. 环境准备请参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。
3. 配置demo下的scen.yaml文件，请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)。scen.yaml中提供了建议参数，开发者可根据实际需求修改。
4. 修改demo下的user\_module.py文件，模型接口定义请参见[PyTorch开发者自定义接口](cannkit-network-structure-search-training.md#pytorch开发者自定义接口)。user\_module.py中提供了建议配置，开发者可根据实际需求进行修改。
5. 执行脚本run\_release.sh，在results下，生成多个model\_arch\_result\_\*.py文件。开发者可根据log\_classification中提供的信息选择合适的网络结构进行训练。后续训练可参考readme.md中的指导。

### NASEA分割网络

分割网络Demo位于tools\_dopt/dopt\_pytorch\_py3/demo/nas\_ea/ea\_seg\_voc\_pytorch，包含 6个文件，如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/N7sf-Oa5ToS1R0lPIvIwuQ/zh-cn_image_0000002589325587.png?HW-CC-KV=V1&HW-CC-Date=20260429T054054Z&HW-CC-Expire=86400&HW-CC-Sign=DF8CF290E84572A547537533EF46100AB460314FA5F71ADD65CD8EE6E2517ADA)

* blocks.so：搜索空间文件
* pre\_train.yaml：预训练的配置项
* readme.md：搜索训练指导文件
* run\_release.sh：开始搜索的执行脚本
* scen.yaml：配置项
* user\_module.py：工具的自定义接口

执行步骤：

1. 准备数据集，包括用于预训练的ImageNet数据集（原始格式）和用于训练VOC数据集（原始格式）。若有完成预训练的ckpt文件，则不需再准备ImageNet数据集。请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)，修改scen.yaml文件中的数据集路径。
2. 环境准备请参见[环境准备](cannkit-network-structure-search-training.md#环境准备)。
3. 加载依赖的开源代码：参考tools\_dopt/dopt\_pytorch\_py3/demo/nas\_ea/ea\_seg\_voc\_pytorch/readme.md
4. 配置demo下的scen.yaml文件和pre\_train.yaml文件，请参见[搜索参数配置](cannkit-network-structure-search-training.md#搜索参数配置)。scen.yaml中提供了建议参数，开发者可根据实际需求修改。
5. 修改demo下的user\_module.py文件，模型接口定义请参见[PyTorch开发者自定义接口](cannkit-network-structure-search-training.md#pytorch开发者自定义接口)。user\_module.py中提供了建议配置，开发者可根据实际需求进行修改。
6. 执行脚本run\_release.sh，在results下，生成多个model\_arch\_result\_\*.py文件。开发者可根据log\_segmentation中提供的信息选择合适的网络结构进行训练。后续训练可参考readme.md中的指导。
