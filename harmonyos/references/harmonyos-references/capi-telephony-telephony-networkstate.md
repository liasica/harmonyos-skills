---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-telephony-networkstate
title: Telephony_NetworkState
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > C API > 结构体 > Telephony_NetworkState
category: harmonyos-references
scraped_at: 2026-09-02T15:02:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec3d78871f136fc05d961138583633c41fcf3c4169102c203971b2334f5d254e
---

```c
typedef struct {...} Telephony_NetworkState
```

## 概述

网络状态信息。可用于获取设备当前注册网络的运营商名称、PLMN码、漫游状态、网络注册状态、无线接入技术等，适用于需要展示当前网络状态或根据网络状态进行业务逻辑判断的场景。

**起始版本：** 13

**相关模块：** [Telephony](capi-telephony.md)

**所在头文件：** [telephony\_radio\_type.h](capi-telephony-radio-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char longOperatorName\_[TELEPHONY\_MAX\_OPERATOR\_LEN] | 注册网络的长运营商名称。 |
| char shortOperatorName\_[TELEPHONY\_MAX\_OPERATOR\_LEN] | 注册网络的短运营商名称。 |
| char plmnNumeric\_[TELEPHONY\_MAX\_PLMN\_NUMERIC\_LEN] | 注册网络的PLMN码。 |
| bool isRoaming\_ | 是否处于漫游状态。true表示处于漫游状态，false表示未处于漫游状态。 |
| Telephony\_RegState regState\_ | 设备的网络注册状态。 |
| Telephony\_RadioTechnology cfgTech\_ | 设备的无线接入技术。 |
| Telephony\_NsaState nsaState\_ | 设备的NSA网络注册状态。 |
| bool isCaActive\_ | CA（Carrier Aggregation，载波聚合）是否处于激活状态。true表示CA已激活，false表示CA未激活。 |
| bool isEmergency\_ | 此设备是否只允许拨打紧急呼叫。true表示只允许拨打紧急呼叫，false表示不限于紧急呼叫。 |
