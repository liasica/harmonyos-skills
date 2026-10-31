---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:00+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:4d1272acd8faf94f4f3f297f36add4c5e7bb287fd4ef5742a6aafc527334e4b0
---

## 异步栈缝合

在异步回栈时，可单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/e1PT0qUsTJe_XaZD4d0yLA/zh-cn_image_0000002731382645.png "点击放大")按钮，配置异步栈嵌套层数和异步回栈层数。

如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/8ciAitnaTOiAZvy4X5X7RQ/zh-cn_image_0000002701823342.png "点击放大")
