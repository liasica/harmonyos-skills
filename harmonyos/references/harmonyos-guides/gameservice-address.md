---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-address
title: 配置回调地址
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 附录 > 配置回调地址
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:58+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:c3e19825d3e293a503beecac9d55c76d95f8936105b1bf4647381876b06fd549
---

若在关键事件发生时，华为游戏服务器向开发者服务器发送事件通知，请前往AppGallery Connect配置开发者服务器的回调地址。发送通知的接口原型等信息请参见[解绑账号通知](../harmonyos-references/gameservice-unbindplayer-notification.md)接口。涉及的关键事件及对应的处理逻辑如下：

| 关键事件 | 游戏自行实现的处理逻辑 |
| --- | --- |
| 玩家注销华为账号。 | 清理账号数据。 |

在AppGallery Connect配置服务器的回调地址步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏。
2. 左侧菜单选择“构建 > 游戏服务”，在“账号方案接入回调地址配置”配置开发者服务器地址，回调地址要求支持HTTPS协议，且具有合法商用证书，用于华为游戏服务器在发生关键事件时向该地址发送事件通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/pT1IfDvLQE6y9M9RdeFRAQ/zh-cn_image_0000002820406317.png?HW-CC-KV=V1&HW-CC-Date=20261119T014858Z&HW-CC-Expire=31536000000&HW-CC-Sign=C30E4EB474BDC512C0C3D6417EEA519DFFCEFC9EEEDD362C9289CE0CA3ED870D)
