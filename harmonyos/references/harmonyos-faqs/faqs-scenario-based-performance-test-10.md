---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-scenario-based-performance-test-10
title: 卡顿率指标是怎么定义的
breadcrumb: FAQ > DevEco Testing > 专项测试 > 场景化性能测试 > 卡顿率指标是怎么定义的
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f8bd276e93f008af2847174ce6487edf77043136a0c4e264d9549d734acd0ec6
---

卡顿率是指在一段动效区间内累计的丢帧时长，用于评估整个动效时段的画面流畅度。卡顿率的值是累计丢帧时长与动效时长的比值，单位为ms/s。

单帧丢帧时长等于实际上屏时间减去期望上屏时间。上屏时间可在trace图形子系统的present线程中查看，取泳道结束点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/tie2qQVITlWqx8BE8qTQKg/zh-cn_image_0000002194318020.png?HW-CC-KV=V1&HW-CC-Date=20260429T062149Z&HW-CC-Expire=86400&HW-CC-Sign=F060E18628B1F3C65F977B7058CB9D7DB8B776BE404B24129FCB99A2C14EF61F "点击放大")
