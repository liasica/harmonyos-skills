---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-plug-in-quantification
title: Transformer插件式量化
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > Transformer插件式量化
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:6cefa7a79e4e101212043a9daf40ac5e40ddffe81ed3aa2e913f9231a002c3b8
---

## 简介

插件式量化理论上不区分模型类型，但是推荐对视觉类transformers使用。LLM模型也可使用，但仅支持策略为Quant\_INT8-4\_ECO。

## 插件式整体流程

PTQ和QAT是两种量化参数优化策略，PTQ使用推理工程即可完成量化校准，QAT需要结合训练工程来进行量化感知训练。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/_nNj2njGSiKuUde4wmdAKw/zh-cn_image_0000002815400171.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/RKgeFJh6TaWVyOOPOmHPKg/zh-cn_image_0000002786520596.gif)

## 接口使用说明

```python
import os
import sys
sys.path.append('path/to/dopt_pytorch_py3')
####  接口导入
from dopt_lm.do_opt import (
    generate_config_file,   ## 生成量化配置文件
    optimize_model,         ## 使用生成和配置好的量化配置文件将浮点nn.module转成插入量化算子的nn.module
    set_quant_state,        ## 分别对激活和量化设置量化推理使能
    set_calibrate_state,    ## 设置量化参数可更新状态
    generate_quant_params,  ## 导出量化参数接口
)
#### 量化算子插入  首次调用该接口会生成量化配置文件，完成配置后进行PTQ或者QAT
def get_quant_model(model, dopt_config):
    ## model: nn.module实例对象 浮点模型定义
    ## dopt_config: "path/to/config.json"  生成路径
    if not os.path.exists(dopt_config):
        generate_config_file(model, dopt_config)
        exit()
    model = optimize_model(model, dopt_config)
    return model
```

**量化配置文件配置样例：**

**注意** 

group\_size仅在weight\_algo中含“group”时可配置，否则不要配置。group\_size需能被该层输入通道数整除，否则量化结构构建时报错。

```json
{
    "layer_strategy": {
        "node_name": {
            "type": "<class 'torch.nn.modules.linear.Linear'>",
            "quant_strategy": "need to set",
            "weight": {
                "bit": 4,
                "group_size": 128,
                "weight_algo": "group_min_max"
            },
            "input": {
                "bit": 8,
                "input_algo": "min_max",
                "unsigned_quant": true
            }
        }
    }
}
```

**配置说明：**

quant\_strategy 不同策略有默认的配置，可参考下表1进行配置修改，需要逐层配置。

**表1** 配置参数说明

| 配置信息 | 配置信息 | 可选项 | 选项说明 |
| --- | --- | --- | --- |
| quant\_strategy | N/A | Quant\_aigc\_ptq  Quant\_aigc\_qat  Quant\_INT8-4\_ECO | PTQ策略，U8S8。量化器为minmax  QAT策略，U8S8。量化器为omni\_minmax  QAT策略，动态8-4，量化器为grouplinear |
| weight | bit | 4, 8 | 权重量化位宽 |
| weight | group\_size | 128 , 256 | 权重bit为4时，属于低比特量化范畴， 使用grouplinear量化，可配置此信息，否则别配置。group\_size需能被该层输入通道数整除，若该层输入通道数小于group\_size，需选择可整除的更小取值 |
| weight | weight\_algo | min\_max  group\_min\_max  omni\_min\_max  omni\_group\_min\_max | PTQ量化器 perchannel量化  PTQ量化器 pergroup量化  QAT量化器 perchannel量化  QAT量化器 pergroup量化 |
| input | bit | 8, 16 | 激活量化位宽 |
| input | input\_algo | ema\_min\_max  omni\_min\_max  dyn\_s8 | pertensor PTQ量化  pertensor QAT量化器  动态激活量化 推荐策略 |
| input | unsigned\_quant | True  False | 非对称量化  对称量化 |

**说明** 

weight\_algo为group\_min\_max、omni\_group\_min\_max时，权重量化器仅支持Linear层；Conv2d等4D权重算子请将weight\_algo配置为min\_max或omni\_min\_max，或将该层quant\_strategy配置为float，否则量化结构构建或前向推理时会报错。

## 量化参数优化-PTQ

生成的quant\_config中每一层默认都是float策略。需要将其改为Quant\_aigc\_ptq即可，高阶配置请参考上表。

请使用推理工程并选择合适数量的数据对get\_quant\_model接口返回的模型进行前向推理，即可完成对模型的量化优化如下：

```python
## 首次调用会生成config文件，需要手动配置量化策略
model = get_quant_model(model, quant_config)
model.eval()
## 打开量化器
set_quant_state(model, weight_state=True, input_state=True)
## 打开量化参数可标定状态
set_calibrate_state(model, True)
## 使用实际推理数据进行推理，即量化标定
for data in datasets:
    model(data)
set_calibrate_state(model, False)
torch.save(model.state_dict(), 'pth_save_path')
```

## 量化参数优化-QAT

生成的quant\_config中每一层默认都是float策略。需要将其改为Quant\_aigc\_qat，高阶配置请参考上表。

请使用训练工程对插有量化算子的模型进行训练。

```python
model = get_quant_model(model, quant_config)
model.train()
set_quant_state(model, weight_state=True, input_state=True)
set_calibrate_state(model, True)
"""
do training
"""
set_calibrate_state(model, False)
torch.save(model.state_dict(), 'pth_save_path')
```

## 量化参数提取导出

量化标定或量化感知训练完成后，基于量化配置文件与保存的量化权重pth，完成量化参数提取与ONNX导出，具体操作参见[量化模型导出](cannkit-quant-model-export.md)。
