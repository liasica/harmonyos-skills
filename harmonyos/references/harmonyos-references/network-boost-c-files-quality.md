---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-files-quality
title: network_boost_quality.h
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 头文件 > network_boost_quality.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1bad4a2d184958129cc7dd3872a20a75a6c7ebe6bd8ef23c71dc4a940f6c8c29
---

## 概述

PhonePC/2in1Tablet

声明用于网络质量模块的API。提供基本的函数、结构体和const定义。

**引用文件：** <NetworkBoostKit/network\_boost\_quality.h>

**库：** libnetwork\_boost.so

**系统能力：** SystemCapability.Communication.NetworkBoost.Core

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

## 汇总

PhonePC/2in1Tablet

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_NetworkQos](network-boost-c-struct-network_qos.md) | 网络质量回调信息。 |
| struct [NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) | 网络质量变化的详细信息。 |
| struct [NetworkBoost\_WeakSignalPrediction](network-boost-c-struct-weak_signal_prediction.md) | 弱信号预测相关信息。 |
| struct [NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) | 网络场景状态变更回调信息。 |

### 宏定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NETBOOST\_MAX\_PATH\_NUM](network-boost-c-overview.md#netboost_max_path_num) 4 | 网络质量变化的最大路径数量。 |
| [NB\_BPS](network-boost-c-overview.md#nb_bps) 1 | 1bps |
| [NB\_KBPS](network-boost-c-overview.md#nb_kbps) 1000 | 1kbps |
| [NB\_MBPS](network-boost-c-overview.md#nb_mbps) 1000000 | 1mbps |
| [NB\_GBPS](network-boost-c-overview.md#nb_gbps) 1000000000 | 1gbps |
| [NB\_TBPS](network-boost-c-overview.md#nb_tbps) 1000000000000 | 1tbps，请使用uint64\_t类型来避免溢出。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef enum [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction-1) [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction) | 应用数传策略建议。 |
| typedef enum [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype) | 数据路径类型，枚举值。 |
| typedef enum [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene-1) [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene) | 网络场景类型。 |
| typedef enum [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype) | 应用业务类型。 |
| typedef enum [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype) | 应用体验类型。 |
| typedef struct [NetworkBoost\_NetworkQos](network-boost-c-struct-network_qos.md) [NetworkBoost\_NetworkQos](network-boost-c-overview.md#networkboost_networkqos) | 网络质量回调信息。 |
| typedef struct [NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) [NetworkBoost\_NetworkQosArray](network-boost-c-overview.md#networkboost_networkqosarray) | 网络质量变化的详细信息。 |
| typedef struct [NetworkBoost\_WeakSignalPrediction](network-boost-c-struct-weak_signal_prediction.md) [NetworkBoost\_WeakSignalPrediction](network-boost-c-overview.md#networkboost_weaksignalprediction) | 弱信号预测相关信息。 |
| typedef struct [NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) [NetworkBoost\_NetworkScene](network-boost-c-overview.md#networkboost_networkscene) | 网络场景状态变更回调信息。 |
| typedef void(\* [HMS\_NetworkBoost\_NetQosChange](network-boost-c-overview.md#hms_networkboost_netqoschange)) ([NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) \*networkQosArray) | 网络质量变更回调。 |
| typedef void(\* [HMS\_NetworkBoost\_NetSceneChange](network-boost-c-overview.md#hms_networkboost_netscenechange)) ([NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) \*networkScene) | 网络场景状态变更回调。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction-1) {  NB\_ACTION\_DO\_CACHING = 0, NB\_ACTION\_SUSPEND\_DATA = 1, NB\_ACTION\_DECREASE\_DATA = 2, NB\_ACTION\_INCREASE\_DATA = 3,  NB\_ACTION\_KEEP\_DATA = 4  } | 应用数传策略建议。 |
| [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) { NB\_PATH\_CELLULAR\_PRIMARY = 0, NB\_PATH\_CELLULAR\_SECONDARY = 1, NB\_PATH\_WIFI\_PRIMARY = 2, NB\_PATH\_WIFI\_SECONDARY = 3 } | 数据路径类型，枚举值。 |
| [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene-1) { NB\_SCENE\_NORMAL = 0, NB\_SCENE\_CONGESTION = 1, NB\_SCENE\_FREQUENT\_HANDOVER = 2, NB\_SCENE\_WEAK\_SIGNAL = 3 } | 网络场景类型。 |
| [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) {  NB\_SERVICE\_DEFAULT = 0, NB\_SERVICE\_BACKGROUND = 1, NB\_SERVICE\_REAL\_TIME\_VOICE = 2, NB\_SERVICE\_REAL\_TIME\_VIDEO = 3,  NB\_SERVICE\_CALL\_SIGNALING = 4, NB\_SERVICE\_REAL\_TIME\_GAME = 5, NB\_SERVICE\_NORMAL\_GAME = 6, NB\_SERVICE\_SHORT\_VIDEO = 7,  NB\_SERVICE\_LONG\_VIDEO = 8, NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR = 9, NB\_SERVICE\_LIVE\_STREAMING\_WATCHER = 10, NB\_SERVICE\_DOWNLOAD = 11,  NB\_SERVICE\_UPLOAD = 12, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_TRANSACTION = 14, NB\_SERVICE\_DETECTION = 15, NB\_SERVICE\_CLOUDSERVICE = 16, NB\_SERVICE\_VOICE\_CONFERENCE = 17, NB\_SERVICE\_VIDEO\_CONFERENCE = 18, NB\_SERVICE\_NAVIGATION = 19, NB\_SERVICE\_SECKILL\_SERVICE = 20, NB\_SERVICE\_LOGIN = 21, NB\_SERVICE\_AUDIO = 22, NB\_SERVICE\_SHOPPING = 23  } | 应用业务类型。 |
| [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) {  NB\_QOE\_GOOD = 0, NB\_QOE\_BAD\_UNKNOWN = 1, NB\_QOE\_BAD\_SERVER\_ERROR = 2, NB\_QOE\_BAD\_NO\_DATA = 3,  NB\_QOE\_BAD\_PACKET\_LOST = 4, NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER = 5, NB\_QOE\_BAD\_HIGH\_JITTER = 6, NB\_QOE\_BAD\_HIGH\_LATENCY = 7  } | 应用体验类型。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_NetworkBoost\_RegisterNetQosCallback](network-boost-c-overview.md#hms_networkboost_registernetqoscallback) ([HMS\_NetworkBoost\_NetQosChange](network-boost-c-overview.md#hms_networkboost_netqoschange) callback, uint32\_t \*callbackId) | 注册网络质量信息回调。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterNetQosCallback](network-boost-c-overview.md#hms_networkboost_unregisternetqoscallback) (uint32\_t callbackId) | 取消注册网络质量信息回调。 |
| int32\_t [HMS\_NetworkBoost\_RegisterNetSceneCallback](network-boost-c-overview.md#hms_networkboost_registernetscenecallback) ([HMS\_NetworkBoost\_NetSceneChange](network-boost-c-overview.md#hms_networkboost_netscenechange) callback, uint32\_t \*callbackId) | 注册网络场景变化信息回调。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterNetSceneCallback](network-boost-c-overview.md#hms_networkboost_unregisternetscenecallback) (uint32\_t callbackId) | 取消注册网络场景变化信息回调。 |
| int32\_t [HMS\_NetworkBoost\_ReportQoe](network-boost-c-overview.md#hms_networkboost_reportqoe) ([NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) serviceType, [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) qoeType) | 应用传输体验反馈。 |
