---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-17
title: 指标检测值无法点击拉起profiler
breadcrumb: FAQ > DevEco Studio > 性能分析 > 指标检测值无法点击拉起profiler
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:34+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:8d8bf3ebef7e216573707e2be14334f6ab4191d5b2982b79914c83a835038828
---

**问题现象**

报告详情页，指标检测值无法点击，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/5vyETZ4wTnKyw4xtfaruJw/zh-cn_image_0000002527522192.png)

预期是可以点击指标检测值并拉起profiler，如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/FMNKmpxLTfORI16D4kJB6w/zh-cn_image_0000002558681913.png)

**问题原因**

体检卡片勾选冷启动场景，但在录制开始时未重启应用，导致堆栈抓取失败。

**解决措施**

1、建议冷启动场景，使用“手动性能冷启动体检”卡片进行检测。

2、如果是自定义卡片场景勾选“冷启动”场景，需要在录制开始时，强制重启应用，之后再进行体检。
