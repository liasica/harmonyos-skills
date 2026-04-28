---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-network_scene
title: NetworkBoost_NetworkScene
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_NetworkScene
category: harmonyos-references
scraped_at: 2026-04-28T08:08:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f44dc5f8e66f766e41099e2e4d84438cfce900890e1aed934725af5f975ab949
---

## 概述

PhonePC/2in1Tablet

网络场景状态变更回调信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](network-boost-c-files-quality.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) [pathType](network-boost-c-struct-network_scene.md#pathtype) | 表明相应的数据路径上的网络场景信息。 |
| [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene-1) [scene](network-boost-c-struct-network_scene.md#scene) | 网络场景类型。 |
| [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction-1) [recommendedAction](network-boost-c-struct-network_scene.md#recommendedaction) | 建议的数传策略。 |
| [NetworkBoost\_WeakSignalPrediction](network-boost-c-struct-weak_signal_prediction.md) [weakSignalPrediction](network-boost-c-struct-network_scene.md#weaksignalprediction) | 弱信号预测相关信息。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### pathType

PhonePC/2in1Tablet

```
1. NetworkBoost_PathType NetworkBoost_NetworkScene::pathType
```

**描述**

表明相应的数据路径上的网络场景信息。

### recommendedAction

PhonePC/2in1Tablet

```
1. NetworkBoost_RecommendedAction NetworkBoost_NetworkScene::recommendedAction
```

**描述**

建议的数传策略。

### scene

PhonePC/2in1Tablet

```
1. NetworkBoost_Scene NetworkBoost_NetworkScene::scene
```

**描述**

网络场景类型。

### weakSignalPrediction

PhonePC/2in1Tablet

```
1. NetworkBoost_WeakSignalPrediction NetworkBoost_NetworkScene::weakSignalPrediction
```

**描述**

弱信号预测相关信息。
