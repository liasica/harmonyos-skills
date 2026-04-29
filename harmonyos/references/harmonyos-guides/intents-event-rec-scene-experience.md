---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e74e33092c3ed3788c5cc6cbcf7e39950a7eb0784bcb30b0faa35a0bae3d617a
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/9jgvuDa6TFCfCsJdg5cGRg/zh-cn_image_0000002558765816.png?HW-CC-KV=V1&HW-CC-Date=20260429T054330Z&HW-CC-Expire=86400&HW-CC-Sign=C801AB3DCD9EE29A3E615A8209B06F43C21A2A9230133E35FE9CC963BCE4139B)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/quPGfs_kTgqjnu_yuqLI5w/zh-cn_image_0000002558606160.png?HW-CC-KV=V1&HW-CC-Date=20260429T054330Z&HW-CC-Expire=86400&HW-CC-Sign=A414BAC6FA229A88A1CDF6E560C38B42461D48B05FCBA460020C69FB06A3AC0F)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/dlM_CzaiRVyIs8WRIqif_w/zh-cn_image_0000002589325687.png?HW-CC-KV=V1&HW-CC-Date=20260429T054330Z&HW-CC-Expire=86400&HW-CC-Sign=A6515724EF1A9E2E4105864F2A53F420A24E2BF1A4EDDFCB732B055615ABDBE3)
