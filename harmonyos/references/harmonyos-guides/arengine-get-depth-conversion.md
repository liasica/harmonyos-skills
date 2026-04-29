---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-get-depth-conversion
title: 深度估计介绍
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 深度估计 > 深度估计介绍
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:0416758aa8e4d44739ba6f3396e6f2c03df7ec4823d76d0c67bd8b2ac628314a
---

AR Engine支持持续输出周围环境相对终端设备的深度信息，利用这些深度信息，可以实现更加自然、无缝的虚实体验。

本功能提供的深度信息是指从终端设备摄像头到显示场景中各点的深度值，每个像素点都有深度值、置信度信息，开发者可自行根据应用需求根据置信度选择更稠密或者更精确的深度信息。

该技术可应用于例如测量、体积估算、场景重建等获取空间物体深度信息场景，基于此信息完成一些空间计算任务，比如计算物体体积等。

**图1** 深度渲染示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/UGnTPUQYQKmxXpWwlZRo5g/zh-cn_image_0000002589324993.png?HW-CC-KV=V1&HW-CC-Date=20260429T053555Z&HW-CC-Expire=86400&HW-CC-Sign=E7BA598682BCE6C5235CF3980D240AA97E960BEFE1883610D5A6291F4A4E0783)
