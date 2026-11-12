---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-12
title: 如何结合trace，分析卡顿率指标异常问题
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 如何结合trace，分析卡顿率指标异常问题
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:244fcec40345afc99b7b17407b1e14231730d62270c818ab4d5ae60a8a0227bf
---

下载并打开trace后，通过上报的Present ID字段搜索，可快速定位问题点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/jsw03qDjSG6gjGk-WvmKPg/zh-cn_image_0000002624638878.png?HW-CC-KV=V1&HW-CC-Date=20261112T233218Z&HW-CC-Expire=31536000000&HW-CC-Sign=F8FD14A780D80D09558BA65FA1B028608AAC6E7EFCE6F5A9A6B28AF531BEF74D "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/l6P2agLKQgCGdU8hGrLqBg/zh-cn_image_0000002654838299.png?HW-CC-KV=V1&HW-CC-Date=20261112T233218Z&HW-CC-Expire=31536000000&HW-CC-Sign=456F33CFB2BCE16B397936AEAC61811555BEACF08B15B09310DC32DFDBF595C7 "点击放大")

上图中，99009这一帧在屏幕上持续了33ms，超出应持续的16.6ms，被统计为丢1帧。
