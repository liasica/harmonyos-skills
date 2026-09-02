---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-16
title: 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
breadcrumb: FAQ > DevEco Studio > 性能分析 > 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c628013c375641d62b8aef1c6f39c86bce422464ed8e41fcdc485d9add9ebad
---

**问题现象**

录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致。

**可能原因**

Memory泳道内是所选择应用的实际物理内存占用（Proportional Set Size, PSS），Native Allocation泳道展示的是应用在运行过程中动态向操作系统申请的虚拟内存，并不代表实际物理内存占用。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/pxSoQn1AQd6AOXS-pMs0mg/zh-cn_image_0000002513253146.png)按钮，设置最小跟踪内存（Native Allocation Filter Size）为0或极小值，以采集更多甚至全量的虚拟内存分配事件，让Native Allocation泳道与Memory泳道的数据变化量接近。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/NYhNIOACRxWK2V8kvhJRUA/zh-cn_image_0000002544733119.png "点击放大")
