---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-71
title: 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:53+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:e921b3d82e380c576bfcd12bfd909a0fe53aa76010bb1b244eaeac7183386769
---

**说明** 

注：此方法为临时规避方案，后续将修复该问题，建议仅在阻塞时使用。

用于减少编译HSP和闭源HAR包时生成声明文件的耗时。

修改 ets\_checker.js 文件（文件路径：SDK路径\default\base\ets\build-tools\ets-loader\lib\ets\_checker.js），编辑 processBuildHap 函数。

1. 生成 sourceFile，在遍历文件时生成声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/EwYHpcZ6QRCUKBbLKdyO3Q/zh-cn_image_0000002654797893.png "点击放大")
2. 修改 getEmitOutput 函数，将其改为 getFileEmitOutput 函数，以获取声明文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/ArX8QtT5SPCrxEBh04s0Kw/zh-cn_image_0000002624638440.png "点击放大")
