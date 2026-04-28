---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-radio-type-h
title: telephony_radio_type.h
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > C API > 头文件 > telephony_radio_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:22+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:494e583789ae9156139112f989fccf9e8a826d97a3845bfb0082db7302c2f56a
---

## 概述

PhoneTabletWearable

定义网络搜索模块的C接口需要的数据结构。

**引用文件：** <telephony/core\_service/telephony\_radio\_type.h>

**库：** libtelephony\_radio.so

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 13

**相关模块：** [Telephony](capi-telephony.md)

## 汇总

PhoneTabletWearable

### 结构体

PhoneTabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Telephony\_NetworkState](capi-telephony-telephony-networkstate.md) | Telephony\_NetworkState | 网络状态信息。 |

### 枚举

PhoneTabletWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Telephony\_RadioResult](capi-telephony-radio-type-h.md#telephony_radioresult) | Telephony\_RadioResult | 错误码类型枚举。 |
| [Telephony\_RegState](capi-telephony-radio-type-h.md#telephony_regstate) | Telephony\_RegState | 设备的网络注册状态类型。 |
| [Telephony\_RadioTechnology](capi-telephony-radio-type-h.md#telephony_radiotechnology) | Telephony\_RadioTechnology | 设备的无线接入技术类型。 |
| [Telephony\_NsaState](capi-telephony-radio-type-h.md#telephony_nsastate) | Telephony\_NsaState | 设备的NSA网络注册状态类型。 |

### 宏定义

PhoneTabletWearable

| 名称 | 描述 |
| --- | --- |
| TELEPHONY\_MAX\_OPERATOR\_LEN 64 | 定义运营商名称的最大长度。  **起始版本：** 13 |
| TELEPHONY\_MAX\_PLMN\_NUMERIC\_LEN 6 | 定义PLMN的最大长度。  **起始版本：** 13 |

## 枚举类型说明

PhoneTabletWearable

### Telephony\_RadioResult

PhoneTabletWearable

```
1. enum Telephony_RadioResult
```

**描述**

错误码类型枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| TEL\_RADIO\_SUCCESS = 0 | 成功。 |
| TEL\_RADIO\_PERMISSION\_DENIED = 201 | 权限错误。 |
| TEL\_RADIO\_ERR\_INVALID\_PARAM = 401 | 参数错误。 |
| TEL\_RADIO\_ERR\_MARSHALLING\_FAILED = 8300001 | 编组错误，这是一个低概率错误，请稍后在遇到此错误时重试。 |
| TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED = 8300002 | 连接电话服务错误，当出现此错误时，请稍后重试。 |
| TEL\_RADIO\_ERR\_OPERATION\_FAILED = 8300003 | 操作电话服务错误，当出现此错误时，请稍后重试。 |

### Telephony\_RegState

PhoneTabletWearable

```
1. enum Telephony_RegState
```

**描述**

设备的网络注册状态类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| TEL\_REG\_STATE\_NO\_SERVICE = 0 | 设备不能使用任何服务。 |
| TEL\_REG\_STATE\_IN\_SERVICE = 1 | 设备可以正常使用服务。 |
| TEL\_REG\_STATE\_EMERGENCY\_CALL\_ONLY = 2 | 设备只能使用紧急呼叫业务。 |
| TEL\_REG\_STATE\_POWER\_OFF = 3 | 蜂窝无线电已关闭。 |

### Telephony\_RadioTechnology

PhoneTabletWearable

```
1. enum Telephony_RadioTechnology
```

**描述**

设备的无线接入技术类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| TEL\_RADIO\_TECHNOLOGY\_UNKNOWN = 0 | 未知无线接入技术（RAT）。 |
| TEL\_RADIO\_TECHNOLOGY\_GSM = 1 | 无线接入技术GSM（Global System for Mobile Communication）。 |
| TEL\_RADIO\_TECHNOLOGY\_1XRTT = 2 | 无线接入技术1XRTT（Single-Carrier Radio Transmission Technology）。 |
| TEL\_RADIO\_TECHNOLOGY\_WCDMA = 3 | 无线接入技术WCDMA（Wideband Code Division Multiple Access）。 |
| TEL\_RADIO\_TECHNOLOGY\_HSPA = 4 | 无线接入技术HSPA（High Speed Packet Access）。 |
| TEL\_RADIO\_TECHNOLOGY\_HSPAP = 5 | 无线接入技术HSPAP（High Speed Packet Access (HSPA+) ）。 |
| TEL\_RADIO\_TECHNOLOGY\_TD\_SCDMA = 6 | 无线接入技术TDSCDMA（Time Division-Synchronous Code Division Multiple Access）。 |
| TEL\_RADIO\_TECHNOLOGY\_EVDO = 7 | 无线接入技术EVDO（Evolution Data Optimized）。 |
| TEL\_RADIO\_TECHNOLOGY\_EHRPD = 8 | 无线接入技术EHRPD（Evolved High Rate Package Data）。 |
| TEL\_RADIO\_TECHNOLOGY\_LTE = 9 | 无线接入技术LTE（Long Term Evolution）。 |
| TEL\_RADIO\_TECHNOLOGY\_LTE\_CA = 10 | 无线接入技术LTE\_CA（Long Term Evolution\_Carrier Aggregation）。 |
| TEL\_RADIO\_TECHNOLOGY\_IWLAN = 11 | 无线接入技术IWLAN（Industrial Wireless LAN）。 |
| TEL\_RADIO\_TECHNOLOGY\_NR = 12 | 无线接入技术NR（New Radio）。 |

### Telephony\_NsaState

PhoneTabletWearable

```
1. enum Telephony_NsaState
```

**描述**

设备的NSA网络注册状态类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| TEL\_NSA\_STATE\_NOT\_SUPPORTED = 1 | 设备在不支持NSA的LTE小区下处于空闲状态或连接状态。 |
| TEL\_NSA\_STATE\_NO\_DETECTED = 2 | 在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。 |
| TEL\_NSA\_STATE\_CONNECTED\_DETECTED = 3 | 设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。 |
| TEL\_NSA\_STATE\_IDLE\_DETECTED = 4 | 支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。 |
| TEL\_NSA\_STATE\_DUAL\_CONNECTED = 5 | 设备在支持NSA的LTE小区下连接到LTE + NR网络。 |
| TEL\_NSA\_STATE\_SA\_ATTACHED = 6 | 设备在5GC附着时在NG-RAN小区下空闲或连接到NG-RAN小区。 |
