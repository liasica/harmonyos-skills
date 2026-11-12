---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-llm-two-stage-quantification
title: 两段式量化步骤
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > LLM大模型对接 > CANN LLM模型量化 > 量化使用步骤 > 两段式量化步骤
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:86d14584e583026b8fad7c0ac20a4664abb4baa001c5b29f9cad23359a833f90
---

量化工具采用标准的两段式执行流程：权重量化、激活量化。对于激活张量支持静态s16量化以及动态s8量化，动态量化在权重量化完成后即可完成，推荐使用动态量化；静态量化需完成两段式全流程。所有阶段均需在GPU（CUDA）或NPU环境下运行，支持单机单卡。

运行前请先按[环境准备](cannkit-llm-usage-environmental-preparation.md)完成量化工程搭建（config.yaml与run.sh配置）。

## **阶段一：权重量化（stage1）**

1. 执行命令sh run.sh stage1，生成dopt\_config.json配置文件。

   * 首次执行命令，会出现generate plugin quang config please set quant strategy firstly代表执行成功。此时工程会遍历模型的所有linear算子，在量化工程内会生成dopt\_config.json文件。
2. 根据模型层类型，修改dopt\_config.json文件内的quant\_strategy值，配置量化策略。

   * decoder层策略：Quant\_INT8-4\_ECO
   * lm\_head层策略：Quant\_INT8-4\_ECO
   * embedding层策略：Quant\_Embed\_MinMax

   **推荐配置样例：（dopt\_config.json）** 。

   ```json
   {
       "layer_strategy":{
           "model.embed_tokens": {
               "type": "<class 'torch.nn.modules.sparse.Embedding'>",
               "quant_strategy": "Quant_Embed_MinMax",
           },
           "model.layers.0.self_attn.q_proj": {
               "type": "<class 'torch.nn.modules.linear.Linear'>",
               "quant_strategy": "Quant_INT8-4_ECO",
           },
           "lm_head": {
               "type": "<class 'torch.nn.modules.linear.Linear'>",
               "quant_strategy": "Quant_INT8-4_ECO",
           }
       }
   }
   ```
3. 再次执行sh run.sh stage1，即可进行权重量化。

* 出现“weight quant done!!!”日志，在量化工程内生成trained\_quant\_weight.pth文件。动态量化得到此输出即可。
* 如需将激活修改为静态量化、调整权重量化位宽（bit）与分组大小（group\_size）等高阶配置，请在dopt\_config.json中逐层补充对应字段，配置说明参见[dopt\_config.json量化配置文件说明](cannkit-large-language-one-stop.md#dopt_configjson量化配置文件说明)，静态量化建议激活bit为16。

## **阶段二：激活量化（stage2）**

仅静态量化时需要本阶段，动态量化无需执行。

执行命令：sh run.sh stage2，如果日志输出“quant done!!!”，则说明成功生成量化文件trained.pth。

* 动态量化权重取trained\_quant\_weight.pth，静态量化权重取trained.pth，两者均可用于量化仿真推理，量化仿真方法参见[LLM模型一站式量化](cannkit-large-language-one-stop.md)。

## **量化参数提取与ONNX模型导出**

量化完成后，可通过量化模型导出流程完成量化参数提取与ONNX模型（量化IR）导出，供OMC/OMG离线模型编译使用，具体操作参见[量化模型导出](cannkit-quant-model-export.md)。
