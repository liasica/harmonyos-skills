---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-usage-environmental-preparation
title: 环境准备
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型能力开放 > CANN LLM模型量化 > 量化使用步骤 > 环境准备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:44+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:d7244d7e7b64a441fa21dba47e1093d0b4a1e4c4127aaac90f940372efa0fcb6
---

将大模型部署到资源受限的PC设备时，通常需要对模型进行量化，CANN LLM模型量化提供了对应的量化工具链。

* LLM大模型量化工具：提供16-4 grouplinear量化能力，涵盖embedding、decoder以及lm head层。
* 输入：用户的原始模型Pytorch模型和参与量化的数据集。
* 输出：量化后的模型以及量化配置文件。
* 支持平台：Kirin X90（支持以下所有模型）。

从模型社区网站下载所需的源模型文件：

[Qwen2.5-1.5B下载链接](https://link.gitcode.com/?target=https://huggingface.co/Qwen/Qwen2.5-1.5B&from=https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Guide/CANN%2520LLM%2520%25E5%25A4%25A7%25E8%25AF%25AD%25E8%25A8%2580%25E6%25A8%25A1%25E5%259E%258B%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588.md&lang=zh&theme=white)

[DeepSeek-R1-Distill-Qwen-1.5B下载链接](https://link.gitcode.com/?target=https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B&from=https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Guide/CANN%2520LLM%2520%25E5%25A4%25A7%25E8%25AF%25AD%25E8%25A8%2580%25E6%25A8%25A1%25E5%259E%258B%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588.md&lang=zh&theme=white)

[Glm-1.5B下载链接](https://link.gitcode.com/?target=https://huggingface.co/zai-org/glm-edge-1.5b-chat&from=https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Guide/CANN%2520LLM%2520%25E5%25A4%25A7%25E8%25AF%25AD%25E8%25A8%2580%25E6%25A8%25A1%25E5%259E%258B%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588.md&lang=zh&theme=white)

[Qwen2.5-7B-Instruct下载链接](https://link.gitcode.com/?target=https://huggingface.co/Qwen/Qwen2.5-7B-Instruct&from=https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Guide/CANN%2520LLM%2520%25E5%25A4%25A7%25E8%25AF%25AD%25E8%25A8%2580%25E6%25A8%25A1%25E5%259E%258B%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588.md&lang=zh&theme=white)

[Qwen3-8B下载链接](https://link.gitcode.com/?target=https://huggingface.co/Qwen/Qwen3-8B&from=https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/blob/master/CANN_LLM/CANN_LLM_Engine_Guide/CANN%2520LLM%2520%25E5%25A4%25A7%25E8%25AF%25AD%25E8%25A8%2580%25E6%25A8%25A1%25E5%259E%258B%25E8%25A7%25A3%25E5%2586%25B3%25E6%2596%25B9%25E6%25A1%2588.md&lang=zh&theme=white)

## 软件依赖

1. 环境配置：下载[量化工程](https://gitcode.com/HarmonyOS_Samples/cannkit_samplecode_lm_engine_cpp/tree/master/CANN_LLM/CANN_LLM_Engine_Model)，参考cannkit\_samplecode\_lm\_engine\_cpp/requirements.txt进行环境配置。
2. DDK\_tools工具包：

   * 下载 DDK\_tools[工具包](cannkit-preparations.md)与[平台插件包](cannkit-preparations.md)。
   * 注意：确保插件包与CANN Kit版本匹配（匹配关系请参见[开发准备](cannkit-preparations.md)）。

## 目录结构配置

下载OMG工具和对应平台的插件包，将插件包解压后放到OMG工具的platform文件夹下（根据平台下载对应插件包，插件包以实际为准）。确保目录结构如下：

```text
  tools
  ├── platform
  │  ├── kirinx90
  ├── tools_ascendc // 自定义算子工具，配合自定义算子工程使用
  ├── tools_dopt // 量化工具链所在文件夹，以下流程中量化部分使用
  ├── tools_omg // omg工具所在文件夹，以下流程omg转换流程使用
```

## 数据集准备

量化工具需要校准数据。请按照以下JSON格式在json文件配置数据集（例如dataset.json）。

数据文本格式示例：

```json
[
    {
        "text": "who you are?"
    }
 ]
```

* 注意：开发者使用自己场景数据时需要将数据文本格式规范到上述格式，按照以上json格式和提问的方式进行数据集制作。

## 修改配置

在量化工程根目录CANN\_LLM\_Engine\_Model/下，创建config.yaml和run.sh两个文件。

## config.yaml

注意：拷贝使用时需要删除相关注释，避免出现报错。

```yaml
kd:
  enable: False // 蒸馏量化使能，false时使用PTQ优化策略
  loss: mse // 蒸馏loss函数
  micro_batch_size: 2 // 每个卡的batch数
  gradient_accumulation_steps: 4 // 梯度累计步数
  weight_decay: 0.0 // 权重衰减系数
  warmup_steps: 10 // 预热步数
  num_epochs: 3 // 训练迭代次数
  learning_rate: !!float 1e-4 // 学习率
  eval_step: 1 // 验证步数
  logging_step: 50 // log打印步数
  lr_scheduler_type: cosine // 学习率调整策略
  trainable_keys: // 配置可训练参数，可选[quant_alpha,norm]
    - quant_alpha
    - norm
  no_split_module_classes: // 多卡切分时，选择切分粒度
    - Qwen3DecoderLayer
    - Qwen2DecoderLayer
    - GlmDecoderLayer
    - LlamaDecoderLayer
    - HunYuanDecoderLayer

dataset:
  train_files: // 此处填写dataset.json or "wikitext2"训练集路径
  train_samples: 1024 // 训练集样本数 缺省默认全量数据集
  ptq_samples: 1024 // PTQ优化样本数 缺省默认全量数据集

extra_training_config: // 训练dtype
  fp16: True

cutoff_len: 128 // 样本序列长度
num_samples: 256 // 激活量化校准样本数
quant_param_2: False // kirinx90默认false，kirin9020平台默认为true
embedding_separate: True // True表示单独保存为bin文件，False表示导出embedding的量化参数到量化文件
lm_head_size: // 指定lmhead长度
```

## **run.sh**

请根据实际环境修改脚本中的4个关键点。

```shell
# !/bin/bash
# script description: run_develop script
# Copyright Huawei Technologies Co,Ltd.2010-2025.All rights reserved

# 修改点1 填写DDK_tools工具包中tools_dopt/dopt_pytorch_py3的真实路径
qlibs='path/to/dopt_pytorch_py3'
export WANDB_DISABLED=true
export HF_DATASETS_OFFLINE=0
export PYTHONPATH=${qlibs}:$PYTHONPATH

# 修改点2 设置为cuda或npu模式 二选一
# cuda模式，如果有多个设备，CUDA_VISIBLE_DEVICES可写0,1,2,3....
export DEVICE=cuda
export CUDA_VISIBLE_DEVICES=0
# npu模式
# export DEVICE=npu
# export ASCEND_RT_VISIBLE_DEVICES=0

# 修改点3 选择创建工程的路径，以testcase创建同名文件夹，存放生成的量化文件
ROOT=.
testcase='output_dir'
RUN_FILE=${qlibs}/dopt/dopt_lm/opt_main.py
output_dir=${ROOT}/${testcase}/train_output
mkdir -p ${output_dir}
cp ${ROOT}/config.yaml $output_dir

# 修改点4 huggingface源模型所在路径
model_path='path/to/model'
dopt_config=./${testcase}/dopt_config.json
quant_stage=$1
block_size=128 # PTQ量化重建误差的block大小。

python -u \
    ${RUN_FILE} --model-path $model_path \
    --dopt-config $dopt_config \
    --optimize-config ${ROOT}/config.yaml \
    --quant-stage $quant_stage \
    --block-size $block_size \
    --output-dir ${output_dir} 2>&1 | tee ${output_dir}/logs.log
```
