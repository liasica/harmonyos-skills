---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-quantization-effect-evaluation
title: 量化效果评估
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型对接 > CANN LLM模型量化 > 量化效果评估
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:830006819cef8a53228b2af4ee8196913a04fba797bd931cdd182dd3cb38a237
---

用户如果要测试量化后模型效果，可参考插件方法，对浮点模型插入量化算子进行推理，通过对比量化模型与原始浮点模型的输出结果，来评估量化模型精度是否满足要求。模型推理框架和输入不变。

**插件方法：**

以下为推理时对浮点模型插入量化算子，转换浮点模型到量化模型的示例：

```python
import sys
import torch

sys.path.append("轻量化工具链目录")

def get_quanted_model(base_model, dopt_config, quanted_ckpt):
     from dopt_lm.do_opt import(
         optimize_model,
         set_quant_state,
         set_calibrate_state,
     )
     model = optimize_model(base_model, dopt_config)
     model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
     set_quant_state(model, weight_state=True, input_state=True)
     set_calibrate_state(model, False)
     model.eval()
     return model
```

其中，参数的定义分别为：

* base\_model：开发者浮点模型（使用transformers库AutoModelForCausalLM类进行加载）。
* dopt\_config：量化配置文件。
* quanted\_ckpt：量化后pth文件，静态量化取trained.pth，动态量化取trained\_quant\_weight.pth。

**插件方法推理完整示例**：

以下提供qwen2量化推理完整示例供用户参考，在该示例中添加了插件方法去验证量化效果，以量化工具包和量化文件作为输入，进行仿真推理，如果推理结果正常，说明量化成功。

```python
import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.append('轻量化工具链目录')
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def get_quanted_model(base_model, dopt_config, quanted_ckpt):
    from dopt_lm.do_opt import(
        optimize_model,
        set_quant_state,
        set_calibrate_state,
    )
    model = optimize_model(base_model, dopt_config)
    model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
    set_quant_state(model, weight_state=True, input_state=True)
    set_calibrate_state(model, False)
    model.eval()
    return model

def generate(prompt = "Give me a short introduction to large language model."):
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud..."},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    generated_ids = model.generate(
        **model_inputs,
        max_new_tokens=512,
    )
    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    return tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]

if __name__ == '__main__':
    # === 1. 加载原始模型 ===
    model_name = "path/to/model"  # 需替换为实际模型路径
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    # === 2. 加载量化模型 ===
    quant_res_root = 'you_output_path'  # 量化结果目录
    dopt_config = f"./{quant_res_root}/dopt_config.json"  # 阶段一生成的配置文件
    quanted_ckpt = f"./{quant_res_root}/train_output/trained.pth" #静态量化
    quanted_ckpt = f"./{quant_res_root}/train_output/trained_quant_weight.pth" #动态量化
    model = get_quanted_model(
        model,
        dopt_config,
        quanted_ckpt
    )
    # === 3. 执行推理测试 ===
    prompt = "who are you?"
    response = generate(prompt)
    print("量化模型推理结果：", response)
```
