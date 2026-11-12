---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-external-lora-fine-tuning
title: 量化基模外挂LoRA微调
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > 量化基模外挂LoRA微调
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:314aaec703004c13f60319d763e59e868bce37f267bd010001f74dddeb2c0ab5
---

## 简介

Transform结构作为基模完成量化后，可支持基模结构挂载LoRA分支进行特定场景训练。即量化基模+浮点LoRA的结构微调，作用于量化损失修复和下游场景任务续训。

微调整体分为两个阶段：

* 训练阶段：先将量化基模权重转换为伪量化权重（fakequant.pth）并替换浮点基模权重，再注入PEFT（Parameter Efficient Fine Tuning，参数高效微调）浮点LoRA适配器完成训练。此时模型结构为普通浮点网络，与常规LoRA微调完全一致，训练框架无需感知量化结构。
* 适配阶段：将训练产出的LoRA adapter权重适配回量化基模结构，lora\_A权重完成minmax量化，lora\_B保持浮点，产出量化态权重lora\_calibrated.pth，供量化参数导出与ONNX导出使用，详见[量化模型导出](cannkit-quant-model-export.md)。

微调准备：

1. 浮点模型：Huggingface开源形式加载即可。
2. 量化策略文件：基模量化的dopt\_config.json，LoRA配置块在适配阶段自动生成。
3. 量化基模权重：基模量化保存的trained\_quant\_weight.pth（动态量化）或trained.pth（静态量化）。
4. 微调框架：Transformers Trainer + PEFT库，或者用户自定义训练架构。

微调步骤：

1. 导出伪量化权重：将量化基模权重转换为伪量化权重fakequant.pth。
2. 微调模型：加载伪量化权重，注入PEFT LoRA适配器训练，保存adapter权重与配置。
3. 生成LoRA量化策略文件：基于基模量化策略文件与adapter配置，生成含lora配置块的dopt\_config\_lora.json。
4. 适配LoRA权重：将adapter权重适配回量化基模结构，产出lora\_calibrated.pth。
5. 导出量化参数与ONNX模型：基于dopt\_config\_lora.json与lora\_calibrated.pth导出，参见[量化模型导出](cannkit-quant-model-export.md)。

## 导出伪量化权重

伪量化权重（fakequant.pth）是指将量化基模的量化结果直接写入浮点权重后的产物：加载浮点基模并注入量化结构、载入量化基模权重后，将每层权重量化器（weight\_quantizer）的伪量化输出回写到模块的weight.data，再剔除state\_dict中所有quant\_op相关key后保存。fakequant.pth与浮点基模的state\_dict键完全一致，训练阶段可直接替换基模浮点权重，模型保持普通浮点网络结构。

示例：

```python
import sys
import torch
from transformers import AutoModelForCausalLM
sys.path.append('轻量化工具链目录')
from dopt_lm.do_opt import (
    optimize_model,
    set_quant_state,
    set_calibrate_state,
)

MODEL_NAME = 'your model path'              ### 浮点基模路径
DOPT_CONFIG = 'dopt_config.json'           ### 基模量化策略文件
QUANT_WEIGHT = 'trained_quant_weight.pth'  ### 基模量化权重
OUTPUT_PTH = 'fakequant.pth'               ### 伪量化权重输出路径

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, trust_remote_code=True, torch_dtype=torch.bfloat16, device_map='auto'
)
### 注入量化结构并加载量化基模权重
model = optimize_model(model, DOPT_CONFIG)
model.load_state_dict(torch.load(QUANT_WEIGHT, map_location='cpu'), strict=False)
set_quant_state(model, weight_state=True, input_state=True)
set_calibrate_state(model, False)
### 将weight_quantizer的伪量化结果写回weight.data
with torch.no_grad():
    for name, m in model.named_modules():
        quant_op = getattr(m, 'quant_op', None)
        if quant_op is None or quant_op.weight_quantizer is None:
            continue
        m.weight.data.copy_(quant_op.weight_quantizer(m.weight.data))
### 剔除state_dict中所有quant_op相关key后保存
ckpt = model.state_dict()
for key in list(ckpt.keys()):
    if 'quant_op' in key:
        ckpt.pop(key)
torch.save(ckpt, OUTPUT_PTH)
```

## 微调模型

