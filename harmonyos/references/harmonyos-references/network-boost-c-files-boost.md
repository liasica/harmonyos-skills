---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-boost
title: network_boost.h
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 头文件 > network_boost.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5121591b156ff6340f7f581ceb82eb50fbe4fc7d1ed3f81b366fda496246688d
---

## 概述

PhonePC/2in1Tablet

声明用于网络加速的API。提供基本的函数、结构体和const定义。

**引用文件：** <NetworkBoostKit/network\_boost.h>

**库：** libnetwork\_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

## 汇总

PhonePC/2in1Tablet

## 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) | 业务场景描述信息。 |

## 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_SceneEvent](network-boost-c-overview.md#networkboost_sceneevent){  SCENE\_EVENT\_ENTER = 0, SCENE\_EVENT\_UPDATE = 1, SCENE\_EVENT\_LEAVE = 2  } | 业务事件枚举。 |

## 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_NetworkBoost\_SetSceneDesc](network-boost-c-overview.md#hms_networkboost_setscenedesc)([NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) sceneDesc) | 设置业务场景。 |
