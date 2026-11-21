---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-interpolation-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 内插模式 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c442555c514675356a8807b7c3892857726b9df2fc8341c8c6033bfcf016d5b0
---

超帧内插模式是利用相邻两个真实渲染帧进行超帧计算生成中间的预测帧，即利用第N-1帧和第N帧真实渲染帧预测第N-0.5帧预测帧，如下图所示。由于中间预测帧的像素点通常能在前后两帧中找到对应位置，因此内插模式的预测帧效果较外插模式更优。由于第N帧真实渲染帧需要等待第N-0.5帧预测帧生成并送显后才能最终送显，因此会新增1~2帧的响应时延。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/yC_zbnwaTQOSU8mm1vrHvg/zh-cn_image_0000002821757713.png?HW-CC-KV=V1&HW-CC-Date=20261121T011045Z&HW-CC-Expire=31536000000&HW-CC-Sign=8B84CA56034F64E218BA86613D04CC385E942E0296AF666EFBECC4F6045B1D54)
