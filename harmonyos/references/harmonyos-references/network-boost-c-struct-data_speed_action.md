---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-data_speed_action
title: NetworkBoost_DataSpeedAction
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_DataSpeedAction
category: harmonyos-references
scraped_at: 2026-04-28T08:08:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d768c6ed9f9db74cb793a851f36045f5595550a16bd878aa924629e1b54578f2
---

## 概述

PhonePC/2in1Tablet

发包速率建议。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](network-boost-c-files-quality.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [NetworkBoost\_DataSpeedSimpleAction](network-boost-c-overview.md#networkboost_dataspeedsimpleaction-1) [dataSpeedSimpleAction](network-boost-c-struct-data_speed_action.md#dataspeedsimpleaction) | 应用发包策略的简单建议。 |
| uint64\_t [linkUpBandwidth](network-boost-c-struct-data_speed_action.md#linkupbandwidth) | 上行带宽。 |
| uint64\_t [linkDownBandwidth](network-boost-c-struct-data_speed_action.md#linkdownbandwidth) | 下行带宽。 |

## 结构体成员变量说明

PhonePC/2in1Tablet

### dataSpeedSimpleAction

PhonePC/2in1Tablet

```
1. NetworkBoost_DataSpeedSimpleAction NetworkBoost_DataSpeedAction::dataSpeedSimpleAction
```

**描述**

应用发包策略的简单建议。

### linkDownBandwidth

PhonePC/2in1Tablet

```
1. uint64_t NetworkBoost_DataSpeedAction::linkDownBandwidth
```

**描述**

下行带宽。

### linkUpBandwidth

PhonePC/2in1Tablet

```
1. uint64_t NetworkBoost_DataSpeedAction::linkUpBandwidth
```

**描述**

上行带宽。
