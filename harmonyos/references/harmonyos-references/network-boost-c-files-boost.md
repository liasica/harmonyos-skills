---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost
title: network_boost.h
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 头文件 > network_boost.h
category: harmonyos-references
scraped_at: 2026-09-02T14:52:23+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf9a86075cc9a3916ebdce5f3f9783bd6c3235cd9de0547a8015105f417202ef
---

## 概述

声明用于网络加速的API。提供基本的函数、结构体和const定义。

**引用文件：** <NetworkBoostKit/network\_boost.h>

**库：** libnetwork\_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

## 汇总

## 结构体

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) | 业务场景描述信息。 |

## 枚举

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_SceneEvent](network-boost-c-overview.md#networkboost_sceneevent){  NB\_SCENE\_EVENT\_ENTER = 0, NB\_SCENE\_EVENT\_UPDATE = 1, NB\_SCENE\_EVENT\_LEAVE = 2  } | 业务事件枚举。 |

## 函数

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_NetworkBoost\_SetSceneDesc](network-boost-c-overview.md#hms_networkboost_setscenedesc)([NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) sceneDesc) | 设置业务场景。 |
