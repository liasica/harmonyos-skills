---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-overview
title: ArkTS卡片界面开发概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片界面开发概述
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0b1f279fcf8e07482ce43d7a3747b705f50f2c29a88ce1febe313cb1f1b24cc2
---

ArkTS卡片开发采用通用[ArkTS语言](learning-arkts.md)，开发者可以使用[ArkTS声明式开发范式](arkts-ui-development-overview.md)开发ArkTS卡片页面。

如下卡片页面由DevEco Studio模板自动生成，开发者可以根据自身的业务场景进行调整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/G4PvtyvuSJCV9hckkU5AFA/zh-cn_image_0000002589244595.png?HW-CC-KV=V1&HW-CC-Date=20260429T052953Z&HW-CC-Expire=86400&HW-CC-Sign=4FBEB03D01152E0B5D81757FCD00EF71D72C90E12FD6E6841E69776A4D149EEE)

## ArkTS卡片支持的页面能力

ArkTS卡片具备JS卡片的全量能力，并且新增了动效能力和自定义绘制的能力，支持[ArkTS声明式开发范式](arkts-ui-development-overview.md)的部分组件、事件、动效、数据管理、状态管理能力。

对于支持在ArkTS卡片UI界面中使用的接口，会添加“卡片能力”的标记，如：从API version 12开始，该接口支持在ArkTS卡片中使用。同时请留意卡片场景下的能力差异说明。

例如：以下说明表示CircleShape可在ArkTS卡片中使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/KaO3DoTZSnGtYTWdqYl0cA/zh-cn_image_0000002558764790.png?HW-CC-KV=V1&HW-CC-Date=20260429T052953Z&HW-CC-Expire=86400&HW-CC-Sign=68B5BE4B8AEFCD206DEE024FAB6A85CE2002A4B655407E32D57A0C9D15C5722F)
