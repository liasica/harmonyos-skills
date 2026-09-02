---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action
title: NetworkBoost_DataSpeedAction
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_DataSpeedAction
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e135f5673752af698d574704e4112b9d64ed0783f1a8c3ada59099b6e757cfe1
---

## 概述

发包速率建议。该结构体用于网络加速模块中，当系统需要为特定应用提供定制化的上下行带宽建议时使用。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_handover.h](network-boost-c-files-handover.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_DataSpeedSimpleAction](network-boost-c-overview.md#networkboost_dataspeedsimpleaction-1) [dataSpeedSimpleAction](network-boost-c-struct-data_speed_action.md#dataspeedsimpleaction) | 应用发包策略的简单建议。该字段表示应用在当前网络环境下推荐使用的发包策略，用于指导应用优化数据传输行为。 |
| uint64\_t [linkUpBandwidth](network-boost-c-struct-data_speed_action.md#linkupbandwidth) | 上行带宽，单位为bps。该字段表示设备当前网络连接的上行带宽能力，可用于评估上传速度和资源分配。 |
| uint64\_t [linkDownBandwidth](network-boost-c-struct-data_speed_action.md#linkdownbandwidth) | 下行带宽，单位为bps。该字段表示设备当前网络连接的下行带宽能力，可用于评估下载速度和资源分配。 |

## 结构体成员变量说明

### dataSpeedSimpleAction

```c
NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedAction::dataSpeedSimpleAction
```

**描述**

应用发包策略的简单建议。

### linkDownBandwidth

```c
uint64_t NetworkBoost_DataSpeedAction::linkDownBandwidth
```

**描述**

下行带宽。

### linkUpBandwidth

```c
uint64_t NetworkBoost_DataSpeedAction::linkUpBandwidth
```

**描述**

上行带宽。