训练阶段加载伪量化权重后，按标准PEFT LoRA流程注入LoRA适配器，仅LoRA参数可学习，基模权重全部冻结。开发者也可根据自己需求设计训练架构。示例使用jsonl文本数据集（text字段作为训练语料）：

```python
import json
import torch
from dataclasses import dataclass
from typing import Dict, List
from datasets import Dataset
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    Trainer,
    TrainingArguments,
)
from peft import LoraConfig, get_peft_model, TaskType

MODEL_NAME = 'your model path'   ### 浮点基模路径
FAKEQUANT_PTH = 'fakequant.pth'  ### 伪量化权重
OUTPUT_DIR = './lora_finetuned'
MAX_SEQ_LENGTH = 2048

### 1. 加载分词器与浮点基模
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, trust_remote_code=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, trust_remote_code=True, torch_dtype=torch.bfloat16
)
### 2. 加载伪量化权重替换浮点权重（fakequant.pth与浮点基模的state_dict结构完全一致）
model.load_state_dict(torch.load(FAKEQUANT_PTH, map_location='cpu'), strict=True)
### 3. 注入PEFT LoRA适配器
lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=32,              ### LoRA秩大小，影响模型表达能力
    lora_alpha=64,     ### LoRA缩放因子
    lora_dropout=0.0,  ### LoRA的dropout比例
    target_modules=['q_proj', 'k_proj', 'v_proj', 'o_proj', 'gate_proj', 'up_proj', 'down_proj'],  ### 挂载LoRA分支的模块
    bias='none',
)
model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
### 4. 数据集准备（训练样本量与单条截断长度可按任务场景配置）
texts = []
with open('train_data.jsonl') as f:
    for line in f:
        line = line.strip()
        if line:
            texts.append(json.loads(line)['text'])

def tokenize_fn(examples):
    tokenized = tokenizer(examples['text'], truncation=True, max_length=MAX_SEQ_LENGTH)
    tokenized['labels'] = [list(ids) for ids in tokenized['input_ids']]
    return tokenized

train_dataset = Dataset.from_dict({'text': texts}).map(
    tokenize_fn, batched=True, remove_columns=['text']
)

@dataclass
class DataCollatorForCausalLM:
    ### 填充到batch内最长，label填充-100不参与loss计算
    pad_token_id: int

    def __call__(self, features: List[Dict]):
        max_len = max(len(f['input_ids']) for f in features)
        input_ids, labels, attention_mask = [], [], []
        for f in features:
            pad_len = max_len - len(f['input_ids'])
            input_ids.append(f['input_ids'] + [self.pad_token_id] * pad_len)
            labels.append(f['labels'] + [-100] * pad_len)
            attention_mask.append([1] * len(f['input_ids']) + [0] * pad_len)
        return {
            'input_ids': torch.tensor(input_ids, dtype=torch.long),
            'labels': torch.tensor(labels, dtype=torch.long),
            'attention_mask': torch.tensor(attention_mask, dtype=torch.long),
        }

data_collator = DataCollatorForCausalLM(pad_token_id=tokenizer.pad_token_id)
### 5. 训练参数与Trainer
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,  ### 模拟更大的batch size（4 * 4 = 16）
    learning_rate=2e-4,             ### LoRA通常可以使用更高的学习率
    num_train_epochs=3,
    lr_scheduler_type='cosine',
    warmup_ratio=0.1,
    weight_decay=0.01,
    fp16=True,
    logging_steps=50,
    save_strategy='epoch',
    save_total_limit=2,
    seed=1234,
    remove_unused_columns=False,
    report_to=[],
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
)
### 6. 开始训练，并保存LoRA适配器与分词器
trainer.train()
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)
```

训练产物与建议：

* 训练完成后在OUTPUT\_DIR下产出adapter\_model.safetensors（LoRA权重）与adapter\_config.json（LoRA配置，含target\_modules与rank），后续适配步骤依赖这两个文件。
* 7B以上大模型微调建议开启gradient\_checkpointing并将per\_device\_train\_batch\_size调整为2；遇到显存OOM时，优先开启gradient\_checkpointing，减小per\_device\_train\_batch\_size，并同步增大gradient\_accumulation\_steps，保持等效batch size，或切换空闲GPU。

