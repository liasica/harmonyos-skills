---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-external-lora-fine-tuning
title: 量化基模外挂LoRA微调
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > 量化基模外挂LoRA微调
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3b04755c0872e38470fce70184c09543633a4f82d654d61b3f011dd40b699f4d
---

## 简介

Transform结构作为基模完成量化后，可支持基模结构挂载LoRA分支进行特定场景训练。即量化基模+浮点LoRA的结构微调，作用于量化损失修复和下游场景任务续训。

微调准备：

1. 浮点模型:Huggingface开源形式加载即可
2. 量化策略文件: 基于基模量化，需要新增LoRA config配置
3. 量化基模权重: 基于基模量化保存的trained.pth
4. 微调框架：Transform Trainer库架构，或者用户自定义训练架构

微调步骤：

1. 修改基模量化策略文件，增加LoRA相关配置
2. 使用插件式接口进行模型改造
3. 微调模型
4. 保存训练后模型参数
5. 导出量化参数
6. 导出ONNX模型

## 修改基模配置文件

```
1. {
2. "layer_strategy": {
3. "time_embedding.linear_1": {
4. "type": "<class 'torch.nn.modules.linear.Linear'>",
5. "quant_strategy": "XXX",  ### 基模策略
6. ### 新增外挂lora，追加以下内容
7. "lora_config": {
8. "rank": 32,
9. "alpha": 32,
10. "quant_state": false
11. }
12. }
13. }
14. }
```

quant\_state为LoRA结构的量化使能标志，训练时建议使用false，即使用浮点LoRA训练。

## 插件式接口使用

```
1. import os
2. import torch
3. from dopt.dopt_lm.do_opt import (
4. generate_config_file,
5. optimize_model,
6. set_trainable_lora
7. )
8. ### dopt lora ####
9. dopt_config = "dopt_config_withlora.json"
10. model = "your model define"
11. if not os.path.exists(dopt_config):
12. generate_config_file(model, dopt_config)
13. exit()
14. model = optimize_model(model, dopt_config)     ### 基于基模策略文件，已经完成添加lora配置
15. model.load_state_dict(torch.load('xxx.pth'))   ### 基模量化权重trained.pth  strict=False
16. model = set_trainable_lora(model, initia_method='gaussian')
17. ## 即可获得外挂浮点lora+量化基模的torch模型，且支持lora参数可学习，其余参数冻结，支持lora微调。
18. ## initia_method：初始化方法可选："kaiming", "gaussian", "pissa" , 或者不传参默认全0构造。
```

## 微调模型

简单示例：可根据自己需求设计训练框架。

```
1. import torch
2. from datasets import load_dataset
3. from transformers import (
4. AutoModelForCausalLM, # 或 AutoModelForSequenceClassification, etc.
5. AutoTokenizer,
6. TrainingArguments,
7. Trainer,
8. DataCollatorForLanguageModeling
9. )
10. from dopt.dopt_lm.do_opt import (
11. optimize_model,
12. set_trainable_lora
13. )
14. # -------------------- 1. 定义模型和分词器 --------------------
15. # 这是一个用于文本生成的 LLM 示例，您可以替换为任何其他任务的模型
16. MODEL_NAME = "facebook/opt-125m" # 替换为您想微调的模型
17. OUTPUT_DIR = "./opt_lora_finetuned"
18. MAX_SEQ_LENGTH = 128
19. tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
20. # 很多 LLM 没有 pad_token，需要在 LoRA/PEFT 训练中设置
21. if tokenizer.pad_token is None:
22. tokenizer.pad_token = tokenizer.eos_token
23. # 加载基座模型
24. model = AutoModelForCausalLM.from_pretrained(
25. MODEL_NAME,
26. device_map="auto"
27. )
28. # -------------------- 2. LoRA使能 --------------------
29. ## 基于基模策略文件，已经完成添加lora配置
30. dopt_config = "dopt_config.json"
31. model = optimize_model(model, dopt_config)
32. ## 基模量化权重 trained.pth  strict=False
33. model.load_state_dict(torch.load('xxx.pth'), strict=False)
34. model = set_trainable_lora(model, initia_method='gaussian')
35. # -------------------- 3. 数据集准备和预处理 --------------------
36. # 示例：加载一个简单的文本数据集
37. dataset = load_dataset("Abirate/english_quotes", split="train")
38. def preprocess_function(examples):
39. # 简单的格式化：将 quote 和 author 连接起来
40. texts = [f"Quote: {q}\nAuthor: {a}" for q, a in zip(examples["quote"], examples["author"])]
41. # 使用 tokenizer 进行编码
42. return tokenizer(texts,
43. padding="max_length",
44. truncation=True,
45. max_length=MAX_SEQ_LENGTH)
46. # 应用预处理
47. tokenized_dataset = dataset.map(
48. preprocess_function,
49. batched=True,
50. remove_columns=["quote", "author"]
51. )
52. # 分割训练集和验证集 (可选)
53. tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.1)
54. train_dataset = tokenized_dataset["train"]
55. eval_dataset = tokenized_dataset["test"]
56. # Data Collator: 对于 LLM 训练，使用 DataCollatorForLanguageModeling
57. data_collator = DataCollatorForLanguageModeling(
58. tokenizer=tokenizer,
59. mlm=False # Causal LM (GPT-style) 训练设置为 False
60. )
61. # -------------------- 4. 训练参数和 Trainer --------------------
62. training_args = TrainingArguments(
63. output_dir=OUTPUT_DIR,
64. per_device_train_batch_size=4,
65. gradient_accumulation_steps=4, # 模拟更大的 batch size (4 * 4 = 16)
66. warmup_steps=100,
67. max_steps=500, # 限制训练步数，以加快演示速度
68. learning_rate=2e-4, # LoRA 通常可以使用更高的学习率
69. logging_steps=50,
70. save_strategy="steps",
71. save_steps=500,
72. do_eval=True,
73. evaluation_strategy="steps",
74. eval_steps=500,
75. fp16=True, # 启用混合精度训练以提高速度
76. )
77. # 初始化 Trainer
78. trainer = Trainer(
79. model=model,
80. args=training_args,
81. train_dataset=train_dataset,
82. eval_dataset=eval_dataset,
83. tokenizer=tokenizer,
84. data_collator=data_collator,
85. )
86. # -------------------- 5. 开始训练 --------------------
87. print("\n" + "="*20 + " 开始 LoRA 训练 " + "="*20)
88. trainer.train()
89. print("="*20 + " 训练完成 " + "="*20)
90. # -------------------- 6. 保存 LoRA 适配器 --------------------
91. torch.save(model.state_dict(), 'trained_lora.pth')
```

