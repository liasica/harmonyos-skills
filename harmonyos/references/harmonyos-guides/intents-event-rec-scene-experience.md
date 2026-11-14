---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8fe1d1480d5207d5ab34f2cb132c954e25ac8af77e44ecd03dfc3f39a45a6c03
---

## 典型场景

**事件推荐典型场景包括：**

* 关注提醒事件（购物车降价、加追更新）
* 订单履行提醒事件（门票、机票、打车、外卖、挂号）
* 核销转化事件（会员、优惠券、话费余额）

各垂域也可根据垂域的实际情况定义具体的事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/xV0sLa1DS1ewNsV3fqlixg/zh-cn_image_0000002788468408.png?HW-CC-KV=V1&HW-CC-Date=20261114T004839Z&HW-CC-Expire=31536000000&HW-CC-Sign=EEC28317062492E98756A6CA1677A2D164C690BE203CA0D04B7CCD55807980E3)

以电影开场提醒为例，用户在应用/元服务中购买了电影票，在电影开场前半小时（具体生效时间将根据具体垂域的情况和用户最佳体验确定），用户可在小艺建议入口看到电影取票提醒的卡片，点击卡片可跳转到应用/元服务的订单详情页，用户可在该页面完成电影取票。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/r8B8LRjZTzOUhAsbIvAR_g/zh-cn_image_0000002817507897.png?HW-CC-KV=V1&HW-CC-Date=20261114T004839Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE9E95985C35D24AF77044522FEE3F566F5D7A4BDC60BEC0CAA094EE42004538)

## 卡片展示效果

意图框架将提供系统标准的事件模板卡片，无需开发者开发，开发者只需按照具体垂域事件的[意图Schema](../service/intents-schema-0000001901962713.md)将事件推送至智慧分发平台服务器即可。各垂域事件卡片样式的示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/3MAlSDQBSiC-yiM5D5WTaQ/zh-cn_image_0000002788308466.png?HW-CC-KV=V1&HW-CC-Date=20261114T004839Z&HW-CC-Expire=31536000000&HW-CC-Sign=072C7AC45CD990DB9FC360BAD9C402363286D2B9D59CE14F3C647929A241EA0E)
