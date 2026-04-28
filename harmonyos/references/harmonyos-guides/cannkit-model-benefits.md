---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-model-benefits
title: 模型收益
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > 模型优化 > 模型轻量化 > 模型收益
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7a6dfd58ba30b918e6caa901a461934f57f1990edc2ca295a1598e0f17257e0b
---

## Quant\_INT8-8量化收益

以resnet-18为例，使用轻量化工具后（Quant\_INT8-8量化）的收益如下。

| 框架 | 数据集 | 模型 | 原始精度 | 重训练后精度 | 非量化OM离线  模型体积(MB) | Quant\_INT8-8量化OM  离线模型体积(MB) |
| --- | --- | --- | --- | --- | --- | --- |
| TensorFlow | ImageNet | resnet-18(v2) | 70.0% | 70.0% | 22.457 | 11.9 |

## 网络结构搜索工具分类场景收益对比

以resnet-18为例，使用轻量化工具后（网络结构搜索）的收益如下。

| 框架 | 数据集 | 模型 | 参数量（M） | 精度 |
| --- | --- | --- | --- | --- |
| TensorFlow | ImageNet | ResNet-18 | 11.69 | 70.32% |
| TensorFlow | ImageNet | NASEA | 10.93 | 72.13%[1] |
| PyTorch | ImageNet | ResNet-18 | 11.69 | 69.6% |
| PyTorch | ImageNet | NASEA | 11.4 | 72.88% |

### 检测场景收益对比

| 框架 | 数据集 | 模型 | 计算量（G） | mAP@[.5, .95][2] |
| --- | --- | --- | --- | --- |
| SSD(backbone：ResNet-18) | COCO | ResNet-18 | 11.6 | 17.8[3] |
| SSD(backbone：ResNet-18) | COCO | NASEA | 9.25 | 18.4[3] |

### 分割场景收益对比

| 框架 | 数据集 | 模型 | 计算量（G） | mIOU[4] |
| --- | --- | --- | --- | --- |
| TensorFlow | VOC | ResNet-18 + Deeplab v3 | 40.9 | 54.1[5] |
| TensorFlow | VOC | NASEA | 28.3 | 56.1[5] |
| PyTorch | VOC | ResNet-18 + Deeplab v3 | 43.7 | 64.2 |
| PyTorch | VOC | NASEA | 30.7 | 65.1 |

说明

[1] 此精度是使用tensorpack重训练模型得出。

[2] 此指标的计算方法为：IoU(Intersection over Union)从0.5~0.95区间上，以0.05为间隔计算AP的值，再计算所有AP的均值。

[3] 此精度是在COCO val2017数据集上测试得出。

[4] 此指标为平均交并比，计算方法为先求每个类别的交并比，再平均。

[5] 此精度是在VOC val2012数据集上测试得出。
