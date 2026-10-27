---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5
title: Profiler录制Allocation没有Native信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Allocation没有Native信息
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:9686e55a19f68e0bc4565d9688ee3a31fc53782f7198fb9529dffc37b22af370
---

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/NauYjEOsQVe4llBzVGe3tQ/zh-cn_image_0000002624638716.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/pME_WZb5Sg6xUZnJIesDtw/zh-cn_image_0000002654838129.png)
