---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:91225ada81e30e3c8793c165cb86cd754404416883fd86a3566b7f9cef7e0012
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/FmHFYE5OS6WngyqcSEcXDw/zh-cn_image_0000002788467770.png?HW-CC-KV=V1&HW-CC-Date=20261114T004807Z&HW-CC-Expire=31536000000&HW-CC-Sign=4EB156F19243589D86B4D3A7B0E4F97D9AC8BAB13FB392BA8C887171982FE0C7)
