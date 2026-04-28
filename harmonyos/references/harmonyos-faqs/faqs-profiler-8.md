---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-8
title: Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Launch，详情中Load ETS Files和TOP Redundant页签无数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:30:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:30c487bc1f1e86a667a566cd26d0ee68d4612afd9a42392f98160ec6569ba3a5
---

**问题现象**

Profiler录制Launch，将ETS文件监控时长配置为20000，录制成功后，详情中Load ETS Files和TOP Redundant页签无数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/uj3MM3CKQK6XJVWGD9W7FA/zh-cn_image_0000002314311052.png?HW-CC-KV=V1&HW-CC-Date=20260428T003013Z&HW-CC-Expire=86400&HW-CC-Sign=6E5CF3C44423AF17BF72202E02A69E8EE4CDFEAD730B67B4F62618E74F6CC787 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/RDpH3spHQdimPOpxe6sd9A/zh-cn_image_0000002314151220.png?HW-CC-KV=V1&HW-CC-Date=20260428T003013Z&HW-CC-Expire=86400&HW-CC-Sign=CBC4A37C0419FD35A70B4A6B7900422C2AA25EFFAA2372DAFC7834854F337B98 "点击放大")

**问题原因**

ETS文件监控时长配置为20000，需要在拉起应用20000ms之后，才能生成对应的ETS冗余打点文件。

**解决措施**

将ETS文件监控时长配置为20000后，录制时长一定要大于配置时长。
