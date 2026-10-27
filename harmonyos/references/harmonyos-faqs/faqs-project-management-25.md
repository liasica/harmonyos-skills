---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-25
title: ExternalCpp视图中显示SDK的系统API
breadcrumb: FAQ > DevEco Studio > 工程管理 > ExternalCpp视图中显示SDK的系统API
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:50+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e39b0b1ce2982d8456dcd66e75e2a556e7988a2c863bc85ffe65536fa21b56e1
---

**问题现象**

ExternalCpp视图中显示SDK的系统API。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/LWUR3s7vSv-MtjKefUpvsA/zh-cn_image_0000002624478440.png)

**可能原因**

在本地存在多个DevEco Studio（包括Command Line Tools）打开同一个工程，并且使用daemon模式构建该工程。

**解决措施**

关闭多余的DevEco Studio（包括Command Line Tools）或者使用--no-daemon模式构建工程。

**参考链接**

[守护进程](../harmonyos-guides/ide-hvigor-daemon.md)
