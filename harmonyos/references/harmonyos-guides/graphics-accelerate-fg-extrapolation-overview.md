---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-extrapolation-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 外插模式 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:00262a47a7c62f997da2b8195e9fe669acac6287821615b4011ab45154c1e175
---

超帧外插模式是利用相邻两个真实渲染帧进行超帧计算并生成未来一帧预测帧，即利用第N-1帧、第N帧真实帧预测第N+0.5帧预测帧，如下图所示。由于外插模式不改变渲染时间线和显示时间线的帧间顺序，因此不会导致响应时延的增加。但由于外插模式预测的是未来帧画面，当发生场景画面帧间差异大、相机或物体运动方向突变时，在预测帧的画面边缘和物体边缘容易出现拖影和模糊现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/M7GuvBaET3mqBPkqgTaJzQ/zh-cn_image_0000002552958708.png?HW-CC-KV=V1&HW-CC-Date=20260427T234723Z&HW-CC-Expire=86400&HW-CC-Sign=2E205E551166B38051C606953D8A9C8E4A66994D7D5DA0402E0DE7E65BE950CA)
