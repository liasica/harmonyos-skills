---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-search-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9dd12ab483af50328cce592d185b2fb131cbf8317398e6138247009b43fdc687
---

## 典型场景

**功能搜索：** 开发者将应用内的功能接入Intents Kit后，在小艺搜索入口，搜索对应功能名或者应用名，可以将应用内功能直接搜出，比如视频应用接入“会员中心”功能后，用户可通过搜索应用名或功能名搜出具体功能，点击后直接拉起应用中的功能页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/251b16vsSneG64E-hfanng/zh-cn_image_0000002552799688.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=980578908F621F18E2E3B08C30D07F95D3FDF08B89102C3E1DBEB870509B8BF9)

**内容搜索：** 以音乐为例，当用户在使用应用时，应用可以将音乐数据通过端侧API共享到意图框架，这里的音乐数据可以是用户收听过的歌曲，或是应用预测用户感兴趣的歌曲，那么后续用户在小艺搜索入口中搜索歌名时，系统将会在应用共享数据中检索对应内容，并使用模板卡片展示内容结果。当用户点击对应卡片热区时，可以跳转进具体音乐播放页或者后台执行播放。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/kg8FKwBrSRqIfOEwShf3Sg/zh-cn_image_0000002583439383.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=3F26C236964AEDA88D39E924DFFDA53F829450865218CAD35E7038BC0E2F615E)

## 卡片展示效果

意图框架提供各垂域在小艺搜索展示使用的标准模板卡片，开发者无需开发展示卡片。

模板卡片包含应用/元服务和内容必要信息，比如歌曲名称、歌曲封面图、歌曲描述，这类参数需要开发者共享到系统。各垂域适用的风格卡片不同，以实际特性场景要求为准。以下为歌曲本地搜索的模板卡样式的示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/dCh-YzVFQwOzeHue-ZJoAg/zh-cn_image_0000002552959338.png?HW-CC-KV=V1&HW-CC-Date=20260427T235340Z&HW-CC-Expire=86400&HW-CC-Sign=78270626489CDFC2D8F27C173F7C4539438B4CD9760EED37F5A3A0F77C3FE231)