## 导出量化参数

参考[量化参数提取导出](cannkit-plug-in-quantification.md#量化参数提取导出)。量化参数导出的作用是输出量化文件和导出onnx所用的fake\_quant\_weight.pth。

## 导出ONNX模型

示例

```
1. import os
2. import sys
3. import onnx
4. import torch
5. import tempfile
6. from onnxsim import simplify
7. sys.path.append('path/to/dopt_tool')
8. from dopt.common_utils.onnx_helper import OnnxHelper
9. from dopt.dopt_lm.do_opt import (
10. optimize_model,
11. set_quant_state
12. )
13. def aigc_model_save(onnx_model, save_path):
14. model_size = onnx_model.ByteSize()
15. file_name = os.path.basename(save_path)
16. if model_size > 2 * 1024 * 1024 * 1024:
17. logging.info(f"Current ONNX model size is over than 2GB")
18. onnx.save(onnx_model, save_path, save_as_external_data=True,
19. all_tensors_to_one_file=True, location=f'{file_name}.data',
20. size_threshold=1024, convert_attribute=False
21. )
22. else:
23. from onnx.shape_inference import infer_shapes
24. onnx_model = infer_shapes(onnx_model)
25. onnx.save(onnx_model, save_path)
26. transformer_model = "your model define"
27. transformer_model = optimize_model(transformer_model, './dopt_config.json')
28. transformer_model.load_state_dict(torch.load('trained_lora.pth'))
29. set_quant_state(transformer_model, False, False)
30. ## 根据模型输入，随机生成导出onnx所用的输入。
31. dummy_input = ()
32. transformer_model(*dummy_input) ### 检查模型前向推理
33. ## set you onnx input and output node name
34. input_names=["in0_name", "in1_name", "..."]
35. output_names=["out0_name", "out1_name", "..."]
36. onnx_save_path = './xxx.onnx'
37. with torch.no_grad():
38. with tempfile.NamedTemporaryFile() as f:
39. onnx_1 = f.name
40. torch.onnx.export(
41. transformer_model,
42. dummy_input,
43. onnx_1,
44. input_names=input_names,
45. output_names=output_names,
46. opset_version=17,
47. do_constant_folding=True
48. )
49. onnx_model = onnx.load(onnx_1)
50. with tempfile.TemporaryDirectory() as temp_dir:
51. onnx_2 = temp_dir + '/tmp.onnx'
52. aigc_model_save(onnx_model, onnx_2)
53. onnx_model = onnx.load(onnx_2)
54. onnx_rename = OnnxHelper(onnx_model).onnx_model
55. onnx_simed,_ = simplify(
56. onnx_rename,
57. skipped_optimizers=[
58. 'fuse_qkv',
59. 'fuse_matmul_add_bias_into_gemm',
60. 'eliminate_duplicate_initializer'
61. ]
62. )
63. aigc_model_save(onnx_simed, onnx_save_path)
```
