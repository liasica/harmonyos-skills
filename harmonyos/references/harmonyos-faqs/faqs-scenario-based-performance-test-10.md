---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-10
title: 卡顿率指标是怎么定义的
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 卡顿率指标是怎么定义的
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:04+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:664ff8ee1ec87de1c1e7f053a56477e11da8d0609d502c723970dc3bf31b1237
---

卡顿率是指在一段动效区间内累计的丢帧时长，用于评估整个动效时段的画面流畅度。卡顿率的值是累计丢帧时长与动效时长的比值，单位为ms/s。

单帧丢帧时长等于实际上屏时间减去期望上屏时间。上屏时间可在trace图形子系统的present线程中查看，取泳道结束点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/myx3EGc7SSujhHG5TlJJeg/zh-cn_image_0000002624478980.png "点击放大")
