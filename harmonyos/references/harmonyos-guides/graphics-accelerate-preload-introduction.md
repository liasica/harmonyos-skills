---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:2c11b7d41f6a161b9632dce4e719b594bb978e777e21beeb0527b629a8603ee6
---

从API版本26.0.0开始，支持游戏预启动能力。

预启动是一种系统级启动优化机制，根据用户的使用习惯，在系统资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。

## 约束与限制

游戏预启动能力支持Phone（运行内存大于8G）、Tablet、PC/2in1设备。

## 用户体验

打开游戏时，自动跳过游戏资源加载、编译阶段，直达游戏界面。

* 游戏预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/np4nNnWpS9K3c6mNblqvWQ/zh-cn_image_0000002815559535.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=E5DFCD655E97CCC5C092D9EDF2682AB7023F3F3F9D2E3E622B93146A9C2348D3 "点击放大")
* 游戏未预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/KIRa1jLIQiGbSBxLNR2iAA/zh-cn_image_0000002815399619.gif?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0F8E7423BBF3A89DC2E2804AB2A9A9850DCDA8D96E49EC5BCD3AEA19DB79789A "点击放大")
