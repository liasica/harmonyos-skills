---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-12
title: 如何结合trace，分析卡顿率指标异常问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 如何结合trace，分析卡顿率指标异常问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3e69d4affd802a17836d4439f62fdf65203f089371cac9c188f1142a370c705e
---

下载并打开trace后，通过上报的Present ID字段搜索，可快速定位问题点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/jvGmSb6ET7KypTfDODLbiw/zh-cn_image_0000002229758405.png?HW-CC-KV=V1&HW-CC-Date=20260428T003031Z&HW-CC-Expire=86400&HW-CC-Sign=E2B465A227B0C185FA19B6D9911831875E7D9F9C1D5649BA9C6177B8721DDAE6 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/AlJWubLJQ8asFIKn51vOKg/zh-cn_image_0000002194318144.png?HW-CC-KV=V1&HW-CC-Date=20260428T003031Z&HW-CC-Expire=86400&HW-CC-Sign=DD50C3F2AE6CAD7F0472CDD71368C54C4F6FC2891B050C6961B808AC29380802 "点击放大")

上图中，99009这一帧在屏幕上持续了33ms，超出应持续的16.6ms，被统计为丢1帧。
