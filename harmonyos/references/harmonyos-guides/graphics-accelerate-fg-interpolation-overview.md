---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-interpolation-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 内插模式 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2d1f0f90bc692df2a10553b6afdff4785e00c9b7e3a802af63d89037ce6efef2
---

超帧内插模式是利用相邻两个真实渲染帧进行超帧计算生成中间的预测帧，即利用第N-1帧和第N帧真实渲染帧预测第N-0.5帧预测帧，如下图所示。由于中间预测帧的像素点通常能在前后两帧中找到对应位置，因此内插模式的预测帧效果较外插模式更优。由于第N帧真实渲染帧需要等待第N-0.5帧预测帧生成并送显后才能最终送显，因此会新增1~2帧的响应时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/IJ8b6_VqShefuR7XqZqkjw/zh-cn_image_0000002583478707.png?HW-CC-KV=V1&HW-CC-Date=20260427T234723Z&HW-CC-Expire=86400&HW-CC-Sign=E1537F8BBDDB9D63BF6A3FB78E3F5FCE9126D6B8F2ABA6277E1B55C686FFB631)
