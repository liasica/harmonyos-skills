---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8
title: Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f695cc9296b98c63d4ea1d37afe8d8e6608da991b2ab9e86065680387ebab255
---

**问题现象**

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/uj3MM3CKQK6XJVWGD9W7FA/zh-cn_image_0000002314311052.png?HW-CC-KV=V1&HW-CC-Date=20260429T062129Z&HW-CC-Expire=86400&HW-CC-Sign=10F922367DEDEAF94385C07F07AAB0B7C1506CFCDEA737E01542BE3E2380041B "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RDpH3spHQdimPOpxe6sd9A/zh-cn_image_0000002314151220.png?HW-CC-KV=V1&HW-CC-Date=20260429T062129Z&HW-CC-Expire=86400&HW-CC-Sign=A0E81F77523AA59ED2BD897DA8DC9E776F5539F4FF077F4FF4A3FCAB9D59E328 "点击放大")

**问题原因**

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

**解决措施**

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。
