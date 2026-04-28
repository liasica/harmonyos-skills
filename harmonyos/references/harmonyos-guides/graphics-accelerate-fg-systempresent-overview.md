---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2b9edfab93c7d2b4729ee9bd2dcc31aac4c2347d2f03baae04941fcdac42a2b1
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/lwzgH2APQqC_WA1ZabBSfw/zh-cn_image_0000002583478711.png?HW-CC-KV=V1&HW-CC-Date=20260427T234725Z&HW-CC-Expire=86400&HW-CC-Sign=66F180CFF5CF05BC329B4B4E2E079C0DCB1643AB11E8EA8275D92F787F1783C1)
