---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-quant-model-export
title: 量化模型导出
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > 量化模型导出
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:420b37e02426e767290ff11efd8b89158b201758c09db95149948d441b97cebe
---

## 简介

Transformer结构模型完成量化（LLM模型一站式量化、插件式量化PTQ/QAT），或完成量化基模外挂LoRA微调适配后，可通过本章流程提取量化参数文件并导出ONNX模型（量化IR）。量化参数文件与ONNX模型供OMC/OMG等离线模型编译使用。

支持的量化权重来源：

| 量化权重来源 | 量化策略文件 | 量化权重 | 说明 |
| --- | --- | --- | --- |
| LLM模型一站式量化 | dopt\_config.json | trained\_quant\_weight.pth（动态量化）或trained.pth（静态量化） | 量化阶段产物 |
| 插件式量化（PTQ/QAT） | 量化配置文件 | 标定或量化感知训练后保存的量化权重pth | 参见[插件式量化](cannkit-plug-in-quantification.md) |
| 量化基模外挂LoRA微调 | dopt\_config\_lora.json | lora\_calibrated.pth | LoRA适配产物，参见[量化基模外挂LoRA微调](cannkit-external-lora-fine-tuning.md) |

导出步骤：

1. 导出量化参数：基于量化策略文件与量化权重，提取量化参数文件。
2. 导出ONNX模型：导出包含量化误差的ONNX模型。

对于LLM模型，导出的ONNX模型转换为CANN离线模型的方法可参见[ONNX模型转换CANN模型](cannkit-llm-onnx2cann.md)。

对于AIGC VIT类模型导出参考下面说明，分别导出量化参数和ONNX模型，CANN模型转换参考[ONNX模型转换CANN模型](cannkit-llm-onnx2cann.md)。

## 导出量化参数

使用optimize\_model接口注入量化结构并载入量化权重后，调用generate\_quant\_params提取量化参数文件。量化参数文件用于后续omc离线模型转换，同时会生成伪量化权重fakequant\_weight.pth，产物位置与命名说明如下：

* 量化参数文件为<output\_dir>\_v2（如在./quant\_params\_output下提取，则生成./quant\_params\_output\_v2），该文件生成在output\_dir的同级目录（父目录）下，逐层量化scale包含在该量化参数文件中。
* fakequant\_weight.pth、quant\_info.txt同样生成在output\_dir的同级目录（父目录）下；output\_dir目录本身不存放任何产物，仅用于占位标识输出位置。

**说明** 

量化参数提取也可以在标定完成后直接进行，步骤分离的目的是为了防止过程中有错误，导致标定步骤重来。

```python
import sys
import torch
sys.path.append('轻量化工具链目录')
from dopt_lm.do_opt import (
    generate_quant_params,
    optimize_model,
    set_quant_state,
    set_calibrate_state,
)

output_dir = './quant_params_output'  ### 量化参数输出位置标识目录
model = "your model define"  ### 浮点 nn.module 实例对象
### 量化策略文件与量化权重按上表选择，以下以量化基模为例
quant_config = 'dopt_config.json'  ### LoRA则使用'dopt_config_lora.json'
quant_weight = 'trained_quant_weight.pth' ### LoRA则使用lora_calibrated.pth
model = optimize_model(model, quant_config)
### 加载量化标定后保存的量化权重
model.load_state_dict(torch.load(quant_weight, map_location='cpu'), strict=False)
### 关闭量化参数更新，导出量化参数
set_quant_state(model, weight_state=True, input_state=True)
set_calibrate_state(model, False)
platform = "9030"  ### "9030"/"9050"/"9020"根据实际平台选择，4bit及其以下必须传参，否则不需要（若不传参，工具不会报错，但产物与目标平台不匹配）
generate_quant_params(model, output_dir, platform=platform)
### 量化参数文件为'./quant_params_output_v2'（output_dir同名加"_v2"后缀），生成在output_dir同级目录（父目录）下
### 同级目录还会生成fakequant_weight.pth（仅用作通用ONNX导出方式中替换浮点权重）
### quant_info.txt；output_dir目录本身不会生成存放任何产物
```

## 导出ONNX模型

ONNX导出使用optimize\_model\_for\_onnx\_export接口注入导出用量化结构：该接口内部会剥离量化权重中全部quant\_op相关key（LoRA的lora\_A量化参数不进入ONNX图），并将Linear层替换为ONNX导出专用结构；外挂LoRA场景下lora分支以纯浮点nn.Linear对重建，仅消费lora块中的rank。

