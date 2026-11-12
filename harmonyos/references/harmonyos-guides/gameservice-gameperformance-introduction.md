---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-introduction
title: 概述
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 概述
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:bd4e5c77c39d9056a5d3c4a95e30ba66bf7529b93c67c5c229836d9050e30894
---

## 功能说明

从5.0.0(12)版本开始，新增游戏场景感知服务。从6.0.2(22)版本开始，游戏场景感知服务C API支持返回CPU性能信息及建议工作电流等信息。从API版本26.0.1开始，游戏场景感知服务支持传入触控区域优化游戏跟手性。

游戏场景感知提供API接口，帮助开发者快速实现游戏与系统的交互，开发者通过游戏场景感知，可以完成向系统发送游戏信息以及从系统获取设备状态信息两大动作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/t6VDolNpSFq9PmlXfSoJMg/zh-cn_image_0000002786360294.jpg?HW-CC-KV=V1&HW-CC-Date=20261112T233230Z&HW-CC-Expire=31536000000&HW-CC-Sign=7D9CC1C14DAFC66FA617F731C84429E26370B6423AD1A710ABAC1596EBD1CBF8)

## 场景介绍

游戏场景感知主要服务于游戏场景优化，其特点是可以通过感知游戏场景和运行状态的不同，使用不同策略调度系统资源以达到更精细化的优化效果。
