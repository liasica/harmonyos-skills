---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-23
title: macOS上活动监视器中显示模拟器内存偏高
breadcrumb: FAQ > DevEco Studio > 应用运行 > macOS上活动监视器中显示模拟器内存偏高
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:58+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:edb987f5f119aaff3bbfb523b4a5772b2d64ef6c0e910912770e3bb2c3f3dc20
---

配置模拟器内存为4GB并使用一段时间后，在活动监视器中可能发现模拟器进程占用的内存超过6GB（如下图所示）。请注意，图中的6.49GB不代表模拟器进程实际使用的物理内存（即Dirty内存），而是指其占用的phys\_footprint内存。在Mac系统中，针对虚拟化平台（如模拟器），phys\_footprint内存通常远高于Dirty内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/2G3YJjXeTzKmY90cUD4m8g/zh-cn_image_0000002624478758.png "点击放大")

想要查看模拟器的Dirty内存，首先打开活动监视器，查看Emulator的进程号（PID）。然后通过 `footprint -vmObjectDirty 进程号` 命令可以查看Dirty内存大小。
