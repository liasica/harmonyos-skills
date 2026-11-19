---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:28489cd6c4d97ed940bbfd5d7765b9888f6fc9f0bffee6b1062adc267fe0618a
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/9TscxpjuRwWv7FJaVCY_7g/zh-cn_image_0000002791566156.png?HW-CC-KV=V1&HW-CC-Date=20261119T014753Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A7F71FFB924E75F4572E0B1FB2ECFCB92B03A4AA60DB81EBDE84B4F05AB0387)
