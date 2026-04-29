---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-whole-deployment-process
title: 部署全流程
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 端侧部署 > 部署全流程
category: harmonyos-guides
scraped_at: 2026-04-29T13:40:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2e4c6247e77b200bf86c5069a70f2d54dbb8cbe680ee73f01b347809650936b0
---

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/ZhzQtHlPQiShLxi7tZcC7Q/zh-cn_image_0000002558606064.png?HW-CC-KV=V1&HW-CC-Date=20260429T054057Z&HW-CC-Expire=86400&HW-CC-Sign=53BBF033EDA3D24042D737F3F17B8424330C1811B3AB578B4E5A52A2F9445CC5)

## 离线模型转换

离线模型转换需要将Caffe、TensorFlow、ONNX、MindSpore模型转换为CANN Kit平台支持的模型格式，并可以按需进行AIPP操作、量化操作，使用场景及方法如下：

* AIPP操作

  AIPP用于在硬件上完成图像预处理，包括改变图像尺寸、色域转换（转换图像格式）、减均值/乘系数（改变图像像素），运用后可避免重新训练匹配推理计算平台需要的数据格式，只通过AIPP参数配置或者在软件层面上调用AIPP接口即可完成适配，同时由于硬件专用，可以获得较好的推理性能收益，具体操作可参见[AIPP模型转换](cannkit-model-conversion-example.md#aipp模型转换以caffe模型为例)。
* 量化操作

  量化是一种可以把FP32模型转化为低bit模型的操作，以节约网络存储空间、降低传输时延以及提高运算执行效率，量化操作可参见[量化模型转换](cannkit-model-conversion-example.md#量化模型转换以caffe模型为例)。

## App集成

App集成流程包含创建项目、配置项目里的NAPI、集成模型，集成模型又包含加载模型、编译模型、模型输入数据预处理、运行模型、模型输出数据后处理流程。
