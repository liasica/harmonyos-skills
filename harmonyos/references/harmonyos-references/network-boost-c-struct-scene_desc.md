---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-scene_desc
title: NetworkBoost_SceneDesc
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_SceneDesc
category: harmonyos-references
scraped_at: 2026-04-28T08:08:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:eed095688d24bd3d0288c9a69b5318584d1c2e8beb340e54a774b07fddf1eb47
---

## 概述

PhonePC/2in1Tablet

业务场景描述信息。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost.h](network-boost-c-files-boost.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_ServiceType](network-boost-c-overview.md#networkboost_servicetype) [scene](network-boost-c-struct-scene_desc.md#scene) | 表示业务场景类型。 |
| [NetworkBoost\_SceneEvent](network-boost-c-overview.md#networkboost_sceneevent) [sceneEvent](network-boost-c-struct-scene_desc.md#sceneevent) | 表示业务场景事件。 |
| uint32\_t [startTime](network-boost-c-struct-scene_desc.md#starttime) | 表示要经过多长时间进入到sceneEvent事件，单位为s。  - 0表示立即发生sceneEvent事件，默认为0。  - 大于0表示预测未来多长时间进入sceneEvent事件。 |
| uint32\_t [duration](network-boost-c-struct-scene_desc.md#duration) | 预计本次设置的业务场景会持续的时长，单位为s。0表示持续时长未知，以SceneEvent的离开事件表示终止。开发者可以依据实际的场景类型进行选填。  例如：应用即将在10s后进入秒杀场景，预计持续20s。scene可以传入'seckillService'类型，sceneEvent填写SCENE\_EVENT\_ENTER，startTime可填写10，duration填写20。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

## scene

PhonePC/2in1Tablet

```
1. NetworkBoost_ServiceType NetworkBoost_SceneDesc::scene
```

**描述**

表示业务场景类型。

## sceneEvent

PhonePC/2in1Tablet

```
1. NetworkBoost_SceneEvent NetworkBoost_SceneDesc::sceneEvent
```

**描述**

表示业务场景事件。

## startTime

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_SceneDesc::startTime
```

**描述**

表示要经过多长时间进入到sceneEvent事件，单位为s。

## duration

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_SceneDesc::duration
```

**描述**

预计本次设置的业务场景会持续的时长，单位为s。
