---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-multipath_statechange
title: NetworkBoost_MultiPathStateChange
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_MultiPathStateChange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4ee802fbf19353699f190c148c94be7e83ddc0aba05d6dcf1984cae6e9537ac3
---

## 概述

多网状态信息，用于注册多网状态变化事件回调后，系统多网状态发生变化的事件通知。

**起始版本：** 6.0.2(22)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_MultiPathState](network-boost-c-overview.md#networkboost_multipathstate) [multiPathState](network-boost-c-struct-multipath_statechange.md#multipathstate) | 多网状态。 |
| [NetworkBoost\_MultiPathChangeCause](network-boost-c-overview.md#networkboost_multipathchangecause) [changeCause](network-boost-c-struct-multipath_statechange.md#changecause) | 多网状态变化原因。 |
| [NetworkBoost\_NetHandle](network-boost-c-overview.md#networkboost_nethandle) [netHandle](network-boost-c-struct-multipath_statechange.md#nethandle) | 多网链路的netHandle。 |
| [NetworkBoost\_PathState](network-boost-c-overview.md#networkboost_pathstate) [pathState](network-boost-c-struct-multipath_statechange.md#pathstate) | 多网链路状态。 |
| [NetworkBoost\_PathType](network-boost-c-overview.md#networkboost_pathtype) [pathType](network-boost-c-struct-multipath_statechange.md#pathtype) | 多网链路类型。 |

## 结构体成员变量说明

## multiPathState

```c
NetworkBoost_MultiPathState NetworkBoost_MultiPathStateChange::multiPathState
```

**描述**

多网状态，可以通过该信息获取当前多网所处状态，包含空闲态、建立中、已建立和释放中四种状态。

## changeCause

```c
NetworkBoost_MultiPathChangeCause NetworkBoost_MultiPathStateChange::changeCause
```

**描述**

多网状态变化原因，在多网状态发生变化时，通过该信息可以获取发生多网状态发生变化的原因。

## netHandle

```c
NetworkBoost_NetHandle NetworkBoost_MultiPathStateChange::netHandle
```

**描述**

多网链路的netHandle。

## pathState

```c
NetworkBoost_PathState NetworkBoost_MultiPathStateChange::pathState
```

**描述**

多网链路状态。

## pathType

```c
NetworkBoost_PathType NetworkBoost_MultiPathStateChange::pathType
```

**描述**

多网链路类型。
