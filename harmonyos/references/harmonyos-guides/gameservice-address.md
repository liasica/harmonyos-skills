---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-address
title: 配置回调地址
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 附录 > 配置回调地址
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4524bcd028c584c956bf1cb8abe5f13b2ad8877d4842d8414323758c23094a4a
---

若在关键事件发生时，华为游戏服务器向开发者服务器发送事件通知，请前往AppGallery Connect配置开发者服务器的回调地址。发送通知的接口原型等信息请参见[解绑账号通知](../harmonyos-references/gameservice-unbindplayer-notification.md)接口。涉及的关键事件及对应的处理逻辑如下：

| 关键事件 | 游戏自行实现的处理逻辑 |
| --- | --- |
| 玩家注销华为账号。 | 清理账号数据。 |

在AppGallery Connect配置服务器的回调地址步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)，在“开发与服务”下选择项目及项目下的游戏。
2. 左侧菜单选择“构建 > 游戏服务”，在“账号方案接入回调地址配置”配置开发者服务器地址，用于华为游戏服务器在发生关键事件时向该地址发送事件通知。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/bWEnKJF_Qwm_QMSTmDNiYw/zh-cn_image_0000002552799256.png?HW-CC-KV=V1&HW-CC-Date=20260427T234907Z&HW-CC-Expire=86400&HW-CC-Sign=543D7D4AF034DF6390C62D32BA15035BE78FEECB700B4F2B9AFF327189A9CF38)

   说明

   回调地址要求支持HTTPS协议，且具有合法商用证书。
