---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/corevisionkit-personal-data
title: 个人数据处理说明
breadcrumb: 指南 > AI > Core Vision Kit（基础视觉服务） > 个人数据处理说明
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2c561b0c3b48e3430185080b3924cd3342bee9e737e49f161a69d3d31ce45063
---

此文档针对华为作为最终用户数据处理者，客户作为最终用户数据控制者的数据处理进行说明，包括：

* 华为处理的个人数据清单；
* 指导开发者如何帮助最终用户实现对数据的控制。

## 华为处理的个人数据清单

最后修改时间：2025/6/13

| 个人数据清单 | 使用目的 | 存留期 |
| --- | --- | --- |
| 图片 | Core Vision Kit各子能力API：基础视觉服务基本功能为识别图片中相关内容，需要开发者提供需要分析的图片。具体为，  通用文字识别API：开发者提供图片，Core Vision Kit帮助开发者提取图片上的文本信息。  人脸检测API：开发者提供图片，Core Vision Kit帮助开发者提取图片上的人脸信息，如人脸矩形框坐标、人脸五官位置、人脸朝向、人脸置信度等。  人脸比对API：开发者提供图片，Core Vision Kit帮助开发者比对两张图片中的人脸是否是一个人。  主体分割API：开发者提供图片，Core Vision Kit帮助开发者检测&分离图片中区别于背景的前景物体或区域。  多目标识别API：开发者提供图片，Core Vision Kit帮助开发者检测图片中特定目标，如动物、植物、建筑物等。  骨骼点检测API：开发者提供图片，Core Vision Kit帮助开发者检测图片中人体关键点信息，通过关键点描述人体骨骼信息。 | 不留存 |

## 指导开发者如何帮助最终用户实现对数据的控制

云端不存储用户数据，由数据控制者面向最终用户提供相应的数据主体权利及其相关解释。

在您接入、使用Core Vision Kit服务前，**我们要求您在隐私政策中向用户告知我们是如何处理其个人数据的，并获取用户同意或取得其他合法性基础**。
