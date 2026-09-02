---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5
title: Profiler录制Allocation没有Native信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Allocation没有Native信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:5bcc66a3ec16ec7541fb505cc5b9bfa5a02a58a8769f0b5edb2d5d648a0f09bd
---

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/RSc7EaGLRT6oWprFiJy9pw/zh-cn_image_0000002624638716.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/qYFJ3DqXSIyr-IXhfWssFw/zh-cn_image_0000002654838129.png)
