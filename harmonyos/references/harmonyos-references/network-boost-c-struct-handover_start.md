---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-handover_start
title: NetworkBoost_HandoverStart
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_HandoverStart
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d4a07364ac6e739eaaad8a9a90bc6590319bf1e06e0741a46175cae8497a4d62
---

## 概述

连接迁移开始信息。该结构体用于配置连接迁移开始时的相关参数，通常系统发起多网迁移（Wi-Fi与蜂窝网络切换，主卡与副卡切换等）开始时使用，其主要作用是设置迁移过程中的超时时间和老链路的发包建议，以保证迁移过程的稳定性和效率。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t [expires](network-boost-c-struct-handover_start.md#expires) | 连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。 |
| [NetworkBoost\_DataSpeedAction](network-boost-c-struct-data_speed_action.md) [dataSpeedAction](network-boost-c-struct-handover_start.md#dataspeedaction) | 老链路的发包建议。 |

## 结构体成员变量说明

### dataSpeedAction

```c
NetworkBoost_DataSpeedAction NetworkBoost_HandoverStart::dataSpeedAction
```

**描述**

老链路的发包建议。

### expires

```c
uint32_t NetworkBoost_HandoverStart::expires
```

**描述**

连接迁移全流程的超时时间，单位为s，取值为任意正整数或者0。
