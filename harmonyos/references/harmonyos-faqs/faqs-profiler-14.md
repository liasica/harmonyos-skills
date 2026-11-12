---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-14
title: PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > PC设备录制Allocation模板时，Graphic Memory泳道中OpenGL ES子泳道无数据
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:77e4ea047c95413f7383c3f70d3d08be29b5eb46efc329ed4a3ce918399a77b0
---

**问题现象**

在使用PC设备时，通过FP回栈模式录制Allocation模板，Graphic Memory泳道中的OpenGL ES子泳道无数据。

**可能原因**

GPU底层库不支持FP回栈模式。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/ZkPeltyvTEKdor41zbWTMw/zh-cn_image_0000002654798179.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=1104BC4B39D081ED84B95FBA2CEABCA2D8CFFDA166FBBFFC7BAC17F7CEEE1156 "点击放大")按钮，设置内存分配栈回栈模式为DWARF。使用DWARF回栈模式采集数据时，性能开销较大，因此在录制Graphic Memory泳道时，建议不同时录制Native Allocation泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/w-kS7lnbSlS5nrv0AwUXRQ/zh-cn_image_0000002624638720.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=039A98F6414F856E07A08D00C866A5D07BA2E748A15DB0F5E7720B50ABA665EE "点击放大")
