---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-16
title: 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
breadcrumb: FAQ > DevEco Studio > 性能分析 > 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7c5a6ccd16a1b47f7c81128ed946f167eb349f8a45ced7a9aa3b65875680fcb1
---

**问题现象**

录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致。

**可能原因**

Memory泳道内是所选择应用的实际物理内存占用（Proportional Set Size, PSS），Native Allocation泳道展示的是应用在运行过程中动态向操作系统申请的虚拟内存，并不代表实际物理内存占用。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/pxSoQn1AQd6AOXS-pMs0mg/zh-cn_image_0000002513253146.png?HW-CC-KV=V1&HW-CC-Date=20260429T062133Z&HW-CC-Expire=86400&HW-CC-Sign=25ADBD9C9CA4C80398DF1E914D809CB2A2FDAA474F80D505D4CBAAF2244B668E)按钮，设置最小跟踪内存（Native Allocation Filter Size）为0或极小值，以采集更多甚至全量的虚拟内存分配事件，让Native Allocation泳道与Memory泳道的数据变化量接近。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/NYhNIOACRxWK2V8kvhJRUA/zh-cn_image_0000002544733119.png?HW-CC-KV=V1&HW-CC-Date=20260429T062133Z&HW-CC-Expire=86400&HW-CC-Sign=FC00BC096D9E5213A5D05A39246361B21B87D35284D519BE914040D0957FED93 "点击放大")
