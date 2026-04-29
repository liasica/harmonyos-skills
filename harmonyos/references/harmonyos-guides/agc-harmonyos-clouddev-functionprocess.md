---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-functionprocess
title: 开发流程
breadcrumb: 指南 > 开发环境搭建 > 工程创建 > 模块管理 > 端云一体化开发 > 开发端云工程 > 开发云侧工程 > 开发云函数 > 开发流程
category: harmonyos-guides
scraped_at: 2026-04-29T13:44:59+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:939d94f3ef7dbce1a455794873304ede5cc74f9442b5ae5403851ad95ea3440f
---

云函数是一项Serverless计算服务，可以根据函数的实际流量对函数进行弹性收缩。您只需聚焦业务逻辑，开发与上传业务模块相关的函数，云函数即可为您自动完成资源分配、代码部署、负载均衡等工作，既提高了开发和上线函数的速度，也保证了函数的高可用性。

云函数当前分为传统云函数和云对象两种类型，本章节仅介绍传统云函数，了解云对象详情请参考[开发云对象](agc-harmonyos-clouddev-cloudobj.md)。

使用DevEco Studio在端云一体化云侧工程下开发云函数，总体流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/sqXRV3tnQTuBMzmVqr5pEQ/zh-cn_image_0000002279816360.png?HW-CC-KV=V1&HW-CC-Date=20260429T054457Z&HW-CC-Expire=86400&HW-CC-Sign=18277C8A9D95DB32208F79269F453F47B0D697D0C51E7371986C471B5176AC6A "点击放大")

1. [创建并配置函数](agc-harmonyos-clouddev-createfunc.md)：您可直接在DevEco Studio创建函数、为函数配置入口以及调用的触发器等。
2. [开发函数](agc-harmonyos-clouddev-funccoding.md)：函数创建并配置完成后，您便可以开始编写函数业务代码了。
3. [调试函数](agc-harmonyos-clouddev-debugfunc.md)：您可以对函数进行调试，以测试函数代码运行是否正常。
4. [部署函数](agc-harmonyos-clouddev-deployfunc.md)：完成函数代码开发与调试后，您可将函数部署到AGC云端，支持单个部署和批量部署。

说明

一般建议先将函数调试无误后再部署至云端，但某些业务场景下需要先部署函数才能进行调试。请根据实际业务需要操作。
