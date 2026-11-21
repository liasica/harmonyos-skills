---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a5cbfb451fb01cc781a402f515b48c106fa8baa66641aaa02c37ddc13e08d410
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/9obz0cRuQ3CGXjN5-90CqQ/zh-cn_image_0000002792878448.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=E333EC9E886C220EB2F5DBD30E0E8B41275E2C70771B4099D5B456228ECAC6A9)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/uKunBENCQVio6KMl_cTpNw/zh-cn_image_0000002821838355.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=D3A9CBC4C89D18FCB507EDCBC9197078BB0A0D27B92A295A880BB2BEFB73B395)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/IbfTT9kVS_eTnQebccIVsg/zh-cn_image_0000002821758357.png?HW-CC-KV=V1&HW-CC-Date=20261121T011119Z&HW-CC-Expire=31536000000&HW-CC-Sign=6574E76DD0DE8032E4AF2C68CDCC817825DCC48B911AFAD012BBEA062082B3E7)
