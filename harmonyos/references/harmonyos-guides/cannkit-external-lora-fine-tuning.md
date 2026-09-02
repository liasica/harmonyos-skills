---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-external-lora-fine-tuning
title: 量化基模外挂LoRA微调
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > 量化基模外挂LoRA微调
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:34+08:00
doc_updated_at: 2026-07-17
content_hash: sha256:710b46f3c26411543497437de77e561738f47642c365c7d0a15ddbe37ac99de2
---

## 简介

Transform结构作为基模完成量化后，可支持基模结构挂载LoRA分支进行特定场景训练。即量化基模+浮点LoRA的结构微调，作用于量化损失修复和下游场景任务续训。

微调准备：

1. 浮点模型：Huggingface开源形式加载即可
2. 量化策略文件：基于基模量化，需要新增LoRA config配置
3. 量化基模权重：基于基模量化保存的trained.pth
4. 微调框架：Transform Trainer库架构，或者用户自定义训练架构

微调步骤：

1. 修改基模量化策略文件，增加LoRA相关配置
2. 使用插件式接口进行模型改造
3. 微调模型
4. 保存训练后模型参数
5. 导出量化参数
6. 导出ONNX模型

## 修改基模配置文件

```json
{
    "layer_strategy": {
        "time_embedding.linear_1": {
            "type": "<class 'torch.nn.modules.linear.Linear'>",
            "quant_strategy": "XXX",  ### 基模策略
            ### 新增外挂lora，追加以下内容
            "lora_config": {
                "rank": 32, ### LoRA秩大小，影响模型表达能力
                "alpha": 32, ### LoRA缩放因子，通常设置为与rank相同的值
                "quant_state": false ### 是否启用量化状态，在LoRA训练中建议设为False
            }
        }
}
}
```

quant\_state为LoRA结构的量化使能标志，训练时建议使用false，即使用浮点LoRA训练。

## 插件式接口使用

```python
import os
import torch
from dopt.dopt_lm.do_opt import (
    generate_config_file,
    optimize_model,
    set_trainable_lora
)
### dopt lora ####
dopt_config = "dopt_config_withlora.json"
model = "your model define"
if not os.path.exists(dopt_config):
    generate_config_file(model, dopt_config)
    exit()
model = optimize_model(model, dopt_config)     ### 基于基模策略文件，已经完成添加lora配置
model.load_state_dict(torch.load('xxx.pth'))   ### 基模量化权重trained.pth  strict=False
model = set_trainable_lora(model, initia_method='gaussian')
## 即可获得外挂浮点lora+量化基模的torch模型，且支持lora参数可学习，其余参数冻结，支持lora微调。
## initia_method：初始化方法可选："kaiming", "gaussian", "pissa" , 或者不传参默认全0构造。
```

## 微调模型

简单示例：可根据自己需求设计训练框架。

