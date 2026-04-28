---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/nearlink-manager
title: manager（星闪开关能力）
breadcrumb: API参考 > 系统 > 网络 > NearLink Kit（星闪服务） > ArkTS API参考 > manager（星闪开关能力）
category: harmonyos-references
scraped_at: 2026-04-28T08:08:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c62a6e0b0970713b49a29725805e857a94a5f89126b5c8f1207c049d808180b8
---

本模块提供了管理星闪基础能力，包括获取设备信息、订阅状态变化事件等。

**起始版本：** 5.0.1(13)

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { manager } from '@kit.NearLinkKit';
```

## PairingState

PhonePC/2in1TabletTVWearable

type PairingState = [constant.PairingState](nearlink-constant.md#pairingstate)

表示和远端设备的配对状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.PairingState](nearlink-constant.md#pairingstate) | 和远端设备的配对状态。 |

## ConnectionState

PhonePC/2in1TabletTVWearable

type ConnectionState = [constant.ConnectionState](nearlink-constant.md#connectionstate)

表示和远端设备的连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 类型 | 说明 |
| --- | --- |
| [constant.ConnectionState](nearlink-constant.md#connectionstate) | 和远端设备的连接状态。 |

## AcbState

PhonePC/2in1TabletTVWearable

type AcbState = [constant.AcbState](nearlink-constant.md#acbstate)

表示和远端设备的逻辑链路连接状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 类型 | 说明 |
| --- | --- |
| [constant.AcbState](nearlink-constant.md#acbstate) | 和远端设备的逻辑链路连接状态。 |

## getState

PhonePC/2in1TabletTVWearable

getState(): NearlinkState

查询星闪开关状态。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NearlinkState](nearlink-manager.md#nearlinkstate) | 表示星闪开关状态。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let state: manager.NearlinkState = manager.getState();
6. console.info('state:' + JSON.stringify(state));
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## isNearLinkSupported

PhonePC/2in1TabletTVWearable

isNearLinkSupported(): boolean

查询当前设备是否支持星闪服务。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.1.0(23)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true：设备支持星闪。返回false：设备不支持星闪。 |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let isSupported: boolean = manager.isNearLinkSupported();
6. if (isSupported) {
7. console.info('NearLink is supported on this device.');
8. } else {
9. console.info('NearLink is not supported on this device.');
10. }
11. } catch (err) {
12. console.error('Error occurred: ' + (err as BusinessError).code + ', ' + (err as BusinessError).message);
13. }
```

## getLocalName

PhonePC/2in1TabletTVWearable

getLocalName(): string

查询本机星闪名称。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 表示星闪设备本地名称。最大长度为30。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let name: string = manager.getLocalName();
6. console.info('state:' + JSON.stringify(name));
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## getPairedDevices

PhonePC/2in1TabletTVWearable

getPairedDevices(): Array<string>

获取与当前设备配对的设备列表。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 6.0.1(21)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 配对设备地址的列表。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 801 | Capability not supported |
| 1009700003 | Nearlink is off |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. let pairedDevices: Array<string> = manager.getPairedDevices();
6. if (pairedDevices.length > 0) {
7. console.info('getPairedDevices return: ' + JSON.stringify(pairedDevices));
8. } else {
9. console.info('No Paired Devices found.');
10. }
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

## on( 'stateChange')

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: Callback<NearlinkState>): void

