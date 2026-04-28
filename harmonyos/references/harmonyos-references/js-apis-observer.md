---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-observer
title: @ohos.telephony.observer (observer)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.observer (observer)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:21c499c7161c0a5966d3cd3fc282cd28c577285653736d4f9670155fa76ad61c
---

本模块提供订阅管理功能，可以订阅/取消订阅的事件包括：网络状态变化、信号状态变化、通话状态变化、蜂窝数据链路连接状态、蜂窝数据业务的上下行数据流状态、SIM状态变化。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTabletWearable

```
1. import { observer } from '@kit.TelephonyKit';
```

## NetworkState

PhoneTabletWearable

type NetworkState = radio.NetworkState

网络注册状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [radio.NetworkState](js-apis-radio.md#networkstate) | 网络注册状态。 |

## SignalInformation

PhoneTabletWearable

type SignalInformation = radio.SignalInformation

网络信号强度信息对象。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [radio.SignalInformation](js-apis-radio.md#signalinformation) | 网络信号强度信息对象。 |

## DataConnectState

PhoneTabletWearable

type DataConnectState = data.DataConnectState

描述蜂窝数据链路连接状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [data.DataConnectState](js-apis-telephony-data.md#dataconnectstate) | 描述蜂窝数据链路连接状态。 |

## RatType

PhoneTabletWearable

type RatType = radio.RadioTechnology

无线接入技术。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [radio.RadioTechnology](js-apis-radio.md#radiotechnology) | 无线接入技术。 |

## DataFlowType

PhoneTabletWearable

type DataFlowType = data.DataFlowType

描述蜂窝数据流类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [data.DataFlowType](js-apis-telephony-data.md#dataflowtype) | 描述蜂窝数据流类型。 |

## CallState

PhoneTabletWearable

type CallState = call.CallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [call.CallState](js-apis-call.md#callstate) | 通话状态码（去电过程仅通知CALL\_STATE\_OFFHOOK状态）。 |

## CCallState23+

PhoneTabletWearable

type CCallState = call.CCallState

运营商通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [call.CCallState](js-apis-call.md#ccallstate23) | 通话状态码（运营商通话状态码）。 |

## CardType

PhoneTabletWearable

type CardType = sim.CardType

卡类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [sim.CardType](js-apis-sim.md#cardtype7) | 卡类型。 |

## SimState

PhoneTabletWearable

type SimState = sim.SimState

SIM卡状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [sim.SimState](js-apis-sim.md#simstate) | SIM卡状态。 |

## TelCallState21+

PhoneTabletWearable

type TelCallState = call.TelCallState

通话状态码。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 类型 | 说明 |
| --- | --- |
| [call.TelCallState](js-apis-call.md#telcallstate21) | 通话状态码（去电过程通知去电号码状态TEL\_CALL\_STATE\_OFFHOOK和去电接通状态TEL\_CALL\_STATE\_CONNECTED）。 |

## observer.on('networkStateChange')

PhoneTabletWearable

on(type: 'networkStateChange', callback: Callback<NetworkState>): void

订阅网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| callback | Callback<[NetworkState](js-apis-radio.md#networkstate)> | 是 | 以callback形式异步返回结果。参考radio的[NetworkState](js-apis-radio.md#networkstate)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. observer.on('networkStateChange', (data: observer.NetworkState) => {
2. console.info("on networkStateChange, data:" + JSON.stringify(data));
3. });
```

## observer.on('networkStateChange')

PhoneTabletWearable

on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void

订阅指定卡槽位的网络状态变化事件，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<[NetworkState](js-apis-radio.md#networkstate)> | 是 | 以callback形式异步返回结果，参考radio的[NetworkState](js-apis-radio.md#networkstate)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let options: observer.ObserverOptions = {
2. slotId: 0
3. }
4. observer.on('networkStateChange', options, (data: observer.NetworkState) => {
5. console.info("on networkStateChange, data:" + JSON.stringify(data));
6. });
```

## observer.off('networkStateChange')

PhoneTabletWearable

off(type: 'networkStateChange', callback?: Callback<NetworkState>): void

取消订阅网络状态变化事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 网络状态变化事件，参数固定为'networkStateChange'。 |
| callback | Callback<[NetworkState](js-apis-radio.md#networkstate)> | 否 | 以callback形式异步返回结果，参考radio的[NetworkState](js-apis-radio.md#networkstate)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let callback: (data: observer.NetworkState) => void = (data: observer.NetworkState) => {
2. console.info("on networkStateChange, data:" + JSON.stringify(data));
3. }
4. observer.on('networkStateChange', callback);
5. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
6. observer.off('networkStateChange', callback);
7. observer.off('networkStateChange');
```

## observer.on('signalInfoChange')

PhoneTabletWearable

on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void

订阅信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| callback | Callback<Array<[SignalInformation](js-apis-radio.md#signalinformation)>> | 是 | 以callback形式异步返回结果，参考radio的[SignalInformation](js-apis-radio.md#signalinformation)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { radio } from '@kit.TelephonyKit';

3. observer.on('signalInfoChange', (data: Array<radio.SignalInformation>) => {
4. console.info("on signalInfoChange, data:" + JSON.stringify(data));
5. });
```

## observer.on('signalInfoChange')

PhoneTabletWearable

on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void

订阅指定卡槽位的信号状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<Array<[SignalInformation](js-apis-radio.md#signalinformation)>> | 是 | 以callback形式异步返回结果，参考radio的[SignalInformation](js-apis-radio.md#signalinformation)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { radio } from '@kit.TelephonyKit';

3. let options: observer.ObserverOptions = {
4. slotId: 0
5. }
6. observer.on('signalInfoChange', options, (data: Array<radio.SignalInformation>) => {
7. console.info("on signalInfoChange, data:" + JSON.stringify(data));
8. });
```

## observer.off('signalInfoChange')

PhoneTabletWearable

off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void

取消订阅信号状态变化事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 信号状态变化事件，参数固定为'signalInfoChange'。 |
| callback | Callback<Array<[SignalInformation](js-apis-radio.md#signalinformation)>> | 否 | 以callback形式异步返回结果，参考radio的[SignalInformation](js-apis-radio.md#signalinformation)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { radio } from '@kit.TelephonyKit';

3. let callback: (data: Array<radio.SignalInformation>) => void = (data: Array<radio.SignalInformation>) => {
4. console.info("on signalInfoChange, data:" + JSON.stringify(data));
5. }
6. observer.on('signalInfoChange', callback);
7. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
8. observer.off('signalInfoChange', callback);
9. observer.off('signalInfoChange');
```

## observer.on('callStateChange')

PhoneTabletWearable

on(type: 'callStateChange', callback: Callback<CallStateInfo>): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback<[CallStateInfo](js-apis-observer.md#callstateinfo11)> | 是 | 以callback形式异步返回结果。  应用可获取到CallStateInfo。  其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. observer.on('callStateChange', (data: observer.CallStateInfo) => {
2. console.info("on callStateChange, data:" + JSON.stringify(data));
3. });
```

## observer.on('callStateChange')

PhoneTabletWearable

on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void

订阅通话状态变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<[CallStateInfo](js-apis-observer.md#callstateinfo11)> | 是 | 以callback形式异步返回结果。  应用可获取到CallStateInfo。  其中，三方应用仅能获取state通话状态。number受系统权限管控，仅面向系统应用开放。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let options: observer.ObserverOptions = {
2. slotId: 0
3. }
4. observer.on('callStateChange', options, (data: observer.CallStateInfo) => {
5. console.info("on callStateChange, data:" + JSON.stringify(data));
6. });
```

## observer.off('callStateChange')

PhoneTabletWearable

off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void

取消订阅通话状态变化事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback<[CallStateInfo](js-apis-observer.md#callstateinfo11)> | 否 | 以callback形式异步返回结果，参考call的[CallState](js-apis-call.md#callstate)。  number：电话号码。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let callback: (data: observer.CallStateInfo) => void = (data: observer.CallStateInfo) => {
2. console.info("on callStateChange, data:" + JSON.stringify(data));
3. }
4. observer.on('callStateChange', callback);
5. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
6. observer.off('callStateChange', callback);
7. observer.off('callStateChange');
```

## observer.on('callStateChangeEx')21+

PhoneTabletWearable

on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void

订阅通话状态变化拓展事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChangeEx'。 |
| callback | Callback<[TelCallState](js-apis-call.md#telcallstate21)> | 是 | 以callback形式异步返回结果。  应用可获取到TelCallState。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 否 | 电话相关事件订阅参数可选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**示例：**

```
1. import { call } from '@kit.TelephonyKit';

3. let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
4. console.info("on callStateChangeEx, data:" + JSON.stringify(data));
5. }
6. let options: observer.ObserverOptions = {
7. slotId: 0
8. }

10. observer.on('callStateChangeEx', callback, options);
11. observer.on('callStateChangeEx', callback);
```

## observer.off('callStateChangeEx')21+

PhoneTabletWearable

off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void

取消订阅通话状态变化拓展事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 通话状态变化事件，参数固定为'callStateChange'。 |
| callback | Callback<[TelCallState](js-apis-call.md#telcallstate21)> | 否 | 以callback形式异步返回结果，参考call的[TelCallState](js-apis-call.md#telcallstate21)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**示例：**

```
1. import { call } from '@kit.TelephonyKit';
2. let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
3. console.info("on callStateChangeEx, data:" + JSON.stringify(data));
4. }
5. observer.on('callStateChangeEx', callback);
6. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
7. observer.off('callStateChangeEx', callback);
8. observer.off('callStateChangeEx');
```

## observer.on('cellularDataConnectionStateChange')7+

PhoneTabletWearable

on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void

订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| callback | Callback<[DataConnectionStateInfo](js-apis-observer.md#dataconnectionstateinfo11)> | 是 | 以callback形式异步返回结果，参考data的[DataConnectState](js-apis-telephony-data.md#dataconnectstate)，radio的[RadioTechnology](js-apis-radio.md#radiotechnology)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. observer.on('cellularDataConnectionStateChange', (data: observer.DataConnectionStateInfo) => {
2. console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
3. });
```

## observer.on('cellularDataConnectionStateChange')7+

PhoneTabletWearable

on(type: 'cellularDataConnectionStateChange', options: ObserverOptions, callback: Callback<DataConnectionStateInfo>): void

订阅指定卡槽位的蜂窝数据链路连接状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<[DataConnectionStateInfo](js-apis-observer.md#dataconnectionstateinfo11)> | 是 | 以callback形式异步返回结果，参考data的[DataConnectState](js-apis-telephony-data.md#dataconnectstate)，radio的[RadioTechnology](js-apis-radio.md#radiotechnology)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let options: observer.ObserverOptions = {
2. slotId: 0
3. }
4. observer.on('cellularDataConnectionStateChange', options, (data: observer.DataConnectionStateInfo) => {
5. console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
6. });
```

## observer.off('cellularDataConnectionStateChange')7+

PhoneTabletWearable

off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void

移除订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据链路连接状态事件，参数固定为'cellularDataConnectionStateChange'。 |
| callback | Callback<[DataConnectionStateInfo](js-apis-observer.md#dataconnectionstateinfo11)> | 否 | 以callback形式异步返回结果，参考data的[DataConnectState](js-apis-telephony-data.md#dataconnectstate)，radio的[RadioTechnology](js-apis-radio.md#radiotechnology)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let callback: (data: observer.DataConnectionStateInfo) => void = (data: observer.DataConnectionStateInfo) => {
2. console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
3. }
4. observer.on('cellularDataConnectionStateChange', callback);
5. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
6. observer.off('cellularDataConnectionStateChange', callback);
7. observer.off('cellularDataConnectionStateChange');
```

## observer.on('cellularDataFlowChange')7+

PhoneTabletWearable

on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void

订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| callback | Callback<[DataFlowType](js-apis-telephony-data.md#dataflowtype)> | 是 | 以callback形式异步返回结果，参考data的[DataFlowType](js-apis-telephony-data.md#dataflowtype)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. observer.on('cellularDataFlowChange', (data: data.DataFlowType) => {
4. console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
5. });
```

## observer.on('cellularDataFlowChange')7+

PhoneTabletWearable

on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void

订阅指定卡槽位的蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<[DataFlowType](js-apis-telephony-data.md#dataflowtype)> | 是 | 以callback形式异步返回结果，参考data的[DataFlowType](js-apis-telephony-data.md#dataflowtype)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. let options: observer.ObserverOptions = {
4. slotId: 0
5. }
6. observer.on('cellularDataFlowChange', options, (data: data.DataFlowType) => {
7. console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
8. });
```

## observer.off('cellularDataFlowChange')7+

PhoneTabletWearable

off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void

移除订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 蜂窝数据业务的上下行数据流状态事件，参数固定为'cellularDataFlowChange'。 |
| callback | Callback<[DataFlowType](js-apis-telephony-data.md#dataflowtype)> | 否 | 以callback形式异步返回结果，参考data的[DataFlowType](js-apis-telephony-data.md#dataflowtype)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { data } from '@kit.TelephonyKit';

3. let callback: (data: data.DataFlowType) => void = (data: data.DataFlowType) => {
4. console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
5. }
6. observer.on('cellularDataFlowChange', callback);
7. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
8. observer.off('cellularDataFlowChange', callback);
9. observer.off('cellularDataFlowChange');
```

## observer.on('simStateChange')7+

PhoneTabletWearable

on(type: 'simStateChange', callback: Callback<SimStateData>): void

订阅sim状态更改事件，使用callback方式作为异步方法。

说明

此接口不包含sim卡的激活状态，具体请参见[sim.isSimActive](js-apis-sim.md#simissimactive7)接口。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| callback | Callback<[SimStateData](js-apis-observer.md#simstatedata7)> | 是 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. observer.on('simStateChange', (data: observer.SimStateData) => {
2. console.info("on simStateChange, data:" + JSON.stringify(data));
3. });
```

## observer.on('simStateChange')7+

PhoneTabletWearable

on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void

订阅指定卡槽位的sim状态更改事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 是 | 电话相关事件订阅参数可选项。 |
| callback | Callback<[SimStateData](js-apis-observer.md#simstatedata7)> | 是 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let options: observer.ObserverOptions = {
2. slotId: 0
3. }
4. observer.on('simStateChange', options, (data: observer.SimStateData) => {
5. console.info("on simStateChange, data:" + JSON.stringify(data));
6. });
```

## observer.off('simStateChange')7+

PhoneTabletWearable

off(type: 'simStateChange', callback?: Callback<SimStateData>): void

移除订阅sim状态更改事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | sim状态更改事件，参数固定为'simStateChange'。 |
| callback | Callback<[SimStateData](js-apis-observer.md#simstatedata7)> | 否 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let callback: (data: observer.SimStateData) => void = (data: observer.SimStateData) => {
2. console.info("on simStateChange, data:" + JSON.stringify(data));
3. }
4. observer.on('simStateChange', callback);
5. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
6. observer.off('simStateChange', callback);
7. observer.off('simStateChange');
```

## observer.on('iccAccountInfoChange')10+

PhoneTabletWearable

on(type: 'iccAccountInfoChange', callback: Callback<void>): void

订阅卡帐户变化事件，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 卡帐户变化事件，参数固定为'iccAccountInfoChange'。 |
| callback | Callback<void> | 是 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. observer.on('iccAccountInfoChange', () => {
2. console.info("on iccAccountInfoChange success");
3. });
```

## observer.off('iccAccountInfoChange')10+

PhoneTabletWearable

off(type: 'iccAccountInfoChange', callback?: Callback<void>): void

移除订阅卡帐户变化事件，使用callback方式作为异步方法。

说明

可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 卡帐户变化事件，参数固定为'iccAccountInfoChange'。 |
| callback | Callback<void> | 否 | 以callback形式异步返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. let callback: () => void = () => {
2. console.info("on iccAccountInfoChange success");
3. }
4. observer.on('iccAccountInfoChange', callback);
5. // 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。
6. observer.off('iccAccountInfoChange', callback);
7. observer.off('iccAccountInfoChange');
```

## observer.onGetSimActiveState23+

PhoneTabletWearable

onGetSimActiveState(slotId: number, callback: Callback<boolean>): void

SIM卡激活状态变化的监听，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | Callback<boolean> | 是 | 以callback形式返回结果。  - true：激活。  - false：未激活。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. let sislotId = 0;
5. let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
6. console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
7. }
8. observer.onGetSimActiveState(sislotId, simActiveState);
```

## observer.offGetSimActiveState23+

PhoneTabletWearable

offGetSimActiveState(callback?: Callback<boolean>): void

取消SIM卡激活状态变化的监听，使用callback方式作为异步方法。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

**系统能力**：SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<boolean> | 否 | 以callback形式返回结果。  - true：激活。  - false：未激活。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. let simActiveState: Callback<boolean> = (isSimActive: boolean) => {
5. console.info(`simActiveState slotId ${JSON.stringify(isSimActive)}`);
6. }
7. observer.offGetSimActiveState(simActiveState);
```

## observer.onCCallStateChange23+

PhoneTabletWearable

onCCallStateChange(callback: Callback<CCallStateInfo>, options?: ObserverOptions): void

三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**需要权限**：ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CCallStateInfo](js-apis-observer.md#ccallstateinfo23)> | 是 | 以callback形式异步返回结果。  应用可获取到CCallState。 |
| options | [ObserverOptions](js-apis-observer.md#observeroptions11) | 否 | 电话相关事件订阅参数可选项。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**示例：**

```
1. import { call, observer } from '@kit.TelephonyKit';

3. let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
4. console.info("onCCallStateChange, data:" + JSON.stringify(data));
5. }
6. let options: observer.ObserverOptions = {
7. slotId: 0
8. }

10. observer.onCCallStateChange(callback, options);
11. observer.onCCallStateChange(callback);
```

## observer.offCCallStateChange23+

PhoneTabletWearable

offCCallStateChange(callback?: Callback<CCallStateInfo>): void

取消三方应用监听运营商通话状态并获取通话号码，使用callback方式作为异步方法。

**系统能力**：SystemCapability.Telephony.StateRegistry

**需要权限**：ohos.permission.MANAGE\_CALL\_FOR\_DEVICES

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[CCallStateInfo](js-apis-observer.md#ccallstateinfo23)> | 否 | 以callback形式异步返回结果。  应用可获取到CCallState。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 8800001 | Invalid parameter value. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800999 | Unknown error. |

**示例：**

```
1. import { call, observer } from '@kit.TelephonyKit';

3. let callback: (data: observer.CCallStateInfo) => void = (data: observer.CCallStateInfo) => {
4. console.info("onCCallStateChange, data:" + JSON.stringify(data));
5. }

7. observer.offCCallStateChange(callback);
8. observer.offCCallStateChange();
```

## LockReason8+

PhoneTabletWearable

SIM卡锁类型。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIM\_NONE | 0 | 无锁。 |
| SIM\_PIN | 1 | PIN锁。 |
| SIM\_PUK | 2 | PUK锁。 |
| SIM\_PN\_PIN | 3 | 网络PIN锁。 |
| SIM\_PN\_PUK | 4 | 网络PUK锁。 |
| SIM\_PU\_PIN | 5 | 子网PIN锁。 |
| SIM\_PU\_PUK | 6 | 子网PUK锁。 |
| SIM\_PP\_PIN | 7 | 服务提供商PIN锁。 |
| SIM\_PP\_PUK | 8 | 服务提供商PUK锁。 |
| SIM\_PC\_PIN | 9 | 组织PIN锁。 |
| SIM\_PC\_PUK | 10 | 组织PUK锁。 |
| SIM\_SIM\_PIN | 11 | SIM PIN锁。 |
| SIM\_SIM\_PUK | 12 | SIM PUK锁。 |

## SimStateData7+

PhoneTabletWearable

SIM卡类型和状态。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [CardType](js-apis-sim.md#cardtype7) | 否 | 否 | SIM卡类型。 |
| state | [SimState](js-apis-sim.md#simstate) | 否 | 否 | SIM卡状态。 |
| reason8+ | [LockReason](js-apis-observer.md#lockreason8) | 否 | 否 | SIM卡锁类型。 |

## CallStateInfo11+

PhoneTabletWearable

通话状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [CallState](js-apis-call.md#callstate) | 否 | 否 | 通话类型。 |
| number | string | 否 | 否 | 电话号码。 |

## CCallStateInfo23+

PhoneTabletWearable

通话状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [CCallState](js-apis-call.md#ccallstate23) | 否 | 否 | 通话类型。 |
| teleNumber | string | 否 | 否 | 电话号码。 |

## DataConnectionStateInfo11+

PhoneTabletWearable

数据连接状态相关信息。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [DataConnectState](js-apis-telephony-data.md#dataconnectstate) | 否 | 否 | 数据连接状态。 |
| network | [RatType](js-apis-observer.md#rattype) | 否 | 否 | 网络类型。 |

## ObserverOptions11+

PhoneTabletWearable

电话相关事件订阅参数可选项。

**系统能力**：SystemCapability.Telephony.StateRegistry

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotId | number | 否 | 否 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
