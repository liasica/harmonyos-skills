---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-healthservice-4
title: 华为运动健康服务中的基础运动健康数据是否包含血糖数据
breadcrumb: FAQ > 应用服务开发 > 运动健康数据服务（Health Service Kit） > 华为运动健康服务中的基础运动健康数据是否包含血糖数据
category: harmonyos-faqs
scraped_at: 2026-11-21T09:19:21+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:b4a935294d81afc856c612285631f05baf87f1b91cddab20cdcd080fbb990f56
---

## 问题现象

应用接入运动健康服务后，在后台健康数据中未看到血糖数据的选项，官方基础运动健康数据介绍也未包含血糖数据，目前应用是否支持将血糖数据上传至华为健康？

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/WhMoTl8ERISkzCNVlW8Ckg/zh-cn_image_0000002628394738.png?HW-CC-KV=V1&HW-CC-Date=20261121T011921Z&HW-CC-Expire=31536000000&HW-CC-Sign=9324392954D20D90D85B676528252433F0FA2ED54A4C110A998C12D277085E3A "点击放大")

## 解决方案

Health Service Kit具体规格参考官网[数据开放总览](../doccenter-capabilities/health-permission-description.md)，目前支持获取血糖数据。建议通过云端接入方式（REST API），开发者使用REST API接入Health Service Kit数据平台，应用可以获取用户对数据的单独授权，读写运动健康数据，支持HarmonyOS应用获取血糖，具体参考[云端开放数据类型](../HMSCore-Guides/data_description-0000001467889369.md#section5411841962)。
