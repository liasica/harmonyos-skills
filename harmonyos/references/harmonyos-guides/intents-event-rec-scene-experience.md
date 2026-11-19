---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d3eb6685e8d2edc98000bb0f6ea9bc2798e68a087af08abc6411536a179dea5d
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lbeg5eLIQ3mNLeSI2vaG3Q/zh-cn_image_0000002791566794.png?HW-CC-KV=V1&HW-CC-Date=20261119T014920Z&HW-CC-Expire=31536000000&HW-CC-Sign=89F1051024222D478D7029429ED5CBFD46D72B2C3B1F5F63254B4E8BD37178DB)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/OmB9oF3hSP-Yck3HPaSTog/zh-cn_image_0000002820526747.png?HW-CC-KV=V1&HW-CC-Date=20261119T014920Z&HW-CC-Expire=31536000000&HW-CC-Sign=38129431FEDC8714EC1BE9DA749C0CA9588DB11B9E4FEF681EBD50290D711687)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/PEM-bcCBSsqq30tcaPIn8g/zh-cn_image_0000002820406747.png?HW-CC-KV=V1&HW-CC-Date=20261119T014920Z&HW-CC-Expire=31536000000&HW-CC-Sign=489A44F446C391B73E8F2C7115E687DDB6B05E46986B0521D5E89F6AD4643C45)
