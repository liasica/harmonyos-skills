---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-large-language-one-stop
title: LLM模型一站式量化
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > LLM模型一站式量化
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1573bbaca0a7378ee1dad2a7631fb880b6e2af131cba04a47a058fa67ebe7a09
---

## 简介

本工具提供大语言模型（Large Language Model，以下简称LLM）的4bit低位量化能力，采用标准的三段式量化流程：权重量化、激活量化和量化参数提取。三段式量化流程说明如下表所示。

**表1** 大语言模型4bit低位量化三阶段流程

| 阶段 | 输入 | 输出 |
| --- | --- | --- |
| 阶段一（权重量化） | - 开发者提供  - JSON数据集（text字段作为prompt）  - HuggingFace模型路径（开发者浮点模型）  - 量化配置及执行文件  - config.yaml  - run.sh | - dopt\_config.json：开发者需完成该文件的量化策略配置后，重新执行此阶段  - trained\_quant\_weight.pth：权重量化参数  **说明：** 开发者需根据阶段一生成的dopt\_config.json文件手动进行量化策略配置后，再次执行该阶段。 |
| 阶段二（激活量化） | - 开发者提供  - JSON数据集（text字段作为prompt）  - HuggingFace模型路径（开发者浮点模型）  - 量化配置及执行文件  - config.yaml  - run.sh | trained.pth：用于阶段三加载或量化仿真验证 |
| 阶段三（量化参数提取） | - 开发者提供  - JSON数据集（text字段作为prompt）  - HuggingFace模型路径（开发者浮点模型）  - 量化配置及执行文件  - config.yaml  - run.sh | - fake\_quant\_weight.pth：用于ONNX模型导出  - quant\_params\_file：权重及激活量化参数 |

## 量化前准备工作

