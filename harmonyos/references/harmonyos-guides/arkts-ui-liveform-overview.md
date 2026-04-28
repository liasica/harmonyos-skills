---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-liveform-overview
title: 互动卡片概述
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 互动卡片开发 > 互动卡片概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a433928c9c168f3ed08a41d3b6f70da980cb3f20fe1ad8ac16a08b95ff4e7bbb
---

从API version 20开始，支持互动卡片。互动卡片提供卡片动效能力，例如卡片破框动效，丰富信息提醒、浅层交互功能，显著提升用户体验。

## 使用场景

互动卡片包含两种类型：趣味交互类型互动卡片和场景动效类型互动卡片。

### 趣味交互类型

趣味交互类型互动卡片，提供卡片小游戏功能，当用户点击卡片时，开始体验对应卡片小游戏。当前仅支持基于[快游戏](../quickApp-Guides/quickgame-interact-card-0000002045917828.md)开发。详细请参考[趣味交互类型互动卡片开发指导](arkts-ui-liveform-funinteraction-development.md)。

**图1** 趣味交互类型互动卡片样例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/gMzdJDsLQ3OsXbQgFa6RNA/zh-cn_image_0000002583438353.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234132Z&HW-CC-Expire=86400&HW-CC-Sign=58BC385F9CA36D3379F9720419855568E20B03320B436611C297A08AF30C0AA2)

### 场景动效类型

场景动效类型互动卡片支持实现动态效果。以天气卡片为例，当天气变为雷雨天气时，卡片激活并触发互动卡片动效。动效结束后，卡片恢复原有显示效果。详细信息请参考[场景动效类型互动卡片概述](arkts-ui-liveform-sceneanimation-overview.md)。

## 约束和限制

* 互动卡片作为卡片功能的增强，卡片自身业务不能强依赖互动卡片动效能力。
