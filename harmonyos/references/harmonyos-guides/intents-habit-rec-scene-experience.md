---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b91734f36137e356e978d90d5a2cf8ec50230f96fe7218d46c740135d9bdeed7
---

## 典型场景

当前习惯推荐可在小艺建议入口分发，在不同垂域中，填充功能详细参数或内容的逻辑不同，主要典型场景可分为常用接续、常用复访、常用推新三类。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/oIQbcqBgT_Sjqwxm3pXDMQ/zh-cn_image_0000002786520656.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=AF1F6523116DBB5E2991D46134861B13A5AC3FB2957CF37DB5ADEA957D37A7A3)

以常看视频续播为例，系统预测当前用户使用华为视频的播放视频功能概率较高，会选择用户最近观看且还没看完的视频内容来补充功能细节，在小艺建议中以模板卡形式推荐展示，用户点击卡片后，实现一步跳转进应用的视频播放页。

## 卡片展示效果

意图框架提供各垂域习惯推荐在小艺建议中展示使用的标准模板卡片，开发者无需开发展示卡片。在展示模板上，会展示应用/元服务名称与logo和内容必要信息，比如音乐名、音乐图片，这类参数需要开发者共享到系统。

以下为播放歌曲-习惯推荐的卡片示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/M0lPtzeaTZiOCaJ_qhUzsA/zh-cn_image_0000002786360728.png?HW-CC-KV=V1&HW-CC-Date=20261112T233233Z&HW-CC-Expire=31536000000&HW-CC-Sign=23ED68BBD2BC6762084EAADBC55D98456C20C2D20F6C84D8CB6D128D91BCDDB5)
