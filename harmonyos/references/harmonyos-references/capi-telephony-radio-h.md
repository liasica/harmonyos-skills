---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-telephony-radio-h
title: telephony_radio.h
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > C API > 头文件 > telephony_radio.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2a49d5a07ee363fa5bf10091a03864beaa5e5b417811e212ac3909f51b955fd9
---

## 概述

为网络搜索模块定义C接口，提供获取移动网络状态（包括网络注册状态、运营商信息、网络制式等）的能力，适用于应用需要查询当前卡槽网络连接状态的场景。

**引用文件：** <telephony/core\_service/telephony\_radio.h>

**库：** libtelephony\_radio.so

**系统能力：** SystemCapability.Telephony.CoreService

**起始版本：** 13

**相关模块：** [Telephony](capi-telephony.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [Telephony\_RadioResult OH\_Telephony\_GetNetworkState(Telephony\_NetworkState \*state)](capi-telephony-radio-h.md#oh_telephony_getnetworkstate) | 获取网络状态。 |
| [Telephony\_RadioResult OH\_Telephony\_GetNetworkStateForSlot(int32\_t slotId, Telephony\_NetworkState \*state)](capi-telephony-radio-h.md#oh_telephony_getnetworkstateforslot) | 获取给定卡槽ID的网络状态。 |

## 函数说明

### OH\_Telephony\_GetNetworkState()

```c
Telephony_RadioResult OH_Telephony_GetNetworkState(Telephony_NetworkState *state)
```

**描述**

获取网络状态。

**系统能力：** SystemCapability.Telephony.CoreService

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Telephony\_NetworkState](capi-telephony-telephony-networkstate.md) \*state | 用于接收网络状态信息的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Telephony\_RadioResult](capi-telephony-radio-type-h.md#telephony_radioresult) | 结果定义在 [Telephony\_RadioResult](capi-telephony-radio-type-h.md#telephony_radioresult)。  [TEL\_RADIO\_SUCCESS](capi-telephony-radio-type-h.md#telephony_radioresult) 成功。  [TEL\_RADIO\_PERMISSION\_DENIED](capi-telephony-radio-type-h.md#telephony_radioresult) 权限错误。  [TEL\_RADIO\_ERR\_MARSHALLING\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 编组错误。  [TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 连接电话服务错误。  [TEL\_RADIO\_ERR\_OPERATION\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 操作电话服务错误。  [TEL\_RADIO\_ERR\_INVALID\_PARAM](capi-telephony-radio-type-h.md#telephony_radioresult) 参数错误。 |

### OH\_Telephony\_GetNetworkStateForSlot()

```c
Telephony_RadioResult OH_Telephony_GetNetworkStateForSlot(int32_t slotId, Telephony_NetworkState *state)
```

**描述**

获取给定卡槽ID的网络状态。

**系统能力：** SystemCapability.Telephony.CoreService

**需要权限：** ohos.permission.GET\_NETWORK\_INFO

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t slotId | 卡槽ID。 |
| [Telephony\_NetworkState](capi-telephony-telephony-networkstate.md) \*state | 用于接收网络状态信息的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Telephony\_RadioResult](capi-telephony-radio-type-h.md#telephony_radioresult) | 结果定义在 [Telephony\_RadioResult](capi-telephony-radio-type-h.md#telephony_radioresult)。  [TEL\_RADIO\_SUCCESS](capi-telephony-radio-type-h.md#telephony_radioresult) 成功。  [TEL\_RADIO\_PERMISSION\_DENIED](capi-telephony-radio-type-h.md#telephony_radioresult) 权限错误。  [TEL\_RADIO\_ERR\_MARSHALLING\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 编组错误。  [TEL\_RADIO\_ERR\_SERVICE\_CONNECTION\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 连接电话服务错误。  [TEL\_RADIO\_ERR\_OPERATION\_FAILED](capi-telephony-radio-type-h.md#telephony_radioresult) 操作电话服务错误。  [TEL\_RADIO\_ERR\_INVALID\_PARAM](capi-telephony-radio-type-h.md#telephony_radioresult) 参数错误。 |
