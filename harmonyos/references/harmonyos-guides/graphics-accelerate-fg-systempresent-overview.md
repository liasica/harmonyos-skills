---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-fg-systempresent-overview
title: 概述
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏渲染加速服务 > 超帧功能开发 > 系统送显模式 > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fe02c63c65487829fb8e4971fa7bc78466469ff253cea23838e6276e05d5240f
---

从5.1.0(18)版本开始，新增支持系统送显模式。

系统送显模式是相较于游戏送显模式，能减少开发者集成复杂度的方案。在游戏送显模式下，系统完成预测后需要游戏应用主动调用图形API来完成预测帧的送显。 系统送显模式下游戏虽仍需要触发插帧任务，但不再需要负责预测帧送显，系统会完成送显。当前系统送显模式仅支持内插模式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/hdg1k4D3Sv-BJbVkf_CUmw/zh-cn_image_0000002821757717.png?HW-CC-KV=V1&HW-CC-Date=20261121T011212Z&HW-CC-Expire=31536000000&HW-CC-Sign=670876230CF01C00589A7CC213389F73BE41A3FF62A8C7D1D293F6CA134D77E1)
