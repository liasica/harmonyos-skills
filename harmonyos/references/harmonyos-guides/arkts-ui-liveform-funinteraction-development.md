---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-liveform-funinteraction-development
title: 趣味交互类型互动卡片开发指导
breadcrumb: 指南 > 应用框架 > Form Kit（卡片开发服务） > ArkTS卡片开发（推荐） > 互动卡片开发 > 趣味交互类型互动卡片开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:34+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:9e0d1ecc204d48f4f9031773d049ef87e871f043284738bfeeb9a49ca577d48f
---

趣味交互类型互动卡片当前仅支持基于[快游戏](../quickApp-Guides/quickgame-interact-card-0000002045917828.md)开发的卡片小游戏，互动卡片默认处于非激活态，当用户点击卡片时，卡片切换为激活态，并开始游戏。在游戏过程中，用户可以点击“暂停”按钮进入暂停态。在暂停态，用户可以通过“继续游戏”和“停止游戏”按钮选择返回激活态继续游戏，或者结束游戏。

## 基本概念

趣味交互类型互动卡片主要包含三个状态：激活态、暂停态和非激活态，分别对应游戏进行、游戏暂停、游戏结束。

### 激活态

在此状态下，卡片UI由卡片提供方基于快游戏所开发的卡片小游戏页面承载。此时系统支持游戏内容渲染到卡片自身渲染区域之外的“破框”效果。

**图1** 趣味交互类型互动卡片激活态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/aSpbYFCJQPeEYyEcd3S8iA/zh-cn_image_0000002552958308.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=C1DB8515122904998A89FB72B8167CE64E801396BC12EF2E226B6CB4A7515C41)

### 暂停态

在此状态下，卡片UI由卡片提供方widgetCard.ets中的内容所承载。同时系统在卡片上默认展示“继续游戏”和“停止游戏”按钮。

**图2** 趣味交互类型互动卡片暂停态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/clc08TIvSPyDwZjUpWTidw/zh-cn_image_0000002583478309.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=F712CB51BA9DF81A9C14CF92A4C711868DA4984980373BF26C39CE60FA7EF0E9)

### 非激活态

即普通卡片状态，在此状态下，卡片与普通卡片行为无异，遵循既有的卡片开发规范，卡片UI由卡片提供方widgetCard.ets中的内容所承载。

**图3** 趣味交互类型互动卡片非激活态

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/-__pFYCOR7W3vQ-sYjNoMQ/zh-cn_image_0000002552798660.jpg?HW-CC-KV=V1&HW-CC-Date=20260427T234133Z&HW-CC-Expire=86400&HW-CC-Sign=8B119214651F6B928FFAC0404DEB32C7257F50B6881A6085A3790E14B7D3A6DE)

## 约束与限制

1. 用户与卡片交互时，例如点击、长按、拖拽等，卡片的交互响应热区始终与卡片自身渲染区域等大。即使动效渲染区域大于卡片自身渲染区域，超出部分也仅做UI呈现，不响应交互事件。
2. 激活态时，卡片自身渲染区域范围内交互事件由卡片提供方开发的卡片小游戏页面响应；其他状态下交互事件由卡片提供方开发的普通卡片响应。
3. 同一时刻，全局只支持一个卡片进行趣味交互，即仅支持一个卡片处于激活态或暂停态。用户点击卡片，切换卡片进入激活态时，其他趣味交互类型互动卡片强制切换为非激活态。
4. 其他设计规范和约束请参考创新互动卡片[开发指导](../quickApp-Guides/quickgame-interact-card-dev-0000002045919412.md)。

## 开发指导

游戏内容具体开发可参考[互动卡片小游戏开发指导](../quickApp-Guides/quickgame-interact-card-dev-0000002045919412.md)。

端侧卡片配置开发可参考[趣味交互类型互动卡片配置](arkts-ui-widget-configuration.md#funinteractionparams标签)。
