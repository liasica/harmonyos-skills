---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-10
title: 卡顿率指标是怎么定义的
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 卡顿率指标是怎么定义的
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:86c593f4f50059e0d07ed21fca238406af7d4b7b66fa98fc158c6ef682f7f179
---

卡顿率是指在一段动效区间内累计的丢帧时长，用于评估整个动效时段的画面流畅度。卡顿率的值是累计丢帧时长与动效时长的比值，单位为ms/s。

单帧丢帧时长等于实际上屏时间减去期望上屏时间。上屏时间可在trace图形子系统的present线程中查看，取泳道结束点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/vU_y8qbWQziQTv6fOrls6w/zh-cn_image_0000002624478980.png "点击放大")
