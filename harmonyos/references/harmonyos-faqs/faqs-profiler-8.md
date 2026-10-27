---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8
title: Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:00+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4c4ae1bbc96f4303b982b09c632d7d0f56421f73e8bee5920b6f49e6550f4809
---

**问题现象**

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/9B-mkTFrRLyOEHMDlHnQKw/zh-cn_image_0000002654798177.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/xDFi6_uCSuGWiIvwn2wCdw/zh-cn_image_0000002624638718.png "点击放大")

**问题原因**

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

**解决措施**

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。
