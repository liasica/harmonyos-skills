---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-12
title: 如何结合trace，分析卡顿率指标异常问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 如何结合trace，分析卡顿率指标异常问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:51+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:20503d4294582ff4cd3eee061da2806503e5c29ac0f6b6b8c6b3d31a518f72ab
---

下载并打开trace后，通过上报的Present ID字段搜索，可快速定位问题点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/jvGmSb6ET7KypTfDODLbiw/zh-cn_image_0000002229758405.png?HW-CC-KV=V1&HW-CC-Date=20260429T062150Z&HW-CC-Expire=86400&HW-CC-Sign=CC514A6151BAF555B5BE11076B85673EBBFB46EE226B887979A63BD05E5D2B16 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/AlJWubLJQ8asFIKn51vOKg/zh-cn_image_0000002194318144.png?HW-CC-KV=V1&HW-CC-Date=20260429T062150Z&HW-CC-Expire=86400&HW-CC-Sign=69FB17921AB17EA2F685B1FB04ECF34F2E524E25382AF123D7C243932DAAA205 "点击放大")

上图中，99009这一帧在屏幕上持续了33ms，超出应持续的16.6ms，被统计为丢1帧。
