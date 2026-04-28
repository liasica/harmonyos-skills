---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-overview
title: NetworkBoost
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 模块 > NetworkBoost
category: harmonyos-references
scraped_at: 2026-04-28T08:08:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e17b3c40d80c2dfe52ab63f8c2620450b600a6ba62f1179514b7f69bb52d06ee
---

## 概述

PhonePC/2in1Tablet

提供网络质量与网络连接迁移相关接口。

* 网络质量模块提供网络质量实时评估、网络场景识别以及弱信号预测等能力，以便应用针对弱网等环境下实现网络自适应，包括缓存、码率、帧率、分辨率等策略的调整。应用也可以通过网络质量中的应用传输体验反馈接口，触发系统进行网络加速。
* 连接迁移模块提供网络连接迁移能力，以便在弱网环境下，系统发起多网迁移（Wi-Fi<->蜂窝，主卡<->副卡等）的过程中，给应用提供连接迁移开始和完成通知，应用根据连接迁移通知的建议进行重建，快速恢复业务，给用户带来平滑、高速、低时延的上网体验。
* 多网并发是系统提供接口可以建立多个网络通路，应用发起多网请求后，系统依据业务场景决定并发组合和实施相应的并发管控，并对并发做收益度量。使用多网并发功能的原则是应用申请（受限权限）、系统管控、最小化使用。

**起始版本：** 5.1.0(18)

## 汇总

PhonePC/2in1Tablet

### 文件

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [network\_boost\_handover.h](network-boost-c-files-handover.md) | 声明用于连接迁移的API。提供基本的函数，结构体和const定义。 |
| [network\_boost\_quality.h](network-boost-c-files-quality.md) | 声明用于网络质量的API。提供基本的函数，结构体和const定义。 |
| [network\_boost.h](network-boost-c-files-boost.md) | 声明用于网络加速的API。提供基本的函数，结构体和const定义。 |

### 结构体

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| struct [NetworkBoost\_DataSpeedAction](network-boost-c-struct-data_speed_action.md) | 发包速率建议。 |
| struct [NetworkBoost\_NetHandle](network-boost-c-struct-net_handle.md) | NetHandle信息。 |
| struct [NetworkBoost\_HandoverStart](network-boost-c-struct-handover_start.md) | 连接迁移开始信息。 |
| struct [NetworkBoost\_HandoverComplete](network-boost-c-struct-handover_complete.md) | 连接迁移完成信息。 |
| struct [HMS\_NetworkBoost\_HandoverCallback](network-boost-c-struct-handover_callback.md) | 连接迁移回调信息。 |
| struct [NetworkBoost\_NetworkQos](network-boost-c-struct-network_qos.md) | 单条路径的网络质量回调信息。 |
| struct [NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) | 多条路径的网络质量回调信息。 |
| struct [NetworkBoost\_WeakSignalPrediction](network-boost-c-struct-weak_signal_prediction.md) | 弱信号预测相关信息。 |
| struct [NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) | 网络场景状态变更回调信息。 |
| struct [NetworkBoost\_MultiPathQuotaInfo](network-boost-c-struct-multipath_quotainfo.md) | 配额信息。 |
| struct [NetworkBoost\_MultiPathQuota](network-boost-c-struct-multipath_quota.md) | 应用配额使用信息。 |
| struct [NetworkBoost\_MultiPathRequestResult](network-boost-c-struct-multipath_req_result.md) | 多网请求结果。 |
| struct [NetworkBoost\_MultiPathStateChange](network-boost-c-struct-multipath_statechange.md) | 多网状态信息。 |
| struct [NetworkBoost\_MultiPathRecommendation](network-boost-c-struct-multipath_reco.md) | 多网推荐信息。 |
| struct [NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) | 业务场景描述信息。 |

