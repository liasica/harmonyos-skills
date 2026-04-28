---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-10
title: 卡顿率指标是怎么定义的
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 卡顿率指标是怎么定义的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1d500dd1508b012f3bb2026c06c3ef05661ae769d89b39a5e8d09a09e43116a9
---

卡顿率是指在一段动效区间内累计的丢帧时长，用于评估整个动效时段的画面流畅度。卡顿率的值是累计丢帧时长与动效时长的比值，单位为ms/s。

单帧丢帧时长等于实际上屏时间减去期望上屏时间。上屏时间可在trace图形子系统的present线程中查看，取泳道结束点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/tie2qQVITlWqx8BE8qTQKg/zh-cn_image_0000002194318020.png?HW-CC-KV=V1&HW-CC-Date=20260428T003030Z&HW-CC-Expire=86400&HW-CC-Sign=FC37D7D687F0B18A6D4F049DF23D48750BAF75889128321A86E99293700B99A4 "点击放大")
