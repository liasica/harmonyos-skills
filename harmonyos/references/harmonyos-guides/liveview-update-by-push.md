---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/liveview-update-by-push
title: 通过Push Kit更新实况窗
breadcrumb: 指南 > 应用服务 > Live View Kit（实况窗服务） > 开发实况窗场景 > 通过Push Kit更新实况窗
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:11+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:74a25e959000bceae8ff0b09ff23338a17e99ccf58a0ab8d14a9b5f0ae3f5694
---

## 场景介绍

本地实况窗的更新依赖于应用进程的存活，为了让实况窗在生命周期内正常完成更新和结束，我们更推荐开发者使用Push Kit实时更新实况窗状态。

通过Push Kit更新实况窗的流程如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/HYK8sh3rT2e8xpoHMIysfQ/zh-cn_image_0000002742124153.png)

1. 使用Push Kit，获取Push Token。
2. 使用Live View Kit创建实况窗成功后，开发者需要将实况窗id、pushToken、实况窗场景event以及业务服务的相关的状态属性保存到业务服务端。
3. 当业务服务的用户订单状态发生变化时，通过Push Kit通道推送更新消息，更新/结束实况窗。

详细开发流程请参见Push Kit[推送实况窗消息](push-update-liveview.md)。

具体的Live View Kit ArkTS API和Push Kit REST API的字段关联关系请参见[Live View Kit ArkTS API与Push Kit REST API的字段关联关系表](../harmonyos-references/liveview-api-map.md)。

## 支持网络图片下载

从26.0.0开始，实况窗支持通过Push Kit下载网络图片，存在以下限制条件：

1. 支持下载的网络图片大小不大于512KB。
2. 支持下载的网络图片文件格式包括jpg、jpeg、png、bmp、webp。
3. 仅支持HTTPS协议的网络图片下载，即只支持以"https://"开头的图片网址。
4. 仅如下1到7位置支持网络图片下载，具体请参考[请求体参数说明](../harmonyos-references/push-scenariozed-api-request-param.md)。

| 模板类型 | 示意图 |
| --- | --- |
| 基础模板 |  |
| 进度可视化模板 |  |
| 强调文本模板 |  |
| 左右文本模板 |  |
| 赛事比分模板 |  |
| 胶囊模板 |  |
