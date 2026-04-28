---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-17
title: 指标检测值无法点击拉起profiler
breadcrumb: FAQ > DevEco Studio > 性能分析 > 指标检测值无法点击拉起profiler
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:16+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:aced00d35a5438b6ee2be14f8366e85f1b66872923daa30b8f28d3fa1e4f4022
---

**问题现象**

报告详情页，指标检测值无法点击，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5vyETZ4wTnKyw4xtfaruJw/zh-cn_image_0000002527522192.png?HW-CC-KV=V1&HW-CC-Date=20260428T003015Z&HW-CC-Expire=86400&HW-CC-Sign=B23299F7F656CBE1C208412D04A6D7970C181A6B45BAEAFD318DDE267A99B8C5)

预期是可以点击指标检测值并拉起profiler，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/FMNKmpxLTfORI16D4kJB6w/zh-cn_image_0000002558681913.png?HW-CC-KV=V1&HW-CC-Date=20260428T003015Z&HW-CC-Expire=86400&HW-CC-Sign=0EB41E48FC5B14AC41BC8CFDCFFFBEFAA35A2AC09A526EFA8C1BCA30F966CC1B)

**问题原因**

体检卡片勾选冷启动场景，但在录制开始时未重启应用，导致堆栈抓取失败。

**解决措施**

1、建议冷启动场景，使用“手动性能冷启动体检”卡片进行检测。

2、如果是自定义卡片场景勾选“冷启动”场景，需要在录制开始时，强制重启应用，之后再进行体检。