## 生成LoRA量化策略文件

适配阶段需要为基模量化策略文件中命中LoRA目标模块的Linear层条目新增lora配置块。生成规则：遍历dopt\_config.json的layer\_strategy，模块名后缀命中adapter\_config.json中target\_modules的Linear条目添加或覆盖lora块；未命中的Linear条目若已有lora块则移除；Embedding等其他条目原样保留。lora块中的rank取adapter\_config.json中的r。

```json
{
    "layer_strategy": {
        "model.layers.0.self_attn.q_proj": {
            "type": "<class 'torch.nn.modules.linear.Linear'>",
            "quant_strategy": "XXX",  ### 基模量化策略
            ### 新增外挂LoRA，追加以下内容
            "lora": {
                "rank": 32,  ### LoRA秩大小，与adapter配置中的r一致
                "quant_strategy": "Quant_INT16-8",  ### LoRA分支量化策略
                "float_b": true  ### lora_B保持浮点
            }
        }
    }
}
```

* rank：LoRA秩大小，需与微调时adapter\_config.json中的r一致。
* quant\_strategy：LoRA分支量化策略，建议使用Quant\_INT16-8（数据16bit量化，权重8bit量化）。
* float\_b：LoRA的float-b开关，设置为true时仅lora\_A权重建立量化插槽，lora\_B不建立量化插槽、保持浮点。该字段目前只能支持true，不支持false。

生成示例（也可按上述规则手工编辑策略文件）：

```python
import json

INPUT_DOPT_CONFIG = 'dopt_config.json'   ### 基模量化策略文件
ADAPTER_CONFIG = 'adapter_config.json'   ### 微调训练产出的adapter配置
OUTPUT_DOPT_CONFIG = 'dopt_config_lora.json'

with open(INPUT_DOPT_CONFIG) as f:
    layer_strategy = json.load(f).get('layer_strategy', {})
with open(ADAPTER_CONFIG) as f:
    adapter_cfg = json.load(f)
target_modules = set(adapter_cfg.get('target_modules', []))
lora_rank = adapter_cfg.get('r', 32)
### 为模块名后缀命中target_modules的Linear条目添加或覆盖lora块，未命中的移除lora块，其余条目原样保留
for name, entry in layer_strategy.items():
    if not isinstance(entry, dict) or 'Linear' not in entry.get('type', ''):
        continue
    if name.rsplit('.', 1)[-1] in target_modules:
        entry['lora'] = {
            'rank': lora_rank,
            'quant_strategy': 'Quant_INT16-8',
            'float_b': True,
        }
    elif 'lora' in entry:
        del entry['lora']
with open(OUTPUT_DOPT_CONFIG, 'w') as f:
    json.dump({'layer_strategy': layer_strategy}, f, indent=4)
```

## 适配LoRA权重

适配环节将PEFT adapter权重适配回量化基模结构，步骤如下：

1. 加载浮点基模，使用optimize\_model接口基于dopt\_config\_lora.json注入量化结构（含lora块）。
2. 加载基模量化权重（strict=False，跳过lora相关key）。
3. 读取adapter权重并完成key映射：PEFT的"base\_model.model.<module>.lora\_A.weight"映射为dopt的"<module>.lora.lora\_A.weight"，base\_model.model.<module>.lora\_B.weight"映射为dopt的"<module>.lora.lora\_B.weight，dopt的LoRA结构无alpha缩放因子，lora\_B需乘以lora\_alpha/rank将缩放系数烘焙进权重。
4. lora权重float-b处理：基模保持量化态，使用adapter权重自身对lora\_A的weight\_quantizer做校准收集（按minmax自动计算scale，无需数据校准），并将伪量化结果写回lora\_A权重；lora\_B关闭量化保持浮点。
5. 调用model.eval()完成一次推理验证后，将state\_dict保存为lora\_calibrated.pth。

示例：

