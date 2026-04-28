---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-plug-in-quantification
title: 插件式量化
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > Transformer结构量化 > 插件式量化
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3609738c1043bff83879d5c71e1c472647fd3340b9584bb89d586eae69090d35
---

## 简介

插件式量化不区分模型类型，包含语言类视觉类，可以针对各种Transform结构的模型进行快速量化。

## 插件式整体流程

PTQ和QAT是两种量化参数优化策略，PTQ使用推理工程即可完成量化校准，QAT需要结合训练工程来进行量化感知训练。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/jnEBSzAaQ6yWVzTXyQST_g/zh-cn_image_0000002583439255.png?HW-CC-KV=V1&HW-CC-Date=20260427T235116Z&HW-CC-Expire=86400&HW-CC-Sign=01BFD062FDC75A41FC5249BE155E2B420AF57B83885134777BBE111832E31F84)

## 接口使用说明

```
1. import os
2. import sys
3. sys.path.append('path/to/dopt_torch_py3')
4. ####  接口导入
5. from dopt.dopt_lm.do_opt import (
6. generate_config_file,   ## 生成量化配置文件
7. optimize_model,         ## 使用生成和配置好的量化配置文件将浮点nn.module 转成插入量化算子的nn.module
8. set_quant_state,        ## 分别对激活和量化设置量化推理使能
9. set_calibrate_state,    ## 设置量化参数可更新状态
10. generate_quant_params,  ## 导出量化参数接口
11. )
12. #### 量化算子插入  首次调用该接口会生成量化配置文件，完成配置后进行PTQ或者QAT
13. def get_quant_model(model, dopt_config):
14. ## model: nn.module实例对象 浮点模型定义
15. ## dopt_config: "path/to/config.json"  生成路径
16. if not os.path.exists(dopt_config):
17. generate_config_file(model, dopt_config)
18. exit()
19. model = optimize_model(model, dopt_config)
20. return model
```

**量化策略配置：**

```
1. {
2. "layer_strategy": {
3. "node_name": {
4. "type": "<class 'torch.nn.modules.linear.Linear'>",
5. "quant_strategy": "need to set",
6. "weight": {
7. "bit": 4,
8. "group_size": 128,
9. "weight_algo": "group_min_max",
10. },
11. "input" : {
12. "bit" : 8,
13. "input_algo":  "min_max",
14. "unsigned_quant": True
15. }
16. }
17. }
18. }
```

**配置说明：**

quant\_strategy 不同策略有默认的配置，可参考下表1进行配置修改，需要逐层配置。

**表1** 配置参数说明

| 配置信息 | 配置信息 | 可选项 | 选项说明 |
| --- | --- | --- | --- |
| quant\_strategy | N/A | Quant\_aigc\_ptq  Quant\_aigc\_qat  Quant\_act\_weight\_eco  Quant\_lm\_head  Quant\_Embed\_MinMax | PTQ量化策略，默认U8S8。量化器为minmax  QAT量化策略，默认U8S8。量化器为omni\_minmax  16-4grouplinear 量化策略。默认groupsize128，针对llm大模型，QAT量化器  16-4grouplinear 量化策略。默认groupsize128，针对llm大模型，QAT量化器  8bit embedding量化 |
| weight | bit | 4, 8 | 权重量化位宽 |
| weight | group\_size | 128 , 256 | 权重bit为4时，属于低比特量化范畴， 使用grouplinear量化，可配置此信息，否则请别配置该键值对 |
| weight | weight\_algo | min\_max  group\_min\_max  omni\_min\_max  omni\_group\_min\_max | perchannel量化，最大最小值统计用于PTQ量化  pergroup量化，最大最小值统计，用于PTQ量化  QAT量化器， perchannel量化  QAT量化器， pergroup量化 |
| input | bit | 8, 16 | 激活量化位宽 |
| input | input\_algo | min\_max  ema  omni\_min\_max | pertensor量化，最大最小值统计用于PTQ量化，clip误差小  pertensor量化，滑动平均统计用于PTQ量化，round误差小  pertensor量化，QAT量化器 |
| input | unsigned\_quant | True  False | 非对称量化  对称量化 |

## 量化参数优化-PTQ

生成的quant\_config中每一层默认都是float策略。需要将其改为Quant\_aigc\_ptq即可，高阶配置请参考上表。

请使用推理工程并选择合适数量的数据对get\_quant\_model接口返回的模型进行前向推理 即可完成对模型的量化优化如下：

```
1. ## 首次调用会生成config文件，需要手动配置量化策略
2. model = get_quant_model(model, quant_config)
3. model.eval()
4. ## 打开量化器
5. set_quant_state(model, weight_state=True, input_state=True)
6. ## 打开量化参数可标定状态
7. set_calibrate_state(model, True)
8. ## 使用实际推理数据进行推理 即量化标定###
9. for data in datasets:
10. model(data)
11. set_calibrate_state(model, False)
12. torch.save(model.state_dict(), 'pth_save_path')
```

## 量化参数优化-QAT

生成的quant\_config中每一层默认都是float策略。需要将其改为Quant\_aigc\_qat，高阶配置请参考上表。

请使用训练工程对插有量化算子的模型进行训练。

```
1. model = get_quant_model(model, quant_config)
2. model.train()
3. set_quant_state(model, weight_state=True, input_state=True)
4. set_calibrate_state(model, True)
5. """
6. do training
7. """
8. set_calibrate_state(model, False)
9. torch.save(model.state_dict(), 'pth_save_path')
```

## 量化参数提取导出

```
1. from dopt.dopt_lm.do_opt import generate_quant_params, optimize_model
2. ## model： 浮点 nn.module 实例对象， quant_config：量化配置文件
3. model = optimize_model(model, quant_config)
4. ## 加载量化标定后保存的pth
5. model.load_state_dict(
6. torch.load('pth_save_path', map_location=torch.device('cpu')),
7. strict=True,
8. )
9. ## 关闭量化参数更新，导出量化参数
10. ## Tips：也可以在标定完成后直接到这一步，进行参数导出，步骤分离的目的是为了防止过程中有错误，导致前面步骤重来。
11. set_quant_state(model, weight_state=True, input_state=True)
12. set_calibrate_state(model, False)
13. generate_quant_params(
14. model,
15. output_dir,
16. quant_param_2=False,
17. embedding_separate=True,
18. )
19. ## output_dir 下会生成 fake_quant_weight.pth 以及量化参数文件， fake_quant_weight.pth 仅用作导出onnx图时替换权重
```

**ONNX 导出：**

使用torch.onnx.export 对浮点model进行导出（需要加载fake\_quant\_weight.pth），必要时完成ONNX模型简化，以及确保conv和linear算子名和torch定义名同步。
