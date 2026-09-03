---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:25+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:094f743238fefb87faa5c8a648e40f89e6835c79963f492e0aceff99bcfec323
---

## 异步栈缝合

在异步回栈时，可单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/hFhcEO1VTdmjRf0pGDiPEQ/zh-cn_image_0000002731382645.png "点击放大")按钮，配置异步栈嵌套层数和异步回栈层数。

如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/bnNtIsUyS_-Mwvrv99kzNA/zh-cn_image_0000002701823342.png "点击放大")
