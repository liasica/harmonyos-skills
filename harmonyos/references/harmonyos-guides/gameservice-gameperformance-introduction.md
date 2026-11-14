---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-introduction
title: 概述
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:17+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4a9da17849f837647703c4aa510b03c1123c899cb3ec929468c553b97d8ff6fe
---

## 功能说明

从5.0.0(12)版本开始，新增游戏场景感知服务。从6.0.2(22)版本开始，游戏场景感知服务C API支持返回CPU性能信息及建议工作电流等信息。从API版本26.0.1开始，游戏场景感知服务支持传入触控区域优化游戏跟手性。

游戏场景感知提供API接口，帮助开发者快速实现游戏与系统的交互，开发者通过游戏场景感知，可以完成向系统发送游戏信息以及从系统获取设备状态信息两大动作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/BEScHoDtT4eRgslsKoyjbA/zh-cn_image_0000002817427389.jpg?HW-CC-KV=V1&HW-CC-Date=20261114T004817Z&HW-CC-Expire=31536000000&HW-CC-Sign=F2A732BF136C99C8FE9F9F8975881B066F191398B0719ED5EA6D7961FAB2CE29)

## 场景介绍

游戏场景感知主要服务于游戏场景优化，其特点是可以通过感知游戏场景和运行状态的不同，使用不同策略调度系统资源以达到更精细化的优化效果。
