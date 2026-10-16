---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-10-17T06:43:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:c4b13a18b1cf9c757cf9ab5faff7775a549fddf9e9459575c3bb9acbd7ee1dcd
---

## 异步栈缝合

在异步回栈时，可单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/psGeZSlsQu2DvZ1FVfmf7w/zh-cn_image_0000002731382645.png "点击放大")按钮，配置异步栈嵌套层数和异步回栈层数。

如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/zwSZ75lXQ-KXf43dX7qu2Q/zh-cn_image_0000002701823342.png "点击放大")