```python
import os
import shutil
import sys
import torch
import onnx
sys.path.append('轻量化工具链目录')
from dopt_lm.do_opt import optimize_model_for_onnx_export, process_onnx

transformer_model = "your model define"
### 量化策略文件与量化权重按导出对象选择：
### 量化基模：dopt_config.json + trained_quant_weight.pth（动态量化）或trained.pth（静态量化）
### 外挂LoRA：dopt_config_lora.json + lora_calibrated.pth
quant_config = 'dopt_config.json'
quant_weight = 'trained_quant_weight.pth'
ckpt = torch.load(quant_weight, map_location='cpu')
platform = "9030"  ### "9030"/"9050"/"9020"根据实际SoC型号选择；4bit及其以下必须传参（若不传参，工具不会报错，但导出产物与目标平台不匹配），非4bit场景不需要传递
transformer_model = optimize_model_for_onnx_export(
    transformer_model,
    quant_config, ckpt,
    platform=platform
)
transformer_model.eval()
### 根据模型输入，随机生成导出onnx所用的输入。
dummy_input = ()
transformer_model(*dummy_input)  ### 检查模型前向推理
### 设置你的ONNX输入和输出节点名称
input_names = ["in0_name", "in1_name", "..."]
output_names = ["out0_name", "out1_name", "..."]
### 指定最终输出目录（只落最终交付文件），另建临时目录承接导出中间产物
output_dir = './onnx_output'
tmp_dir = './onnx_export_tmp'
os.makedirs(output_dir, exist_ok=True)
os.makedirs(tmp_dir, exist_ok=True)
tmp_onnx_path = os.path.join(tmp_dir, 'xxx.onnx')
final_onnx_path = os.path.join(output_dir, 'xxx.onnx')
with torch.no_grad():
    torch.onnx.export(
        transformer_model,
        dummy_input,
        tmp_onnx_path,
        input_names=input_names,
        output_names=output_names,
        opset_version=17,
        do_constant_folding=True
    )
### 大模型权重总量超过2GB时，torch.onnx.export无法将权重内联进单个onnx文件，会在导出目录
### 生成大量权重散文件（如onnx__MatMul_xxx）。因此先导出到临时目录（散文件全落在临时目录），
### 再加载模型将全部权重统一保存到指定目录的单一权重文件中：
### 中转权重文件命名为onnx名直接加.pb后缀（xxx.onnx.pb），
### 与process_onnx产出的最终权重文件（xxx.pb）天然区分，不会重名：
relay_weights_name = os.path.basename(final_onnx_path) + '.pb'
m = onnx.load(tmp_onnx_path)   ### 从临时目录连同散文件一并加载权重
onnx.save(m, final_onnx_path,
          save_as_external_data=True,
          all_tensors_to_one_file=True,
          location=relay_weights_name)
shutil.rmtree(tmp_dir)   ### 临时目录（含全部散文件）整体删除
process_onnx(final_onnx_path)   ### 后处理将中转文件中的权重收纳进最终权重文件xxx.pb，onnx图内引用同步改为xxx.pb
os.remove(os.path.join(output_dir, relay_weights_name))   ### 仅删除中转文件xxx.onnx.pb；最终权重文件xxx.pb保留（onnx正引用它）
```

上述流程的最终输出目录仅包含两个交付物：xxx.onnx（图结构）+ xxx.pb（权重文件）。xxx.onnx.pb仅为导出中转文件（承接权重供process\_onnx读取打包），process\_onnx完成后其内容已收纳进xxx.pb，onnx图内引用也同步指向xxx.pb；中转文件在临时目录删除后仍是process\_onnx的唯一权重来源，须在process\_onnx之后再删除（实测删除后onnx加载与推理不受影响）。

xxx.onnx与xxx.pb须成套保留在同目录：onnx图内以location+offset引用pb中的权重，二者任一缺失或分离目录，onnx.load将直接报错（ValidationError），交付与后续OMC转换须保持同目录。

若直接将onnx导出到最终目录且未统一收纳（散文件形态），process\_onnx执行时同样会把散文件收纳进pb，收纳完成后散文件不再被引用、可删除；但过程目录混乱，不推荐。

对于不使用optimize\_model\_for\_onnx\_export的通用导出方式，可加载fakequant\_weight.pth替换浮点模型权重后，使用torch.onnx.export对浮点模型进行导出，必要时完成ONNX模型简化，并确保conv和linear算子名和torch定义名同步。
