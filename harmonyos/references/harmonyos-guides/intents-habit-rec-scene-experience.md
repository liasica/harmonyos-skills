---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-habit-rec-scene-experience
title: 场景体验
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 习惯推荐方案 > 场景体验
category: harmonyos-guides
scraped_at: 2026-11-19T09:49:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34d43005185b78db256e7fbd086c9b4e04a87e402e19b4965f46d7b90e476b93
---

## 典型场景

当前习惯推荐可在小艺建议入口分发，在不同垂域中，填充功能详细参数或内容的逻辑不同，主要典型场景可分为常用接续、常用复访、常用推新三类。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_cYBcUX9ShKxe1FOKQ-OfA/zh-cn_image_0000002791566790.png?HW-CC-KV=V1&HW-CC-Date=20261119T014920Z&HW-CC-Expire=31536000000&HW-CC-Sign=0DCAB1BB5AF0307180E4120FB59CFD2BBAE22F07EA9731FA471094397B442E15)

以常看视频续播为例，系统预测当前用户使用华为视频的播放视频功能概率较高，会选择用户最近观看且还没看完的视频内容来补充功能细节，在小艺建议中以模板卡形式推荐展示，用户点击卡片后，实现一步跳转进应用的视频播放页。

## 卡片展示效果

意图框架提供各垂域习惯推荐在小艺建议中展示使用的标准模板卡片，开发者无需开发展示卡片。在展示模板上，会展示应用/元服务名称与logo和内容必要信息，比如音乐名、音乐图片，这类参数需要开发者共享到系统。

以下为播放歌曲-习惯推荐的卡片示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/2crQZh8VQ8KFbXY7ammGCg/zh-cn_image_0000002820526743.png?HW-CC-KV=V1&HW-CC-Date=20261119T014920Z&HW-CC-Expire=31536000000&HW-CC-Sign=62F2B63436659DED68545BE39C7363B6E63696B73AE6608C7B78755D6BF34646)
