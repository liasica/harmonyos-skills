---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-17
title: 指标检测值无法点击拉起profiler
breadcrumb: FAQ > DevEco Studio > 性能分析 > 指标检测值无法点击拉起profiler
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:344036b45cf87d81d39afb4654b6fb4e917391e99c80faf445319eeddac1473f
---

**问题现象**

报告详情页，指标检测值无法点击，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/7q5OOqHDQBa2MNFRHHjAZQ/zh-cn_image_0000002654798183.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=AB8220CD7ADF9CACA8C484EF0C3FD6DABB99E00A2167F14FFA1EDF70E4C7C94D)

预期是可以点击指标检测值并拉起profiler，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/kBe57oKnR8uzmAGE3RmEdg/zh-cn_image_0000002624638722.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E16139B5A324C692CE2BE38A09BF7D5E2D97A51EFA46468D23FCE7CFD0FC87D)

**问题原因**

体检卡片勾选冷启动场景，但在录制开始时未重启应用，导致堆栈抓取失败。

**解决措施**

1、建议冷启动场景，使用“手动性能冷启动体检”卡片进行检测。

2、如果是自定义卡片场景勾选“冷启动”场景，需要在录制开始时，强制重启应用，之后再进行体检。
