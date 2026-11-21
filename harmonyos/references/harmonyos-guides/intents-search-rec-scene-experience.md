---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-search-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf51b92b5c17e7d3922d8b5cf3224ffb6adaffd81f73f1dd29d5e349ce06a54c
---

## 典型场景

**功能搜索：** 开发者将应用内的功能接入Intents Kit后，在小艺搜索入口，搜索对应功能名或者应用名，可以将应用内功能直接搜出，比如视频应用接入“会员中心”功能后，用户可通过搜索应用名或功能名搜出具体功能，点击后直接拉起应用中的功能页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/bleLAwn7Qaujx72CWY7FOg/zh-cn_image_0000002793038442.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=287307624DB2C8C0C16D174D29CD2B4A541A541B8FB4FB76731304FB43AF852F)

**内容搜索：** 以音乐为例，当用户在使用应用时，应用可以将音乐数据通过端侧API共享到意图框架，这里的音乐数据可以是用户收听过的歌曲，或是应用预测用户感兴趣的歌曲，那么后续用户在小艺搜索入口中搜索歌名时，系统将会在应用共享数据中检索对应内容，并使用模板卡片展示内容结果。当用户点击对应卡片热区时，可以跳转进具体音乐播放页或者后台执行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/uHTn7Zc8RrKzdIv8CeLRmg/zh-cn_image_0000002792878472.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=400D5A80B2D1AB32CDD4E5F749D965F317897FE9DC2695E949430E90FA1BABF0)

## 卡片展示效果

意图框架提供各垂域在小艺搜索展示使用的标准模板卡片，开发者无需开发展示卡片。

模板卡片包含应用/元服务和内容必要信息，比如歌曲名称、歌曲封面图、歌曲描述，这类参数需要开发者共享到系统。各垂域适用的风格卡片不同，以实际特性场景要求为准。以下为歌曲本地搜索的模板卡样式的示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/RUY5oM7HT_Oa-ReWEiWAWA/zh-cn_image_0000002821838379.png?HW-CC-KV=V1&HW-CC-Date=20261121T011247Z&HW-CC-Expire=31536000000&HW-CC-Sign=23E0DFD7671C74C369799E83C085EF59052247D439C3241FFE39751AA04AB976)
