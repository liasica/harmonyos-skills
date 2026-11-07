---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-glossary
title: DevEco Profiler术语
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 优化应用性能 > 附录 > DevEco Profiler术语
category: harmonyos-guides
scraped_at: 2026-11-07T08:02:29+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:73425445a2afaeab8a4375c6e3501296a3774cb0e3d3ba9a5bc668d666f85603
---

## 异步栈缝合

在异步回栈时，可单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/ceVFMDFLT4W0pLEeHk962Q/zh-cn_image_0000002731382645.png "点击放大")按钮，配置异步栈嵌套层数和异步回栈层数。

如下图中的start\_malloc\_xxx\_work异步调用malloc\_xxx\_work，当开关未开启时，仅能回malloc\_xxx\_work栈帧；当开关开启后，支持回malloc\_xxx\_work栈帧和start\_malloc\_xxx\_work栈帧。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/KjMjxH5yRYSNx_vK3kxNlg/zh-cn_image_0000002701823342.png "点击放大")
