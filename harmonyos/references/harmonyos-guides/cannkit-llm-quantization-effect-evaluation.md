---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-quantization-effect-evaluation
title: 量化效果评估
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型能力开放 > CANN LLM模型量化 > 量化效果评估
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:a628bbd6c56045100b8befbdef306a35840cb7e83149c76e504194c870dfbd9d
---

用户如果要测试量化后模型效果，可参考插件方法，对浮点模型插入量化算子进行推理即可。 模型推理框架和输入不变。

**插件方法：**

以下为推理时对浮点模型插入量化算子，转换浮点数到量化模型的示例：

```python
import sys
import torch

sys.path.append("path/to/dopt_torch_py3")

def get_quanted_model(base_model, dopt_config, quanted_ckpt):
    from dopt.dopt_lm.opt_main import (optimize_model, set_quant_state, set_calibrate_state, set_run_mode,)
    model = optimize_model(base_model, dopt_config)
    model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
    set_quant_state(model, weight_state=True, input_state=True)
    set_calibrate_state(model, False)
    model.eval()
    return model
```

其中，参数的定义分别为：

* base\_model：浮点模型定义，加载自AutoModelForCausalLM等接口。
* dopt\_config：量化配置文件。
* quanted\_ckpt：量化后的pth文件。

**插件方法推理完整示例**：

以下提供qwen2量化推理完整示例供用户参考，在该示例中添加了插件方法去验证量化效果，以量化工具包和量化文件作为输入，进行仿真推理，如果推理结果正常，说明量化成功。

```python
import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# 填写DDK_tools工具包中tools_dopt/dopt_pytorch_py3的真实路径
sys.path.append('path/to.dopt')
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def get_quanted_model(base_model, dopt_config, quanted_ckpt):
    from dopt.dopt_lm.opt_main import (optimize_model, set_quant_state, set_calibrate_state, set_run_mode,)
    model = optimize_model(base_model, dopt_config)
    model.load_state_dict(torch.load(quanted_ckpt, map_location=torch.device('cpu')), strict=True)
    set_quant_state(model, weight_state=True, input_state=True)
    set_calibrate_state(model, False)
    model.eval()
    return model

def generate(prompt="Give me a short introduction to large language model."):
    messages = [
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud. You are a helpful assistant"},
        {"role": "user", "content": prompt}
    ]
    text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
    print(model_inputs)
    generated_ids = model.generate(**model_inputs, max_new_tokens=512)
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return response

if __name__ == '__main__':
    # 填写原模型的真实路径
    model_name = "path/to/model"
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.float16,
        device_map="auto"
    )
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    quant_res_root = 'you_output_path'
    # 量化配置
    dopt_config = f"/{quant_res_root}/dopt_config.json"
    # 量化权重
    quanted_ckpt = f"/{quant_res_root}/train_output/trained.pth"
    model = get_quanted_model(
        model,
        dopt_config,
        quanted_ckpt
    )
    prompt = "who are you?"
    response = generate(prompt)
    print(response)
```
