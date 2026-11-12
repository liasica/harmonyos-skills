---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4bfd68ae7f4169d949ce07321ee99d9432fb28847e84a167f968da69834a741b
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/9SN1hfatTCSFrTbWh9rH_A/zh-cn_image_0000002786520660.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7656312DD7354A3DD8FC52C05F23692CB0A1B714B9600867A3DF7595D086443F)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/bkuG-X4zS6Ob0WMUQwXcBQ/zh-cn_image_0000002786360732.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=67255C29037CC3204CF5B8BFBAFFDB88E31B1493460306094B2F109F4D311AAD)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/og5uxHvrSwSf7Xo8fCSrJA/zh-cn_image_0000002815560153.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=ADCAA0260304943639BAA557603A89D3ABC860678435A6CCB41E547272C3DECC)
