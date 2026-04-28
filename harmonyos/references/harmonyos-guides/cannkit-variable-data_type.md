---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-variable-data_type
title: 可变data_type
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型转换 > 可变data_type
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d56633c135a5e95220375bb473e727e79b1fa7a230bdac440888d8ded612d34c
---

## 概述

可变data\_type是OMG工具支持的一个功能，用于模型输入输出数据类型多样性的场景，无需修改训练好的模型，在使用OMG工具进行[模型转换](cannkit-overall-parameter.md)时，通过指定输入、输出数据类型使得同一个模型适用于不同输入输出的场景。

## 使用说明

在进行模型转换时，输入输出数据类型指定分别需要通过[OMG参数](cannkit-overall-parameter.md)的input\_type、output\_type来实现。

使用示例：

```
1. ./omg --model=./model.pb --framework=3 --output=./model --input_shape="inputs:1,512,512,1" --out_nodes="outputs:0" --input_type="inputs:FP16" --output_type="outputs:UINT8"
```
