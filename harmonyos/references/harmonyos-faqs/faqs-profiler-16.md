---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-16
title: 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
breadcrumb: FAQ > DevEco Studio > 性能分析 > 录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:fe2322786d8d7638a7ec1c663bd56b17ff5646164bd988859dfa0430ca6a31db
---

**问题现象**

录制Allocation模板时，Memory泳道和Native Allocation泳道内存不一致。

**可能原因**

Memory泳道内是所选择应用的实际物理内存占用（Proportional Set Size, PSS），Native Allocation泳道展示的是应用在运行过程中动态向操作系统申请的虚拟内存，并不代表实际物理内存占用。

**解决措施**

开始录制前，单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/E9o9q_KwSB6g46z1GqAR4w/zh-cn_image_0000002654838133.png)按钮，设置最小跟踪内存（Native Allocation Filter Size）为0或极小值，以采集更多甚至全量的虚拟内存分配事件，让Native Allocation泳道与Memory泳道的数据变化量接近。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/dtm8CKFFTryYPtlixcwWaQ/zh-cn_image_0000002624478816.png "点击放大")
