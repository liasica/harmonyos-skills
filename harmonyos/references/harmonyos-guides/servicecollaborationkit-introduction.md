---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaborationkit-introduction
title: Service Collaboration Kit简介
breadcrumb: 指南 > 系统 > 网络 > Service Collaboration Kit（协同服务） > Service Collaboration Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:35+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:9d3f23bdb674765f1f99a738a1649333261741524fbdda7ba926b958f05e3db3
---

Service Collaboration Kit（协同服务）提供了多端设备协同的能力。

## 场景介绍

| 场景分类 | 场景说明 |
| --- | --- |
| 跨设备互通场景 | 用户通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。 |
| 碰一碰场景 | 设备间通过顶端碰的方式触发连接、传递信息、断开连接等。 |

## 基本概念

* 跨设备互通通常是指相机、扫描以及图库（图片和视频）能力的跨设备调用，例如：Tablet或PC/2in1设备可以调用Phone的相机、扫描、图库等功能。
* 碰一碰是设备间通过顶端碰的方式触发连接、传递信息、断开连接等。

## 约束与限制

### 支持的设备

| 场景 | Phone | Tablet | 2in1 | Wearable | TV |
| --- | --- | --- | --- | --- | --- |
| 跨设备互通（ArkTS） | 支持 | 支持 | 支持 | 不支持 | 支持 |
| 跨设备互通NDK（C） | 支持 | 支持 | 支持 | 不支持 | 支持 |
| 碰一碰 | 支持 | 不支持 | 不支持 | 不支持 | 不支持 |

### 功能使用限制

| 场景 | 限制条件 |
| --- | --- |
| 跨设备互通 | 1. 双端设备需要登录同一华为账号；双端设备需要打开WLAN和蓝牙开关。  2. 本端需使用HarmonyOS 5及以上版本的Tablet或PC/2in1设备，远端需为具备相机能力的HarmonyOS 5及以上版本的Phone或Tablet。  3. 跨设备互通API支持根据特定调用策略调用设备。调用策略：PC/2in1设备可以调用Tablet和Phone，Tablet可以调用Phone；从API 6.1.0(23)开始，TV、Phone、Tablet或PC/2in1设备可调用具备如下能力的远程设备：支持拍照、扫描及图库（图片与视频）能力的Phone和Tablet，支持图库（图片与视频）能力的PC/2in1设备。  4. 对于6.1.0(23)之前版本，跨设备互通能力的接口在PC/2in1、Tablet可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力；对于6.1.0(23)及之后版本，跨设备互通能力的接口在TV、PC/2in1、Tablet、Phone可正常调用，在其他设备类型上无法展示设备列表，无法使用跨设备互通能力。 |
| 碰一碰 | 1. 双端设备需要打开WLAN和蓝牙开关。  2. 需要申请权限[ohos.permission.KNOCK\_COLLABORATION](restricted-permissions.md#ohospermissionknock_collaboration)，该能力受限开放。权限申请方式请参见[申请使用受限权限](declare-permissions-in-acl.md)。 |

## 模拟器支持情况

本Kit暂不支持模拟器。
