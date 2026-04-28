---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-telephony-networkstate
title: Telephony_NetworkState
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > C API > 结构体 > Telephony_NetworkState
category: harmonyos-references
scraped_at: 2026-04-28T08:09:23+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f53aab4c52958bfe4c1918b094b16160cb042ebcfc9601ef36d4555bd6e8e8e9
---

```
1. typedef struct {...} Telephony_NetworkState
```

## 概述

PhoneTabletWearable

网络状态信息。

**起始版本：** 13

**相关模块：** [Telephony](capi-telephony.md)

**所在头文件：** [telephony\_radio\_type.h](capi-telephony-radio-type-h.md)

## 汇总

PhoneTabletWearable

### 成员变量

PhoneTabletWearable

| 名称 | 描述 |
| --- | --- |
| char longOperatorName\_[TELEPHONY\_MAX\_OPERATOR\_LEN] | 注册网络的长运营商名称。 |
| char shortOperatorName\_[TELEPHONY\_MAX\_OPERATOR\_LEN] | 注册网络的短运营商名称。 |
| char plmnNumeric\_[TELEPHONY\_MAX\_PLMN\_NUMERIC\_LEN] | 注册网络的PLMN码。 |
| bool isRoaming\_ | 是否处于漫游状态。 |
| Telephony\_RegState regState\_ | 设备的网络注册状态。 |
| Telephony\_RadioTechnology cfgTech\_ | 设备的无线接入技术。 |
| Telephony\_NsaState nsaState\_ | 设备的NSA网络注册状态。 |
| bool isCaActive\_ | CA的状态。 |
| bool isEmergency\_ | 此设备是否只允许拨打紧急呼叫。 |