```python
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM, # 或 AutoModelForSequenceClassification, etc.
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from dopt.dopt_lm.do_opt import (
    optimize_model,
    set_trainable_lora
)
# -------------------- 1. 定义模型和分词器 --------------------
# 这是一个用于文本生成的 LLM 示例，您可以替换为任何其他任务的模型
MODEL_NAME = "facebook/opt-125m" # 替换为您想微调的模型
OUTPUT_DIR = "./opt_lora_finetuned"
MAX_SEQ_LENGTH = 128
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
# 很多 LLM 没有 pad_token，需要在 LoRA/PEFT 训练中设置
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
# 加载基座模型
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto"
)
# -------------------- 2. LoRA使能 --------------------
## 基于基模策略文件，已经完成添加lora配置
dopt_config = "dopt_config.json"
model = optimize_model(model, dopt_config)
## 基模量化权重 trained.pth  strict=False
model.load_state_dict(torch.load('xxx.pth'), strict=False)
model = set_trainable_lora(model, initia_method='gaussian')
# -------------------- 3. 数据集准备和预处理 --------------------
# 示例：加载一个简单的文本数据集
dataset = load_dataset("Abirate/english_quotes", split="train")
def preprocess_function(examples):
    # 简单的格式化：将 quote 和 author 连接起来
    texts = [f"Quote: {q}\nAuthor: {a}" for q, a in zip(examples["quote"], examples["author"])]
    # 使用 tokenizer 进行编码
    return tokenizer(texts,
                     padding="max_length",
                     truncation=True,
                     max_length=MAX_SEQ_LENGTH)
# 应用预处理
tokenized_dataset = dataset.map(
    preprocess_function,
    batched=True,
    remove_columns=["quote", "author"]
)
# 分割训练集和验证集 (可选)
tokenized_dataset = tokenized_dataset.train_test_split(test_size=0.1)
train_dataset = tokenized_dataset["train"]
eval_dataset = tokenized_dataset["test"]
# Data Collator: 对于 LLM 训练，使用 DataCollatorForLanguageModeling
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False # Causal LM (GPT-style) 训练设置为 False
)
# -------------------- 4. 训练参数和 Trainer --------------------
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4, # 模拟更大的 batch size (4 * 4 = 16)
    warmup_steps=100,
    max_steps=500, # 限制训练步数，以加快演示速度
    learning_rate=2e-4, # LoRA 通常可以使用更高的学习率
    logging_steps=50,
    save_strategy="steps",
    save_steps=500,
    do_eval=True,
    evaluation_strategy="steps",
    eval_steps=500,
    fp16=True, # 启用混合精度训练以提高速度
)
# 初始化 Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=eval_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
)
# -------------------- 5. 开始训练 --------------------
print("\n" + "="*20 + " 开始 LoRA 训练 " + "="*20)
trainer.train()
print("="*20 + " 训练完成 " + "="*20)
# -------------------- 6. 保存 LoRA 适配器 --------------------
torch.save(model.state_dict(), 'trained_lora.pth')
```

## 导出量化参数

参考[量化参数提取导出](cannkit-plug-in-quantification.md#量化参数提取导出)。量化参数导出的作用是输出量化文件和导出onnx所用的fake\_quant\_weight.pth。

## 导出ONNX模型

示例

```python
import os
import sys
import onnx
import torch
import tempfile
from onnxsim import simplify
sys.path.append('path/to/dopt_tool')
from dopt.common_utils.onnx_helper import OnnxHelper
from dopt.dopt_lm.do_opt import (
    optimize_model,
    set_quant_state
)
def aigc_model_save(onnx_model, save_path):
    model_size = onnx_model.ByteSize()
    file_name = os.path.basename(save_path)
    if model_size > 2 * 1024 * 1024 * 1024:
        logging.info(f"Current ONNX model size is over than 2GB")
        onnx.save(onnx_model, save_path, save_as_external_data=True,
                        all_tensors_to_one_file=True, location=f'{file_name}.data',
                        size_threshold=1024, convert_attribute=False
        )
    else:
        from onnx.shape_inference import infer_shapes
        onnx_model = infer_shapes(onnx_model)
        onnx.save(onnx_model, save_path)
transformer_model = "your model define"
transformer_model = optimize_model(transformer_model, './dopt_config.json')
transformer_model.load_state_dict(torch.load('trained_lora.pth'))
set_quant_state(transformer_model, False, False)
## 根据模型输入，随机生成导出onnx所用的输入。
dummy_input = ()
transformer_model(*dummy_input) ### 检查模型前向推理
## 设置你的ONNX输入和输出节点名称
input_names=["in0_name", "in1_name", "..."]
output_names=["out0_name", "out1_name", "..."]
onnx_save_path = './xxx.onnx'
with torch.no_grad():
    with tempfile.NamedTemporaryFile() as f:
        onnx_1 = f.name
        torch.onnx.export(
            transformer_model,
            dummy_input,
            onnx_1,
            input_names=input_names,
            output_names=output_names,
            opset_version=17,
            do_constant_folding=True
        )
        onnx_model = onnx.load(onnx_1)
    with tempfile.TemporaryDirectory() as temp_dir:
        onnx_2 = temp_dir + '/tmp.onnx'
        aigc_model_save(onnx_model, onnx_2)
        onnx_model = onnx.load(onnx_2)
        onnx_rename = OnnxHelper(onnx_model).onnx_model
    onnx_simed,_ = simplify(
        onnx_rename,
        skipped_optimizers=[
            'fuse_qkv',
            'fuse_matmul_add_bias_into_gemm',
            'eliminate_duplicate_initializer'
        ]
    )
    aigc_model_save(onnx_simed, onnx_save_path)
```
