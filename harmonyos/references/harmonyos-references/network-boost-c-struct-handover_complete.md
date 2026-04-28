---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_complete
title: NetworkBoost_HandoverComplete
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_HandoverComplete
category: harmonyos-references
scraped_at: 2026-04-28T08:08:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1a9d8a223f2bafb381582458c60201edc4184c7eafdf53593bd25460c83d55e6
---

## 概述

PhonePC/2in1Tablet

连接迁移完成信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_ErrorResult](network-boost-c-overview.md#networkboost_errorresult-1) [result](network-boost-c-struct-handover_complete.md#result) | 连接迁移结果。 |
| bool [handoverContinue](network-boost-c-struct-handover_complete.md#handovercontinue) | 是否继续等待HandoverComplete消息，当存在两条以上路径时，会存在多个HandoverComplete消息。  true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。  false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。 |
| uint32\_t [oldPathLifetime](network-boost-c-struct-handover_complete.md#oldpathlifetime) | 老链路的剩余生存时长，单位为s，取值为任意正整数或0。 |
| [NetworkBoost\_DataSpeedAction](network-boost-c-struct-data_speed_action.md) [oldDataSpeedAction](network-boost-c-struct-handover_complete.md#olddataspeedaction) | 老链路发包建议。 |
| bool [pathTypeChanged](network-boost-c-struct-handover_complete.md#pathtypechanged) | 新老链路类型是否发生变更。true表示发生变化，如Wi-Fi<->蜂窝。false表示没有发生变化。 |
| [NetworkBoost\_NetHandle](network-boost-c-struct-net_handle.md) [newNetHandle](network-boost-c-struct-handover_complete.md#newnethandle) | 新链路的NetHandle信息。 |
| [NetworkBoost\_ReEstAction](network-boost-c-overview.md#networkboost_reestaction-1) [reEstAction](network-boost-c-struct-handover_complete.md#reestaction) | 链路重建类型。 |
| [NetworkBoost\_DataSpeedAction](network-boost-c-struct-data_speed_action.md) [newDataSpeedAction](network-boost-c-struct-handover_complete.md#newdataspeedaction) | 新链路发包建议。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### handoverContinue

PhonePC/2in1Tablet

```
1. bool NetworkBoost_HandoverComplete::handoverContinue
```

**描述**

是否继续等待HandoverComplete消息，当存在两条以上路径时，会存在多个HandoverComplete消息。

true表示还有新链路待激活，系统还会上报HandoverComplete消息，一般发生在连接迁移到多个网络的场景。

false表示当前已经是最后一个HandoverComplete消息，连接迁移流程完成。

### newDataSpeedAction

PhonePC/2in1Tablet

```
1. NetworkBoost_DataSpeedAction NetworkBoost_HandoverComplete::newDataSpeedAction
```

**描述**

新链路发包建议。

### newNetHandle

PhonePC/2in1Tablet

```
1. NetworkBoost_NetHandle NetworkBoost_HandoverComplete::newNetHandle
```

**描述**

新链路的NetHandle信息。

### oldDataSpeedAction

PhonePC/2in1Tablet

```
1. NetworkBoost_DataSpeedAction NetworkBoost_HandoverComplete::oldDataSpeedAction
```

**描述**

老链路发包建议。

### oldPathLifetime

PhonePC/2in1Tablet

```
1. uint32_t NetworkBoost_HandoverComplete::oldPathLifetime
```

**描述**

老链路的剩余生存时长，单位为s，取值为任意正整数或0。

### pathTypeChanged

PhonePC/2in1Tablet

```
1. bool NetworkBoost_HandoverComplete::pathTypeChanged
```

**描述**

新老链路类型是否发生变更。true表示发生变化，如Wi-Fi<->蜂窝。false表示没有发生变化。

### reEstAction

PhonePC/2in1Tablet

```
1. NetworkBoost_ReEstAction NetworkBoost_HandoverComplete::reEstAction
```

**描述**

链路重建类型。

### result

PhonePC/2in1Tablet

```
1. NetworkBoost_ErrorResult NetworkBoost_HandoverComplete::result
```

**描述**

连接迁移结果。
