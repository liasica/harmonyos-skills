---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-controller-introduction
title: Game Controller Kit简介
breadcrumb: 指南 > 应用服务 > Game Controller Kit（游戏控制器服务） > Game Controller Kit简介
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ca225f399a038fd960bda01fb73ca4df4745607e5d3b95f5a4e2f14620b25b71
---

Game Controller Kit（游戏控制器服务）支持游戏适配控制器外设（当前仅支持手柄），解决玩家操控性问题，保障用户体验。游戏开发者可通过接入该服务轻松实现游戏外设的上下线和按键及轴事件监听等功能。

## 能力范围

Game Controller Kit支持的能力包括：

* 监听设备上下线，查询所有在线设备的具体信息
* 监听游戏手柄的轴和按键事件

## 约束与限制

### 支持的设备

支持Phone、PC/2in1、Tablet、TV

### 支持的国家/地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

## 模拟器支持情况

当前模拟器支持Phone、PC/2in1、Tablet。

由于模拟器无法连接手柄，仅支持接口调用，因此模拟器暂不支持验证手柄事件和设备事件的回调。