订阅星闪开关状态变化事件。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"stateChange"字符串，表示星闪开关状态变化事件。 |
| callback | Callback<[NearlinkState](nearlink-manager.md#nearlinkstate)> | 是 | 表示开关状态变化回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<manager.NearlinkState> = (data: manager.NearlinkState) => {
6. if (data === manager.NearlinkState.STATE_TURNING_ON) {
7. console.info('nearlink STATE_TURNING_ON');
8. } else if (data === manager.NearlinkState.STATE_ON) {
9. console.info('nearlink STATE_ON');
10. } else if (data === manager.NearlinkState.STATE_TURNING_OFF) {
11. console.info('nearlink STATE_TURNING_OFF');
12. } else if (data === manager.NearlinkState.STATE_OFF) {
13. console.info('nearlink STATE_OFF');
14. }
15. };
16. try {
17. manager.on('stateChange', callback);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
```

## off( 'stateChange')

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: Callback<NearlinkState>): void

取消订阅星闪开关状态变化事件。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"stateChange"字符串，表示星闪开关状态变化事件。 |
| callback | Callback<[NearlinkState](nearlink-manager.md#nearlinkstate)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. manager.off('stateChange');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## on( 'pairingStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'pairingStateChange', callback: Callback<PairingStateParam>): void

订阅配对请求事件。回调函数携带远端设备的随机地址。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"pairingStateChange"字符串，表示配对请求事件。 |
| callback | Callback<[PairingStateParam](nearlink-manager.md#pairingstateparam)> | 是 | 表示配对状态变化回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let onPairingStateEvent:(data: manager.PairingStateParam) => void = (data: manager.PairingStateParam) => {
5. console.info('onPairStateChange addr: '+ data.address + 'state:' + data.state);
6. }
7. try {
8. manager.on('pairingStateChange', onPairingStateEvent);
9. } catch (err) {
10. console.info('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## off( 'pairingStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'pairingStateChange', callback?: Callback<PairingStateParam>): void

取消订阅配对请求事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写'pairingStateChange'字符串，表示配对请求事件。 |
| callback | Callback<[PairingStateParam](nearlink-manager.md#pairingstateparam)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. manager.off('pairingStateChange');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## on( 'connectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<ConnectionStateParam>): void

订阅连接状态变化事件。回调函数携带远端设备的随机地址。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionStateParam](nearlink-manager.md#connectionstateparam)> | 是 | 表示连接状态变化回调函数的入参。回调函数由用户创建通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<manager.ConnectionStateParam> = (data: manager.ConnectionStateParam) => {
6. console.info('data:' + JSON.stringify(data));
7. };
8. try {
9. manager.on('connectionStateChange', callback);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## off( 'connectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<ConnectionStateParam>): void

取消订阅连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[ConnectionStateParam](nearlink-manager.md#connectionstateparam)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Invalid parameter |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. manager.off('connectionStateChange');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## on('acbStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'acbStateChange', callback: Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)>): void

订阅逻辑链路连接状态变化事件。回调函数携带远端设备的随机地址。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"acbStateChange"字符串，表示逻辑链路连接状态变化事件。 |
| callback | Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)> | 是 | 表示逻辑链路连接状态变化回调函数的入参。回调函数由用户创建，通过该接口注册。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { Callback } from '@kit.BasicServicesKit';

5. let callback: Callback<manager.AcbStateParam> = (data: manager.AcbStateParam) => {
6. console.info('data:' + JSON.stringify(data));
7. };
8. try {
9. manager.on('acbStateChange', callback);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## off( 'acbStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'acbStateChange', callback?: Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)>): void

取消订阅逻辑链路连接状态变化事件。

**需要权限：** ohos.permission.ACCESS\_NEARLINK

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 固定填写"acbStateChange"字符串，表示逻辑链路连接状态变化事件。 |
| callback | Callback<[AcbStateParam](nearlink-manager.md#acbstateparam)> | 否 | 可选参数，需要取消注册的回调函数，需与订阅时传入的回调函数是同一个。若无此参数，则取消注册所有的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](nearlink-error-code.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported |
| 1009700099 | Operation failed |

**示例：**

```
1. import { manager } from '@kit.NearLinkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. try {
5. manager.off('acbStateChange');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## PairingStateParam

PhonePC/2in1TabletTVWearable

订阅的配对状态变化结果。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的配对状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。 |
| preState | [PairingState](nearlink-constant.md#pairingstate) | 否 | 否 | 本次上报之前的配对状态。 |
| state | [PairingState](nearlink-constant.md#pairingstate) | 否 | 否 | 当前配对状态。 |
| reason | [PairingReason](nearlink-manager.md#pairingreason) | 否 | 否 | 原因值。 |

## PairingRequestParam

PhonePC/2in1TabletTVWearable

表示订阅的配对请求事件上报结果。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示收到该设备的配对请求上报。地址格式参考："11:22:33:AA:BB:FF"。 |
| passkey | string | 否 | 否 | 表示配对交互的配对码，显示给用户确认。长度固定为6，字符串内容为数字。 |
| pairingType | [PairingType](nearlink-manager.md#pairingtype) | 否 | 否 | 表示配对类型。 |

## ConnectionStateParam

PhonePC/2in1TabletTVWearable

订阅的连接状态变化事件上报结果。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的连接状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。 |
| preState | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 本次上报之前的连接状态。 |
| state | [ConnectionState](nearlink-constant.md#connectionstate) | 否 | 否 | 当前连接状态。 |
| connectionReason | [ConnectionReason](nearlink-manager.md#connectionreason) | 否 | 否 | 原因值。 |

## NearlinkState

PhonePC/2in1TabletTVWearable

星闪的开关状态，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_TURNING\_ON | 0 | 表示星闪正在打开。 |
| STATE\_ON | 1 | 表示星闪已打开。 |
| STATE\_TURNING\_OFF | 2 | 表示星闪正在关闭。 |
| STATE\_OFF | 3 | 表示星闪已关闭。 |

## PairingReason

PhonePC/2in1TabletTVWearable

表示星闪配对状态变化结果的原因值，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PAIRING\_REASON\_SUCCESS | 0 | 表示配对成功。 |
| PAIRING\_REASON\_FAILURE | 1 | 表示配对失败。 |
| PAIRING\_REASON\_PROFILE\_UNSUPPORTED | 2 | 表示对端设备不支持服务导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_EXCEED\_ACB\_MAX | 3 | 表示连接设备数已达上限导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_REMOTE\_CANCELED | 4 | 表示对端设备取消配对导致配对失败。  **起始版本：** 5.1.0(18) |
| PAIRING\_REASON\_LOCAL\_CANCELED | 5 | 表示本端设备取消配对导致配对失败。  **起始版本**：5.1.0(18) |

## PairingType

PhonePC/2in1TabletTVWearable

星闪配对类型，为枚举值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NO\_PASSKEY\_CONFIRMATION | 0 | 表示不需要passkey的配对方式，用户无需检查配对码。 |
| PAIRING\_TYPE\_PASSCODE | 1 | 表示通行码鉴权方式，用户需在一端设备输入另一端设备显示的配对码。  **起始版本：** 5.1.0(18) |
| PAIRING\_TYPE\_NUMBER\_COMPARE | 2 | 表示数字比较鉴权方式，用户需在两端设备确认配对码一致。  **起始版本：** 5.1.0(18) |

## ConnectionReason

PhonePC/2in1TabletTVWearable

星闪连接状态变化结果的原因值。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.0.1(13)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONNECTION\_SUCCESS | 0 | 表示连接成功。 |
| CONNECTION\_FAILURE | 1 | 表示连接失败。 |

## AcbStateParam

PhonePC/2in1TabletTVWearable

订阅的逻辑链路连接状态变化事件上报结果。

**系统能力：** SystemCapability.Communication.NearLink.Core

**起始版本：** 5.1.0(18)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| address | string | 否 | 否 | 设备地址，表示和该设备的逻辑链路连接状态发生变化。地址格式参考："11:22:33:AA:BB:FF"。 |
| state | [AcbState](nearlink-constant.md#acbstate) | 否 | 否 | 当前逻辑链路连接状态。 |
