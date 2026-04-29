---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ringtone-introduction
title: Ringtone Kit简介
breadcrumb: 指南 > 媒体 > Ringtone Kit（铃声服务） > Ringtone Kit简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ca250126ec3dac9e82cc19fd7cbb35ddd17ff2c4b42ff8f6d22bb0b0af46246d
---

Ringtone Kit（铃声服务）是一个用于设置铃声的工具库。通过使用Ringtone Kit，开发者可以在HarmonyOS应用中提供铃声设置的功能，为用户提供简单一致、安全高品质的铃声设置体验。

## 场景介绍

Ringtone Kit支持将音频文件设置成多种铃声类型，满足各类铃声需求场景。

* 多种铃声类型：可设置来电铃声、通知铃声、信息铃声、闹钟铃声。
* 支持双卡铃声：可对双卡分别设置不同来电铃声和信息铃声。
* 铃声快捷管理：点击我的铃声按钮快速跳转“设置-声音与振动”管理铃声。

铃声设置组件效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/h_99r260RyG_XVFNDcc-Aw/zh-cn_image_0000002558765110.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053538Z&HW-CC-Expire=86400&HW-CC-Sign=D4241EC9585FFA295B6E6AE58285CF7B097EA5C3B7E600452566C50D6617DA4E "点击放大")

## 约束与限制

### 支持的国家/地区

当前仅支持在中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）提供服务。

### 支持的设备

本示例仅支持标准系统上运行，支持设备：Phone，Tablet。

### 使用限制

当不满足所需条件时，部分功能不可使用：

* 当HarmonyOS设备无SIM卡槽时，来电铃声和信息铃声设置功能将不可用。
* 设置的铃声最大时长为5分钟。

## 模拟器支持情况

本Kit支持模拟器。

模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md)”。
