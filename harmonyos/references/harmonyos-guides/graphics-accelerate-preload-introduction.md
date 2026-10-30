---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-introduction
title: 业务概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 业务概述
category: harmonyos-guides
scraped_at: 2026-10-31T07:32:52+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:c0d3976c4b6b8b111c412d57a6e2760c3294d66eea941ed536c6a4c3445b480d
---

从API版本26.0.0开始，支持游戏预启动能力。

预启动是一种系统级启动优化机制，根据用户的使用习惯，在系统资源充足时提前加载游戏进行部分初始化和资源加载，从而在用户触发启动时显著缩短游戏启动时间，提升用户体验。

## 约束与限制

游戏预启动能力支持Phone（运行内存大于8G）、Tablet、PC/2in1设备。

## 用户体验

打开游戏时，自动跳过游戏资源加载、编译阶段，直达游戏界面。

* 游戏预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/PQjWzOiMR7aVBDiINBYB5w/zh-cn_image_0000002806029417.gif "点击放大")
* 游戏未预启动

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/KDMGyO7YT0W7XdKGCFGJcA/zh-cn_image_0000002806109307.gif "点击放大")
