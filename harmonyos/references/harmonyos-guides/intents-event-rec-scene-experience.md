---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cadcef398e96f6706646151b841e620f7740f7318db69bb8b2883ac3a6b5351e
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/HSwlCdP0ShWVtpk9NkotnQ/zh-cn_image_0000002583479315.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=D839233A70371109C7F8E23019EE060AB129F9791AAB73717805A5D96537E6BA)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/iMDzNIQ3Tuy3b5l8WJvCzg/zh-cn_image_0000002552799666.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=102BCA892546436CB935BB65A730C0293142E496FE05B5CD064EA59D47B00471)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/AfpkmVBuRUOVN2gCuDpK6g/zh-cn_image_0000002583439361.png?HW-CC-KV=V1&HW-CC-Date=20260427T235331Z&HW-CC-Expire=86400&HW-CC-Sign=0E022D24792F87646D60F295A9C386A9290309A7ED0D07176E7B76E39167F253)
