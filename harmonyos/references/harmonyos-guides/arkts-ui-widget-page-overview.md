---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-overview
title: ArkTS卡片界面开发概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > ArkTS卡片提供方开发指导 > ArkTS卡片UI界面开发 > ArkTS卡片界面开发概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:11:22+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dd952afd0de227d82d9cc0f192f9d41724a8ed21b9b022d0bd43420bb33a47b4
---

ArkTS卡片开发采用通用[ArkTS语言](learning-arkts.md)，开发者可以使用[ArkTS声明式开发范式](arkts-ui-development-overview.md)开发ArkTS卡片页面。

如下卡片页面由DevEco Studio模板自动生成，开发者可以根据自身的业务场景进行调整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/CnWKxL80TVyfPFkpSzQm8Q/zh-cn_image_0000002792877238.png?HW-CC-KV=V1&HW-CC-Date=20261121T010957Z&HW-CC-Expire=31536000000&HW-CC-Sign=78BE5924B9D1F737CF19584521A044A29E670AC01D5F777BD4A8FC943644DB2C)

## ArkTS卡片支持的页面能力

ArkTS卡片具备JS卡片的全量能力，并且新增了动效能力和自定义绘制的能力，支持[ArkTS声明式开发范式](arkts-ui-development-overview.md)的部分组件、事件、动效、数据管理、状态管理能力。

对于支持在ArkTS卡片UI界面中使用的接口，会添加“卡片能力”的标记，如：从API version 12开始，该接口支持在ArkTS卡片中使用。同时请留意卡片场景下的能力差异说明。

例如：以下说明表示CircleShape可在ArkTS卡片中使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/6_eAKtsVR6-kUUec7gHdfg/zh-cn_image_0000002821837145.png?HW-CC-KV=V1&HW-CC-Date=20261121T010957Z&HW-CC-Expire=31536000000&HW-CC-Sign=2E39CA64DD890EF85C7813FAC43C0281037F566451568ECFC751BDBB365E7757)
