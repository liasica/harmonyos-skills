---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-terminology
title: Share Kit术语
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit术语
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:204b97373f929b35fcf58f66ab3e69a9e5d46090bae8bd8d058df62f1e495cfd
---

## Content area内容预览区

负责显示分享内容标题、预览、是否选中等信息，供用户选择。

## Host app宿主应用

分享行为的发起者。通过调用分享接口，配置分享的内容、预览样式等信息后展示分享面板。

## Operation area操作区

内容相关的操作，由系统提供的复制、保存、另存为、打印等能力。

## Recommendation area推荐区

对接华为分享和[意图框架](intents-introduction.md)，通过算法高效、精准推荐能够处理内容的设备和目标应用用户。

## Sharing mode area分享方式区

通过HarmonyOS的包管理服务获取支持分享内容的目标应用。支持2种跳转方式：

1、跳转目标应用内UIAbility组件。

2、跳转目标应用提供的ExtensionAbility组件。

应用组件需通过在[module.json5配置文件](module-configuration-file.md)中配置UIAbility组件和ExtensionAbility组件的描述信息，以声明支持分享的能力。

## Sharing details page分享详情页

点击分享方式可跳转"分享详情页"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/EuHynymySjeFQNaJ4YUR8w/zh-cn_image_0000002552799528.png?HW-CC-KV=V1&HW-CC-Date=20260427T235055Z&HW-CC-Expire=86400&HW-CC-Sign=7E86EAF1FDB365AD720B4C610E5D1ACA7D77CF06BC214D531853FF4EE0856BC5)

## Source device源端设备

分享内容的发起端设备。发起端设备通过华为分享服务，将分享数据发送到对端设备。

## Target app目标应用

分享内容的接收者。需要在应用中构建数据处理能力并按照目标应用接入指南进行能力声明，使得包管理服务可以识别应用支持的能力。

## Target device目标设备

分享内容的接收设备。接收端将根据分享数据类型，选择合适的应用存储或打开分享内容。
