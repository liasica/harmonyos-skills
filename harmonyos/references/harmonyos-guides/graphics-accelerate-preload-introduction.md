---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:08+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:8a0822915c2562ef6920ac881162bad8ba13197048847fbf1a5f9afdc80a5b69
---

从API版本26.0.0开始，支持游戏预启动能力。

预启动是一种系统级启动优化机制，根据用户的使用习惯，在系统资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。

## 约束与限制

游戏预启动能力支持Phone（运行内存大于8G）、Tablet、PC/2in1设备。

## 用户体验

打开游戏时，自动跳过游戏资源加载、编译阶段，直达游戏界面。

* 游戏预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/ES12ggQsThSFuA_eqmoSCQ/zh-cn_image_0000002788467790.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004807Z&HW-CC-Expire=31536000000&HW-CC-Sign=DFF5CE2CBCE4CB9B1D1B4F1164EF0FC03A0D48D115E6087E88C9CCF97D05ABF8 "点击放大")
* 游戏未预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/hKTeFB5yQfmvsRfWBvAIwQ/zh-cn_image_0000002817507279.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004807Z&HW-CC-Expire=31536000000&HW-CC-Sign=2EF3F516A31E7DCF74F3FAB377D9B7EF8F943D612B177435F277794BD0F7E67F "点击放大")
