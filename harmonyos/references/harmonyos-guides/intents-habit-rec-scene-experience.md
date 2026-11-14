---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c8ced4d9feb43dcb4cb163cbb76a293220474b76da2c6ee9a0ad2f8489ea691c
---

## 典型场景

当前习惯推荐可在小艺建议入口分发，在不同垂域中，填充功能详细参数或内容的逻辑不同，主要典型场景可分为常用接续、常用复访、常用推新三类。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/NOW45o3eSwSZsSUG50bS_A/zh-cn_image_0000002788468404.png?HW-CC-KV=V1&HW-CC-Date=20261114T004654Z&HW-CC-Expire=31536000000&HW-CC-Sign=DE0AC38A2EA143FC4FF01873438450961D2BDACDF9BC20C33CFEC5B86119101E)

以常看视频续播为例，系统预测当前用户使用华为视频的播放视频功能概率较高，会选择用户最近观看且还没看完的视频内容来补充功能细节，在小艺建议中以模板卡形式推荐展示，用户点击卡片后，实现一步跳转进应用的视频播放页。

## 卡片展示效果

意图框架提供各垂域习惯推荐在小艺建议中展示使用的标准模板卡片，开发者无需开发展示卡片。在展示模板上，会展示应用/元服务名称与logo和内容必要信息，比如音乐名、音乐图片，这类参数需要开发者共享到系统。

以下为播放歌曲-习惯推荐的卡片示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/KuWWkQf_TGST9rM-s5OKug/zh-cn_image_0000002817507893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004654Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CD234127466ECC1CA92E357E1752777C5064E70BB9A4F3A2787EB13A04447C7)
