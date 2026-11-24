---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-cloudobjprocess
title: 开发流程
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 开发流程
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:21+08:00
doc_updated_at: 2026-10-28
content_hash: sha256:4d2139328c67907d04848aa5ecd74ff0d8411b53a4d3d4cd7f1fe910085cdf85
---

除去传统的云函数，您还可在端云一体化云侧工程下开发云对象。云对象是一种特殊的云函数，本质是对云函数的一种封装，客户端可通过导入一个云对象来直接使用这个对象的方法，为您提供在端侧直接调用云侧代码的开发体验。相比普通云函数方式，云对象代码更精简、逻辑更清晰，大多数场景下推荐使用云对象代替传统云函数。开发流程大致如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/reOm-Bu_SZ6sUjLY6VGKNQ/zh-cn_image_0000002314475725.png?HW-CC-KV=V1&HW-CC-Date=20261124T044221Z&HW-CC-Expire=31536000000&HW-CC-Sign=2F3D5176421DA35E363260F299ECED204E59E282400C47F5C82EC8E1ED05EC00 "点击放大")

1. [创建云对象](agc-harmonyos-clouddev-createcloudobj.md)：您可直接在DevEco Studio创建云对象。
2. [开发云对象](agc-harmonyos-clouddev-cloudobj-coding.md)：云对象创建完成后，您便可以开始编写云对象业务代码了。
3. [调试云对象](agc-harmonyos-clouddev-debugcloudobj.md)：您可以对云对象进行调试，以测试云对象代码运行是否正确。
4. [部署云对象](agc-harmonyos-clouddev-deploycloudobj.md)：完成云对象代码开发与调试后，您可将云对象部署到HarmonyOS 开发者中心，支持单个部署和批量部署。

**说明** 

一般建议先将云对象调试无误后再部署至云端，但某些业务场景下需要先部署云对象才能进行调试。请根据实际业务需要操作。
