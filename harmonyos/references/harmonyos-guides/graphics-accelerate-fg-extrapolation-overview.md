---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-extrapolation-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 外插模式 > 概述
category: harmonyos-guides
scraped_at: 2026-09-10T06:23:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9d423d848a3dbe21533ce156d3c2ff5ff028bd3860662ab765b8383516d2b709
---

超帧外插模式是利用相邻两个真实渲染帧进行超帧计算并生成未来一帧预测帧，即利用第N-1帧、第N帧真实帧预测第N+0.5帧预测帧，如下图所示。由于外插模式不改变渲染时间线和显示时间线的帧间顺序，因此不会导致响应时延的增加。但由于外插模式预测的是未来帧画面，当发生场景画面帧间差异大、相机或物体运动方向突变时，在预测帧的画面边缘和物体边缘容易出现拖影和模糊现象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/I2rwwVFHTMm4HR3tk1Q6eQ/zh-cn_image_0000002717611572.png)