```python
import sys
import json
import torch
from transformers import AutoModelForCausalLM
from safetensors.torch import safe_open
sys.path.append('轻量化工具链目录')
from dopt_lm.do_opt import (
    optimize_model,
    set_quant_state,
    set_calibrate_state,
)

MODEL_NAME = 'your model path'
DOPT_CONFIG_LORA = 'dopt_config_lora.json'      ### 含lora块的量化策略文件
QUANT_WEIGHT = 'trained_quant_weight.pth'       ### 基模量化权重
ADAPTER_WEIGHTS = 'adapter_model.safetensors'   ### LoRA权重
ADAPTER_CONFIG = 'adapter_config.json'          ### LoRA配置
OUTPUT_PTH = 'lora_calibrated.pth'

### 1. 加载浮点基模并注入量化结构（含lora块，lora权重为随机初始化）
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, trust_remote_code=True, torch_dtype=torch.bfloat16
)
model = optimize_model(model, DOPT_CONFIG_LORA)
### 2. 加载基模量化权重，跳过lora相关key
quant_sd = torch.load(QUANT_WEIGHT, map_location='cpu')
quant_sd = {k: v for k, v in quant_sd.items() if 'lora.lora' not in k}
model.load_state_dict(quant_sd, strict=False)
### 3. 读取adapter权重并完成key映射，lora_B融合alpha/rank缩放
with open(ADAPTER_CONFIG) as f:
    adapter_cfg = json.load(f)
lora_rank = adapter_cfg.get('r', 32)
lora_alpha = adapter_cfg.get('lora_alpha', lora_rank * 2)
scaling = lora_alpha / lora_rank
model_state = model.state_dict()
with safe_open(ADAPTER_WEIGHTS, framework='pt') as f:
    for key in f.keys():
        tensor = f.get_tensor(key)
        if key.startswith('base_model.model.'):
            key = key[len('base_model.model.'):]
        if key.endswith('.lora_A.weight'):
            dopt_key = key.replace('.lora_A.weight', '.lora.lora_A.weight')
        elif key.endswith('.lora_B.weight'):
            dopt_key = key.replace('.lora_B.weight', '.lora.lora_B.weight')
            tensor = tensor * scaling  ### dopt的LoRA结构无alpha，缩放系数烘焙进lora_B
        else:
            continue
        if dopt_key not in model_state:
            continue
        with torch.no_grad():
            model_state[dopt_key].copy_(tensor.to(model_state[dopt_key].dtype))
### 4. lora权重float-b处理：基模保持量化态，lora_A权重minmax量化，lora_B保持浮点
set_quant_state(model, weight_state=True, input_state=True)
set_calibrate_state(model, False)
for name, m in model.named_modules():
    if not (hasattr(m, 'lora_A') and hasattr(m, 'lora_B')):
        continue
    wq = getattr(getattr(m.lora_A, 'quant_op', None), 'weight_quantizer', None)
    if wq is None:
        continue
    with torch.no_grad():
        ### 使用adapter权重自身做校准收集，minmax自动计算scale，无需数据校准
        wq.set_calibrate_state(True)
        w_fake = wq(m.lora_A.weight.data)
        wq.set_calibrate_state(False)
        ### 伪量化结果写回lora_A权重，保证导出时lora_A为量化权重
        m.lora_A.weight.data.copy_(w_fake)
    ### lora_B关闭量化，保持浮点
    q_b = getattr(m.lora_B, 'quant_op', None)
    if q_b is not None:
        q_b.set_quant_state(False, False)
### 5. 推理验证后保存量化态权重
model.eval()
torch.save(model.state_dict(), OUTPUT_PTH)
```

**说明** 

optimize\_model注入lora结构后，lora\_A量化插槽的scale为占位值，必须执行float-b校准收集，否则lora\_A量化等价于将lora路径压零。

lora\_A的激活量化为动态量化，无参数需收集。

lora\_calibrated.pth为完整量化权重快照，包含基模量化权重、lora\_A/lora\_B权重（lora\_B已融合scaling）及lora\_A量化参数，可直接用于[量化模型导出](cannkit-quant-model-export.md)。

## 模型导出

适配完成后，lora\_calibrated.pth与dopt\_config\_lora.json即为导出输入，量化参数文件提取与ONNX导出的完整流程参见[量化模型导出](cannkit-quant-model-export.md)。

* 量化基模与外挂LoRA权重均支持ONNX导出，LoRA场景导出ONNX时与量化基模导出流程一致，参见[量化模型导出](cannkit-quant-model-export.md)。
* 量化参数文件基于lora\_calibrated.pth与dopt\_config\_lora.json提取，用于离线模型编译。
