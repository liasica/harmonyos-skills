---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-terminology
title: Share Kit术语
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:02+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6a0aaa5018fad5b8868bd3978ff2db284c9c1322416a17781f17743f30935fae
---

## C

### Content area；内容预览区

负责显示分享内容标题、预览、是否选中等信息，供用户选择。

## H

### Host app；宿主应用

分享行为的发起者。通过调用分享接口，配置分享的内容、预览样式等信息后展示分享面板。

## O

### Operation area；操作区

内容相关的操作，由系统提供的复制、保存、另存为、打印等能力。

## R

### Recommendation area；推荐区

对接Share Kit和[Intents Kit](intents-introduction.md)，通过算法高效、精准推荐能够处理内容的设备和目标应用用户。

## S

### Sharing mode area；分享方式区

通过HarmonyOS的包管理服务获取支持分享内容的目标应用，用于展示可分享的目标应用列表。

### Sharing details page；分享详情页

点击分享方式可跳转"分享详情页"。"分享详情页"由应用提供，用来完成分享数据的接收。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/m8j3PzxhRouT_S5SNAqRqw/zh-cn_image_0000002736314327.png)

### Source device；源端设备

分享内容的发起端设备。发起端设备通过华为分享服务，将分享数据发送到对端设备。

## T

### Target app；目标应用

分享内容的接收者。需要在应用中构建数据处理能力并按照目标应用接入指南进行能力声明，使得包管理服务可以识别应用支持的能力。

### Target device；目标设备

分享内容的接收设备。接收端将根据分享数据类型，选择合适的应用存储或打开分享内容。
