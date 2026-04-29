---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-5
title: Profiler录制Allocation没有Native信息
breadcrumb: FAQ > DevEco Studio > 性能分析 > Profiler录制Allocation没有Native信息
category: harmonyos-faqs
scraped_at: 2026-04-29T14:21:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ae52f166cc6d00f1f89adfc3813b1e6b6f2555bfb087f4b5866963ba5e2512d2
---

**解决措施**

取消勾选Run > Edit Configurations > Diagnostics 内的Address Sanitizer、Thread Sanitizer、Hardware-Assisted Address Sanitizer选项重新运行应用录制即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/75GAKXn_Qwaljjt3jic1HQ/zh-cn_image_0000002269366576.png?HW-CC-KV=V1&HW-CC-Date=20260429T062129Z&HW-CC-Expire=86400&HW-CC-Sign=DB9F5CE774B65E9BA76E67E09B52AE747AB35D16D9CF5D73A7EF58FACB47A4A3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/9hA2bskERo-sJTXFzSh5sA/zh-cn_image_0000002304120341.png?HW-CC-KV=V1&HW-CC-Date=20260429T062129Z&HW-CC-Expire=86400&HW-CC-Sign=EE470BA702B11D13F2E47B0CE8461586EDB02F35E5812C7D8A9F42442423B9F4)
