---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:48+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:ed45a540ab42940697385ee0d6c8ed4948934b59ce3296117674e0c18f790822
---

从API版本26.0.0开始，支持游戏预启动能力。

预启动是一种系统级启动优化机制，根据用户的使用习惯，在系统资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。

## 约束与限制

游戏预启动能力支持Phone（运行内存大于8G）、Tablet、PC/2in1设备。

## 用户体验

打开游戏时，自动跳过游戏资源加载、编译阶段，直达游戏界面。

* 游戏预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/3O2Dw66NSQGcSMu54Nao0A/zh-cn_image_0000002791566176.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=C5F6020C8566EC2D5A85C7161613604875B06F45D983089697AAF8D69F0A4C9D "点击放大")
* 游戏未预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/CY6j6FIsQqCTk0njb5jK1Q/zh-cn_image_0000002820526129.gif?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=C53B1FDB70BF05B360C5DD52D74797D98880073993ED370A586A630F3B655B2B "点击放大")