### 宏定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NETBOOST\_MAX\_PATH\_NUM](network-boost-c-overview.md#netboost_max_path_num) 4 | 网络质量变化信息的最大路径数量。 |
| [NB\_BPS](network-boost-c-overview.md#nb_bps) 1 | 1bps |
| [NB\_KBPS](network-boost-c-overview.md#nb_kbps) 1000 | 1kbps |
| [NB\_MBPS](network-boost-c-overview.md#nb_mbps) 1000000 | 1mbps |
| [NB\_GBPS](network-boost-c-overview.md#nb_gbps) 1000000000 | 1gbps |
| [NB\_TBPS](network-boost-c-overview.md#nb_tbps) 1000000000000 | 1tbps，请使用uint64\_t类型来避免溢出。 |

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef enum [NetworkBoost\_DataSpeedSimpleAction](network-boost-c-overview.md#networkboost_dataspeedsimpleaction-1) [NetworkBoost\_DataSpeedSimpleAction](network-boost-c-overview.md#networkboost_dataspeedsimpleaction) | 应用发包策略的建议。 |
| typedef enum [NetworkBoost\_ErrorResult](network-boost-c-overview.md#networkboost_errorresult-1) [NetworkBoost\_ErrorResult](network-boost-c-overview.md#networkboost_errorresult) | 连接迁移结果枚举。 |
| typedef enum [NetworkBoost\_ReEstAction](network-boost-c-overview.md#networkboost_reestaction-1) [NetworkBoost\_ReEstAction](network-boost-c-overview.md#networkboost_reestaction) | 重建枚举。 |
| typedef struct [NetworkBoost\_DataSpeedAction](network-boost-c-struct-data_speed_action.md) [NetworkBoost\_DataSpeedAction](network-boost-c-overview.md#networkboost_dataspeedaction) | 发包速率建议。 |
| typedef struct [NetworkBoost\_NetHandle](network-boost-c-struct-net_handle.md) [NetworkBoost\_NetHandle](network-boost-c-overview.md#networkboost_nethandle) | NetHandle信息。 |
| typedef struct [NetworkBoost\_HandoverStart](network-boost-c-struct-handover_start.md) [NetworkBoost\_HandoverStart](network-boost-c-overview.md#networkboost_handoverstart) | 连接迁移开始信息。 |
| typedef struct [NetworkBoost\_HandoverComplete](network-boost-c-struct-handover_complete.md) [NetworkBoost\_HandoverComplete](network-boost-c-overview.md#networkboost_handovercomplete) | 连接迁移完成信息。 |
| typedef enum [NetworkBoost\_HandoverMode](network-boost-c-overview.md#networkboost_handovermode-1) [NetworkBoost\_HandoverMode](network-boost-c-overview.md#networkboost_handovermode) | 连接迁移模式枚举。 |
| typedef void(\* [HMS\_NetworkBoost\_OnHandoverStart](network-boost-c-overview.md#hms_networkboost_onhandoverstart)) ([NetworkBoost\_HandoverStart](network-boost-c-struct-handover_start.md) \*handoverStart) | 连接迁移开始的回调函数原型。 |
| typedef void(\* [HMS\_NetworkBoost\_OnHandoverComplete](network-boost-c-overview.md#hms_networkboost_onhandovercomplete)) ([NetworkBoost\_HandoverComplete](network-boost-c-struct-handover_complete.md) \*handoverComplete) | 连接迁移结束的回调函数原型。 |
| typedef struct [HMS\_NetworkBoost\_HandoverCallback](network-boost-c-struct-handover_callback.md) [HMS\_NetworkBoost\_HandoverCallback](network-boost-c-overview.md#hms_networkboost_handovercallback) | 连接迁移回调注册函数的参数，包含连接迁移开始和完成的回调函数。 |
| typedef enum [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction-1) [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction) | 应用数传策略建议。 |
| typedef enum [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype) | 数据路径类型，枚举值。 |
| typedef enum [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene-1) [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene) | 网络场景类型。 |
| typedef enum [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype) | 应用业务类型。 |
| typedef enum [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype) | 应用体验类型。 |
| typedef struct [NetworkBoost\_NetworkQos](network-boost-c-struct-network_qos.md) [NetworkBoost\_NetworkQos](network-boost-c-overview.md#networkboost_networkqos) | 单条路径的网络质量回调信息。 |
| typedef struct [NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) [NetworkBoost\_NetworkQosArray](network-boost-c-overview.md#networkboost_networkqosarray) | 多条路径的网络质量回调信息。 |
| typedef struct [NetworkBoost\_WeakSignalPrediction](network-boost-c-struct-weak_signal_prediction.md) [NetworkBoost\_WeakSignalPrediction](network-boost-c-overview.md#networkboost_weaksignalprediction) | 弱信号预测相关信息。 |
| typedef struct [NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) [NetworkBoost\_NetworkScene](network-boost-c-overview.md#networkboost_networkscene) | 网络场景状态变更回调信息。 |
| typedef void(\* [HMS\_NetworkBoost\_NetQosChange](network-boost-c-overview.md#hms_networkboost_netqoschange)) ([NetworkBoost\_NetworkQosArray](network-boost-c-struct-network_qos_array.md) \*networkQosArray) | 网络质量变更回调函数原型。 |
| typedef void(\* [HMS\_NetworkBoost\_NetSceneChange](network-boost-c-overview.md#hms_networkboost_netscenechange)) ([NetworkBoost\_NetworkScene](network-boost-c-struct-network_scene.md) \*networkScene) | 网络场景状态变更回调函数原型。 |
| typedef void (\* [HMS\_NetworkBoost\_OnMultiPathRequestResult](network-boost-c-overview.md#hms_networkboost_onmultipathrequestresult))([NetworkBoost\_MultiPathRequestResult](network-boost-c-struct-multipath_req_result.md)\* result) | 多网请求结果回调函数原型。 |
| typedef void (\* [HMS\_NetworkBoost\_OnMultiPathStateChange](network-boost-c-overview.md#hms_networkboost_onmultipathstatechange))([NetworkBoost\_MultiPathStateChange](network-boost-c-struct-multipath_statechange.md)\* multiPathState) | 多网状态变化回调函数原型。 |
| typedef void (\* [HMS\_NetworkBoost\_OnMultiPathRecommendation](network-boost-c-overview.md#hms_networkboost_onmultipathrecommendation))([NetworkBoost\_MultiPathRecommendation](network-boost-c-struct-multipath_reco.md)\* recommendation) | 系统多网建议变化回调函数原型。 |

### 枚举

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_DataSpeedSimpleAction](network-boost-c-overview.md#networkboost_dataspeedsimpleaction-1) { NB\_SIMPLEACTION\_SUSPEND\_DATA = 1, NB\_SIMPLEACTION\_DECREASE\_DATA = 2, NB\_SIMPLEACTION\_INCREASE\_DATA = 3, NB\_SIMPLEACTION\_KEEP\_DATA = 4 } | 应用发包策略的建议。 |
| [NetworkBoost\_ErrorResult](network-boost-c-overview.md#networkboost_errorresult-1) { NB\_ERROR\_NONE = 0, NB\_ERROR\_HANDOVER\_TIMEOUT = 1, NB\_ERROR\_NEW\_PATH\_ACTIVATION\_FAILED = 2, NB\_ERROR\_ABORT = 3 } | 连接迁移结果枚举。 |
| [NetworkBoost\_ReEstAction](network-boost-c-overview.md#networkboost_reestaction-1) {  NB\_REEST\_DEFAULT = 0, NB\_REEST\_QUERY\_DNS = 1, NB\_REEST\_CHANGE\_REMOTE\_IP = 2, NB\_REEST\_CHANGE\_IP\_VERSION = 3,  NB\_NO\_EST = 4  } | 重建枚举。 |
| [NetworkBoost\_HandoverMode](network-boost-c-overview.md#networkboost_handovermode-1) { NB\_MODE\_DELEGATION = 0, NB\_MODE\_DISCRETION = 1 } | 连接迁移模式枚举。 |
| [NetworkBoost\_RecommendedAction](network-boost-c-overview.md#networkboost_recommendedaction-1) {  NB\_ACTION\_DO\_CACHING = 0, NB\_ACTION\_SUSPEND\_DATA = 1, NB\_ACTION\_DECREASE\_DATA = 2, NB\_ACTION\_INCREASE\_DATA = 3,  NB\_ACTION\_KEEP\_DATA = 4  } | 应用数传策略建议。 |
| [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype-1) { NB\_PATH\_CELLULAR\_PRIMARY = 0, NB\_PATH\_CELLULAR\_SECONDARY = 1, NB\_PATH\_WIFI\_PRIMARY = 2, NB\_PATH\_WIFI\_SECONDARY = 3 } | 数据路径类型，枚举值。 |
| [NetworkBoost\_Scene](network-boost-c-overview.md#networkboost_scene-1) { NB\_SCENE\_NORMAL = 0, NB\_SCENE\_CONGESTION = 1, NB\_SCENE\_FREQUENT\_HANDOVER = 2, NB\_SCENE\_WEAK\_SIGNAL = 3 } | 网络场景类型。 |
| [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) {  NB\_SERVICE\_DEFAULT = 0, NB\_SERVICE\_BACKGROUND = 1, NB\_SERVICE\_REAL\_TIME\_VOICE = 2, NB\_SERVICE\_REAL\_TIME\_VIDEO = 3,  NB\_SERVICE\_CALL\_SIGNALING = 4, NB\_SERVICE\_REAL\_TIME\_GAME = 5, NB\_SERVICE\_NORMAL\_GAME = 6, NB\_SERVICE\_SHORT\_VIDEO = 7,  NB\_SERVICE\_LONG\_VIDEO = 8, NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR = 9, NB\_SERVICE\_LIVE\_STREAMING\_WATCHER = 10, NB\_SERVICE\_DOWNLOAD = 11,  NB\_SERVICE\_UPLOAD = 12, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_BROWSER = 13, NB\_SERVICE\_TRANSACTION = 14, NB\_SERVICE\_DETECTION = 15, NB\_SERVICE\_CLOUDSERVICE = 16, NB\_SERVICE\_VOICE\_CONFERENCE = 17, NB\_SERVICE\_VIDEO\_CONFERENCE = 18, NB\_SERVICE\_NAVIGATION = 19, NB\_SERVICE\_SECKILL\_SERVICE = 20, NB\_SERVICE\_LOGIN = 21, NB\_SERVICE\_AUDIO = 22, NB\_SERVICE\_SHOPPING = 23  } | 应用业务类型。 |
| [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) {  NB\_QOE\_GOOD = 0, NB\_QOE\_BAD\_UNKNOWN = 1, NB\_QOE\_BAD\_SERVER\_ERROR = 2, NB\_QOE\_BAD\_NO\_DATA = 3,  NB\_QOE\_BAD\_PACKET\_LOST = 4, NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER = 5, NB\_QOE\_BAD\_HIGH\_JITTER = 6, NB\_QOE\_BAD\_HIGH\_LATENCY = 7  } | 应用体验类型。 |
| [NetworkBoost\_PathState](network-boost-c-overview.md#networkboost_pathstate) {  NB\_PATH\_IDLE = 0，NB\_PATH\_CONNECTED = 1，NB\_PATH\_SUSPENDED = 2  } | 多网链路状态的枚举。 |
| [NetworkBoost\_MultiPathErrorResult](network-boost-c-overview.md#networkboost_multipatherrorresult) {  NB\_MULTIPATH\_ERROR\_NONE = 0，NB\_MULTIPATH\_ERROR\_NETWORK\_REFUSED = 1， NB\_MULTIPATH\_ERROR\_TIMEOUT = 2， NB\_MULTIPATH\_ERROR\_LOCAL = 3  } | 多网建立结果的枚举。 |
| [NetworkBoost\_MultiPathChangeCause](network-boost-c-overview.md#networkboost_multipathchangecause) {  NB\_MULTIPATH\_CAUSE\_REQUEST\_NORMAL = 0, NB\_MULTIPATH\_CAUSE\_RELEASE\_NORMAL = 50, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK = 51, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED = 52, NB\_MULTIPATH\_CAUSE\_RELEASE\_NO\_QUOTA = 53, NB\_MULTIPATH\_CAUSE\_RELEASE\_POWER\_CONSUMPTION = 54, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC = 55, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT = 56, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING = 57, NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT = 99, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER = 100, NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE = 101, NB\_MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE = 102  } | 多网变化原因的枚举。 |
| [NetworkBoost\_MultiPathState](network-boost-c-overview.md#networkboost_multipathstate) {  NB\_MULTIPATH\_IDLE = 0, NB\_MULTIPATH\_CREATEING = 1, NB\_MULTIPATH\_CREATED = 2, NB\_MULTIPATH\_RELEASING = 3  } | 多网状态的枚举。 |
| [NetworkBoost\_MultiPathAction](network-boost-c-overview.md#networkboost_multipathaction) {  NB\_MULTIPATH\_ACTION\_REQUEST = 0， NB\_MULTIPATH\_ACTION\_RELEASE = 1  } | 多网推荐动作的枚举。 |
| [NetworkBoost\_SceneEvent](network-boost-c-overview.md#networkboost_sceneevent) {  NB\_SCENE\_EVENT\_ENTER = 0， NB\_SCENE\_EVENT\_UPDATE = 1，NB\_SCENE\_EVENT\_LEAVE = 2  } | 业务事件枚举。 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_NetworkBoost\_RegisterHandoverChangeCallback](network-boost-c-overview.md#hms_networkboost_registerhandoverchangecallback) ([HMS\_NetworkBoost\_HandoverCallback](network-boost-c-struct-handover_callback.md) \*callback, uint32\_t \*callbackId) | 注册连接迁移回调。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterHandoverChangeCallback](network-boost-c-overview.md#hms_networkboost_unregisterhandoverchangecallback) (uint32\_t callbackId) | 取消注册连接迁移回调。 |
| int32\_t [HMS\_NetworkBoost\_SetHandoverMode](network-boost-c-overview.md#hms_networkboost_sethandovermode) ([NetworkBoost\_HandoverMode](network-boost-c-overview.md#networkboost_handovermode-1) mode) | 应用可通过该接口变更连接迁移模式，包括委托模式(由系统发起连接迁移)，和自主模式(由应用发起连接迁移)，默认为委托模式。 |
| int32\_t [HMS\_NetworkBoost\_RegisterNetQosCallback](network-boost-c-overview.md#hms_networkboost_registernetqoscallback) ([HMS\_NetworkBoost\_NetQosChange](network-boost-c-overview.md#hms_networkboost_netqoschange) callback, uint32\_t \*callbackId) | 注册网络质量变化回调。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterNetQosCallback](network-boost-c-overview.md#hms_networkboost_unregisternetqoscallback) (uint32\_t callbackId) | 取消注册网络质量变化回调。 |
| int32\_t [HMS\_NetworkBoost\_RegisterNetSceneCallback](network-boost-c-overview.md#hms_networkboost_registernetscenecallback) ([HMS\_NetworkBoost\_NetSceneChange](network-boost-c-overview.md#hms_networkboost_netscenechange) callback, uint32\_t \*callbackId) | 注册网络场景变化回调。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterNetSceneCallback](network-boost-c-overview.md#hms_networkboost_unregisternetscenecallback) (uint32\_t callbackId) | 取消注册网络场景变化回调。 |
| int32\_t [HMS\_NetworkBoost\_ReportQoe](network-boost-c-overview.md#hms_networkboost_reportqoe) ([NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype-1) serviceType, [NetworkBoost\_QoeType](network-boost-c-overview.md#networkboost_qoetype-1) qoeType) | 应用传输体验反馈。 |
| int32\_t [HMS\_NetworkBoost\_GetMultiPathQuotaStats](network-boost-c-overview.md#hms_networkboost_getmultipathquotastats)([NetworkBoost\_MultiPathQuota](network-boost-c-struct-multipath_quota.md) \*quota) | 获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。 |
| int32\_t [HMS\_NetworkBoost\_RequestMultiPath](network-boost-c-overview.md#hms_networkboost_requestmultipath)([HMS\_NetworkBoost\_OnMultiPathRequestResult](network-boost-c-struct-multipath_req_result.md) result) | 发起多网请求。 |
| int32\_t [HMS\_NetworkBoost\_ReleaseMultiPath](network-boost-c-overview.md#hms_networkboost_releasemultipath)() | 释放多网请求。 |
| int32\_t [HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback](network-boost-c-overview.md#hms_networkboost_registermultipathstatechangecallback)([HMS\_NetworkBoost\_OnMultiPathStateChange](network-boost-c-overview.md#hms_networkboost_onmultipathstatechange) callback, uint32\_t\* callbackId) | 注册多网状态变化事件。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback](network-boost-c-overview.md#hms_networkboost_unregistermultipathstatechangecallback)(uint32\_t callbackId) | 去注册多网状态变化事件。 |
| int32\_t [HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback](network-boost-c-overview.md#hms_networkboost_registermultipathrecommendationcallback)([HMS\_NetworkBoost\_OnMultiPathRecommendation](network-boost-c-overview.md#hms_networkboost_onmultipathrecommendation) callback, uint32\_t\* callbackId) | 注册系统多网建议变化事件。 |
| int32\_t [HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback](network-boost-c-overview.md#hms_networkboost_unregistermultipathrecommendationcallback)(uint32\_t callbackId) | 去系统多网建议变化事件。 |
| int32\_t [HMS\_NetworkBoost\_SetSceneDesc](network-boost-c-overview.md#hms_networkboost_setscenedesc)([NetworkBoost\_SceneDesc](network-boost-c-struct-scene_desc.md) sceneDesc) | 设置业务场景。 |

## 宏定义说明

PhonePC/2in1Tablet

### NB\_BPS

PhonePC/2in1Tablet

```
1. #define NB_BPS   1
```

**描述**

1bps

**起始版本：** 5.1.0(18)

### NB\_GBPS

PhonePC/2in1Tablet

```
1. #define NB_GBPS   1000000000
```

**描述**

1gbps

**起始版本：** 5.1.0(18)

### NB\_KBPS

PhonePC/2in1Tablet

```
1. #define NB_KBPS   1000
```

**描述**

1kbps

**起始版本：** 5.1.0(18)

### NB\_MBPS

PhonePC/2in1Tablet

```
1. #define NB_MBPS   1000000
```

**描述**

1mbps

**起始版本：** 5.1.0(18)

### NB\_TBPS

PhonePC/2in1Tablet

```
1. #define NB_TBPS   1000000000000
```

**描述**

1tbps。请使用uint64\_t类型来避免溢出。

**起始版本：** 5.1.0(18)

### NETBOOST\_MAX\_PATH\_NUM

PhonePC/2in1Tablet

```
1. #define NETBOOST_MAX_PATH_NUM   4
```

**描述**

网络质量变化的详细信息数组的最大长度值。

**起始版本：** 5.1.0(18)

## 类型定义说明

PhonePC/2in1Tablet

### HMS\_NetworkBoost\_HandoverCallback

PhonePC/2in1Tablet

```
1. typedef struct HMS_NetworkBoost_HandoverCallback HMS_NetworkBoost_HandoverCallback
```

**描述**

连接迁移回调信息。回调中的每个方法都不能为空。

**起始版本：** 5.1.0(18)

### HMS\_NetworkBoost\_NetQosChange

PhonePC/2in1Tablet

```
1. typedef void(* HMS_NetworkBoost_NetQosChange) (NetworkBoost_NetworkQosArray *networkQosArray)
```

**描述**

回调函数，返回网络质量变化的详细信息。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| networkQosArray | 网络质量变化的详细信息 |

### HMS\_NetworkBoost\_NetSceneChange

PhonePC/2in1Tablet

```
1. typedef void(* HMS_NetworkBoost_NetSceneChange) (NetworkBoost_NetworkScene *networkScene)
```

**描述**

回调函数，返回网络场景变化的详细信息。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| networkScene | 网络场景变化的详细信息 |

### HMS\_NetworkBoost\_OnHandoverComplete

PhonePC/2in1Tablet

```
1. typedef void(* HMS_NetworkBoost_OnHandoverComplete) (NetworkBoost_HandoverComplete *handoverComplete)
```

**描述**

回调函数，返回连接迁移完成变化的详细信息。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| handoverComplete | 连接迁移完成的详细信息 |

### HMS\_NetworkBoost\_OnHandoverStart

PhonePC/2in1Tablet

```
1. typedef void(* HMS_NetworkBoost_OnHandoverStart) (NetworkBoost_HandoverStart *handoverStart)
```

**描述**

回调函数，返回连接迁移开始的详细信息。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| handoverStart | 连接迁移开始的详细信息 |

### HMS\_NetworkBoost\_OnMultiPathRequestResult

PhonePC/2in1Tablet

```
1. typedef void (*HMS_NetworkBoost_OnMultiPathRequestResult)(NetworkBoost_MultiPathRequestResult* result)
```

**描述**

多网请求结果回调原型。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 发起多网的结果。 |

### HMS\_NetworkBoost\_OnMultiPathStateChange

PhonePC/2in1Tablet

```
1. typedef void (*HMS_NetworkBoost_OnMultiPathStateChange)(NetworkBoost_MultiPathStateChange* multiPathState)
```

**描述**

多网状态变化回调原型。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| multiPathState | 多网状态信息。 |

### HMS\_NetworkBoost\_OnMultiPathRecommendation

PhonePC/2in1Tablet

```
1. typedef void (*HMS_NetworkBoost_OnMultiPathRecommendation)(NetworkBoost_MultiPathRecommendation* recommendation)
```

**描述**

多网推荐信息变化回调原型。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| recommendation | 多网推荐信息。 |

### NetworkBoost\_DataSpeedAction

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_DataSpeedAction NetworkBoost_DataSpeedAction
```

**描述**

发包速率建议。

**起始版本：** 5.1.0(18)

### NetworkBoost\_DataSpeedSimpleAction

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedSimpleAction
```

**描述**

应用发包策略的建议。

**起始版本：** 5.1.0(18)

### NetworkBoost\_ErrorResult

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_ErrorResult NetworkBoost_ErrorResult
```

**描述**

连接迁移结果。

**起始版本：** 5.1.0(18)

### NetworkBoost\_HandoverComplete

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_HandoverComplete NetworkBoost_HandoverComplete
```

**描述**

连接迁移完成信息。

**起始版本：** 5.1.0(18)

### NetworkBoost\_HandoverMode

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_HandoverMode NetworkBoost_HandoverMode
```

**描述**

连接迁移模式。

**起始版本：** 5.1.0(18)

### NetworkBoost\_HandoverStart

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_HandoverStart NetworkBoost_HandoverStart
```

**描述**

连接迁移开始信息。

**起始版本：** 5.1.0(18)

### NetworkBoost\_NetHandle

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_NetHandle NetworkBoost_NetHandle
```

**描述**

数据网络的句柄。

**起始版本：** 5.1.0(18)

### NetworkBoost\_NetworkQos

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_NetworkQos NetworkBoost_NetworkQos
```

**描述**

单条路径的网络质量回调信息。

**起始版本：** 5.1.0(18)

### NetworkBoost\_NetworkQosArray

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_NetworkQosArray NetworkBoost_NetworkQosArray
```

**描述**

多条路径的网络质量回调信息。

**起始版本：** 5.1.0(18)

### NetworkBoost\_NetworkScene

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_NetworkScene NetworkBoost_NetworkScene
```

**描述**

网络场景状态变更回调信息。

**起始版本：** 5.1.0(18)

### NetworkBoost\_PathType

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_PathType NetworkBoost_PathType
```

**描述**

路径类型。

**起始版本：** 5.1.0(18)

### NetworkBoost\_QoeType

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_QoeType NetworkBoost_QoeType
```

**描述**

应用体验类型。

**起始版本：** 5.1.0(18)

### NetworkBoost\_RecommendedAction

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_RecommendedAction NetworkBoost_RecommendedAction
```

**描述**

建议的数传策略。

**起始版本：** 5.1.0(18)

### NetworkBoost\_ReEstAction

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_ReEstAction NetworkBoost_ReEstAction
```

**描述**

路径重建类型。

**起始版本：** 5.1.0(18)

### NetworkBoost\_Scene

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_Scene NetworkBoost_Scene
```

**描述**

网络场景类型。

**起始版本：** 5.1.0(18)

### NetworkBoost\_ServiceType

PhonePC/2in1Tablet

```
1. typedef enum NetworkBoost_ServiceType NetworkBoost_ServiceType
```

**描述**

应用业务类型。

**起始版本：** 5.1.0(18)

### NetworkBoost\_WeakSignalPrediction

PhonePC/2in1Tablet

```
1. typedef struct NetworkBoost_WeakSignalPrediction NetworkBoost_WeakSignalPrediction
```

**描述**

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

## 枚举类型说明

PhonePC/2in1Tablet

### NetworkBoost\_DataSpeedSimpleAction

PhonePC/2in1Tablet

```
1. enum NetworkBoost_DataSpeedSimpleAction
```

**描述**

应用发包策略的建议。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_SIMPLEACTION\_SUSPEND\_DATA | 停止发包。 |
| NB\_SIMPLEACTION\_DECREASE\_DATA | 降低发包速率。 |
| NB\_SIMPLEACTION\_INCREASE\_DATA | 增加发包速率。 |
| NB\_SIMPLEACTION\_KEEP\_DATA | 保持当前发包速率。 |

### NetworkBoost\_ErrorResult

PhonePC/2in1Tablet

```
1. enum NetworkBoost_ErrorResult
```

**描述**

连接迁移结果枚举。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_ERROR\_NONE | 连接迁移成功。 |
| NB\_ERROR\_HANDOVER\_TIMEOUT | 连接迁移超时。 |
| NB\_ERROR\_NEW\_PATH\_ACTIVATION\_FAILED | 连接迁移时新链路激活失败。 |
| NB\_ERROR\_ABORT | 连接迁移被取消。 |

### NetworkBoost\_HandoverMode

PhonePC/2in1Tablet

```
1. enum NetworkBoost_HandoverMode
```

**描述**

连接迁移模式枚举。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_MODE\_DELEGATION | 委托模式，表示由系统发起连接迁移。默认为该模式。 |
| NB\_MODE\_DISCRETION | 自主模式，表示由应用发起连接迁移。应用可以通过该接口禁止系统发起连接迁移。在某些场景下，比如该应用切换到后台时，依旧有可能由系统触发切换。 |

### NetworkBoost\_PathType

PhonePC/2in1Tablet

```
1. enum NetworkBoost_PathType
```

**描述**

数据路径类型。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_PATH\_CELLULAR\_PRIMARY | 蜂窝主卡。 |
| NB\_PATH\_CELLULAR\_SECONDARY | 蜂窝副卡。 |
| NB\_PATH\_WIFI\_PRIMARY | 主Wi-Fi。 |
| NB\_PATH\_WIFI\_SECONDARY | 辅Wi-Fi。 |

### NetworkBoost\_QoeType

PhonePC/2in1Tablet

```
1. enum NetworkBoost_QoeType
```

**描述**

应用体验类型。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_QOE\_GOOD | 体验良好。 |
| NB\_QOE\_BAD\_UNKNOWN | 体验差：未知原因。 |
| NB\_QOE\_BAD\_SERVER\_ERROR | 体验差：服务器异常。 |
| NB\_QOE\_BAD\_NO\_DATA | 体验差：无数据。 |
| NB\_QOE\_BAD\_PACKET\_LOST | 体验差：丢包。 |
| NB\_QOE\_BAD\_PACKET\_OUT\_OF\_ORDER | 体验差：乱序。 |
| NB\_QOE\_BAD\_HIGH\_JITTER | 体验差：高抖动。 |
| NB\_QOE\_BAD\_HIGH\_LATENCY | 体验差：高时延。 |

### NetworkBoost\_RecommendedAction

PhonePC/2in1Tablet

```
1. enum NetworkBoost_RecommendedAction
```

**描述**

应用数传策略建议。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_ACTION\_DO\_CACHING | 做缓存动作。 |
| NB\_ACTION\_SUSPEND\_DATA | 停止发包。 |
| NB\_ACTION\_DECREASE\_DATA | 降低发包速率。 |
| NB\_ACTION\_INCREASE\_DATA | 增加发包速率。 |
| NB\_ACTION\_KEEP\_DATA | 保持当前发包速率。 |

### NetworkBoost\_ReEstAction

PhonePC/2in1Tablet

```
1. enum NetworkBoost_ReEstAction
```

**描述**

重建枚举。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_REEST\_DEFAULT | 应用需要使用同样的远端IP，进行重建链路。 |
| NB\_REEST\_QUERY\_DNS | 数据链路类型发生变化，比如Wi-Fi <-> CELL，或者是数据链路所在的运营商信息等变化。 |
| NB\_REEST\_CHANGE\_REMOTE\_IP | 应用需要使用不同的远端IP进行重建。 |
| NB\_REEST\_CHANGE\_IP\_VERSION | 应用需要修改IP类型进行重建，比如IPV4 <-> IPV6。 |
| NB\_NO\_EST | 应用应该在老链路进行立即重试，再次发起网络资源请求和交互，无需重建链路。 |

### NetworkBoost\_Scene

PhonePC/2in1Tablet

```
1. enum NetworkBoost_Scene
```

**描述**

网络场景类型。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_SCENE\_NORMAL | 正常场景。 |
| NB\_SCENE\_CONGESTION | 拥塞场景。 |
| NB\_SCENE\_FREQUENT\_HANDOVER | 小区切换频繁场景。 |
| NB\_SCENE\_WEAK\_SIGNAL | 弱信号场景。 |

### NetworkBoost\_ServiceType

PhonePC/2in1Tablet

```
1. enum NetworkBoost_ServiceType
```

**描述**

应用业务类型。

**起始版本：** 5.1.0(18)

| 枚举值 | 描述 |
| --- | --- |
| NB\_SERVICE\_DEFAULT | 默认服务类型。 |
| NB\_SERVICE\_BACKGROUND | 后台类型。 |
| NB\_SERVICE\_REAL\_TIME\_VOICE | 实时语音类型。 |
| NB\_SERVICE\_REAL\_TIME\_VIDEO | 实时视频类型。 |
| NB\_SERVICE\_CALL\_SIGNALING | 语音信令类型。 |
| NB\_SERVICE\_REAL\_TIME\_GAME | 实时游戏类型。 |
| NB\_SERVICE\_NORMAL\_GAME | 普通游戏类型。 |
| NB\_SERVICE\_SHORT\_VIDEO | 短视频类型。 |
| NB\_SERVICE\_LONG\_VIDEO | 长视频类型。 |
| NB\_SERVICE\_LIVE\_STREAMING\_ANCHOR | 直播主播类型。 |
| NB\_SERVICE\_LIVE\_STREAMING\_WATCHER | 直播观看类型。 |
| NB\_SERVICE\_DOWNLOAD | 下载类型。 |
| NB\_SERVICE\_UPLOAD | 上传类型。 |
| NB\_SERVICE\_BROWSER | 浏览页面类型。 |
| NB\_SERVICE\_TRANSACTION | 交易支付或者扫码类型。 |
| NB\_SERVICE\_DETECTION | 探测类型。 |
| NB\_SERVICE\_CLOUDSERVICE | 云业务、云游戏类型。 |
| NB\_SERVICE\_VOICE\_CONFERENCE | 语音会议类型。 |
| NB\_SERVICE\_VIDEO\_CONFERENCE | 视频会议类型。 |
| NB\_SERVICE\_NAVIGATION | 导航定位类型。 |
| NB\_SERVICE\_SECKILL\_SERVICE | 秒杀业务类型，如抢票、抢购、抢单、抢红包等。 |
| NB\_SERVICE\_LOGIN | 登录（含一键登录）类型。 |
| NB\_SERVICE\_AUDIO | 音乐、音频类型。 |
| NB\_SERVICE\_SHOPPING | 购物类型。 |

### NetworkBoost\_PathState

PhonePC/2in1Tablet

```
1. enum NetworkBoost_PathState
```

**描述**

多网链路状态枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_PATH\_IDLE | 多网链路处于空闲状态。 |
| NB\_PATH\_CONNECTED | 多网链路已连接。 |
| NB\_PATH\_SUSPENDED | 多网链路处于挂起状态。 |

### NetworkBoost\_MultiPathChangeCause

PhonePC/2in1Tablet

```
1. enum NetworkBoost_MultiPathChangeCause
```

**描述**

多网变化原因的枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_MULTIPATH\_CAUSE\_REQUEST\_NORMAL | 正常发起多网请求。 |
| NB\_MULTIPATH\_CAUSE\_RELEASE\_NORMAL | 正常释放多网请求。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_NETWORK | 网络原因释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_USER\_REFUSED | 用户操作开关释放多网。 |
| NB\_MULTIPATH\_CAUSE\_RELEASE\_NO\_QUOTA | 配额耗尽释放多网。 |
| NB\_MULTIPATH\_CAUSE\_RELEASE\_POWER\_CONSUMPTION | 功耗原因释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_INSUFFICIENT\_TRAFFIC | 流量原因释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_CONFLICT | 场景冲突释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_FUSING | 应用使用不规范，比如长时间拉起多网不释放，系统释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_RELEASE\_SYS\_DEFAULT | 系统网络状态变化释放多网。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_ENTER | 多网进入挂起状态，此时多网虽未释放，但是实际链路无法传输数据。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_SUSPEND\_LEAVE | 多网退出挂起状态。 |
| NB\_MULTIPATH\_CHANGE\_CAUSE\_CONN\_PROPERTIES\_UPDATE | 多网链路的链接属性信息更新，比如IP地址更新。 |

### NetworkBoost\_MultiPathErrorResult

PhonePC/2in1Tablet

```
1. enum NetworkBoost_MultiPathErrorResult
```

**描述**

多网建立结果的枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_MULTIPATH\_ERROR\_NONE | 多网建立成功。 |
| NB\_MULTIPATH\_ERROR\_NETWORK\_REFUSED | 多网请求被网络拒绝。 |
| NB\_MULTIPATH\_ERROR\_TIMEOUT | 多网建立超时。 |
| NB\_MULTIPATH\_ERROR\_LOCAL | 多网建立过程中，本地释放，例如在建立过程中数据开关关闭，或者其他事件发生，已经不满足拉起多网的条件。 |

### NetworkBoost\_MultiPathState

PhonePC/2in1Tablet

```
1. enum NetworkBoost_MultiPathState
```

**描述**

多网状态的枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_MULTIPATH\_IDLE | 多网处于空闲状态。 |
| NB\_MULTIPATH\_CREATEING | 多网正在建立中。 |
| NB\_MULTIPATH\_CREATED | 多网已建立。 |
| NB\_MULTIPATH\_RELEASING | 多网正在释放中。 |

### NetworkBoost\_MultiPathAction

PhonePC/2in1Tablet

```
1. enum NetworkBoost_MultiPathAction
```

**描述**

多网推荐动作的枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_MULTIPATH\_ACTION\_REQUEST | 建议发起多网请求。 |
| NB\_MULTIPATH\_ACTION\_RELEASE | 建议释放多网请求。 |

### NetworkBoost\_SceneEvent

PhonePC/2in1Tablet

```
1. enum NetworkBoost_SceneEvent
```

**描述**

业务事件枚举。

**起始版本：** 6.0.2(22)

| 枚举值 | 描述 |
| --- | --- |
| NB\_SCENE\_EVENT\_ENTER | 进入业务场景。 |
| NB\_SCENE\_EVENT\_UPDATE | 更新上一次的业务事件信息。 |
| NB\_SCENE\_EVENT\_LEAVE | 离开业务场景。 |

## 函数说明

PhonePC/2in1Tablet

### HMS\_NetworkBoost\_RegisterHandoverChangeCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RegisterHandoverChangeCallback (HMS_NetworkBoost_HandoverCallback * callback, uint32_t * callbackId )
```

**描述**

注册连接迁移信息回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 连接迁移回调函数。 |
| callbackId | 回调函数的ID，由系统分配，用于取消注册回调。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

62100003 - 注册请求达到上限。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_RegisterNetQosCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RegisterNetQosCallback (HMS_NetworkBoost_NetQosChange callback, uint32_t * callbackId )
```

**描述**

注册网络质量信息回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 网络质量回调函数。 |
| callbackId | 回调函数的ID，由系统分配，用于取消注册回调。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

62100003 - 注册请求达到上限。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_RegisterNetSceneCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RegisterNetSceneCallback (HMS_NetworkBoost_NetSceneChange callback, uint32_t * callbackId )
```

**描述**

注册网络场景变化回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 网络场景变化回调函数。 |
| callbackId | 回调函数的ID，由系统分配，用于取消注册回调。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

62100003 - 注册请求达到上限。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_ReportQoe()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_ReportQoe (NetworkBoost_ServiceType serviceType, NetworkBoost_QoeType qoeType )
```

**描述**

应用传输体验反馈。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| serviceType | 应用的业务类型。 |
| qoeType | 应用的网络体验类型。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_SetHandoverMode()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_SetHandoverMode (NetworkBoost_HandoverMode mode)
```

**描述**

变更连接迁移模式。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| mode | 连接迁移模式。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_UnregisterHandoverChangeCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_UnregisterHandoverChangeCallback (uint32_t callbackId)
```

**描述**

取消注册连接迁移信息回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callbackId | 回调的ID，在注册回调函数时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_UnregisterNetQosCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_UnregisterNetQosCallback (uint32_t callbackId)
```

**描述**

取消注册网络质量信息回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callbackId | 回调的ID，在注册回调函数时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_UnregisterNetSceneCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_UnregisterNetSceneCallback (uint32_t callbackId)
```

**描述**

取消注册网络场景变化回调。

**起始版本：** 5.1.0(18)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callbackId | 回调的ID，在注册回调函数时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

401 - 参数错误。

801 - 系统能力不支持。

62100001 - 内部错误。

62100002 - 系统服务操作失败。

**权限：**

ohos.permission.GET\_NETWORK\_INFO

### HMS\_NetworkBoost\_GetMultiPathQuotaStats()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_GetMultiPathQuotaStats(NetworkBoost_MultiPathQuota* quota)
```

**描述**

获取当前应用多网使用的配额，包括已使用的配额信息和剩余配额信息。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| quota | 获取到的应用配额信息。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部错误。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013600041 - 传入参数有误，例如入参为空指针。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_RequestMultiPath()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RequestMultiPath(HMS_NetworkBoost_OnMultiPathRequestResult result)
```

**描述**

发起多网请求。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| result | 发起多网的结果。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013600041 - 传入参数有误，例如入参为空指针。

1013620000 - 多网功能没有使能。

1013620001 - 多网已经激活或者是在激活的过程中。

1013620002 - 应用多网请求已经达到上限。

1013620003 - 功耗限制不允许发起多网。

1013620004 - 限额耗尽。

1013620005 - 多网请求场景的冲突。

1013620006 - 多网发起太频繁。

1013620007 - 没有合适的多网链路可用。

1013620008 - 流量不足。

1013620009 - 不支持并发。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_ReleaseMultiPath()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_ReleaseMultiPath()
```

**描述**

释放多网请求。

**起始版本：** 6.0.2(22)

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013620100 - 多网已经激活状态，但是多网不是当前发起release的应用拉起的。

1013620101 - 多网不在激活态。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_RegisterMultiPathStateChangeCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RegisterMultiPathStateChangeCallback(HMS_NetworkBoost_OnMultiPathStateChange callback, uint32_t* callbackId)
```

**描述**

注册多网状态变化事件。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 网状态变化回调函数。 |
| callbackId | 回调的ID，注册多网状态时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013600041 - 传入参数有误，例如入参为空指针。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_UnregisterMultiPathStateChangeCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_UnregisterMultiPathStateChangeCallback(uint32_t callbackId)
```

**描述**

去注册多网状态变化事件。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callbackId | 回调的ID，注册多网状态时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_RegisterMultiPathRecommendationCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_RegisterMultiPathRecommendationCallback(HMS_NetworkBoost_OnMultiPathRecommendation callback, uint32_t* callbackId)
```

**描述**

注册系统多网建议变化事件。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callback | 系统多网建议变化回调函数。 |
| callbackId | 回调的ID，注册多网状态时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

1013600041 - 传入参数有误，例如入参为空指针。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_UnregisterMultiPathRecommendationCallback()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_UnregisterMultiPathRecommendationCallback(uint32_t callbackId)
```

**描述**

去注册系统多网建议变化事件。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| callbackId | 回调的ID，注册多网状态时由系统分配。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**权限：**

ohos.permission.LINKTURBO

### HMS\_NetworkBoost\_SetSceneDesc()

PhonePC/2in1Tablet

```
1. int32_t HMS_NetworkBoost_SetSceneDesc(NetworkBoost_SceneDesc sceneDesc)
```

**描述**

设置业务场景。

**起始版本：** 6.0.2(22)

**参数:**

| 名称 | 描述 |
| --- | --- |
| sceneDesc | 要设置的业务场景信息。 |

**返回：**

0 - 成功。

201 - 权限不足。

1013600001 - 内部处理异常，例如内部处理异常，例如内部管理状态机异常，内部消息队列处理阻塞等。

1013600002 - 系统处理异常，例如IPC跨进程调用失败，网络管理服务启动失败。

**权限：**

ohos.permission.INTERNET
