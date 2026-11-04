---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-11-04T08:30:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:19244cd3de08bfbd0be96ba4fcc2f1a00cd1294fd9f83ac19f3969316d3250fe
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/jMJpc7d8RvqZcrAb0FWVdA/zh-cn_image_0000002809010799.png)
