---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-introduction
title: 概述
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 概述
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b97a0499d7cd84e87d862c58862f14aae576667f89678c2f2d58917e3debbd18
---

## 功能说明

从5.0.0(12)版本开始，新增游戏场景感知服务。从6.0.2(22)版本开始，游戏场景感知服务C API支持返回CPU性能信息及建议工作电流等信息。从API版本26.0.1开始，游戏场景感知服务支持传入触控区域优化游戏跟手性。

游戏场景感知提供API接口，帮助开发者快速实现游戏与系统的交互，开发者通过游戏场景感知，可以完成向系统发送游戏信息以及从系统获取设备状态信息两大动作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/9ToVgh8uRSysM42kityXMw/zh-cn_image_0000002821837915.jpg?HW-CC-KV=V1&HW-CC-Date=20261121T011223Z&HW-CC-Expire=31536000000&HW-CC-Sign=B019CDD438334AF035252E9A03F8E9175F1780577A61346A2574D82089DDC74F)

## 场景介绍

游戏场景感知主要服务于游戏场景优化，其特点是可以通过感知游戏场景和运行状态的不同，使用不同策略调度系统资源以达到更精细化的优化效果。
