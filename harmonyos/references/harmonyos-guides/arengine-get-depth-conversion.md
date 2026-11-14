---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-depth-conversion
title: 深度估计介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 深度估计 > 深度估计介绍
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:04+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:579daf899ff92dfb159db5440091bf8c959b3c3a29d837553524df324ea1c20d
---

AR Engine支持持续输出周围环境相对终端设备的深度信息，利用这些深度信息，可以实现更加自然、无缝的虚实体验。

本功能提供的深度信息是指从终端设备摄像头到显示场景中各点的深度值，每个像素点都有深度值、置信度信息，开发者可自行根据应用需求根据置信度选择更稠密或者更精确的深度信息。

该技术可应用于例如测量、体积估算、场景重建等获取空间物体深度信息场景，基于此信息完成一些空间计算任务，比如计算物体体积等。

**图1** 深度渲染示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/gs4QDedUQBm3CB-tBfE5dQ/zh-cn_image_0000002817507153.png?HW-CC-KV=V1&HW-CC-Date=20261114T004804Z&HW-CC-Expire=31536000000&HW-CC-Sign=F0BF1A9A047F46165A2D390FF8AE3D398B2ACEF1599BBF6FDD0BB78F441915DF)
