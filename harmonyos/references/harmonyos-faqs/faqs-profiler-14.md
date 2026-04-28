---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-14
title: PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8acecbc9529cd681af610583f19d363a7723f84742070e545b6dd35e2ff3bfc7
---

**问题现象**

在使用PC设备时，通过FP回栈模式录制Allocation模板，Graphic Memory泳道中的OpenGL ES子泳道无数据。

**可能原因**

GPU底层库不支持FP回栈模式。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/oy307YKSQ7SldcXKSWt6wQ/zh-cn_image_0000002538356035.png?HW-CC-KV=V1&HW-CC-Date=20260428T003014Z&HW-CC-Expire=86400&HW-CC-Sign=C83F9E59CA7AACB271B5F7F93303C98DD12779AB40F17D9F2B370DD6CC1CD25B)按钮，设置内存分配栈回栈模式为DWARF。使用DWARF回栈模式采集数据时，性能开销较大，因此在录制Graphic Memory泳道时，建议不同时录制Native Allocation泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/HKe3xljNS1S6vGr6Xs_pXQ/zh-cn_image_0000002506636162.png?HW-CC-KV=V1&HW-CC-Date=20260428T003014Z&HW-CC-Expire=86400&HW-CC-Sign=015C32BD1588F82A4AC55B52A833FE7EE290A5256D5827D467AAFAC5EEE38997 "点击放大")
