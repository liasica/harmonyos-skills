---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:37+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:483e453561ec3e00ca0a77921c8b2d2d908e1c796ff040891d3dc35204e52da4
---

## 异步栈缝合

在异步回栈时，可单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/3rddHgJcQcKLqTUJnqlTCQ/zh-cn_image_0000002779567202.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=18AF8618EFE38B226353B4A185FA4F34B0E05A870DFD4F561DA3941040961608 "点击放大")按钮，配置异步栈嵌套层数和异步回栈层数。

如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/vLyrxKi7QdupVyj_NY5ujA/zh-cn_image_0000002808766781.png?HW-CC-KV=V1&HW-CC-Date=20261124T044236Z&HW-CC-Expire=31536000000&HW-CC-Sign=98D7644CB939E47B9C0BE0C6CEBAC9222F38FEDE20EFFC9EA2F3A47C9BDC1E19 "点击放大")