* HuggingFace浮点模型
* JSON格式数据集，使用“text”字段作为prompt关键字
* 量化配置文件[config.yaml](cannkit-large-language-one-stop.md#configyaml示例)
* [run.sh](cannkit-large-language-one-stop.md#runsh示例)执行脚本

说明

* LLM在量化过程中使用AutoModelForCausalLM以及AutoTokenizer加载，所以开发者的HuggingFace浮点模型需要满足该加载方式约束。
* run.sh执行脚本环境须与开发者推理或者训练环境保持一致，否则模型加载或推理失败。

### config.yaml示例

config.yaml用于模型量化配置，开发者可根据实际需要进行配置。以下示例可供参考，主要参数说明请参见[config.yaml配置参数说明](cannkit-large-language-one-stop.md#configyaml配置参数说明)。

```
1. kd:
2. enable: False
3. loss: mse
4. micro_batch_size: 2
5. gradient_accumulation_steps: 4
6. weight_decay: 0.0
7. warmup_steps: 10
8. num_epochs: 3
9. learning_rate: !!float 1e-4
10. eval_step: 1
11. logging_step: 50
12. lr_scheduler_type: cosine
13. trainable_keys:
14. - quant_alpha
15. - norm
16. no_split_module_classes:
17. - Qwen2DecoderLayer
18. - GlmDecoderLayer
19. - LlamaDecoderLayer
20. - HunYuanDecoderLayer
21. dataset:
22. train_files: dataset.json
23. train_samples: 1024
24. ptq_samples: 1024
25. extra_training_config:
26. fp16: True
27. cutoff_len: 128
28. num_samples: 256
29. quant_param_2: False
30. embedding_separate: True
31. lm_head_size:
```

### config.yaml配置参数说明

以下为config.yaml文件的关键配置参数，具体说明如下表所示。

| 参数 | 参数 | 默认取值 | 说明 |
| --- | --- | --- | --- |
| kd：量化蒸馏相关 | enable | False | - True：使用蒸馏量化策略  - False：使用无训练量化策略，速度快，效果较稳定 |
| kd：量化蒸馏相关 | loss | mse | 量化蒸馏损失函数，仅支持mse |
| kd：量化蒸馏相关 | micro\_batch\_size | 2 | 单卡batch |
| kd：量化蒸馏相关 | gradient\_accumulation\_steps | 4 | 梯度累计步数 |
| kd：量化蒸馏相关 | weight\_decay | 0.0 | 权重衰减系数 |
| kd：量化蒸馏相关 | warmup\_steps | 10 | 预热步数 |
| kd：量化蒸馏相关 | num\_epochs | 3 | 训练迭代次数 |
| kd：量化蒸馏相关 | learning\_rate | 1e-4 | 学习率 |
| kd：量化蒸馏相关 | logging\_step | 50 | log打印步数 |
| kd：量化蒸馏相关 | lr\_scheduler\_type | cosine | 学习率调整策略。 |
| kd：量化蒸馏相关 | trainable\_keys | - | 配置可训练参数。  - quant\_alpha：量化层的可训练参数  - norm：layer\_norm层的可训练参数 |
| kd：量化蒸馏相关 | no\_split\_module\_classes | - | 多卡切分时，选择切分粒度。  - Qwen2DecoderLayer  - GlmDecoderLayer  - LlamaDecoderLayer  - HunYuanDecoderLayer |
| dataset | train\_files | - | JSON格式训练数据文件，dataset.json |
| dataset | train\_samples | 1024 | kd使能为True时， 训练集样本数，缺省默认全量数据集 |
| dataset | ptq\_samples | 1024 | PTQ优化样本数，缺省默认全量数据集 |
| dataset | extra\_training\_config | fp16 | 训练数据类型，仅支持fp16 |
| dataset | cutoff\_len | 128 | 激活量化样本序列长度。 |
| dataset | num\_samples | 256 | 激活量化校准样本数 |
| dataset | quant\_param\_2 | False | - True：Kirin9020  - False：KirinX90 |
| dataset | embedding\_separate | True | - True：单独保存为bin文件  - False: 导出embedding的量化参数到量化文件，合并形态。 |
| dataset | lm\_head\_size: | - | 可指定lmhead长度，硬件对齐。 |

## 执行三段式量化

按以下步骤执行run.sh文件，stagex为传入参数，具体可参考[run.sh示例](cannkit-large-language-one-stop.md#runsh示例)。

1. 权重量化。

   1. 选配量化策略。

      生成插件式量化配置文件[dopt\_config.json](cannkit-large-language-one-stop.md#dopt_configjson量化配置文件说明)。

      ```
      1. bash run.sh stage1
      ```

      量化策略可选配置为：

      ```
      1. Quant_act_weight_eco   decode层策略
      2. Quant_lm_head          lm_head层策略
      3. Quant_Embed_MinMax     embedding层策略
      ```
   2. 进行权重量化。

      ```
      1. bash run.sh stage1
      ```
2. 激活量化。

   ```
   1. bash run.sh stage2
   ```
3. 提取量化参数。

   ```
   1. bash run.sh stage3
   ```

### run.sh示例

```
1. #!/bin/bash
2. set -e
3. qlibs='path/to/dopt_pytorch_py3'
4. export WANDB_DISABLED=true
5. export HF_DATASETS_OFFLINE=0
6. export PYTHONPATH=${qlibs}:$PYTHONPATH
7. # 设置为cuda或npu模式，二选一
8. # cuda模式
9. export DEVICE=cuda
10. export CUDA_VISIBLE_DEVICES=1
11. # npu模式
12. # export DEVICE=npu
13. # export ASCEND_RT_VISIBLE_DEVICES=2,3
14. ROOT=.
15. testcase='output_dir'
16. RUN_FILE=${qlibs}/dopt/dopt_lm/opt_main.py
17. output_dir=${ROOT}/${testcase}/train_output
18. mkdir -p ${output_dir}
19. cp ${ROOT}/config.yaml $output_dir
20. model_path='path/to/model'
21. dopt_config=./${testcase}/dopt_config.json
22. quant_stage=$1
23. block_size=128
24. python -u \
25. ${RUN_FILE} --model-path $model_path \
26. --dopt-config $dopt_config \
27. --optimize-config ${ROOT}/config.yaml \
28. --quant-stage $quant_stage \
29. --block-size $block_size \
30. --output-dir ${output_dir} 2>&1 | tee ${output_dir}/logs.log
```

### dopt\_config.json量化配置文件说明

工具支持开发者插件式自定义LLM量化规格：

* 逐层权重量化位宽(bit)和分组大小(group\_size)。
* 逐层激活量化位宽(bit)。
* 量化策略：decoder层使用"Quant\_act\_weight\_eco"，lm\_head层使用"Quant\_lm\_head"，embedding层使用"Quant\_Embed\_MinMax"。

```
1. {
2. "layer_strategy": {
3. "model.layers.0.self_attn.q_proj": {
4. "type": "<class 'torch.nn.modules.linear.Linear'>",
5. "quant_strategy": "Quant_act_weight_eco",
6. "weight":{
7. "bit": 4,
8. "group_size": 64
9. }
10. "input":{
11. "bit": 16
12. }
13. }
14. }
15. }
```

## 量化工具输出件

```
1. trained.pth            ### 量化仿真可使用该文件
2. fake_quant_weight.pth  ### 导出onnx文件使用该权重
3. trained_quant_weight.pth ### 阶段一的输出，阶段二的输入
```

## 量化仿真

量化完成后，开发者可进行量化仿真推理，通过对比量化模型与原始浮点模型的输出结果，来评估量化模型精度是否满足要求。量化仿真推理工程可参考[qwen2模型量化仿真推理demo](cannkit-large-language-one-stop.md#qwen2模型量化仿真推理demo)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/HIXwOHSWQKyy-FsLxeQIiQ/zh-cn_image_0000002552799560.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T235115Z&HW-CC-Expire=86400&HW-CC-Sign=6FDC22B54883050CF2E3A3CC21718D60F3B53E2BD4ADE253587FB27518C49744)

### 插件方法

浮点模型完成加载和初始化后，使用以下接口将浮点模型转换为量化模型，模型推理逻辑不变，可参考[qwen2模型量化仿真推理demo](cannkit-large-language-one-stop.md#qwen2模型量化仿真推理demo)。

```
1. import sys
2. sys.path.append("path/to/dopt")
3. def get_quanted_model(base_model, dopt_config, quanted_ckpt):
4. from dopt.dopt_lm.do_opt import(
5. optimize_model,
6. set_quant_state,
7. set_calibrate_state,
8. set_run_mode,
9. )
10. model = optimize_model(base_model, dopt_config)
11. model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
12. set_quant_state(model, weight_state=True, input_state=True)
13. set_calibrate_state(model, False)
14. model.eval()
15. return model
```

* base\_model：开发者浮点模型（使用transformers库AutoModelForCausalLM类进行加载）。
* dopt\_config：量化配置文件。
* quanted\_ckpt：量化后pth文件。

### qwen2模型量化仿真推理demo

```
1. import os
2. import sys
3. import torch
4. from transformers import AutoModelForCausalLM, AutoTokenizer
5. sys.path.append('path/to/dopt')
6. os.environ["CUDA_VISIBLE_DEVICES"] = "0"
7. def get_quanted_model(base_model, dopt_config, quanted_ckpt):
8. """
9. 加载量化模型核心函数
10. :param base_model: 原始HF模型对象
11. :param dopt_config: 量化配置文件路径（dopt_config.json）
12. :param quanted_ckpt: 量化权重路径（trained.pth）
13. :return: 量化后的模型
14. """
15. from dopt.dopt_lm.do_opt import(
16. optimize_model,
17. set_quant_state,
18. set_calibrate_state,
19. set_run_mode,
20. )
21. # 模型量化优化（根据配置文件应用4bit量化策略）
22. model = optimize_model(base_model, dopt_config)
23. # 加载量化权重（强制CPU加载避免显存冲突）
24. model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
25. # 设置量化状态
26. set_quant_state(model, weight_state=True, input_state=True)  # 启用权重和激活量化
27. set_calibrate_state(model, False)  # 关闭校准模式
28. model.eval()
29. return model
30. def generate(prompt = "Give me a short introduction to large language model."):
31. """
32. 量化模型推理函数
33. :param prompt: 输入文本（默认示例prompt）
34. :return: 模型生成的响应
35. """
36. # 构建Qwen2专用对话模板
37. messages = [
38. {"role": "system", "content": "You are Qwen, created by Alibaba Cloud..."},
39. {"role": "user", "content": prompt}
40. ]
41. # 应用模板并tokenize
42. text = tokenizer.apply_chat_template(
43. messages,
44. tokenize=False,
45. add_generation_prompt=True
46. )
47. model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
48. # 执行生成
49. generated_ids = model.generate(
50. **model_inputs,
51. max_new_tokens=512,  # 控制最大生成长度
52. )
53. # 后处理：去除输入部分
54. generated_ids = [
55. output_ids[len(input_ids):]
56. for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
57. ]
58. return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
59. if __name__ == '__main__':
60. # === 1. 加载原始模型 ===
61. model_name = "path/to/model"  # 需替换为实际模型路径
62. model = AutoModelForCausalLM.from_pretrained(
63. model_name,
64. torch_dtype=torch.float16,  # 半精度加载
65. device_map="auto"           # 自动分配GPU
66. )
67. tokenizer = AutoTokenizer.from_pretrained(model_name)
68. # === 2. 加载量化模型 ===
69. quant_res_root = 'dsr1_qwen7b_ptq'  # 量化结果目录
70. dopt_config = f"./{quant_res_root}/dopt_config.json"    # 阶段一生成的配置文件
71. quanted_ckpt = f"./{quant_res_root}/train_output/trained.pth"  # 阶段二生成的权重
72. model = get_quanted_model(
73. model,
74. dopt_config,  # 需确保已正确配置量化参数
75. quanted_ckpt   # 需与当前模型架构匹配
76. )
77. # === 3. 执行推理测试 ===
78. prompt = "who are you?"
79. response = generate(prompt)
80. print("量化模型推理结果：", response)
81. """
82. 预期输出示例：
83. "Hi, I am Qwen, ..."
84. """
```
