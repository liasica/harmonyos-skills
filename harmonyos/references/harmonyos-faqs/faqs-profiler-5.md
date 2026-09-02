---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5
title: Profiler录制Allocation没有Native信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Allocation没有Native信息
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d20c11c1ba72b52a55148b407fa5684131ed26b0496a142959500958a6436567
---

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/75GAKXn_Qwaljjt3jic1HQ/zh-cn_image_0000002269366576.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/9hA2bskERo-sJTXFzSh5sA/zh-cn_image_0000002304120341.png)
