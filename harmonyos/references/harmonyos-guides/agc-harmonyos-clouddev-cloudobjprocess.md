---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-cloudobjprocess
title: 开发流程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云对象 > 开发流程
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:07+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:4c0566ebb39a4929a26930ab325b046310c1b53d501a4b99d7627767a13fe518
---

除去传统的云函数，您还可在端云一体化云侧工程下开发云对象。云对象是一种特殊的云函数，本质是对云函数的一种封装，客户端可通过导入一个云对象来直接使用这个对象的方法，为您提供在端侧直接调用云侧代码的开发体验。相比普通云函数方式，云对象代码更精简、逻辑更清晰，大多数场景下推荐使用云对象代替传统云函数。开发流程大致如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/XRLr49_KTZi9TLuZuB3F7g/zh-cn_image_0000002314475725.png "点击放大")

1. [创建云对象](agc-harmonyos-clouddev-createcloudobj.md)：您可直接在DevEco Studio创建云对象。
2. [开发云对象](agc-harmonyos-clouddev-cloudobj-coding.md)：云对象创建完成后，您便可以开始编写云对象业务代码了。
3. [调试云对象](agc-harmonyos-clouddev-debugcloudobj.md)：您可以对云对象进行调试，以测试云对象代码运行是否正确。
4. [部署云对象](agc-harmonyos-clouddev-deploycloudobj.md)：完成云对象代码开发与调试后，您可将云对象部署到AGC云端，支持单个部署和批量部署。

**说明** 

一般建议先将云对象调试无误后再部署至云端，但某些业务场景下需要先部署云对象才能进行调试。请根据实际业务需要操作。
