---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-71
title: 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:13441317451d31ee4732eeb1319e9f363b8b50a21fff7785ab24b3810d086b0b
---

说明

注：此方法为临时规避方案，后续将修复该问题，建议仅在阻塞时使用。

用于减少编译HSP和闭源HAR包时生成声明文件的耗时。

修改 ets\_checker.js 文件（文件路径：SDK路径\default\base\ets\build-tools\ets-loader\lib\ets\_checker.js），编辑 processBuildHap 函数。

1. 生成 sourceFile，在遍历文件时生成声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/le5KPUZ0SBSFQDWLrqDCiQ/zh-cn_image_0000002229603953.png?HW-CC-KV=V1&HW-CC-Date=20260429T062034Z&HW-CC-Expire=86400&HW-CC-Sign=3F187F1EA7E4055A8032EB44845BAA6512331B7538BCC94ED4BEFA1259D57DA8 "点击放大")
2. 修改 getEmitOutput 函数，将其改为 getFileEmitOutput 函数，以获取声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/H4RrIYuGRr-0mfRzbby6KQ/zh-cn_image_0000002194318168.png?HW-CC-KV=V1&HW-CC-Date=20260429T062034Z&HW-CC-Expire=86400&HW-CC-Sign=C0784EDD95529EE9FF1419E317A27937D5FF526DEFFCF880BC726D8AFE11BA45 "点击放大")
