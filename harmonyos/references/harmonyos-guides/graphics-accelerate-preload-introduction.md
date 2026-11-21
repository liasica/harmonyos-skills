---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:13+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:9ec04fe46493e4fa73457c69defb191d3cba33e91cab72724cdd168c00482d17
---

从API版本26.0.0开始，支持游戏预启动能力。

预启动是一种系统级启动优化机制，根据用户的使用习惯，在系统资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。

## 约束与限制

游戏预启动能力支持Phone（运行内存大于8G）、Tablet、PC/2in1设备。

## 用户体验

打开游戏时，自动跳过游戏资源加载、编译阶段，直达游戏界面。

* 游戏预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/i-8uXoNxSZOsM126PQuRIA/zh-cn_image_0000002821757737.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011046Z&HW-CC-Expire=31536000000&HW-CC-Sign=7AB69ADFCB4414EE855A0D02C04B9FB18574EC0E8C6F2F1E18367327957D025A "点击放大")
* 游戏未预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/LhANXgCdTS-YTtlHtBVrUQ/zh-cn_image_0000002793037800.gif?HW-CC-KV=V1&HW-CC-Date=20261121T011046Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF5802BD6465B1F865AF750927B7078EC6BFEBF0D144BDBA7B3F5BB6DB153E2F "点击放大")
